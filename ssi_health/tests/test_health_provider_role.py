# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHealthProviderRole(YamlTransactionCase):
    """Run the Health Provider Role YAML scenarios."""

    def test_health_provider_role(self):
        """Run every scenario declared in the YAML fixture.

        :return: None
        """
        self.run_yaml_scenario("test_data_health_provider_role.yaml")
