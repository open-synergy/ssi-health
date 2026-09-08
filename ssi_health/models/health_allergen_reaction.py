# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models


class HealthAllergenReaction(models.Model):
    """
    Represents a clinical manifestation caused by an allergic reaction.
    Used to classify how a patient reacts to a given allergen.
    """

    _name = "health.allergen_reaction"
    _inherit = ["mixin.master_data"]
    _description = "Allergen Reaction"
