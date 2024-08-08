# Document Query Application
## Overview

The Document Query Application allows users to upload documents, query them for relevant information, view their query history, and download their chat history. The application securely stores data in an SQLite database with encryption to ensure data privacy and integrity.

## Features

- **Document Upload**: Support for `.pdf`, `.docx`, and `.txt` file formats.
- **Querying**: Efficient search functionality to retrieve relevant information from uploaded documents.
- **User History**: Maintains a record of user interactions, including queries and responses.
- **Download History**: Option for users to download their chat history in CSV format.
- **Secure Storage**: Uses encryption to securely store documents and user data.

## Requirements

- Python 3.x
- Libraries: `streamlit`, `pandas`, `sqlalchemy`, `cryptography`, `pdfminer.six`, `python-docx`
