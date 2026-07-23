# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class HealthDiseaseCategory(models.Model):
    """
    Represents a DSM-5 diagnostic class used to categorize diseases.
    Categories can be nested to represent classes and sub-classes.
    """

    _name = "health.disease_category"
    _inherit = ["mixin.master_data"]
    _description = "Disease Category"
    _parent_name = "parent_id"

    parent_id = fields.Many2one(
        string="Parent Category",
        comodel_name="health.disease_category",
        ondelete="restrict",
    )
