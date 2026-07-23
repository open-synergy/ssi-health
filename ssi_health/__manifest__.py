# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Health",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_master_data_mixin",
        "web_tour",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_groups/health_disease_category.xml",
        "security/res_groups/health_disease.xml",
        "security/res_groups/health_allergen_category.xml",
        "security/res_groups/health_allergen.xml",
        "security/ir_model_access/health_disease_category.xml",
        "security/ir_model_access/health_disease.xml",
        "security/ir_model_access/health_allergen_category.xml",
        "security/ir_model_access/health_allergen.xml",
        "data/health_disease_category_data.xml",
        "data/health_allergen_category_data.xml",
        "menu.xml",
        "views/health_disease_category_views.xml",
        "views/health_disease_views.xml",
        "views/health_allergen_category_views.xml",
        "views/health_allergen_views.xml",
        "views/assets.xml",
    ],
    "demo": [],
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
}
