import pandas as pd
import io

# We use io.StringIO to simulate a CSV file exported directly from SolidWorks
solidworks_bom_csv = """Part Number,Description,Material,Quantity,Unit Mass (kg)
SW-001,Universal Coupling Hub,Steel,2,1.4
SW-002,Center Block,Bronze,1,0.8
SW-003,Knuckle Pin,High-Carbon Steel,1,0.3
SW-004,Base Flange,Aluminum,1,2.1
SW-005,Fastener M8,Steel,4,0.02
"""

# Dictionary to simulate real-world raw material costs per kg ($)
material_costs_per_kg = {
    'Steel': 2.50,
    'Bronze': 8.00,
    'High-Carbon Steel': 3.50,
    'Aluminum': 4.20
}

# Load the BOM into a Pandas DataFrame
df = pd.read_csv(io.StringIO(solidworks_bom_csv))

# Calculate total mass for each line item
df['Total Mass (kg)'] = df['Quantity'] * df['Unit Mass (kg)']

# Map the material cost per kg and calculate the total cost per line item
df['Cost per kg ($)'] = df['Material'].map(material_costs_per_kg)
df['Total Cost ($)'] = df['Total Mass (kg)'] * df['Cost per kg ($)']

# Display the processed Engineering BOM
print("--- Automated SolidWorks BOM Cost Report ---")
print(df[['Part Number', 'Description', 'Total Mass (kg)', 'Total Cost ($)']].to_string(index=False))

# Calculate Assembly Totals
total_assembly_mass = df['Total Mass (kg)'].sum()
total_assembly_cost = df['Total Cost ($)'].sum()

print("-" * 45)
print(f"Total Assembly Mass: {total_assembly_mass:.2f} kg")
print(f"Estimated Material Cost: ${total_assembly_cost:.2f}")
