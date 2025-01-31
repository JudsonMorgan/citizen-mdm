# Citizen MDM Service

## Overview
A Master Data Management (MDM) service to merge and serve citizen records from Health and Education ministries.

## Setup Instructions

### 1. Install Dependencies
 ```on bash on windows terminal;```
pip install -r requirements.txt

### 2. Setup POSTGRESQL 
`CREATE DATBASE citizen_db`

### 3. Load Data into POSTGRESQL 
`Python load_data.py` 

### 4. Start RESTAPIs 
`uvicorn app:app --reload` 

### 5. Test Endpoints 

Get specific citizen: ``http://127.0.0.1:8000/docs#/default/get_citizen_citizens__citizen_id__get``
Get all citizens: ``http://127.0.0.1:8000/docs#/default/list_citizens_citizens_get``

**Note: The limit and offset has been included on the code in order to save time for processing the large number of rows.**