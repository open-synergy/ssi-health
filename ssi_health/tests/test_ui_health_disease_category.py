# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthDiseaseCategory(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.disease_category"].create(
            {
                "name": "TOUR-EDIT-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.disease_category"].create(
            {
                "name": "TOUR-DELETE-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.disease_category"].create(
            {
                "name": "TOUR-DEACTIVATE-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.disease_category"].create(
            {
                "name": "TOUR-ACTIVATE-CATEGORY",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """IK: docs/health_disease_category/01-create.md"""
        self.start_tour(
            "/web", "ssi_health_health_disease_category_create", login="admin"
        )

    def test_edit(self):
        """IK: docs/health_disease_category/02-edit.md"""
        self.start_tour(
            "/web", "ssi_health_health_disease_category_edit", login="admin"
        )

    def test_delete(self):
        """IK: docs/health_disease_category/03-delete.md"""
        self.start_tour(
            "/web", "ssi_health_health_disease_category_delete", login="admin"
        )

    def test_deactivate(self):
        """IK: docs/health_disease_category/04-deactivate.md"""
        self.start_tour(
            "/web", "ssi_health_health_disease_category_deactivate", login="admin"
        )

    def test_activate(self):
        """IK: docs/health_disease_category/05-activate.md"""
        self.start_tour(
            "/web", "ssi_health_health_disease_category_activate", login="admin"
        )
