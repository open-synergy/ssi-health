# Activate Medication

> **Module:** `ssi_health`\
> **Model:** `health.medication`\
> **Menu:** Health > Configuration > Medications\
> **Actor:** user in group _Medication_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The Medication is archived (inactive).
- **Access:** user in group _Medication_.

## Flow

1. Open the **Health > Configuration > Medications** menu.
2. Enable the **Archived** filter in the search bar.
3. Open the archived Medication record to reactivate.
4. Click the **Edit** button.
5. Toggle the **Active** field on.
6. Click **Save**.

## Post-Condition

- The record is restored and appears again in the default list view.
- The **Archived** ribbon no longer appears on the form.
