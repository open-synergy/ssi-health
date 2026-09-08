# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models


class HealthMedication(models.Model):
    """
    Represents a medication as master data.
    Used as a controlled vocabulary for a patient's ongoing medications.
    """

    _name = "health.medication"
    _inherit = ["mixin.master_data"]
    _description = "Medication"
