from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import sqlite3
import google.generativeai as genai 

genai.configure(api_key=os.environ['GEMINI_API'])


def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text

def get_db_connection(sql,db):
    conn = sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt="""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""

st.title("Text to SQL Query Generator")

question = st.text_input("Enter your request:", "")

if st.button("Generate SQL Query"):
    if question:
        sql_query = get_gemini_response(question,prompt)
        print(sql_query)
        data=get_db_connection(sql_query , "student.db")
        st.subheader("The Response is")
        for row in data:
            print(row)
            st.subheader(row)