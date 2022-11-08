import streamlit as st
import mysql.connector as mc

# initialize connection with singleton to only run once
@st.experimental_singleton
def init_connection():
    return mc.connect(**st.secrets["mysql"])

conn = init_connection()


# perform query with use of singleton
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * from Country;")

# print the results
for row in rows:
    st.write(f"Country code: {row[0]} Country name: {row[1]} GDP: {row[2]} Inflation: {row[3]}")
