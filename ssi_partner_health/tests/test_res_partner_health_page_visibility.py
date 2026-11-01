# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestResPartnerHealthPageVisibility(YamlTransactionCase):
    """Cover visibility of the health page on the contact form."""

    def setUp(self):
        """Create an internal user with and one without the health group.

        Fixtures live in ``setUp`` because the base class does not
        provide ``cls.env``. Only users are created, so no record owned
        by the superuser is read back as a restricted user.
        """
        super().setUp()
        obj_user = self.env["res.users"].with_context(no_reset_password=True)
        group_user = self.env.ref("base.group_user")
        group_health = self.env.ref("ssi_partner_health.partner_health_group")
        self.user_plain = obj_user.create(
            {
                "name": "Plain Internal User",
                "login": "plain_page_visibility@example.com",
                "groups_id": [(6, 0, [group_user.id])],
            }
        )
        self.user_health = obj_user.create(
            {
                "name": "Health Internal User",
                "login": "member_page_visibility@example.com",
                "groups_id": [(6, 0, [group_user.id, group_health.id])],
            }
        )

    def _get_form_arch(self, user):
        """Return the contact form arch as rendered for a user.

        Pure Python test, trigger P1 (L-01: the ``call`` action discards
        the return value of ``fields_view_get``).

        :param user: ``res.users`` record to read the view as.
        :return: the processed form arch as a string.
        """
        view = self.env.ref("base.view_partner_form")
        result = (
            self.env["res.partner"]
            .with_user(user)
            .fields_view_get(view_id=view.id, view_type="form")
        )
        return result["arch"]

    def test_page_hidden_without_group(self):
        """The page is absent from the form arch of a non-member.

        Pure Python test, trigger P1 (L-01: ``fields_view_get`` return
        value cannot be captured by the ``call`` action).
        """
        arch = self._get_form_arch(self.user_plain)
        self.assertNotIn('name="body_measurement"', arch)

    def test_page_visible_with_group(self):
        """The page is present in the form arch of a group member.

        Pure Python test, trigger P1 (L-01: ``fields_view_get`` return
        value cannot be captured by the ``call`` action).
        """
        arch = self._get_form_arch(self.user_health)
        self.assertIn('name="body_measurement"', arch)
