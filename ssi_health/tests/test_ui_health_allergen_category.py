# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthAllergenCategory(HttpSavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.allergen_category"].create(
            {
                "name": "TOUR-EDIT-ALLERGEN-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.allergen_category"].create(
            {
                "name": "TOUR-DELETE-ALLERGEN-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.allergen_category"].create(
            {
                "name": "TOUR-DEACTIVATE-ALLERGEN-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.allergen_category"].create(
            {
                "name": "TOUR-ACTIVATE-ALLERGEN-CATEGORY",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """IK: docs/health_allergen_category/01-create.md"""
        self.start_tour(
            "/web", "ssi_health_health_allergen_category_create", login="admin"
        )

    def test_edit(self):
        """IK: docs/health_allergen_category/02-edit.md"""
        self.start_tour(
            "/web", "ssi_health_health_allergen_category_edit", login="admin"
        )

    def test_delete(self):
        """IK: docs/health_allergen_category/03-delete.md"""
        self.start_tour(
            "/web", "ssi_health_health_allergen_category_delete", login="admin"
        )

    def test_deactivate(self):
        """IK: docs/health_allergen_category/04-deactivate.md"""
        self.start_tour(
            "/web", "ssi_health_health_allergen_category_deactivate", login="admin"
        )

    def test_activate(self):
        """IK: docs/health_allergen_category/05-activate.md"""
        self.start_tour(
            "/web", "ssi_health_health_allergen_category_activate", login="admin"
        )
