from flask import Flask

from flask_swagger_pytest_container_demo.main import configure_routes


def test_base_route():
    app = Flask(__name__)
   
    configure_routes(app)
    client = app.test_client()
    url = '/driver/1'
    
    response = client.get(url)
    assert response.get_data() == b'{"status": "Could not retrieve information", "statusCode": "500", "message": "Mapping key not found."}\n'
    assert response.status_code == 500
