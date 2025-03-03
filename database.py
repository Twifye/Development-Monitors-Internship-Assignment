import psycopg2

def connect_db():
    """Connect to the PostgreSQL database and return the connection and cursor."""
    try:
        conn = psycopg2.connect(
            dbname="DM_MovieRecords",
            user="postgres",
            password="user",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Database connection failed:", e)
        return None, None
