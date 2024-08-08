import sqlite3
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load or create a new key
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

def create_connection():
    conn = sqlite3.connect('app_database.db')
    return conn

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS documents
                      (id INTEGER PRIMARY KEY, name TEXT, content TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_history
                      (id INTEGER PRIMARY KEY, user_id TEXT, query TEXT, response TEXT)''')

    conn.commit()
    conn.close()

def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(data):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()
