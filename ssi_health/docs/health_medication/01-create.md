# Create Medication

> **Module:** `ssi_health`\
> **Model:** `health.medication`\
> **Menu:** Health > Configuration > Medications\
> **Actor:** user in group _Medication_

## Pre-Condition

- **Access:** user in group _Medication_.

## Flow

1. Open the **Health > Configuration > Medications** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter the name of the medication.
   - **Code**: Enter a unique code identifying this medication. Enter **/** to generate
     the code automatically later using the **Generate Code** button.
4. Click **Save**.
5. Click the **Medications** breadcrumb link to return to the list.

## Post-Condition

- A new Medication record is created and active.
- The new Medication appears in the Medications list view.
