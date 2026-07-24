# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerHeadCircumference(models.Model):
    """
    Represents a single head circumference measurement of a contact, in
    centimeters.
    """

    _name = "partner.head_circumference"
    _inherit = ["partner.body_measurement.mixin"]
    _description = "Partner Head Circumference"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this head circumference measurement belongs to.",
    )
    value = fields.Float(
        string="Head Circumference (cm)",
        required=True,
        help="Head circumference measurement in centimeters. Must be "
        "greater than zero.",
    )
