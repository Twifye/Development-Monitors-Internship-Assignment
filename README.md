# Movie Counter System

## Overview
This project is a simple movie counter system built using **Python** and **PostgreSQL**. It allows users to:
- Add new movies with a ticket count.
- Update the available ticket count for a movie.
- Book tickets (decrease ticket count).
- List all movies and their available tickets.

The project demonstrates fundamental **Python and SQL skills**, following best practices for database interaction and error handling.

---

## Setup Instructions

### **1. Install PostgreSQL**
If you don't have PostgreSQL installed, download and install it from [here](https://www.postgresql.org/download/).

### **2. Create the Database and Table**
Open **pgAdmin** or run the following commands in your terminal:
```sql
CREATE DATABASE movie_db;

\c movie_db; -- Connect to the database

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    tickets_available INTEGER NOT NULL
);
```

### **3. Install Dependencies**
Make sure you have Python installed, then install the required package:
```bash
pip install psycopg2
```

### **4. Run the Application**
Execute the script from your terminal:
```bash
python main.py
```

---

## Approach
- **Modular Structure**: The project is divided into separate files:
  - `database.py` handles database connection.
  - `movie_manager.py` includes functions for database operations.
  - `main.py` provides a user-friendly text-based interface.
- **Error Handling**: Proper error handling for database connections and user inputs.
- **User Interaction**: A simple terminal-based menu for seamless interaction.

---

## Assumptions & Decisions
- **Unique Movie Titles**: Each movie title must be unique.
- **Tickets Cannot be Negative**: The system ensures that ticket values remain non-negative.
- **Database Connection**: Uses **PostgreSQL**, but can be adapted to other SQL databases.

---

## Future Improvements
- Add a **search function** for movies.
- Implement **movie deletion**.
- Create a **web-based interface** instead of a text-based menu.
