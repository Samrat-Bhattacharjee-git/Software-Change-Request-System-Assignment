import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('scr_system.db')

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

# Function to insert a new change request
def create_change_request(title, description, priority, due_date, requester_id, assigned_team_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO ChangeRequests (title, description, priority, due_date, status, requester_id, assigned_team_id)
    VALUES (?, ?, ?, ?, 'Pending', ?, ?);
    ''', (title, description, priority, due_date, requester_id, assigned_team_id))

    conn.commit()
    conn.close()
    print("Change request created successfully!")

# Function to retrieve all change requests
def get_all_change_requests():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ChangeRequests;')
    change_requests = cursor.fetchall()

    conn.close()
    return change_requests

# Function to update a change request's status
def update_change_request_status(request_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE ChangeRequests
    SET status = ?, updated_at = CURRENT_TIMESTAMP
    WHERE id = ?;
    ''', (new_status, request_id))

    conn.commit()
    conn.close()
    print(f"Change request {request_id} status updated to '{new_status}'.")

# Function to delete a change request
def delete_change_request(request_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM ChangeRequests WHERE id = ?;', (request_id,))
    conn.commit()
    conn.close()
    print(f"Change request {request_id} deleted successfully.")

# Example Usage
if __name__ == "__main__":
    create_change_requests_table()

    # Create a sample change request
    create_change_request(
        title="Update User Interface",
        description="Redesign the user interface for better usability.",
        priority="High",
        due_date="2024-11-15",
        requester_id=1,  # Adjust as necessary
        assigned_team_id=1  # Adjust as necessary
    )

    # Retrieve all change requests
    requests = get_all_change_requests()
    print("All Change Requests:", requests)

    # Update a change request status
    update_change_request_status(1, "In Development")  # Adjust ID as necessary

    # Delete a change request
    delete_change_request(1)  # Adjust ID as necessary
