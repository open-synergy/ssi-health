# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class HealthAllergen(models.Model):
    """
    Represents an allergen as master data.
    An allergen may optionally be grouped under an allergen category.
    """

    _name = "health.allergen"
    _inherit = ["mixin.master_data"]
    _description = "Allergen"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="health.allergen_category",
        required=False,
        ondelete="restrict",
    )
