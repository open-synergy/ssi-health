# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Partner Health",
    "version": "14.0.1.2.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_partner",
        "ssi_health",
        "web_tour",
    ],
    "data": [
        "security/ir_model_access/partner_height.xml",
        "security/ir_model_access/partner_weight.xml",
        "security/ir_model_access/partner_head_circumference.xml",
        "security/ir_model_access/partner_allergy.xml",
        "security/ir_model_access/partner_disease_history.xml",
        "security/ir_model_access/partner_medication.xml",
        "security/ir_model_access/partner_health_provider.xml",
        "views/res_partner_views.xml",
        "views/assets.xml",
    ],
    "demo": [],
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
}
