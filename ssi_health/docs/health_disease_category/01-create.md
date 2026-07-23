# Create Disease Category

## Pre-Condition

- None.

## Flow

1. Open the **Health > Configuration > Disease Categories** menu.
2. Click the **New** button.
3. Fill in the required fields:
   - **Name**: Enter the name of the disease category.
   - **Code**: Enter a unique code identifying this disease category. Enter **/** to
     generate the code automatically later using the **Generate Code** button.
   - **Parent Category**: Select the parent disease category, if this category is a
     sub-class of another category. Leave empty for a top-level category.
4. Click **Save**.

## Post-Condition

- A new Disease Category record is created and active.
- The new Disease Category becomes selectable as a **Parent Category** for other Disease
  Categories and as a **Category** for Disease records.
