## Overview

Reverse-engineered the HOSxP database structure of a legacy hospital information system released in 1999, analyzing 15+ OPD-related tables and 1,000,000+ patient records using SQL DESCRIBE queries without a data dictionary, saving THB 300,000 in training costs.

## Tools & Technologies

- **SQL:** Database exploration and schema analysis.
- **Python:** Data extraction and tabular output using Pandas and SQLAlchemy.
- **Database:** MySQL (HOSxP).

## How to Use

### SQL Queries
1. Open the `.sql` file for the query you need.
2. Review the query and adjust table names or conditions if necessary.
3. Execute the query in your SQL editor (e.g., press `F9`, depending on the editor).

### Python Scripts
1. Install the required dependencies:
   `pip install pandas sqlalchemy pymysql tabulate`
2. Configure your MySQL connection settings.
3. Run  `python mysql_connector.py` to extract and display the selected data.

## Example output

![Python](https://res.cloudinary.com/dpa96jvla/image/upload/v1793072392/%E0%B8%AA%E0%B8%81%E0%B8%A3%E0%B8%B5%E0%B8%99%E0%B8%8A%E0%B9%87%E0%B8%AD%E0%B8%95_2026-10-27_103936_hfluov.png)
