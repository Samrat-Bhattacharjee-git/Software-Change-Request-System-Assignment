import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('scr_system.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create Roles table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL
);
''')

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    role_id INTEGER,
    project_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES Roles(id)
);
''')

# Create Teams table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    project_id INTEGER
);
''')

# Create ChangeRequests table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ChangeRequests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT,
    due_date DATE,
    status TEXT,
    requester_id INTEGER,
    assigned_team_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (requester_id) REFERENCES Users(id),
    FOREIGN KEY (assigned_team_id) REFERENCES Teams(id)
);
''')

# Create Timeline table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Timeline (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    change_request_id INTEGER,
    stage TEXT,
    start_date DATETIME,
    completion_date DATETIME,
    assigned_user_id INTEGER,
    comments TEXT,
    FOREIGN KEY (change_request_id) REFERENCES ChangeRequests(id),
    FOREIGN KEY (assigned_user_id) REFERENCES Users(id)
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
