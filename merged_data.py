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

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Load data from the health and education tables
health_df = pd.read_sql("SELECT * FROM health", engine)
education_df = pd.read_sql("SELECT * FROM education", engine)

# Merge dataframes on 'citizen_id'
merged_df = pd.merge(health_df, education_df, on="citizen_id", how="outer", suffixes=('_health', '_education'))

# Resolve conflicts: choose the most frequent value between datasets for name and dob
merged_df['name'] = merged_df[['name_health', 'name_education']].mode(axis=1)[0]
merged_df['dob'] = merged_df[['dob_health', 'dob_education']].mode(axis=1)[0]

# Drop unnecessary columns (health_name, education_name, etc.)
merged_df.drop(columns=['name_health', 'name_education', 'dob_health', 'dob_education'], inplace=True)

# Optionally, you can store the merged data into a new table or just print it
merged_df.to_sql('merged_citizens', con=engine, if_exists='replace', index=False)

print(f"Merged data successfully loaded into 'merged_citizens' table.")
