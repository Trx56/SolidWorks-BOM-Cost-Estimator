# SolidWorks BOM Cost Estimator 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**SolidWorks BOM Cost Estimator** is a data analysis script utilizing Python and Pandas to process exported SolidWorks Bill of Materials (BOM) files. It bridges mechanical design and industrial engineering by automatically mapping raw material prices to CAD-generated mass data, outputting total assembly weights and manufacturing cost estimates.

---

## Key Features

* **Automated BOM Parsing:** Reads and structures standard CSV outputs exported directly from multi-part SolidWorks machine assemblies (e.g., universal couplings, screw jacks).
* **Dynamic Cost Mapping:** Cross-references CAD part materials (Steel, Aluminum, Bronze, High-Carbon Steel) with a dictionary of real-world raw material costs per kilogram.
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
