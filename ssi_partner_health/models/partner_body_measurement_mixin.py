# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PartnerBodyMeasurementMixin(models.AbstractModel):
    """
    Abstract base for a single anthropometric measurement record.

    Concrete models (height, weight, head circumference) inherit this mixin
    to store one dated measurement value each. Keeping every measurement as
    its own record (instead of a single static value) preserves the full
    measurement history of a contact.
    """

    _name = "partner.body_measurement.mixin"
    _description = "Abstract Class for Partner Body Measurement"
    _order = "date desc, id desc"

    date = fields.Date(
        string="Date",
        required=True,
        default=lambda self: datetime.date.today(),
        help="Date the measurement was taken.",
    )
    value = fields.Float(
        string="Value",
        required=True,
        help="Measured value. Must be greater than zero.",
    )

    @api.constrains("value")
    def _check_value(self):
        for record in self.sudo():
            if not record._check_value_condition():
                error_message = """
Document Type: %s
Context: Create/update body measurement
Database ID: %s
Problem: Value must be greater than zero
Solution: Enter a measurement value greater than zero
""" % (
                    record._description,
                    record.id,
                )
                raise UserError(_(error_message))

    def _check_value_condition(self):
        self.ensure_one()
        return self.value > 0
