# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models


class HealthAllergenCategory(models.Model):
    """
    Represents a flat grouping used to categorize allergens.
    Allergen categories are not nested, unlike disease categories.
    """

    _name = "health.allergen_category"
    _inherit = ["mixin.master_data"]
    _description = "Allergen Category"
