import re
import pytest
from time_api_backend.app import app

@pytest.fixture
def client():
    """Fixture for Flask test client."""
    with app.test_client() as client:
        yield client

def test_time_status_code(client):
    """Test that the /time endpoint returns 200 OK."""
    response = client.get('/time/')
    assert response.status_code == 200

def test_time_json_format(client):
    """Test that the JSON contains a 'current_time' string value in ISO 8601 format."""
    response = client.get('/time/')
    json_data = response.get_json()
    assert 'current_time' in json_data
    current_time = json_data['current_time']
    # Check that the string is in ISO 8601 format ending with 'Z' for UTC
    assert isinstance(current_time, str)
    assert current_time.endswith('Z')
    # Basic ISO8601 UTC time pattern (not exhaustive)
    iso_utc_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$'
    assert re.match(iso_utc_pattern, current_time)
