import streamlit as st
import psycopg2
import pandas as pd
import os  # Importing os for environment variables

# Function to establish a connection to PostgreSQL
def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),  # Use environment variable for host
            database=os.getenv("DB_NAME", "postgres"),  # Use environment variable for database
            user=os.getenv("DB_USER", "postgres"),  # Use environment variable for user
            password=os.getenv("DB_PASS", "dmql"),  # Use environment variable for password
            port=os.getenv("DB_PORT", "5433")  # Use environment variable for port
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Function to execute a query
def execute_query(query):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                if cur.description:  # If the query returns rows
                    columns = [desc[0] for desc in cur.description]
                    rows = cur.fetchall()
                    df = pd.DataFrame(rows, columns=columns)
                    conn.close()
                    return df
                else:  # For INSERT, UPDATE, DELETE queries
                    conn.commit()
                    conn.close()
                    return None
        except Exception as e:
            st.error(f"Query failed: {e}")
            conn.close()
            return None

# Streamlit App
def main():
    st.title(" Courier Nexus")

    st.sidebar.header("Query Options")
    selected_query = st.sidebar.selectbox(
        "Choose a Query",
        [
            "Show all Shipments",
            "Show Claims with Resolved Status",
            "Feedback with High Ratings",
            "Custom Query"
        ]
    )

    # Predefined queries
    queries = {
        "Show all Shipments": "SELECT * FROM Shipments;",
        "Show Claims with Resolved Status": "SELECT * FROM Claims WHERE claim_status = 'Resolved';",
        "Feedback with High Ratings": "SELECT * FROM CustomerFeedback WHERE rating > 4;"
    }

    # Execute predefined queries
    if selected_query != "Custom Query":
        query = queries[selected_query]
        st.subheader(f"Results for: {selected_query}")
        df = execute_query(query)
        if df is not None:
            st.dataframe(df)
        else:
            st.info("No data found or query returned no results.")

    # Execute custom queries
    else:
        st.subheader("Custom Query Execution")
        custom_query = st.text_area("Write your SQL query here:")
        if st.button("Run Query"):
            df = execute_query(custom_query)
            if df is not None:
                st.dataframe(df)
            else:
                st.info("No data found or query returned no results.")

if __name__ == "__main__":
    main()
