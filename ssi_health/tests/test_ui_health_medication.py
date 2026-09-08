# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthMedication(HttpSavepointCase):
    """Run the Medication UI tours.

    IK: docs/health_medication/
    """

    @classmethod
    def setUpClass(cls):
        """Create the fixture records each tour needs before it starts.

        :return: None
        """
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.medication"].create(
            {
                "name": "TOUR-EDIT-MEDICATION",
                "code": "/",
            }
        )
        cls.env["health.medication"].create(
            {
                "name": "TOUR-DELETE-MEDICATION",
                "code": "/",
            }
        )
        cls.env["health.medication"].create(
            {
                "name": "TOUR-DEACTIVATE-MEDICATION",
                "code": "/",
            }
        )
        cls.env["health.medication"].create(
            {
                "name": "TOUR-ACTIVATE-MEDICATION",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour.

        :return: None

        IK: docs/health_medication/01-create.md
        """
        self.start_tour("/web", "ssi_health_health_medication_create", login="admin")

    def test_edit(self):
        """Run the edit tour.

        :return: None

        IK: docs/health_medication/02-edit.md
        """
        self.start_tour("/web", "ssi_health_health_medication_edit", login="admin")

    def test_delete(self):
        """Run the delete tour.

        :return: None

        IK: docs/health_medication/03-delete.md
        """
        self.start_tour("/web", "ssi_health_health_medication_delete", login="admin")

    def test_deactivate(self):
        """Run the deactivate tour.

        :return: None

        IK: docs/health_medication/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_health_health_medication_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour.

        :return: None

        IK: docs/health_medication/05-activate.md
        """
        self.start_tour("/web", "ssi_health_health_medication_activate", login="admin")
