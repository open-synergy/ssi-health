# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthAllergen(HttpSavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.allergen_category"].create(
            {
                "name": "TOUR-ALLERGEN-CATEGORY",
                "code": "/",
            }
        )
        cls.env["health.allergen"].create(
            {
                "name": "TOUR-EDIT-ALLERGEN",
                "code": "/",
            }
        )
        cls.env["health.allergen"].create(
            {
                "name": "TOUR-DELETE-ALLERGEN",
                "code": "/",
            }
        )
        cls.env["health.allergen"].create(
            {
                "name": "TOUR-DEACTIVATE-ALLERGEN",
                "code": "/",
            }
        )
        cls.env["health.allergen"].create(
            {
                "name": "TOUR-ACTIVATE-ALLERGEN",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """IK: docs/health_allergen/01-create.md"""
        self.start_tour("/web", "ssi_health_health_allergen_create", login="admin")

    def test_edit(self):
        """IK: docs/health_allergen/02-edit.md"""
        self.start_tour("/web", "ssi_health_health_allergen_edit", login="admin")

    def test_delete(self):
        """IK: docs/health_allergen/03-delete.md"""
        self.start_tour("/web", "ssi_health_health_allergen_delete", login="admin")

    def test_deactivate(self):
        """IK: docs/health_allergen/04-deactivate.md"""
        self.start_tour("/web", "ssi_health_health_allergen_deactivate", login="admin")

    def test_activate(self):
        """IK: docs/health_allergen/05-activate.md"""
        self.start_tour("/web", "ssi_health_health_allergen_activate", login="admin")
