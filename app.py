from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import mysql.connector
import google.generativeai as genai
import os
import pandas as pd

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

# Database Connection
def create_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn

# Generate Optimized SQL Query
def generate_sql(question):
    prompt = f"""
    You are a MySQL Expert.
    User can ask in Hindi, English, or Hinglish.

    Database Table: employee
    Columns: id, name, department, salary, age

    Task:
    1. Understand question in Hindi/English/Hinglish.
    2. Convert it into optimized MySQL query.
    3. If table/column not found, return "Table or column not found".
    4. Return only SQL query.

    Question:
    {question}
    """

    response = model.generate_content(prompt)
    sql_query = response.text.strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "")
    return sql_query

# Execute Query
def execute_query(query):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return rows, columns

# Streamlit UI
st.set_page_config(page_title="SQL Assistant")

st.title("QueryMind AI Assistant")

st.markdown("""
### Welcome Intelligent Natural Language SQL Assistant
            
Ask questions in English, Hindi, or Hinglish and instantly convert natural language into optimized MySQL queries with real-time database results.
""")

st.header("Ask Your Database Anything")

question = st.text_input("Enter your question")

if st.button("Ask"):
    sql_query = generate_sql(question)
    st.subheader("Generated Optimized SQL Query")
    st.code(sql_query, language="sql")

    try:
        if "not found" in sql_query.lower():
            st.error("⚠️ Table or column not found in database.")
        else:
            rows, columns = execute_query(sql_query)
            df = pd.DataFrame(rows, columns=columns)
            st.subheader("Results")
            st.dataframe(df)
    except Exception as e:
        error_msg = str(e)
    if "1146" in error_msg or "doesn't exist" in error_msg.lower() or "no data" in error_msg.lower():
        st.markdown(
            """
            📌 **Note:- No relevant data was found in the database.**

            <div style="text-align:center; font-weight:bold;">
                Thank you for using QueryMind AI.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("⚠️ Something went wrong: " + error_msg)