# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from lxml import etree
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

    O2M_FIELDS = (
        "height_ids",
        "weight_ids",
        "head_circumference_ids",
        "allergy_ids",
        "disease_history_ids",
        "medication_ids",
        "health_provider_ids",
    )

    def _get_form_arch(self, user):
        """Return the contact form arch as rendered for a user.

        Pure Python test, trigger P1 (L-01: the ``call`` action discards
        the return value of ``fields_view_get``).

        :param user: ``res.users`` record to read the view as.
        :return: the processed form arch as an ``lxml`` element.
        """
        view = self.env.ref("base.view_partner_form")
        result = (
            self.env["res.partner"]
            .with_user(user)
            .fields_view_get(view_id=view.id, view_type="form")
        )
        return etree.fromstring(result["arch"])

    def test_page_hidden_without_group(self):
        """The page is invisible and its O2M fields are dropped.

        Pure Python test, trigger P1 (L-01: ``fields_view_get`` return
        value cannot be captured by the ``call`` action).
        """
        arch = self._get_form_arch(self.user_plain)
        pages = arch.xpath("//page[@name='body_measurement']")
        self.assertEqual(len(pages), 1)
        self.assertEqual(pages[0].get("invisible"), "1")
        for field_name in self.O2M_FIELDS:
            self.assertFalse(
                arch.xpath("//field[@name='%s']" % field_name),
                "%s must not be in the arch" % field_name,
            )

    def test_page_visible_with_group(self):
        """The page is visible and its O2M fields are present.

        Pure Python test, trigger P1 (L-01: ``fields_view_get`` return
        value cannot be captured by the ``call`` action).
        """
        arch = self._get_form_arch(self.user_health)
        pages = arch.xpath("//page[@name='body_measurement']")
        self.assertEqual(len(pages), 1)
        self.assertNotEqual(pages[0].get("invisible"), "1")
        for field_name in self.O2M_FIELDS:
            self.assertTrue(
                arch.xpath("//field[@name='%s']" % field_name),
                "%s must be in the arch" % field_name,
            )
