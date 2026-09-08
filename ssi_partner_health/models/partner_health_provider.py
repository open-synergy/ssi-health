# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PartnerHealthProvider(models.Model):
    """
    Represents a health care provider (a physician or a health
    facility) linked to a contact. Providers are ordered by
    ``sequence``; the top-ranked individual and the top-ranked
    organization are surfaced on ``res.partner`` as the contact's
    family doctor and health facility respectively.
    """

    _name = "partner.health_provider"
    _description = "Partner Health Provider"
    _order = "sequence, id"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this health provider is linked to.",
    )
    provider_id = fields.Many2one(
        string="Provider",
        comodel_name="res.partner",
        required=True,
        ondelete="restrict",
        help="The health care provider contact (physician or " "facility).",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=10,
        help="Determines ranking among the contact's providers. The "
        "top individual provider becomes the Family Doctor; the top "
        "organization provider becomes the Health Facility.",
    )
    role_id = fields.Many2one(
        string="Role",
        comodel_name="health.provider_role",
        ondelete="restrict",
        help="Descriptive role of this provider, e.g. General "
        "Practitioner. Optional, does not affect ranking.",
    )
    date_start = fields.Date(
        string="Start Date",
        help="Date this contact started being served by this " "provider.",
    )
    note = fields.Text(
        string="Note",
        help="Additional information about this provider link.",
    )

    @api.constrains(
        "partner_id",
        "provider_id",
    )
    def _check_no_duplicate_provider(self):
        """Forbid recording the same provider twice for one contact.

        :raises UserError: when another ``partner.health_provider``
            row already exists for the same ``partner_id`` and
            ``provider_id``.
        """
        obj_provider = self.env["partner.health_provider"]
        for provider in self:
            criteria = [
                ("id", "!=", provider.id),
                ("partner_id", "=", provider.partner_id.id),
                ("provider_id", "=", provider.provider_id.id),
            ]
            result = obj_provider.search_count(criteria)
            if result > 0:
                msg = _("No duplicate provider")
                raise UserError(msg)
