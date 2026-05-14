# Courier Nexus — Optimizing Logistics Through Data

A scalable relational database and analytics system built to manage shipment tracking, claims processing, and operational reporting for courier operations. The project demonstrates end-to-end data engineering: schema design, ETL pipeline development, SQL-based analysis, and interactive dashboard delivery — skills directly applicable to large-scale investigative and public-sector data work.

---

## Project Summary

As logistics operations scale, spreadsheet-based workflows become error-prone and impossible to audit. This project replaces those workflows with a structured PostgreSQL database, a Python-based ETL pipeline, and a Streamlit web interface for real-time querying and reporting. The result is a reproducible, queryable system capable of supporting operational decisions across shipment tracking, claims resolution, and customer feedback analysis.

**Role:** Database architect, SQL query developer, and ETL pipeline engineer (team of 2)
**Scale:** 15,000+ synthetic records across 10+ relational entities
**Timeline:** September – October 2024

---

## Skills Demonstrated

| Area | Details |
|---|---|
| **SQL** | Schema design, advanced queries (JOINs, subqueries, GROUP BY, aggregates, window functions), indexing |
| **Database design** | BCNF normalization, functional dependency analysis, Chase Test, integrity constraints |
| **ETL** | Python-based data generation, transformation, and loading via Faker and psycopg2 |
| **Query optimization** | Indexing on high-frequency query columns — reduced query time from seconds to milliseconds |
| **Data quality** | Constraint enforcement, deduplication, outlier handling, referential integrity |
| **Visualization** | Streamlit dashboard for non-technical stakeholders; real-time filtering and reporting |

---

## Repository Structure

| File | Description |
|---|---|
| `create.sql` | Full schema definition — tables, primary keys, foreign keys, constraints |
| `index.sql` | Indexing strategy for query optimization on shipment and claims tables |
| `shipment_analysis.sql` | Analytical queries: shipment counts by status, claims aggregation, top-rated feedback, recent claims by shipment |
| `data_generator.ipynb` | Python ETL pipeline — generates and loads 15,000+ synthetic records into PostgreSQL |
| `app.py` | Streamlit dashboard — interactive querying, data visualization, and record exploration |
| `requirements.txt` | Python dependencies |

---

## Database Schema

Ten entities modeled with full relational integrity:

- **Shipments** — status, method, sender/receiver relationships, delivery timeline
- **Packages** — dimensions, weight, descriptions
- **Claims** — dates, resolution status, associated amounts
- **CustomerFeedback** — ratings and comments per shipment
- **DeliveryAttempts / DeliveryLocations** — delivery log with geolocation timestamps
- **Senders / Receivers** — core party data with contact information

All tables satisfy **Boyce-Codd Normal Form (BCNF)** — decomposition verified via functional dependency analysis and the Chase Test.

---

## Analytical Queries (`shipment_analysis.sql`)

Queries are written for reproducibility and stakeholder communication:

- **Shipment counts by status** — operational volume overview
- **Shipments with open claims** — exception identification via JOIN across Shipments and Claims
- **Claims aggregated by resolution status** — trend analysis using GROUP BY and aggregate functions
- **Top-rated feedback with sender information** — multi-table JOIN with filtering
- **Recent claims by shipment** — temporal query using ORDER BY and subquery filtering

Each query is annotated with the business question it answers and the methodology used.

---

## ETL Pipeline (`data_generator.ipynb`)

The pipeline follows a standard extract-transform-load pattern:

1. **Extract** — parameter configuration and schema validation
2. **Transform** — Faker-based synthetic record generation, referential integrity enforcement, outlier removal
3. **Load** — psycopg2 batch insertion into PostgreSQL with error handling and rollback logic

The pipeline is idempotent — re-running it produces consistent results without duplicate records.

---

## Query Optimization

Indexing strategy documented in `index.sql`:

- Indexes on `shipment_id`, `claim_status`, `delivery_date`, and `sender_id`
- Before indexing: full table scans on 15,000+ rows
- After indexing: query execution time reduced from seconds to milliseconds
- Validated using PostgreSQL `EXPLAIN ANALYZE`

---

## Setup

```bash
# 1. Create schema
psql -U postgres -d your_db -f create.sql

# 2. Apply indexes
psql -U postgres -d your_db -f index.sql

# 3. Generate and load data
jupyter notebook data_generator.ipynb

# 4. Run analytical queries
psql -U postgres -d your_db -f shipment_analysis.sql

# 5. Launch dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## Author

**Pranavi Chintala**
M.S. Data Science, University at Buffalo
[linkedin.com/in/pranavi-chintala18](https://linkedin.com/in/pranavi-chintala18)
