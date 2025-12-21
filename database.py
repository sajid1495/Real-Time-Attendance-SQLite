"""
SQLite Database Module for Face Recognition Attendance System
This module provides centralized database handling for portability.
No installation required - SQLite comes built into Python!
"""

import sqlite3
import os

# Database file path (in the same directory as this script)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.db")


def get_connection():
    """Get a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enable column access by name
    return conn


def init_database():
    """Initialize the database and create tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create student table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            Dept TEXT,
            Course TEXT,
            Year TEXT,
            Semester TEXT,
            Student_id TEXT PRIMARY KEY,
            Name TEXT,
            Division TEXT,
            Roll TEXT,
            Gender TEXT,
            Dob TEXT,
            Email TEXT,
            Phone TEXT,
            Address TEXT,
            Teacher TEXT,
            PhotoSample TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")


# Auto-initialize database when module is imported
init_database()
