from pathlib import Path
from extract import DataExtract
from load import DataLoader
import pandas as pd

base_path = Path(__file__).resolve().parents[1]
file_path = "..\\data\\"
path_db = "..\\data\\DataEmployee.db"



extractor = DataExtract(base_path)

df_contacts = extractor.from_numbers("contacts.numbers", "contacts.csv")
df_departments = extractor.from_csv("departments.csv", headers=["id", "department"])
df_jobs = extractor.from_csv("jobs.csv", headers=["id", "job"])
df_hired_employees = extractor.from_csv("hired_employees.csv", first_row_header=True)

df_hired_employees["datetime"] = pd.to_datetime(df_hired_employees["datetime"], errors="coerce")



dataframes = {
    "contacts": df_contacts,
    "departments": df_departments,
    "hired_employees": df_hired_employees,
    "jobs": df_jobs
}

dataframes_limpios = {}

for name, df in dataframes.items():
    duplicados = df.duplicated().sum()
    nulos = df.isnull().sum().sum()
    df = df.drop_duplicates()
    df = df.dropna()
    dataframes_limpios[name] = df
    print(f"{name} tiene {duplicados} registos Duplicados y {nulos} registros Nulos")

contacts = """
CREATE TABLE IF NOT EXISTS etl_monitor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                country TEXT,
                region TEXT,
                department_id INTEGER,
                Price REAL,
                contect_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id)

)
"""

departments = """
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY,
    department TEXT
)
"""

hired_employees = """
CREATE TABLE IF NOT EXISTS calificaciones (
    id INTEGER PRIMARY KEY,
    name TEXT,
    datetime DATE,
    department_id INTEGER,
    job_id INTEGER,
    FOREIGN KEY (job_id) REFERENCES jobs(id)
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
"""

jobs = """
CREATE TABLE IF NOT EXISTS matriculas (
    id INTEGER PRIMARY KEY,
    job TEXT
)
"""

tables = [
    ("contacts", contacts),
    ("departments", departments),
    ("hired_employees", hired_employees),
    ("jobs", jobs)
]

conn = DataLoader.init_db(path_db = path_db)
for name, create_sql in tables:
    DataLoader.create_table(conn= conn, create_table_sql = create_sql, table_name=name)

for name, df in dataframes_limpios.items():
    DataLoader.insert_data(conn= conn, table_name= name, df=df)

qry= """ 
select 
    *
from hired_employees
 """
df = DataLoader.run_query(conn= conn,query= qry)

print(df.head())


