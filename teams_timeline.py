import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('scr_system.db')

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

# Function to add a new team
def create_team(name, project_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Teams (name, project_id)
    VALUES (?, ?);
    ''', (name, project_id))

    conn.commit()
    conn.close()
    print("Team created successfully!")

# Function to retrieve all teams
def get_all_teams():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Teams;')
    teams = cursor.fetchall()

    conn.close()
    return teams

# Function to add a new timeline entry
def add_timeline_entry(change_request_id, stage, start_date, assigned_user_id, comments):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Timeline (change_request_id, stage, start_date, assigned_user_id, comments)
    VALUES (?, ?, ?, ?, ?);
    ''', (change_request_id, stage, start_date, assigned_user_id, comments))

    conn.commit()
    conn.close()
    print("Timeline entry created successfully!")

# Function to retrieve all timeline entries
def get_all_timeline_entries():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Timeline;')
    timeline_entries = cursor.fetchall()

    conn.close()
    return timeline_entries

# Example Usage
if __name__ == "__main__":
    create_teams_table()
    create_timeline_table()

    # Create a sample team
    create_team(name="Development Team A", project_id=1)  # Adjust project_id as necessary

    # Retrieve and print all teams
    teams = get_all_teams()
    print("All Teams:", teams)

    # Add a sample timeline entry
    add_timeline_entry(change_request_id=1, stage="Request Raised", start_date="2024-10-27 21:11:41", assigned_user_id=1, comments="Initial request submitted.")

    # Retrieve and print all timeline entries
    timeline_entries = get_all_timeline_entries()
    print("All Timeline Entries:", timeline_entries)
