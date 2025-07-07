# Passport OCR and Metadata Storage Tool

This Python-based tool extracts essential information from scanned **passport images** (JPEG, PNG, PDF) using **Azure Form Recognizer** and stores the extracted metadata in a **MySQL database** and a local **JSON file**. It includes a file dialog interface for user-friendly image selection.

---

##  Features

-  Extracts key passport details: `FirstName`, `DocumentNumber`, `Nationality`, and `DateOfBirth`.
-  Uses **Azure Cognitive Services – Form Recognizer** (prebuilt ID document model).
-  Stores metadata as:
  - A row in a *MySQL database*
  - A `.json` file in the same directory as the image
-  File picker interface using *Tkinter*
-  Auto-creates the database and table if not already present

---


---

## ⚙️ Requirements

- Python 3.7+
- Azure Cognitive Services Account (Form Recognizer)
- MySQL Server (local or remote)

---

##  Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/passport-ocr.git
   cd passport-ocr

   

## Azure Setup
Go to Azure Portal

Create a Form Recognizer resource

Copy:

Endpoint

Key

Enable the prebuilt-idDocument model



