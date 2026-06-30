import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="studyplanner",
    user="admin",
    password="admin123",
    port=5432
)

cur = conn.cursor()
cur.execute("SELECT version();")
db_version = cur.fetchone()

print("Connected to:", db_version)

cur.close()
conn.close()