# Deactivate Allergen Reaction

> **Module:** `ssi_health`\
> **Model:** `health.allergen_reaction`\
> **Menu:** Health > Configuration > Allergen Reactions\
> **Actor:** user in group _Allergen Reaction_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** user in group _Allergen Reaction_.

## Flow

1. Open the **Health > Configuration > Allergen Reactions** menu.
2. Open the Allergen Reaction record to deactivate.
3. Click the **Edit** button.
4. Toggle the **Active** field off.
5. Click **Save**.

## Post-Condition

- The record is archived; an **Archived** ribbon appears on the form.
- The record no longer appears in the default list view.
- Deactivated Allergen Reactions cannot be selected in new records.
