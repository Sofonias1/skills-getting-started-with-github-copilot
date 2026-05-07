import pytest
from src.app import activities

INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Train for soccer matches and improve fitness",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["alex@mergington.edu", "nina@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and compete in friendly games",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["maria@mergington.edu", "david@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore painting, drawing, and creative design",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["lily@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Society": {
        "description": "Practice acting, stagecraft, and perform school plays",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["ava@mergington.edu", "ethan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 14,
        "participants": ["mia@mergington.edu", "jack@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Prepare for science competitions and explore STEM challenges",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
    }
}

@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)