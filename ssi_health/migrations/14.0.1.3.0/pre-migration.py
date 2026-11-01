# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Migration: 14.0.1.2.0 -> 14.0.1.3.0
#
# Changes: The module now ships seed data (ICD-10 disease categories,
#          DSM-5 / ICD-10 diseases, allergens and WHO ATC medications)
#          with xml_ids. An instance may already hold the same records
#          keyed in by hand, without any xml_id; loading the XML would
#          then fail on the unique ``code`` constraint of the master
#          data mixin. This "pre" script registers the xml_id of every
#          seed record on the existing row that has the same ``code``,
#          so the XML load updates nothing and creates no duplicate.
#          Rows are never updated or deleted, and ids are kept.

import logging
import os
import xml.etree.ElementTree as ET

from openupgradelib import openupgrade

from odoo.modules.module import get_module_path

_logger = logging.getLogger(__name__)

MODULE = "ssi_health"
DATA_FILES = (
    "health_disease_category_data.xml",
    "health_disease_category_icd10_data.xml",
    "health_disease_data.xml",
    "health_allergen_category_data.xml",
    "health_allergen_data.xml",
    "health_medication_data.xml",
)
ADOPTED_MODELS = (
    "health.disease_category",
    "health.disease",
    "health.allergen",
    "health.medication",
)


def _read_seed_records():
    """Read the seed records declared by the module data files.

    :return: list of ``(xml_id, model, code)`` tuples for the adopted
        models only
    :rtype: list
    """
    base = os.path.join(get_module_path(MODULE), "data")
    result = []
    for filename in DATA_FILES:
        root = ET.parse(os.path.join(base, filename)).getroot()
        for record in root.iter("record"):
            model = record.get("model")
            if model not in ADOPTED_MODELS:
                continue
            code = None
            for field in record.findall("field"):
                if field.get("name") == "code":
                    code = field.text
            if code:
                result.append((record.get("id"), model, code))
    return result


def _adopt_record(cr, xml_id, model, code):
    """Register ``xml_id`` on the existing row having the same code.

    The row is searched in the model table including archived rows, and
    only among rows that have no ``ir_model_data`` entry yet. Nothing is
    done when the xml_id is already registered.

    :param cr: database cursor
    :param str xml_id: xml_id name, without module prefix
    :param str model: model name
    :param str code: code of the seed record
    :return: ``True`` when a row was adopted
    :rtype: bool
    """
    cr.execute(
        "SELECT 1 FROM ir_model_data WHERE module = %s AND name = %s",
        (MODULE, xml_id),
    )
    if cr.fetchone():
        return False
    table = model.replace(".", "_")
    cr.execute(
        """
        SELECT t.id
        FROM {table} t
        WHERE t.code = %s
          AND NOT EXISTS (
              SELECT 1 FROM ir_model_data d
              WHERE d.model = %s AND d.res_id = t.id
          )
        ORDER BY t.id
        LIMIT 1
        """.format(
            table=table
        ),
        (code, model),
    )
    row = cr.fetchone()
    if not row:
        return False
    openupgrade.add_xmlid(cr, MODULE, xml_id, model, row[0], noupdate=True)
    return True


@openupgrade.migrate()
def migrate(env, version):
    """Adopt manually created seed records into the module xml_ids.

    :param env: the migration environment
    :param version: the version being migrated from (unused)
    :return: nothing; inserts ``ir_model_data`` rows only
    """
    cr = env.cr
    counts = {model: 0 for model in ADOPTED_MODELS}
    for xml_id, model, code in _read_seed_records():
        if _adopt_record(cr, xml_id, model, code):
            counts[model] += 1
    for model in ADOPTED_MODELS:
        _logger.info("Adopted %s existing %s record(s).", counts[model], model)
