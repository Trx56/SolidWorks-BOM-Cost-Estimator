# SolidWorks BOM Cost Estimator 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**SolidWorks BOM Cost Estimator** is a data analysis script utilizing Python and Pandas to process exported SolidWorks Bill of Materials (BOM) files. It bridges mechanical design and industrial engineering by automatically mapping raw material prices to CAD-generated mass data, outputting total assembly weights and manufacturing cost estimates.

---

## Key Features

* **Automated BOM Parsing:** Reads a SolidWorks-style BOM in CSV format (a sample BOM is embedded in the script).
* **Dynamic Cost Mapping:** assumed raw material costs per kilogram (editable in the script).
* **Mass & Budget Aggregation:** Automatically calculates per-part cost/weight parameters and generates a final summation for the entire machine assembly layout.
* **Financial Reporting:** Outputs a clean, terminal-based engineering cost report ready for facility planning and manufacturing budgeting.

---

## Tech Stack & Libraries
* **Language:** Python
* **Data Analysis:** Pandas (DataFrames)

---

## Code Architecture
```text
 SolidWorks-BOM-Cost-Estimator
 ┣ bom_estimator.py    # Pandas DataFrame logic and material cost mapping
 ┗ README.md           # Project documentation

## How to Run

pip install pandas
python bom_estimator.py

## Data Note

The parts list and material prices are sample values for demonstration. To use a real SolidWorks export, replace the embedded CSV with `pd.read_csv("your_bom.csv")` using the same columns: Part Number, Description, Material, Quantity, Unit Mass (kg).
