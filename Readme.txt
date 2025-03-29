### README for Logistics Database Management System with Streamlit Integration

---

#### Project Description

This project creates a comprehensive database solution for a logistics company to overcome the inefficiencies of traditional tools like Excel. The database includes detailed records of shipments, claims, delivery attempts, and customer feedback while ensuring scalability, data integrity, and ease of access for multiple user groups.

The system uses SQL for database creation, Python scripts for synthetic data generation, and provides a web-based user interface using Streamlit for seamless interaction and data visualization.

---

#### Files Included

1. **create.sql**: Defines the schema for the database, creating tables with necessary primary and foreign key constraints.
2. index.sql: Implements indexing on key attributes to optimize query performance and accelerate data retrieval.
3. **data_generator.ipynb**: Python notebook used to generate synthetic data and populate the database. This replaces the need for `.csv` or `.dat` files and a separate `load.sql` file.
4. **app.py**: Streamlit application script that provides a web-based interface for querying and visualizing data from the database.
5. **Milestone_2.pdf**: A detailed project report describing the problem statement, target users, database schema, and the normalization process.

---

#### Steps to Set Up the Database and Application

1. **Schema Creation**:
   - Use `create.sql` to set up the database schema. The script creates tables and establishes relationships with appropriate constraints.

2. **Indexing**:
   -Execute index.sql to create indexes on frequently queried columns for faster data retrieval.

2. **Data Generation and Loading**:
   - Open and run the `data_generator.ipynb` script in a Jupyter Notebook environment. It:
     - Connects to the database.
     - Creates the schema (if not already created).
     - Generates synthetic data and inserts it into the database tables.

3. **Streamlit Web Application**:
   - Install Streamlit if not already installed:  
     ```bash
     pip install streamlit
     ```
   - Run the application with the following command:
     ```bash
     streamlit run app.py
     ```
   - This launches a web interface where you can:
     - View data visualizations.
     - Execute pre-defined queries.
     - Explore and interact with database records through an intuitive UI.

4. **Querying**:
   - Use SQL queries for custom analysis and reporting, as demonstrated in the milestone report.

---

#### Data Source

- Synthetic data is generated using Python's `Faker` library.
- The script creates realistic logistics data for various entities like packages, shipments, senders, and receivers.

---

#### Features of the Streamlit App

- **Dashboard**: Displays key metrics and visual summaries of the logistics data.
- **Query Execution**: Execute common queries, like tracking shipments, viewing claims, or analyzing customer feedback.
- **Interactive Reports**: View detailed records with filtering and sorting capabilities.
- **Data Exploration**: Drill down into specific tables for deeper insights into the data.

---

#### Table Overview

| Table                | Description                                                    |
|----------------------|----------------------------------------------------------------|
| `Shipments`          | Tracks shipment details including sender, receiver, and status.|
| `Packages`           | Stores package dimensions and descriptions.                   |
| `Senders`            | Information about package senders.                            |
| `Receivers`          | Information about package receivers.                          |
| `Claims`             | Details about claims related to shipments.                    |
| `CustomerFeedback`   | Stores customer feedback and ratings.                         |
| `DeliveryAttempts`   | Logs multiple attempts to deliver a shipment.                 |
| `DeliveryLocations`  | Records locations and timestamps for deliveries.              |

---

#### Directory Structure

```
Project/
├── create.sql
├── index.sql
├── data_generator.ipynb
├── app.py
├── Milestone_2.pdf
└── README.txt
└── requirements.txt
```

---

#### Notes

- The index.sql file creates indexes for optimizing key queries, especially on shipment tracking and claims processing.
- The Python script eliminates the need for separate `.csv` or `.dat` files and a `load.sql` file, as data generation and loading are integrated into one process.
- Streamlit provides a user-friendly interface for non-technical users to interact with the database and visualize insights.
- The project complies with BCNF normalization to ensure data integrity and eliminate redundancy.
- Indexing was implemented on key attributes to optimize query performance.
- For large datasets, consider configuring the database server for better performance (e.g., memory allocation, indexing).

Enjoy visualizing and managing our logistics database with Streamlit!
