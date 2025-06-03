import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('restaurant.db')

st.title("Restaurant Monitoring Dashboard")

# Show occupied tables
st.header("Occupied Tables")
df_tables = pd.read_sql("SELECT * FROM customers WHERE end_time IS NULL", conn)
st.write(df_tables)

# Show staff visits
st.header("Staff Visits (Last 30 Minutes)")
df_staff = pd.read_sql('''SELECT * FROM staff_visits 
                          WHERE visit_time >= datetime('now', '-30 minutes')''', conn)
st.bar_chart(df_staff.groupby("table_id").size())