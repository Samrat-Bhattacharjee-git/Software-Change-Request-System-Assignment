import unittest
import sqlite3
from index2 import connect_db, create_users_table, create_roles_table, create_change_requests_table


class TestDatabaseFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = connect_db()
        cls.cursor = cls.conn.cursor()
        create_roles_table()
        create_users_table()
        create_change_requests_table()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_create_role(self):
        self.cursor.execute("INSERT INTO Roles (name) VALUES ('Tester');")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM Roles WHERE name='Tester';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Tester')

    def test_create_user(self):
        self.cursor.execute("INSERT INTO Users (username, role_id) VALUES ('TestUser', 1);")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM Users WHERE username='TestUser';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'TestUser')

if __name__ == "__main__":
    unittest.main()
