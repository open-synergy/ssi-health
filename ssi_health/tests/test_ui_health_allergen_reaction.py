# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthAllergenReaction(HttpSavepointCase):
    """Run the Allergen Reaction UI tours.

    IK: docs/health_allergen_reaction/
    """

    @classmethod
    def setUpClass(cls):
        """Create the fixture records each tour needs before it starts.

        :return: None
        """
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.allergen_reaction"].create(
            {
                "name": "TOUR-EDIT-ALLERGEN-REACTION",
                "code": "/",
            }
        )
        cls.env["health.allergen_reaction"].create(
            {
                "name": "TOUR-DELETE-ALLERGEN-REACTION",
                "code": "/",
            }
        )
        cls.env["health.allergen_reaction"].create(
            {
                "name": "TOUR-DEACTIVATE-ALLERGEN-REACTION",
                "code": "/",
            }
        )
        cls.env["health.allergen_reaction"].create(
            {
                "name": "TOUR-ACTIVATE-ALLERGEN-REACTION",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour.

        :return: None

        IK: docs/health_allergen_reaction/01-create.md
        """
        self.start_tour(
            "/web", "ssi_health_health_allergen_reaction_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour.

        :return: None

        IK: docs/health_allergen_reaction/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_health_health_allergen_reaction_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour.

        :return: None

        IK: docs/health_allergen_reaction/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_health_health_allergen_reaction_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour.

        :return: None

        IK: docs/health_allergen_reaction/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_health_health_allergen_reaction_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour.

        :return: None

        IK: docs/health_allergen_reaction/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_health_health_allergen_reaction_activate", login="admin"
        )
