# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerHeight(models.Model):
    """
    Represents a single height measurement of a contact, in centimeters.
    """

    _name = "partner.height"
    _inherit = ["partner.body_measurement.mixin"]
    _description = "Partner Height"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this height measurement belongs to.",
    )
    value = fields.Float(
        string="Height (cm)",
        required=True,
        help="Height measurement in centimeters. Must be greater than zero.",
    )
