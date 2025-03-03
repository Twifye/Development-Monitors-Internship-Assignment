from database import connect_db
import psycopg2

def add_movie(title, tickets):
    """Add a new movie to the database."""
    conn, cursor = connect_db()
    if not conn:
        return
    try:
        cursor.execute("INSERT INTO movies (title, tickets_available) VALUES (%s, %s)", (title, tickets))
        conn.commit()
        print(f"Movie '{title}' added successfully!")
    except psycopg2.IntegrityError:  # Handles duplicate movie entries
        conn.rollback()
        print(f"Error: Movie '{title}' already exists.")
    except psycopg2.DatabaseError as db_err:  # Handles general database errors
        conn.rollback()
        print("Database Error:", db_err)
    except Exception as e:  # Catches unexpected errors
        conn.rollback()
        print("Unexpected Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_tickets(title, count):
    """Increment tickets for a movie."""
    conn, cursor = connect_db()
    if not conn:
        return
    try:
        cursor.execute("UPDATE movies SET tickets_available = tickets_available + %s WHERE title = %s", (count, title))
        if cursor.rowcount == 0:  # Check if movie exists
            print(f"Error: Movie '{title}' not found.")
        else:
            conn.commit()
            print(f"Updated tickets for '{title}'!")
    except psycopg2.DatabaseError as db_err:
        conn.rollback()
        print("Database Error:", db_err)
    except Exception as e:
        conn.rollback()
        print("Unexpected Error:", e)
    finally:
        cursor.close()
        conn.close()

def book_ticket(title):
    """Book a ticket (decrease ticket count)."""
    conn, cursor = connect_db()
    if not conn:
        return
    try:
        cursor.execute("SELECT tickets_available FROM movies WHERE title = %s", (title,))
        result = cursor.fetchone()
        if not result:  # Movie does not exist
            print(f"Error: Movie '{title}' not found.")
        elif result[0] > 0:
            cursor.execute("UPDATE movies SET tickets_available = tickets_available - 1 WHERE title = %s", (title,))
            conn.commit()
            print(f"Ticket booked for '{title}'!")
        else:
            print(f"No tickets available for '{title}'.")
    except psycopg2.DatabaseError as db_err:
        conn.rollback()
        print("Database Error:", db_err)
    except Exception as e:
        conn.rollback()
        print("Unexpected Error:", e)
    finally:
        cursor.close()
        conn.close()

def list_movies():
    """Display all movies."""
    conn, cursor = connect_db()
    if not conn:
        return
    try:
        cursor.execute("SELECT title, tickets_available FROM movies")
        movies = cursor.fetchall()
        if movies:
            print("\nAvailable Movies:")
            for title, tickets in movies:
                print(f"{title} - Tickets Available: {tickets}")
        else:
            print("No movies found.")
    except psycopg2.DatabaseError as db_err:
        print("Database Error:", db_err)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        cursor.close()
        conn.close()
