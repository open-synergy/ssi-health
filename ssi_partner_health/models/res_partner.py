# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    height_ids = fields.One2many(
        comodel_name="partner.height",
        inverse_name="partner_id",
        string="Heights",
        help="Height measurement history of this contact.",
    )
    weight_ids = fields.One2many(
        comodel_name="partner.weight",
        inverse_name="partner_id",
        string="Weights",
        help="Weight measurement history of this contact.",
    )
    head_circumference_ids = fields.One2many(
        comodel_name="partner.head_circumference",
        inverse_name="partner_id",
        string="Head Circumferences",
        help="Head circumference measurement history of this contact.",
    )
    height = fields.Float(
        string="Height (cm)",
        compute="_compute_height",
        store=True,
        compute_sudo=True,
        help="Latest recorded height (cm), taken from the most recent "
        "entry in the height history. 0.0 if no measurement is recorded.",
    )
    weight = fields.Float(
        string="Weight (kg)",
        compute="_compute_weight",
        store=True,
        compute_sudo=True,
        help="Latest recorded weight (kg), taken from the most recent "
        "entry in the weight history. 0.0 if no measurement is recorded.",
    )
    head_circumference = fields.Float(
        string="Head Circumference (cm)",
        compute="_compute_head_circumference",
        store=True,
        compute_sudo=True,
        help="Latest recorded head circumference (cm), taken from the "
        "most recent entry in the head circumference history. 0.0 if no "
        "measurement is recorded.",
    )

    @api.depends(
        "height_ids",
        "height_ids.date",
        "height_ids.value",
    )
    def _compute_height(self):
        for record in self:
            record.height = record.height_ids[0].value if record.height_ids else 0.0

    @api.depends(
        "weight_ids",
        "weight_ids.date",
        "weight_ids.value",
    )
    def _compute_weight(self):
        for record in self:
            record.weight = record.weight_ids[0].value if record.weight_ids else 0.0

    @api.depends(
        "head_circumference_ids",
        "head_circumference_ids.date",
        "head_circumference_ids.value",
    )
    def _compute_head_circumference(self):
        for record in self:
            record.head_circumference = (
                record.head_circumference_ids[0].value
                if record.head_circumference_ids
                else 0.0
            )
