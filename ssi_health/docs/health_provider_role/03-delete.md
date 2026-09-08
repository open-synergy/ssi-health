# Delete Health Provider Role

> **Module:** `ssi_health`\
> **Model:** `health.provider_role`\
> **Menu:** Health > Configuration > Provider Roles\
> **Actor:** user in group _Health Provider Role_\
> **Requires:** `01-create`

## Pre-Condition

- **Access:** user in group _Health Provider Role_.

## Flow

1. Open the **Health > Configuration > Provider Roles** menu.
2. Open the Health Provider Role record to delete.
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.
5. Click the **Provider Roles** breadcrumb link to return to the list.

## Post-Condition

- The record is permanently removed from the system.
- After deleting, the form shows the next record in the list (or returns to the list
  directly if none remain).
- The list view no longer shows the deleted record.
