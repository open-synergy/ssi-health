odoo.define("ssi_health.health_medication_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/health_medication/01-create.md
    tour.register(
        "ssi_health_health_medication_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Health > Configuration > Medications menu
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Health app",
                trigger: '.o_app[data-menu-xmlid="ssi_health.menu_health"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.menu_health_configuration"]',
            },
            {
                content: "Open the Medications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.health_medication_menu"]',
            },
            {
                // Guard: opening the Health app lands on the FIRST configuration
                // menu, so the Medications action may still be loading
                // right after the menu click. Wait for its breadcrumb before
                // touching anything.
                content: "Medications list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Medications)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Click the New button
            {
                content: "Click New",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },

            // ── Flow 3 — Fill in the required fields
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-CREATE-MEDICATION",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text /",
            },

            // ── Flow 4 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Medication record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 5 — Click the Medications breadcrumb to return
            // to the list
            {
                content: "Click the Medications breadcrumb",
                trigger: ".breadcrumb-item.o_back_button a:contains(Medications)",
            },

            // ── Post-Condition — The new Medication appears in the list
            {
                content: "New record is shown in the list",
                trigger: ".o_list_view .o_data_row:contains(TOUR-CREATE-MEDICATION)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/health_medication/02-edit.md
    tour.register(
        "ssi_health_health_medication_edit",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Health > Configuration > Medications menu
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Health app",
                trigger: '.o_app[data-menu-xmlid="ssi_health.menu_health"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.menu_health_configuration"]',
            },
            {
                content: "Open the Medications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.health_medication_menu"]',
            },
            {
                content: "Medications list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Medications)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Find and open the Medication record to edit
            {
                content: "Open the medication record",
                trigger:
                    ".o_data_row:contains(TOUR-EDIT-MEDICATION) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 3 — Click the Edit button
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 4 — Change the required fields (Name, Code)
            {
                content: "Change the Name field",
                trigger: ".o_field_widget[name='name']",
                run: "text TOUR-EDIT-MEDICATION UPDATED",
            },

            // ── Flow 5 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // ── Post-Condition — The record is updated with the new values
            {
                content: "Medication record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/health_medication/03-delete.md
    tour.register(
        "ssi_health_health_medication_delete",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Health > Configuration > Medications menu
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Health app",
                trigger: '.o_app[data-menu-xmlid="ssi_health.menu_health"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.menu_health_configuration"]',
            },
            {
                content: "Open the Medications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.health_medication_menu"]',
            },
            {
                content: "Medications list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Medications)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Open the Medication record to delete
            {
                content: "Open the medication record",
                trigger:
                    ".o_data_row:contains(TOUR-DELETE-MEDICATION) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 3 — Click Action > Delete
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Delete",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    // Match the item by its exact label instead of a
                    // substring :contains() selector, so an unrelated item
                    // (e.g. "Archive") can never be picked by mistake.
                    var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Delete";
                        }
                    );
                    $delete[0].click();
                },
            },

            // ── Flow 4 — Click OK to confirm
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // ── Flow 5 — Click the Medications breadcrumb to return
            // to the list (after a delete, the form may show the next record
            // in the list instead of navigating back on its own)
            {
                content: "Click the Medications breadcrumb",
                trigger: ".breadcrumb-item.o_back_button a:contains(Medications)",
            },

            // ── Post-Condition — The record is permanently removed; list no
            // longer shows it
            {
                content: "Record no longer in the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR-DELETE-MEDICATION)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/health_medication/04-deactivate.md
    tour.register(
        "ssi_health_health_medication_deactivate",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Health > Configuration > Medications menu
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Health app",
                trigger: '.o_app[data-menu-xmlid="ssi_health.menu_health"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.menu_health_configuration"]',
            },
            {
                content: "Open the Medications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.health_medication_menu"]',
            },
            {
                content: "Medications list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Medications)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Open the Medication record to deactivate
            {
                content: "Open the medication record",
                trigger:
                    ".o_data_row:contains(TOUR-DEACTIVATE-MEDICATION) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 3 — Click the Edit button
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 4 — Toggle the Active field off
            {
                content: "Toggle the Active field off",
                trigger: ".o_field_widget[name='active'] input",
                run: "click",
            },

            // ── Flow 5 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // ── Post-Condition — Archived ribbon appears on the form
            {
                content: "Archived ribbon is displayed",
                trigger: ".o_form_view .ribbon:contains(Archived)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/health_medication/05-activate.md
    tour.register(
        "ssi_health_health_medication_activate",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Health > Configuration > Medications menu
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Health app",
                trigger: '.o_app[data-menu-xmlid="ssi_health.menu_health"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.menu_health_configuration"]',
            },
            {
                content: "Open the Medications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_health.health_medication_menu"]',
            },
            {
                content: "Medications list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Medications)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Enable the Archived filter in the search bar
            {
                content: "Wait for the list data to finish loading",
                trigger: ".o_list_view .o_data_row",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Filters menu",
                trigger: ".o_filter_menu .o_dropdown_toggler_btn",
                run: function () {
                    // Use the native click() activation instead of the
                    // synthetic mouse-event sequence: this dropdown is an
                    // Owl component whose open state must flip via a real
                    // browser-level click activation.
                    this.$anchor[0].click();
                },
            },
            {
                content: "Enable the Archived filter",
                trigger: ".o_filter_menu .o_menu_item:contains(Archived) a",
                run: function () {
                    this.$anchor[0].click();
                },
            },

            // ── Flow 3 — Open the archived Medication record to
            // reactivate
            {
                content: "Open the archived medication record",
                trigger:
                    ".o_data_row:contains(TOUR-ACTIVATE-MEDICATION) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 4 — Click the Edit button
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 5 — Toggle the Active field on
            {
                content: "Toggle the Active field on",
                trigger: ".o_field_widget[name='active'] input",
                run: "click",
            },

            // ── Flow 6 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // ── Post-Condition — Archived ribbon no longer appears
            {
                content: "Archived ribbon is no longer displayed",
                trigger: ".o_form_view:not(:has(.ribbon:visible:contains(Archived)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
