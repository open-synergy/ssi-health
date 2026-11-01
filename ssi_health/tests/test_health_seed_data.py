# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import importlib.util
import os

from odoo_yaml_test import YamlTransactionCase

from odoo.modules.module import get_module_path
from odoo.tests import tagged
from odoo.tools import mute_logger

MODULE = "ssi_health"
ADOPTED = (
    ("health_disease_j45", "health.disease", "health_disease"),
    ("health_disease_adhd", "health.disease", "health_disease"),
    ("health_allergen_peanut", "health.allergen", "health_allergen"),
    ("health_medication_r03ac02", "health.medication", "health_medication"),
    ("icd10_resp", "health.disease_category", "health_disease_category"),
)


@tagged("post_install", "-at_install")
class TestHealthSeedData(YamlTransactionCase):
    """Cover the seed data and its xml_id adoption migration."""

    def test_health_seed_data(self):
        """Run the seed data scenarios.

        :return: nothing
        """
        self.run_yaml_scenario("test_data_health_seed_data.yaml")

    def _load_script(self):
        """Import the pre-migration script from its file.

        :return: the imported script module
        """
        path = os.path.join(
            get_module_path(MODULE),
            "migrations",
            "14.0.1.3.0",
            "pre-migration.py",
        )
        spec = importlib.util.spec_from_file_location("pre_migration_1_3_0", path)
        script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script)
        return script

    def _xmlid_rows(self, name):
        """Return the ``res_id`` of every xml_id row named ``name``.

        :param str name: xml_id name, without module prefix
        :return: list of ``res_id`` values
        """
        self.env.cr.execute(
            "SELECT res_id FROM ir_model_data WHERE module = %s AND name = %s",
            (MODULE, name),
        )
        return [row[0] for row in self.env.cr.fetchall()]

    def _count_by_code(self, table, code):
        """Count the rows of ``table`` having ``code``, archived included.

        :param str table: table name
        :param str code: code to look for
        :return: number of rows
        """
        self.env.cr.execute(
            "SELECT count(*) FROM {} WHERE code = %s".format(table), (code,)
        )
        return self.env.cr.fetchone()[0]

    @mute_logger("OpenUpgrade")
    def test_pre_migration_adopts_existing_records(self):
        """Adopt rows that lost their xml_id, keeping ids, once only.

        Pure Python -- trigger P10 (L-11: the migration script must be
        imported from its file; ``EVAL:`` cannot do it). The xml_id rows
        of a few seed records of each adopted model are deleted, one
        record is archived, then the script is run twice.
        ``mute_logger("OpenUpgrade")`` silences the ERROR line the
        ``migrate`` decorator logs when it is not called by Odoo's
        migration loader, so ``oca_checklog_odoo`` does not fail the CI.
        """
        expected = {}
        for name, _model, table in ADOPTED:
            record = self.env.ref("%s.%s" % (MODULE, name))
            expected[name] = (record.id, table, record.code)
        self.env["health.disease"].browse(expected["health_disease_adhd"][0]).write(
            {"active": False}
        )
        self.env["health.disease"].flush()
        self.env.cr.execute(
            "DELETE FROM ir_model_data WHERE module = %s AND name IN %s",
            (MODULE, tuple(expected)),
        )
        for name in expected:
            self.assertFalse(self._xmlid_rows(name))
        script = self._load_script()
        for _run in range(2):
            script.migrate(self.env.cr, "14.0.1.2.0")
            for name, (res_id, table, code) in expected.items():
                self.assertEqual(self._xmlid_rows(name), [res_id])
                self.assertEqual(self._count_by_code(table, code), 1)
