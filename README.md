Excel Schema Extractor & Data Dictionary Generator
A lightweight, memory-efficient Python tool designed to automate the initial discovery phase of legacy Excel migrations to relational database management systems (RDBMS).
This utility safely scans directories containing multiple .xlsx / .xls spreadsheets, inspects column names and infers data types, and exports a unified data dictionary into a standalone SQLite database for easy analysis in SQL clients like DBeaver.

🔑 Key Features
    • Zero Data Overwrite Guarantee: Operates strictly on a read-only logic layer to preserve source files intact.
    • Low-Memory Footprint: Uses chunked/partial reading via Pandas (nrows=5) to safely process massive spreadsheet collections on constrained hardware (e.g., 8 GB RAM).
    • Automated Schema Discovery: Detects all worksheets per workbook, pulls header names, and infers preliminary SQL/Pandas data types.
    • DBeaver & SQLite Native Integration: Instantly dumps extracted schema metadata into an indexed SQLite table (esquema_excels) for rapid SQL querying.
    • Data Security Ready: Pre-configured with .gitignore rules to prevent sensitive client data or raw spreadsheets from being exposed to remote VCS repositories.

🛠️ Architecture & Tech Stack
    • Language: Python 3.8+
    • Data Manipulation: pandas, openpyxl
    • Database Engine: SQLite3 (Native Python library)
    • Target DB Client: DBeaver, VS Code SQLite Viewers, SQLite CLI

📁 Repository Structure
excel-schema-extractor/
├── datos_origen/              # Directory for raw Excel source files (git-ignored)
├── salida_bd/                 # Output directory for generated SQLite files (git-ignored)
│   └── metadatos.db           # Output database file
├── extractor_metadatos.py     # Main metadata parser script
├── .gitignore                 # Security rules to keep data files local
└── README.md                  # Project documentation

🚀 Quickstart Guide
1. Prerequisites & Environment Setup
Clone the repository and navigate into the project directory:
git clone https://github.com/your-username/excel-schema-extractor.git
cd excel-schema-extractor
Create and activate a virtual environment (optional but recommended):
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/macOS
python3 -m venv venv
source venv/bin/activate
Install required dependencies:
pip install pandas openpyxl
2. File Setup
Place all .xlsx or .xls spreadsheets you want to inspect inside the datos_origen/ folder:
mkdir -p datos_origen salida_bd
3. Run the Extractor
Execute the main execution script:
python extractor_metadatos.py
Upon execution, the script will iterate over all spreadsheets, inspect every sheet, log completion progress in the terminal, and output the database file at salida_bd/metadatos.db.

🔍 Inspecting Extracted Schemas
Open salida_bd/metadatos.db in DBeaver or your preferred database client. Run queries against the esquema_excels table to analyze your target tables:
-- View all unique column names across all files
SELECT DISTINCT columna, tipo_dato 
FROM esquema_excels;

-- Count total worksheets parsed per Excel file
SELECT archivo, COUNT(DISTINCT hoja) AS total_hojas 
FROM esquema_excels 
GROUP BY archivo;

🛡️ Security & Privacy Note
This repository enforces strict strict .gitignore rules to comply with enterprise security policies:
    • Raw spreadsheets (*.xlsx, *.xls, *.csv) are never tracked.
    • Local database instances (*.db, *.sqlite) are never committed.
Only core Python logic, documentation, and structural templates are pushed to remote repositories.

📜 License
Distributed under the MIT License. See LICENSE for more information.
