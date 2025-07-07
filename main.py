import os
import json
import mysql.connector
from azure.ai.formrecognizer import DocumentAnalysisClient #to use OCR options
from azure.core.credentials import AzureKeyCredential #to be able to use key
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from datetime import date

# Function to open file dialog
def get_file_path():
    root = Tk()
    root.withdraw()  # Hides the root window
    file_path = askopenfilename(
        title="Select Passport Image File",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.pdf")]  # Supported file types
    )
    return file_path

# Get the file path from user
file_path = get_file_path()
AZURE_ENDPOINT = ""
AZURE_KEY = ""
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""    
DB_NAME = ""   


client = DocumentAnalysisClient(endpoint= AZURE_ENDPOINT , credential= AzureKeyCredential(AZURE_KEY)) #initialize client
#-----
def process_passport(file_path):
    try:
        with open(file_path, "rb") as file:  # binary read to extract from PDF too
            poller = client.begin_analyze_document("prebuilt-idDocument", document=file)
            result = poller.result()
    except Exception as e:
        print(f"Error processing passport: {e}")
        return {}  # Return empty dict so the caller can handle failure gracefully

    fields = ["FirstName", "DocumentNumber", "Nationality", "DateOfBirth"]
    return {key: result.documents[0].fields.get(key).value for key in fields}

#key is a dictionary that takes values in fields each key corresponds to field name 
# .get is used to avoid an error if nothing is returned
# .value used to attribute actual text we got
#--------
def save_data(metadata):
    json_file_path = r""  #Path for your passport image
    
    for key, value in metadata.items():
        if isinstance(value, date):  
            metadata[key] = value.isoformat() #convert into string if date is used
    with open(json_file_path , "w") as file: #create file
        json.dump(metadata, file) #dump the metadata inside the file
    
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            )
        cursor = connection.cursor()
        print("Connected to MySQL Server successfully.")
    
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

        connection.database = DB_NAME #create DB then set it up as the connection db
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passports(
                name VARCHAR(225),
                passport_number VARCHAR(225),
                nationality VARCHAR(225),
                date_of_birth VARCHAR(225),
                json_data JSON
        )               
        """) #create table to store data
    
        cursor.execute(""" 
            INSERT INTO passports(name,passport_number,nationality,date_of_birth, json_data)
            VALUES (%s,%s,%s,%s,%s)
        """,(
            metadata.get('FirstName'), 
            metadata.get('DocumentNumber'), 
            metadata.get('Nationality'),  #use .get() tp       
            metadata.get('DateOfBirth'), # extracts DateofBirth from metadata dict. then uses it for %s 
            json.dumps(metadata) #converts data we got into json string
        ))
    
        connection.commit()
        print("Data inserted successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")  # Print the error if there is one
    finally:
        if cursor:
                cursor.close()  # Ensure the cursor is closed if it was created
        if connection:
                connection.close()  # Ensure the connection is closed
 #close connections and save 

# Check if the file exists before processing
if os.path.isfile(file_path):
    print("File exists!")
    metadata = process_passport(file_path)
    save_data(metadata)
else:
    print("File does not exist!")
