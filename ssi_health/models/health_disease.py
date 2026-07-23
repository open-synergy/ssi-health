# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class HealthDisease(models.Model):
    """
    Represents a disease as master data.
    A disease may optionally be classified under a DSM-5 diagnostic class.
    """

    _name = "health.disease"
    _inherit = ["mixin.master_data"]
    _description = "Disease"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="health.disease_category",
        required=False,
        ondelete="restrict",
    )
