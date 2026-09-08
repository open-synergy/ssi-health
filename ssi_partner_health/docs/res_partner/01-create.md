# Create Contact

> **Module:** `ssi_partner_health`\
> **Extends:** ssi_partner — model `res.partner`, aksi `01-create`

## Additional Fields

When this module is installed, the Contacts form gains a **Body Measurements** page
(individual contacts only, i.e. **Individual** is selected instead of **Company**), with
the following sections.

- **Heights**: One or more height measurements over time. Optional — zero or more rows
  may be added. Each row has:
  - **Date**: Date the measurement was taken. Required per row.
  - **Value**: Height in centimeters. Required per row.
- **Weights**: One or more weight measurements over time. Optional. Each row has:
  - **Date**: Date the measurement was taken. Required per row.
  - **Value**: Weight in kilograms. Required per row.
- **Head Circumferences**: One or more head circumference measurements over time.
  Optional. Each row has:
  - **Date**: Date the measurement was taken. Required per row.
  - **Value**: Head circumference in centimeters. Required per row.
- **Allergies**: One or more allergens the contact is allergic to. Optional. Each row
  has:
  - **Allergen**: The allergen, selected from the **Allergen** master data. Required per
    row. The same allergen cannot be recorded twice for the same contact.
  - **Severity**: One of Mild, Moderate, Severe. Defaults to Mild.
  - **Reactions**: One or more clinical manifestations observed for this allergy,
    selected from the **Allergen Reaction** master data, shown as tags. Optional — zero
    or more may be selected.
  - **Note**: Free-text note. Optional.
- **Disease History**: One or more diseases the contact has been diagnosed with.
  Optional. Each row has:
  - **Disease**: The disease, selected from the **Disease** master data. Required per
    row.
  - **Date Diagnosed**: Date of diagnosis. Optional.
  - **Date Recovered**: Date of recovery. Optional. Must not be earlier than **Date
    Diagnosed**.
  - **Note**: Free-text note. Optional.
- **Medications**: One or more medications the contact is or was taking. Optional. Each
  row has:
  - **Medication**: The medication, selected from the **Medication** master data.
    Required per row. The same medication may be recorded more than once for the same
    contact.
  - **Dose**: Free-text dose, e.g. `500mg`. Optional.
  - **Frequency**: One of Once a day, Twice a day, Three times a day, Four times a day,
    As needed (PRN), Other. Defaults to Once a day.
  - **Route**: One of Oral, Topical, Injection, Inhalation, Other. Defaults to Oral.
  - **Start Date**: Date the contact started taking this medication. Required per row.
    Defaults to today.
  - **End Date**: Date the contact stopped taking this medication. Optional. Leave empty
    while still ongoing. Must not be earlier than **Start Date**.
  - **Ongoing**: Automatically filled from **End Date** — checked while **End Date** is
    empty.
  - **Disease History**: The disease history entry this medication was prescribed for,
    if any. Optional, hidden by default (available from the column selector).
  - **Instruction**: Free-text instruction for taking this medication. Optional.
- **Family Doctor**: Read-only. Automatically filled from **Health Providers** — shows
  the individual provider with the lowest **Sequence** in the list below. Empty when no
  individual provider row exists.
- **Health Facility**: Read-only. Automatically filled from **Health Providers** — shows
  the organization provider with the lowest **Sequence** in the list below. Empty when
  no organization provider row exists.
- **Health Providers**: One or more health care providers (physicians or facilities)
  linked to this contact. Optional. Each row has:
  - **Sequence**: Drag handle used to reorder the rows. The top individual row
    determines **Family Doctor**; the top organization row determines **Health
    Facility**. Defaults to `10`.
  - **Provider**: The provider contact, selected from contacts in the Health
    Practitioner or Health Facility category. Required per row. The same provider cannot
    be recorded twice for the same contact.
  - **Role**: Descriptive role of this provider, e.g. General Practitioner, selected
    from the **Health Provider Role** master data. Optional, does not affect ranking.
  - **Start Date**: Date the contact started being served by this provider. Optional.
  - **Note**: Free-text note. Optional.

## Modified Validation

- Saving an allergy row fails with a validation error if the same **Allergen** is
  already recorded for this contact.
- Saving a medication row fails with a validation error if **End Date** is set and
  earlier than **Start Date**.
- Saving a health provider row fails with a validation error if the same **Provider** is
  already recorded for this contact.
