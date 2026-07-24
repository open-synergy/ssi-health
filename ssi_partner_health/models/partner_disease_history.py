# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PartnerDiseaseHistory(models.Model):
    """
    Represents a disease a contact has been diagnosed with, and its
    diagnosis/recovery dates. A disease may be recorded more than once for
    the same contact to reflect a relapse.
    """

    _name = "partner.disease_history"
    _description = "Partner Disease History"
    _order = "date_diagnosed desc, id desc"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this disease history belongs to.",
    )
    disease_id = fields.Many2one(
        string="Disease",
        comodel_name="health.disease",
        required=True,
        ondelete="restrict",
        help="Disease the contact has been diagnosed with.",
    )
    date_diagnosed = fields.Date(
        string="Date Diagnosed",
        help="Date the contact was diagnosed with this disease.",
    )
    date_recovered = fields.Date(
        string="Date Recovered",
        help="Date the contact recovered from this disease.",
    )
    note = fields.Text(
        string="Note",
        help="Additional information about this disease history.",
    )

    @api.constrains(
        "date_diagnosed",
        "date_recovered",
    )
    def _check_date_recovered(self):
        for record in self:
            if not (record.date_diagnosed and record.date_recovered):
                continue
            if record.date_recovered < record.date_diagnosed:
                msg = _("Date recovered cannot be earlier than date diagnosed")
                raise UserError(msg)
