import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('scr_system.db')

# Create Users table
def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        role_id INTEGER,
        FOREIGN KEY (role_id) REFERENCES Roles(id)
    );
    ''')

    conn.commit()
    conn.close()
    print("Users table created successfully!")

# Create Roles table
def create_roles_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    ''')

    conn.commit()
    conn.close()
    print("Roles table created successfully!")

# Create Teams table
def create_teams_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        project_id INTEGER,
        FOREIGN KEY (project_id) REFERENCES Projects(id)  -- Assuming Projects table exists
    );
    ''')

    conn.commit()
    conn.close()
    print("Teams table created successfully!")

# Create ChangeRequests table
def create_change_requests_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ChangeRequests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')),
        due_date DATE,
        status TEXT CHECK(status IN ('Pending', 'Approved', 'In Development', 'Completed')),
        requester_id INTEGER,
        assigned_team_id INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (requester_id) REFERENCES Users(id),
        FOREIGN KEY (assigned_team_id) REFERENCES Teams(id)
    );
    ''')

    conn.commit()
    conn.close()
    print("ChangeRequests table created successfully!")

# Create Timeline table
def create_timeline_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Timeline (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        change_request_id INTEGER,
        stage TEXT NOT NULL,
        start_date DATETIME,
        completion_date DATETIME,
        assigned_user_id INTEGER,
        comments TEXT,
        FOREIGN KEY (change_request_id) REFERENCES ChangeRequests(id),
        FOREIGN KEY (assigned_user_id) REFERENCES Users(id)
    );
    ''')

    conn.commit()
    conn.close()
    print("Timeline table created successfully!")

# Example Usage
if __name__ == "__main__":
    create_roles_table()
    create_users_table()
    create_teams_table()
    create_change_requests_table()
    create_timeline_table()

    # Sample data creation can be added here
