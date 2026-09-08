# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHealthProviderRole(HttpSavepointCase):
    """Run the Health Provider Role UI tours.

    IK: docs/health_provider_role/
    """

    @classmethod
    def setUpClass(cls):
        """Create the fixture records each tour needs before it starts.

        :return: None
        """
        super().setUpClass()
        # Pre-Condition IK disiapkan di sini — BUKAN lewat klik UI.
        cls.env["health.provider_role"].create(
            {
                "name": "TOUR-EDIT-PROVIDER-ROLE",
                "code": "/",
            }
        )
        cls.env["health.provider_role"].create(
            {
                "name": "TOUR-DELETE-PROVIDER-ROLE",
                "code": "/",
            }
        )
        cls.env["health.provider_role"].create(
            {
                "name": "TOUR-DEACTIVATE-PROVIDER-ROLE",
                "code": "/",
            }
        )
        cls.env["health.provider_role"].create(
            {
                "name": "TOUR-ACTIVATE-PROVIDER-ROLE",
                "code": "/",
                "active": False,
            }
        )

    def test_create(self):
        """Run the create tour.

        :return: None

        IK: docs/health_provider_role/01-create.md
        """
        self.start_tour("/web", "ssi_health_health_provider_role_create", login="admin")

    def test_edit(self):
        """Run the edit tour.

        :return: None

        IK: docs/health_provider_role/02-edit.md
        """
        self.start_tour("/web", "ssi_health_health_provider_role_edit", login="admin")

    def test_delete(self):
        """Run the delete tour.

        :return: None

        IK: docs/health_provider_role/03-delete.md
        """
        self.start_tour("/web", "ssi_health_health_provider_role_delete", login="admin")

    def test_deactivate(self):
        """Run the deactivate tour.

        :return: None

        IK: docs/health_provider_role/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_health_health_provider_role_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour.

        :return: None

        IK: docs/health_provider_role/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_health_health_provider_role_activate", login="admin"
        )
