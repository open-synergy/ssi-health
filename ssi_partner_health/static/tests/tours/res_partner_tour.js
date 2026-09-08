/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_partner_health.res_partner_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/res_partner/01-create.md (E1 delta -- Additional Fields)
    //
    // res.partner is extended by ssi_partner, whose base Instruksi Kerja
    // has no navigation steps of its own to reuse here (see the delta's
    // "Extends" line). This tour writes the standard Contacts navigation
    // itself: open the Contacts app, click Create, open the Body
    // Measurements page, then assert every section this module's final
    // form contributes -- both the ones that existed before this item
    // (Heights, Weights, Head Circumferences, Allergies, Disease
    // History) and the ones this item adds (Medications, Family Doctor,
    // Health Facility, Health Providers).
    tour.register(
        "ssi_partner_health_res_partner_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Open the Contacts app.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Contacts app",
                trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
            },
            {
                // Gate: wait for the Contacts action to actually be
                // mounted. Its view_mode starts with "kanban".
                content: "Contacts kanban view is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Contacts)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // ── Click Create.
            {
                content: "Click Create",
                trigger: ".o-kanban-button-new",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // ── Open the Body Measurements page. It is appended after
            // the base notebook pages, so it is not active by default.
            {
                content: "Open the Body Measurements tab",
                trigger: ".o_notebook .nav-link:contains(Body Measurements)",
            },

            // ── Additional Fields (docs/res_partner/01-create.md).
            // Pre-existing sections (not touched by this item, but
            // documented here since this is the module's first tour).
            {
                content: "Heights section is displayed",
                trigger: ".o_horizontal_separator:contains(Height)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Weights section is displayed",
                trigger: ".o_horizontal_separator:contains(Weight)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Head Circumferences section is displayed",
                trigger: ".o_horizontal_separator:contains(Head Circumference)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Allergies section is displayed",
                trigger: ".o_horizontal_separator:contains(Allergies)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Disease History section is displayed",
                trigger: ".o_horizontal_separator:contains(Disease History)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // ── Sections added by this item.
            {
                content: "Medications section is displayed",
                trigger: ".o_horizontal_separator:contains(Medications)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Family Doctor field is displayed",
                trigger: ".o_form_label:contains(Family Doctor)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Health Facility field is displayed",
                trigger: ".o_form_label:contains(Health Facility)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Health Providers section is displayed",
                trigger: ".o_horizontal_separator:contains(Health Providers)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ]
    );
});
