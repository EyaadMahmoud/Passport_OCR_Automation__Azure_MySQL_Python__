# Passport OCR Automation with Azure & MySQL

This project provides an automated system to extract key information from passport images using **Azure Form Recognizer** and stores the extracted metadata in a **MySQL database**, with optional JSON file output.

---

## 📌 Features

- Selects a passport image using a GUI file picker (supports `.jpg`, `.jpeg`, `.png`, `.pdf`)
- Uses **Azure Document Intelligence (prebuilt-idDocument)** to extract:
  - First Name
  - Passport Number
  - Nationality
  - Date of Birth
- Saves metadata in:
  - A **MySQL database** (`passports` table)
  - An optional **JSON file**
- Handles PDF and image input types
- Supports error handling for failed OCR or DB connection

---

## 🧰 Tech Stack

- **Python 3**
- **Azure Form Recognizer (Document Intelligence)**
- **MySQL**
- `mysql-connector-python`
- `azure-ai-formrecognizer`
- `tkinter` for file selection
- `json`, `os`, `datetime` for metadata processing

---

## 📦 Installation

 1. Install Required Python Packages

- bash
pip install azure-ai-formrecognizer mysql-connector-python
-----------------------------------------------------------------------------------------------
2. MySQL Server
Ensure your MySQL server is running and accessible. You’ll need:

Host (e.g., localhost)

User (e.g., root)

Password

Database name (e.g., passports_ocr_db)
-----------------------------------------------------------------------------------------------
3. Azure Form Recognizer Setup
Create a Form Recognizer resource from Azure Portal, and get:

AZURE_ENDPOINT

AZURE_KEY
-----------------------------------------------------------------------------------------------

🛡️ Notes
Ensure your Azure resource uses the Document Intelligence (Form Recognizer) service with "prebuilt-idDocument" model.

Passwords are stored in plaintext in this demo. For production, always encrypt sensitive information.

Handle file paths, logging, and exception handling properly in extended versions.
