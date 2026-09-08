# Activate Health Provider Role

> **Module:** `ssi_health`\
> **Model:** `health.provider_role`\
> **Menu:** Health > Configuration > Provider Roles\
> **Actor:** user in group _Health Provider Role_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The Health Provider Role is archived (inactive).
- **Access:** user in group _Health Provider Role_.

## Flow

1. Open the **Health > Configuration > Provider Roles** menu.
2. Enable the **Archived** filter in the search bar.
3. Open the archived Health Provider Role record to reactivate.
4. Click the **Edit** button.
5. Toggle the **Active** field on.
6. Click **Save**.

## Post-Condition

- The record is restored and appears again in the default list view.
- The **Archived** ribbon no longer appears on the form.
