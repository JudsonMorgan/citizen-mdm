import json
import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "citizen_mdm"

# PostgreSQL connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

def load_json_to_db(json_file, table_name):
    """Load JSON data into a PostgreSQL table."""
    with open(json_file, "r") as f:
        data = json.load(f)

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)

    # Load data into PostgreSQL
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"✅ Successfully loaded {len(df)} records into {table_name}")

if __name__ == "__main__":
    # Load both datasets into PostgreSQL
    load_json_to_db("health.json", "health")
    load_json_to_db("education.json", "education")
    print("Data loading completed!")
