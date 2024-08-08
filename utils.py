import pandas as pd
from pdfminer.high_level import extract_text
from docx import Document

def extract_text_from_file(file):
    if file.name.endswith('.pdf'):
        return extract_text(file)
    elif file.name.endswith('.docx'):
        doc = Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        return ""

def store_document(name, content):
    from database import create_connection, encrypt_data
    conn = create_connection()
    cursor = conn.cursor()
    encrypted_content = encrypt_data(content)
    cursor.execute('INSERT INTO documents (name, content) VALUES (?, ?)', (name, encrypted_content))
    conn.commit()
    conn.close()
