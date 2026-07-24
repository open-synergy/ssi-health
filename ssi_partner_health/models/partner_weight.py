# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerWeight(models.Model):
    """
    Represents a single weight measurement of a contact, in kilograms.
    """

    _name = "partner.weight"
    _inherit = ["partner.body_measurement.mixin"]
    _description = "Partner Weight"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this weight measurement belongs to.",
    )
    value = fields.Float(
        string="Weight (kg)",
        required=True,
        help="Weight measurement in kilograms. Must be greater than zero.",
    )
