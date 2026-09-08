# Deactivate Medication

> **Module:** `ssi_health`\
> **Model:** `health.medication`\
> **Menu:** Health > Configuration > Medications\
> **Actor:** user in group _Medication_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** user in group _Medication_.

## Flow

1. Open the **Health > Configuration > Medications** menu.
2. Open the Medication record to deactivate.
3. Click the **Edit** button.
4. Toggle the **Active** field off.
5. Click **Save**.

## Post-Condition

- The record is archived; an **Archived** ribbon appears on the form.
- The record no longer appears in the default list view.
- Deactivated Medications cannot be selected in new records.
