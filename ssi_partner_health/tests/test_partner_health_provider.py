# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPartnerHealthProvider(YamlTransactionCase):
    """Cover CRUD, ranking, and validation of ``partner.health_provider``.

    Also covers the ``family_doctor_id``/``health_facility_id`` compute
    on ``res.partner`` derived from this model's rows.
    """

    def test_partner_health_provider(self):
        """Run the partner health provider scenarios."""
        self.run_yaml_scenario("test_data_partner_health_provider.yaml")
