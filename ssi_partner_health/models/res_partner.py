# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    """
    Adds health-related fields to contacts: body measurement history,
    allergies, disease history, medications, and health care
    providers (family doctor / health facility).
    """

    _inherit = "res.partner"

    height_ids = fields.One2many(
        comodel_name="partner.height",
        inverse_name="partner_id",
        string="Heights",
        help="Height measurement history of this contact.",
    )
    weight_ids = fields.One2many(
        comodel_name="partner.weight",
        inverse_name="partner_id",
        string="Weights",
        help="Weight measurement history of this contact.",
    )
    head_circumference_ids = fields.One2many(
        comodel_name="partner.head_circumference",
        inverse_name="partner_id",
        string="Head Circumferences",
        help="Head circumference measurement history of this contact.",
    )
    allergy_ids = fields.One2many(
        comodel_name="partner.allergy",
        inverse_name="partner_id",
        string="Allergies",
        help="Allergies recorded for this contact.",
    )
    disease_history_ids = fields.One2many(
        comodel_name="partner.disease_history",
        inverse_name="partner_id",
        string="Disease History",
        help="Disease history recorded for this contact.",
    )
    medication_ids = fields.One2many(
        comodel_name="partner.medication",
        inverse_name="partner_id",
        string="Medications",
        help="Medications recorded for this contact.",
    )
    health_provider_ids = fields.One2many(
        comodel_name="partner.health_provider",
        inverse_name="partner_id",
        string="Health Providers",
        help="Health care providers recorded for this contact.",
    )
    family_doctor_id = fields.Many2one(
        string="Family Doctor",
        comodel_name="res.partner",
        compute="_compute_family_doctor_id",
        store=True,
        compute_sudo=True,
        help="Automatically filled: the individual provider with the "
        "lowest Sequence in Health Providers.",
    )
    health_facility_id = fields.Many2one(
        string="Health Facility",
        comodel_name="res.partner",
        compute="_compute_health_facility_id",
        store=True,
        compute_sudo=True,
        help="Automatically filled: the organization provider with "
        "the lowest Sequence in Health Providers.",
    )
    height = fields.Float(
        string="Height (cm)",
        compute="_compute_height",
        store=True,
        compute_sudo=True,
        help="Latest recorded height (cm), taken from the most recent "
        "entry in the height history. 0.0 if no measurement is recorded.",
    )
    weight = fields.Float(
        string="Weight (kg)",
        compute="_compute_weight",
        store=True,
        compute_sudo=True,
        help="Latest recorded weight (kg), taken from the most recent "
        "entry in the weight history. 0.0 if no measurement is recorded.",
    )
    head_circumference = fields.Float(
        string="Head Circumference (cm)",
        compute="_compute_head_circumference",
        store=True,
        compute_sudo=True,
        help="Latest recorded head circumference (cm), taken from the "
        "most recent entry in the head circumference history. 0.0 if no "
        "measurement is recorded.",
    )

    @api.depends(
        "height_ids",
        "height_ids.date",
        "height_ids.value",
    )
    def _compute_height(self):
        for record in self:
            record.height = record.height_ids[0].value if record.height_ids else 0.0

    @api.depends(
        "weight_ids",
        "weight_ids.date",
        "weight_ids.value",
    )
    def _compute_weight(self):
        for record in self:
            record.weight = record.weight_ids[0].value if record.weight_ids else 0.0

    @api.depends(
        "head_circumference_ids",
        "head_circumference_ids.date",
        "head_circumference_ids.value",
    )
    def _compute_head_circumference(self):
        for record in self:
            record.head_circumference = (
                record.head_circumference_ids[0].value
                if record.head_circumference_ids
                else 0.0
            )

    @api.depends(
        "health_provider_ids",
        "health_provider_ids.sequence",
        "health_provider_ids.provider_id",
        "health_provider_ids.provider_id.is_company",
    )
    def _compute_family_doctor_id(self):
        """Set the top-ranked individual provider as family doctor.

        :return: nothing; assigns ``family_doctor_id``
        """
        for record in self:
            result = False
            candidates = record.health_provider_ids.filtered(
                lambda line: not line.provider_id.is_company
            ).sorted(key=lambda line: (line.sequence, line.id))
            if candidates:
                result = candidates[:1].provider_id
            record.family_doctor_id = result

    @api.depends(
        "health_provider_ids",
        "health_provider_ids.sequence",
        "health_provider_ids.provider_id",
        "health_provider_ids.provider_id.is_company",
    )
    def _compute_health_facility_id(self):
        """Set the top-ranked organization provider as facility.

        :return: nothing; assigns ``health_facility_id``
        """
        for record in self:
            result = False
            candidates = record.health_provider_ids.filtered(
                lambda line: line.provider_id.is_company
            ).sorted(key=lambda line: (line.sequence, line.id))
            if candidates:
                result = candidates[:1].provider_id
            record.health_facility_id = result
