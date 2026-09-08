# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class HealthProviderRole(models.Model):
    """
    Represents a role a contact can play as a health care provider.
    Used to classify contacts such as physicians or health facilities.
    """

    _name = "health.provider_role"
    _inherit = ["mixin.master_data"]
    _description = "Health Provider Role"

    provider_type = fields.Selection(
        string="Provider Type",
        selection=[
            ("individual", "Individual"),
            ("organization", "Organization"),
        ],
        required=True,
        default="individual",
        help="Whether this role applies to an individual person (e.g. a "
        "physician) or to an organization (e.g. a health facility).",
    )
