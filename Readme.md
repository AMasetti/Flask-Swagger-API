# Flask App - Swagger UI - Pytest

Create Virtual Environment and install dependencies
```shell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run Pytest on the endpoints
```shell
pytest -v  --disable-warnings
```

```shell
========================================================================================= test session starts ========================================================================================== 
platform win32 -- Python 3.9.5, pytest-7.0.1, pluggy-1.0.0 -- c:\users\amasetti001\desktop\flask demo\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\amasetti001\Desktop\Flask Demo\flask_pytest_example
plugins: flask-1.2.0
collected 1 item                                                                                                                                                                                         

test/test_driver.py::test_base_route PASSED  
```

Build the Container
```shell
docker compose up --build
```