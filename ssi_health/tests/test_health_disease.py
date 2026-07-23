# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestHealthDisease(YamlTransactionCase):
    def test_health_disease(self):
        self.run_yaml_scenario("test_data_health_disease.yaml")

    @mute_logger("odoo.sql_db")
    def test_category_restrict_on_delete(self):
        """Pure Python -- trigger P5 (L-22: `psycopg2.IntegrityError` is
        outside the 12 error types `expect_error` can name).

        `health.disease.category_id` uses `ondelete="restrict"`, so deleting a
        `health.disease_category` still referenced by a `health.disease` raises
        a raw `psycopg2.IntegrityError` at the database level -- there is no
        YAML-expressible way to assert it. `mute_logger("odoo.sql_db")`
        silences the ERROR line PostgreSQL normally writes here; without it
        `oca_checklog_odoo` would fail CI even though the test passes.
        """
        category = self.env["health.disease_category"].create(
            {
                "name": "Restrict Category",
                "code": "RSTC",
            }
        )
        self.env["health.disease"].create(
            {
                "name": "Restrict Disease",
                "code": "RSTD",
                "category_id": category.id,
            }
        )
        with mute_logger("odoo.sql_db"), self.assertRaises(IntegrityError):
            with self.cr.savepoint():
                category.unlink()
