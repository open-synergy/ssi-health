# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPartnerAllergy(YamlTransactionCase):
    """Cover CRUD and reaction handling of ``partner.allergy``."""

    def test_partner_allergy(self):
        """Run the partner allergy scenarios."""
        self.run_yaml_scenario("test_data_partner_allergy.yaml")
