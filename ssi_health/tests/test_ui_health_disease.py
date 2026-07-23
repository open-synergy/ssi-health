# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthDisease(HttpSavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.disease_category"].create(
            {
                "name": "TOUR-DISEASE-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.disease"].create(
            {
                "name": "TOUR-EDIT-DISEASE",
                "code": "/",
            }
        )
        cls.env["health.disease"].create(
            {
                "name": "TOUR-DELETE-DISEASE",
                "code": "/",
            }
        )
        cls.env["health.disease"].create(
            {
                "name": "TOUR-DEACTIVATE-DISEASE",
                "code": "/",
            }
        )
        cls.env["health.disease"].create(
            {
                "name": "TOUR-ACTIVATE-DISEASE",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """IK: docs/health_disease/01-create.md"""
        self.start_tour("/web", "ssi_health_health_disease_create", login="admin")

    def test_edit(self):
        """IK: docs/health_disease/02-edit.md"""
        self.start_tour("/web", "ssi_health_health_disease_edit", login="admin")

    def test_delete(self):
        """IK: docs/health_disease/03-delete.md"""
        self.start_tour("/web", "ssi_health_health_disease_delete", login="admin")

    def test_deactivate(self):
        """IK: docs/health_disease/04-deactivate.md"""
        self.start_tour("/web", "ssi_health_health_disease_deactivate", login="admin")

    def test_activate(self):
        """IK: docs/health_disease/05-activate.md"""
        self.start_tour("/web", "ssi_health_health_disease_activate", login="admin")
