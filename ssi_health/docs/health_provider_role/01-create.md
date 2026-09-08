# Create Health Provider Role

> **Module:** `ssi_health`\
> **Model:** `health.provider_role`\
> **Menu:** Health > Configuration > Provider Roles\
> **Actor:** user in group _Health Provider Role_

## Pre-Condition

- **Access:** user in group _Health Provider Role_.

## Flow

1. Open the **Health > Configuration > Provider Roles** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter the name of the provider role.
   - **Code**: Enter a unique code identifying this provider role. Enter **/** to
     generate the code automatically later using the **Generate Code** button.
   - **Provider Type**: Select whether this role applies to an **Individual** or an
     **Organization**. Defaults to **Individual** if left unchanged.
4. Click **Save**.
5. Click the **Provider Roles** breadcrumb link to return to the list.

## Post-Condition

- A new Health Provider Role record is created and active.
- The new Health Provider Role appears in the Provider Roles list view.
