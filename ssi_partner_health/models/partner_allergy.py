# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

SEVERITY_SELECTION = [
    ("mild", "Mild"),
    ("moderate", "Moderate"),
    ("severe", "Severe"),
]


class PartnerAllergy(models.Model):
    """
    Represents an allergen recorded against a contact, with its severity.
    """

    _name = "partner.allergy"
    _description = "Partner Allergy"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this allergy belongs to.",
    )
    allergen_id = fields.Many2one(
        string="Allergen",
        comodel_name="health.allergen",
        required=True,
        ondelete="restrict",
        help="Allergen the contact is allergic to.",
    )
    severity = fields.Selection(
        string="Severity",
        selection=SEVERITY_SELECTION,
        required=True,
        default="mild",
        help="Severity of the allergic reaction.",
    )
    note = fields.Text(
        string="Note",
        help="Additional information about this allergy.",
    )

    @api.constrains(
        "partner_id",
        "allergen_id",
    )
    def _check_no_duplicate_allergen(self):
        obj_allergy = self.env["partner.allergy"]
        for allergy in self:
            criteria = [
                ("id", "!=", allergy.id),
                ("partner_id", "=", allergy.partner_id.id),
                ("allergen_id", "=", allergy.allergen_id.id),
            ]
            result = obj_allergy.search_count(criteria)
            if result > 0:
                msg = _("No duplicate allergen")
                raise UserError(msg)
