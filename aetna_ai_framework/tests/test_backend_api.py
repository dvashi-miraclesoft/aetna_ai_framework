import pytest
import requests

# We use a public mock API for hands-on execution
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_member_details_success():
    """Validates that a valid member ID returns the correct profile data."""
    
    # 1. ACT: Send a GET request to the backend
    response = requests.get(f"{BASE_URL}/users/1")
    
    # 2. ASSERT: HTTP Status Code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # 3. ASSERT: Headers (Ensure the server returns secure JSON)
    assert "application/json" in response.headers["Content-Type"]
    
    # 4. ASSERT: Data Payload Validation
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    
    # 5. ASSERT: Security/HIPAA Check
    # In healthcare, backend APIs must never return raw SSNs or passwords in a standard payload.
    assert "ssn" not in data, "CRITICAL: Sensitive PII (SSN) exposed in API response!"

def test_get_member_not_found():
    """Validates that the backend handles invalid IDs gracefully."""
    
    # 1. ACT: Request a member ID that does not exist
    response = requests.get(f"{BASE_URL}/users/999999")
    
    # 2. ASSERT: The server should explicitly reject it with a 404, not crash with a 500
    assert response.status_code == 404

def test_create_new_member_post():
    """Validates that a new member record can be created securely via POST."""
    
    # 1. ARRANGE: Define the endpoint and the payload (the data we are sending)
    url = f"{BASE_URL}/posts"  # We use /posts as the mock creation endpoint
    
    # Simulating a clean, secure payload (Notice we don't send sensitive PII here)
    payload = {
        "title": "New Member Enrollment",
        "body": "Plan Type: HMO, Region: CT",
        "userId": 101
    }
    
    # Headers are mandatory for POST requests to tell the backend what to expect
    headers = {
        "Content-type": "application/json; charset=UTF-8",
        "Authorization": "Bearer MOCK_SECURE_TOKEN_ABC123" # Simulating secure access
    }
    
    # 2. ACT: Send the POST request using the 'json=' parameter
    response = requests.post(url, json=payload, headers=headers)
    
    # 3. ASSERT: 201 Created is the standard REST HTTP code for successful creation
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    # 4. ASSERT: Data Integrity - Verify the server correctly processed and saved our data
    response_data = response.json()
    assert response_data["title"] == "New Member Enrollment"
    assert response_data["userId"] == 101
    
    # 5. ASSERT: The backend should have generated and returned a new database ID for this record
    assert "id" in response_data, "Backend failed to generate a new record ID"