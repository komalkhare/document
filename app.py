import streamlit as st
import pandas as pd
from database import create_connection, decrypt_data, setup_database
from utils import extract_text_from_file, store_document

setup_database()

st.title('Document Query Application')

# Upload Document
uploaded_file = st.file_uploader("Upload a document", type=['pdf', 'docx', 'txt'])
if uploaded_file:
    content = extract_text_from_file(uploaded_file)
    store_document(uploaded_file.name, content)
    st.success("Document uploaded and stored successfully!")

# Query Documents
query = st.text_input("Enter your query:")
if query:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, content FROM documents")
    documents = cursor.fetchall()
    relevant_info = []
    for doc_name, doc_content in documents:
        if query.lower() in decrypt_data(doc_content).lower():
            relevant_info.append((doc_name, decrypt_data(doc_content)))
    conn.close()

    if relevant_info:
        st.write("Results:")
        for name, content in relevant_info:
            st.write(f"**Document Name:** {name}")
            st.write(content)
    else:
        st.write("No relevant information found.")

# User History
user_id = "user1"  # For demo purposes, replace with actual user ID
history_df = pd.read_sql_query("SELECT query, response FROM user_history WHERE user_id=?", create_connection(), params=(user_id,))
if not history_df.empty:
    st.write("Your Query History:")
    st.dataframe(history_df)

# Download Chat History
if st.button('Download Chat History'):
    chat_history = history_df.to_csv(index=False)
    st.download_button(label="Download CSV", data=chat_history, file_name="chat_history.csv")
