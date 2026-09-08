# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

FREQUENCY_SELECTION = [
    ("od", "Once a day"),
    ("bd", "Twice a day"),
    ("tds", "Three times a day"),
    ("qds", "Four times a day"),
    ("prn", "As needed (PRN)"),
    ("other", "Other"),
]

ROUTE_SELECTION = [
    ("oral", "Oral"),
    ("topical", "Topical"),
    ("injection", "Injection"),
    ("inhalation", "Inhalation"),
    ("other", "Other"),
]


class PartnerMedication(models.Model):
    """
    Represents a medication a contact is or was taking, with dose,
    frequency, route, and the period it was taken. A medication may be
    recorded more than once for the same contact to reflect a change
    in dose or a repeated course.
    """

    _name = "partner.medication"
    _description = "Partner Medication"
    _order = "date_start desc, id desc"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Contact this medication belongs to.",
    )
    medication_id = fields.Many2one(
        string="Medication",
        comodel_name="health.medication",
        required=True,
        ondelete="restrict",
        help="Medication the contact is taking.",
    )
    disease_history_id = fields.Many2one(
        string="Disease History",
        comodel_name="partner.disease_history",
        ondelete="set null",
        help="Disease history entry this medication was prescribed "
        "for, if any. Optional.",
    )
    dose = fields.Char(
        string="Dose",
        help="Free-text dose, e.g. '500mg'.",
    )
    frequency = fields.Selection(
        string="Frequency",
        selection=FREQUENCY_SELECTION,
        required=True,
        default="od",
        help="How often the medication is taken.",
    )
    route = fields.Selection(
        string="Route",
        selection=ROUTE_SELECTION,
        required=True,
        default="oral",
        help="How the medication is administered.",
    )
    date_start = fields.Date(
        string="Start Date",
        required=True,
        default=fields.Date.context_today,
        help="Date the contact started taking this medication.",
    )
    date_end = fields.Date(
        string="End Date",
        help="Date the contact stopped taking this medication. Leave "
        "empty while the medication is still ongoing.",
    )
    is_ongoing = fields.Boolean(
        string="Ongoing",
        compute="_compute_is_ongoing",
        store=True,
        compute_sudo=True,
        help="Automatically filled: checked while End Date is empty.",
    )
    instruction = fields.Text(
        string="Instruction",
        help="Additional instruction for taking this medication.",
    )

    @api.depends(
        "date_end",
    )
    def _compute_is_ongoing(self):
        """Flag a medication as ongoing while it has no end date.

        :return: nothing; assigns ``is_ongoing``
        """
        for record in self:
            result = not record.date_end
            record.is_ongoing = result

    @api.constrains(
        "date_start",
        "date_end",
    )
    def _check_date_end(self):
        """Forbid an end date earlier than the start date.

        :raises UserError: when ``date_end`` is set and earlier than
            ``date_start``.
        """
        for record in self:
            if not (record.date_start and record.date_end):
                continue
            if record.date_end < record.date_start:
                msg = _("End date cannot be earlier than start date")
                raise UserError(msg)
