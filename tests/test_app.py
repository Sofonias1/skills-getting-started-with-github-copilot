import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app, follow_redirects=False)

def test_get_root():
    # Arrange
    # No specific arrangement needed

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 307  # Temporary Temporary Redirect
    assert response.headers["location"] == "/static/index.html"

def test_get_activities():
    # Arrange
    # Activities are reset by fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    # Verify structure of one activity
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)

def test_signup_successful():
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Signed up {email} for {activity_name}" == data["message"]
    assert email in activities[activity_name]["participants"]

def test_signup_duplicate():
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student is already signed up for this activity" == data["detail"]

def test_signup_activity_not_found():
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" == data["detail"]

def test_remove_participant_successful():
    # Arrange
    activity_name = "Programming Class"
    email = "newparticipant@mergington.edu"
    # First sign up
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Unregistered {email} from {activity_name}" == data["message"]
    assert email not in activities[activity_name]["participants"]

def test_remove_participant_not_found():
    # Arrange
    activity_name = "Programming Class"
    email = "notsignedup@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Participant not found" == data["detail"]

def test_remove_participant_activity_not_found():
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" == data["detail"]