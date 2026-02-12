import pytest
import sqlite3

# 1. SETUP: Create a temporary test database 
@pytest.fixture
def db_connection():
    # ":memory:" creates a lightning-fast temporary DB in RAM (perfect for CI/CD)
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # ARRANGE: Create a mock 'aetna_members' table
    cursor.execute('''
        CREATE TABLE aetna_members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            plan_type TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    
    yield conn  # Pause here and hand the database to the test
    
    # TEARDOWN: Close and destroy the database after the test finishes
    conn.close()

# 2. THE TEST: Verify Data Insertion and Retrieval
def test_member_database_insertion(db_connection):
    """Validates that a new member is correctly written to the SQL database."""
    cursor = db_connection.cursor()
    
    # ACT: Insert a mock patient record
    cursor.execute(
        "INSERT INTO aetna_members (name, plan_type, status) VALUES (?, ?, ?)", 
        ('Jane Smith', 'PPO', 'Active')
    )
    db_connection.commit()
    
    # ACT: Query the database to see if it actually saved
    cursor.execute("SELECT name, plan_type, status FROM aetna_members WHERE name='Jane Smith'")
    db_record = cursor.fetchone()
    
    # ASSERT: Check that the database returned a record, and the data perfectly matches
    assert db_record is not None, "CRITICAL: Member was not saved to the database!"
    assert db_record[0] == 'Jane Smith'
    assert db_record[1] == 'PPO'
    assert db_record[2] == 'Active'