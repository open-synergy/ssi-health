# Deactivate Health Provider Role

> **Module:** `ssi_health`\
> **Model:** `health.provider_role`\
> **Menu:** Health > Configuration > Provider Roles\
> **Actor:** user in group _Health Provider Role_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** user in group _Health Provider Role_.

## Flow

1. Open the **Health > Configuration > Provider Roles** menu.
2. Open the Health Provider Role record to deactivate.
3. Click the **Edit** button.
4. Toggle the **Active** field off.
5. Click **Save**.

## Post-Condition

- The record is archived; an **Archived** ribbon appears on the form.
- The record no longer appears in the default list view.
- Deactivated Health Provider Roles cannot be selected in new records.
