## 🧪 What is a **pytest fixture**?

In **`pytest`**, a **fixture** is a reusable piece of code that you can use to **set up test context** (e.g., create resources, connect to a database, initialize variables) **before a test runs**, and optionally **tear it down** afterward.


#### ✅ Key Features:

* Fixtures can **return data or objects** to tests.
* They help **reduce duplication** in test code.
* You can set **scope**: run once per test, per module, per session, etc.
* Fixtures can **depend on other fixtures**.


#### 🧾 Basic Example

```python
import pytest

@pytest.fixture
def sample_data():
    return {"user": "jinyu", "role": "admin"}

def test_user_role(sample_data):
    assert sample_data["role"] == "admin"
```

* `sample_data` is the fixture.
* It returns a dictionary.
* The test function automatically receives it by **matching the parameter name**.


#### 🧹 Fixture with Setup and Teardown

```python
@pytest.fixture
def file_handler():
    f = open("test.txt", "w")
    yield f
    f.close()  # Teardown logic after test runs
```

* `yield` splits setup and teardown.
* After the test using this fixture finishes, the file is closed.

#### 🔁 Fixture Scope

Control how often the fixture runs:

```python
@pytest.fixture(scope="module")
def db_connection():
    print("Connecting to DB...")
    yield "db_conn"
    print("Disconnecting...")
```

| Scope                | Description                       |
| -------------------- | --------------------------------- |
| `function` (default) | Runs before every test function   |
| `class`              | Runs once per class               |
| `module`             | Runs once per test file           |
| `session`            | Runs once per entire test session |


#### 🧠 When to Use Fixtures?

Use them to:

* Set up mock data
* Open files or sockets
* Connect to test databases
* Configure test environment
* Clean up after tests


## 🔁 `yield` in a `pytest` fixture = **"setup → test runs → teardown"**

#### ✅ What it does:

* Code **before `yield`** = setup (runs **before the test**)
* Code **after `yield`** = teardown (runs **after the test finishes**)


#### 🧪 Example: Setup and Teardown with `yield`

```python
import pytest

@pytest.fixture
def resource():
    print("🔧 Setting up resource")
    res = {"name": "jinyu"}
    yield res  # 🧪 This is passed to the test
    print("🧹 Tearing down resource")
```

```python
def test_something(resource):
    print(f"Using resource: {resource['name']}")
    assert resource["name"] == "jinyu"
```

#### 🧾 Output will look like:

```
🔧 Setting up resource
Using resource: jinyu
🧹 Tearing down resource
```

#### ✅ Why Use `yield`?

Because it allows you to:

* **Provide a resource** to the test (like a DB connection, temp file, mock server)
* **Clean up** afterward (close file, delete data, stop service)

It’s cleaner than `try/finally`, and works naturally with `pytest`.

#### 🧼 Real-World Example: Temporary File Fixture

```python
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    # Code before yield = setup (runs before the test)
    f = tempfile.NamedTemporaryFile(delete=False)  
    yield f.name
    # Code after yield = teardown (runs after the test finishes)
    os.remove(f.name)  # Clean up after test 
```

```python
def test_temp_file(temp_file):
    with open(temp_file, "w") as f:
        f.write("hello")
    with open(temp_file) as f:
        assert f.read() == "hello"
```

## Go deeper with examples of using `yield` in `pytest` fixtures that include **setup, teardown, and scope**, including with real resources like a **database** or **Dockerized service**.


#### ✅ 1. **Fixture with `yield` and `scope="module"` (Database connection)**

```python
import pytest

@pytest.fixture(scope="module")
def db_connection():
    # Setup: connect to the DB
    print("🔧 Connecting to database...")
    conn = {"connected": True}  # This could be a real DB engine
    yield conn
    # Teardown: close the DB
    print("🧹 Closing database connection")
    conn["connected"] = False
```

```python
def test_db_query(db_connection):
    assert db_connection["connected"] is True
```

* `scope="module"` means the DB connection is reused for **all tests in the module**
* `yield` gives access to the connection
* Cleanup happens **after all tests using this fixture are done**


#### ✅ 2. **Fixture with Dockerized service (e.g., start a mock server)**

Imagine you're testing against a local HTTP service (like WireMock or PostgREST):

```python
import pytest
import subprocess
import time

@pytest.fixture(scope="session")
def mock_server():
    print("🔧 Starting mock server...")
    proc = subprocess.Popen(["docker", "run", "-p", "8080:8080", "mock-server-image"])
    time.sleep(5)  # Wait for it to be ready
    yield "http://localhost:8080"
    print("🧹 Stopping mock server...")
    proc.terminate()
    proc.wait()
```

```python
def test_api(mock_server):
    import requests
    response = requests.get(f"{mock_server}/health")
    assert response.status_code == 200
```

* Starts the service before tests
* Provides the base URL
* Stops the container afterward


#### ✅ 3. **Fixture Dependency (Nested Fixtures with `yield`)**

```python
@pytest.fixture
def user_data():
    print("🔧 Creating user data")
    yield {"user": "jinyu", "role": "admin"}
    print("🧹 Deleting user data")

@pytest.fixture
def session_token(user_data):
    print("🔧 Logging in")
    token = f"token-for-{user_data['user']}"
    yield token
    print("🧹 Logging out")
```

```python
def test_auth(session_token):
    assert session_token.startswith("token-for")
```

* `session_token` **depends on** `user_data`
* Both fixtures have their own setup/teardown stages
* Teardown order is **reversed**: child fixture is cleaned up first


#### 🧠 Summary: When to Use `yield` in Fixtures

| Use Case               | Benefit                     |
| ---------------------- | --------------------------- |
| DB connections         | Reuse & clean up after      |
| Temp files or folders  | Delete them after the test  |
| Docker/mocked services | Start/stop around test      |
| Token or login session | Logout or expire token      |
| Nested fixtures        | Structured resource control |


## pytest.fixture(scope=function)
In `pytest`, the `@pytest.fixture(scope=...)` **controls how long a fixture lives** and **how often it’s executed** across your tests.


#### 🔁 `scope` in `pytest.fixture`


```python
@pytest.fixture(scope="function")  # or "class", "module", "package", "session"
def my_fixture():
    # setup code
    yield
    # teardown code
```

#### ✅ Available `scope` Options:

| Scope                  | Fixture runs...                    | Use case                                           |
| ---------------------- | ---------------------------------- | -------------------------------------------------- |
| `"function"` (default) | **Once per test function**         | Most common; independent setup per test            |
| `"class"`              | Once per **test class**            | Share setup between methods in one class           |
| `"module"`             | Once per **test module (file)**    | Shared setup for all tests in one file             |
| `"package"`            | Once per **package** (pytest ≥7.0) | Shared across all test files in a package          |
| `"session"`            | Once for the **entire test run**   | Expensive setup (e.g., DB, Docker) reused globally |

#### 🧪 Examples

##### 1. **Function-Scoped (Default)**

```python
@pytest.fixture
def data():
    print("Function-scoped fixture")
    return {"value": 42}

def test_one(data):
    assert data["value"] == 42

def test_two(data):
    assert "value" in data
```

🔄 Output:

```
Function-scoped fixture
Function-scoped fixture
```

##### 2. **Module-Scoped**

```python
@pytest.fixture(scope="module")
def db_conn():
    print("Module-scoped DB connection")
    return {"conn": "ok"}
```

🔄 Runs **once per file**, reused by all tests in that file.

##### 3. **Session-Scoped**

```python
@pytest.fixture(scope="session")
def spark_cluster():
    print("Starting Spark cluster...")
    yield "cluster-ready"
    print("Shutting down Spark cluster...")
```

✅ Ideal for:

* Docker containers
* Cloud service login
* Expensive ML model loading

---

## 🧠 Scope Lifecycle

| Scope      | Setup runs...     | Teardown runs... |
| ---------- | ----------------- | ---------------- |
| `function` | before each test  | after each test  |
| `class`    | once per class    | after class      |
| `module`   | once per file     | after file       |
| `session`  | once per test run | end of run       |


## pytest.fixture(autouse=True)

#### ✅ 1. `autouse=True, scope="function"`

**Run automatically before and after every test function**

```python
import pytest

@pytest.fixture(autouse=True, scope="function")
def log_test_start_and_end():
    print("🔧 [Setup] Starting test")
    yield
    print("🧹 [Teardown] Test finished")

def test_one():
    print("✅ Running test_one")

def test_two():
    print("✅ Running test_two")
```

##### 🔍 Output:

```
🔧 [Setup] Starting test
✅ Running test_one
🧹 [Teardown] Test finished

🔧 [Setup] Starting test
✅ Running test_two
🧹 [Teardown] Test finished
```

#### ✅ 2. `autouse=True, scope="module"`

**Run once for all tests in a module**

```python
import pytest

@pytest.fixture(autouse=True, scope="module")
def setup_database():
    print("📦 [Setup] Connect to test DB")
    yield
    print("🧹 [Teardown] Disconnect test DB")

def test_insert():
    print("🚀 Running test_insert")

def test_query():
    print("🔎 Running test_query")
```

##### 🧾 Output (runs only once):

```
📦 [Setup] Connect to test DB
🚀 Running test_insert
🔎 Running test_query
🧹 [Teardown] Disconnect test DB
```

#### ✅ 3. `autouse=True, scope="class"`

**Run once per test class**

```python
import pytest

@pytest.fixture(autouse=True, scope="class")
def browser_session():
    print("🌐 [Setup] Launch browser")
    yield
    print("🧹 [Teardown] Close browser")

class TestWebApp:
    def test_login(self):
        print("🧪 test_login")

    def test_logout(self):
        print("🧪 test_logout")
```

##### 🧾 Output:

```
🌐 [Setup] Launch browser
🧪 test_login
🧪 test_logout
🧹 [Teardown] Close browser
```

#### ✅ 4. `autouse=True, scope="session"`

**Run once for the entire test run (all files)**

##### `conftest.py`

```python
import pytest

@pytest.fixture(autouse=True, scope="session")
def setup_test_env():
    print("🌍 [Setup] Initialize test session environment")
    yield
    print("🧹 [Teardown] Clean up session environment")
```

##### Any test file

```python
def test_case():
    print("🔍 Running test_case")
```

##### 🧾 Output (once for the whole suite):

```
🌍 [Setup] Initialize test session environment
🔍 Running test_case
🧹 [Teardown] Clean up session environment
```

#### 🧠 When to Use `autouse=True`

| Use Case                                       | Best Scope |
| ---------------------------------------------- | ---------- |
| Logging per test                               | `function` |
| DB or service setup per file                   | `module`   |
| Shared resource per test class                 | `class`    |
| Global service (e.g. Redis, Kafka, AWS config) | `session`  |

## To Avoid AutoUse=True

### ✅ `autouse=True` means the fixture will be **automatically applied** to:

* Every test function (if `scope="function"`)
* Or every test in a module/class/session, depending on the `scope`

#### ❓ But What If I Don’t Want It for Some Tests?

There are **two ways** to handle this, depending on your intent:


#### 🔹 **Option 1: Use `autouse=False` (the default) — and opt in only where needed**

This gives you **manual control** over when to use the fixture.

```python
@pytest.fixture
def setup_data():
    print("📦 Setup only when needed")
    return {"key": "value"}

def test_needs_fixture(setup_data):
    assert setup_data["key"] == "value"

def test_does_not_need_fixture():
    assert True
```

✅ Use this if only **some** tests require the fixture.

#### 🔹 **Option 2: Use `autouse=True` with a condition inside the fixture**

If you still want **automatic behavior**, but skip it for certain tests, you can use:

* **Markers**
* **Test name inspection**
* **Custom flags**

##### Example: Skip fixture logic for specific test names

```python
import pytest

@pytest.fixture(autouse=True)
def conditional_fixture(request):
    if request.function.__name__ == "test_skip_this":
        print("🚫 Skipping fixture for test_skip_this")
        return
    print("✅ Running fixture for:", request.function.__name__)
    yield
    print("🧹 Teardown for:", request.function.__name__)
```

```python
def test_needs_fixture():
    print("Running test_needs_fixture")

def test_skip_this():
    print("Running test_skip_this")
```

#### 💡 Better: Use `@pytest.mark` to control fixture behavior

```python
@pytest.fixture(autouse=True)
def my_fixture(request):
    if request.node.get_closest_marker("no_fixture"):
        print("🚫 Skipping my_fixture")
        return
    print("✅ Running my_fixture")
    yield
    print("🧹 Teardown my_fixture")
```

```python
@pytest.mark.no_fixture
def test_without_fixture():
    print("Running test_without_fixture")

def test_with_fixture():
    print("Running test_with_fixture")
```

##### ✅ Summary

| Goal                                      | Solution                                                        |
| ----------------------------------------- | --------------------------------------------------------------- |
| Fixture only when test opts in            | Use `autouse=False`                                             |
| Auto-run fixture, but skip for some tests | Use `request.function`, or `@pytest.mark` conditions            |
| Full control across tests                 | Use `conftest.py` + scoped fixtures with marker-based condition |


## Real-World Examples using `pytest` fixtures with `autouse=True` 
* `tempfile` (for temporary file handling)
* a **mock server**
* a **Docker container**

Each shows how `autouse` + `yield` + `scope` come together for hands-free setup and teardown.


#### ✅ 1. **Temporary File Fixture with `tempfile` + `autouse=True`**

```python
import pytest
import tempfile
import os

@pytest.fixture(autouse=True)
def create_temp_file():
    fd, path = tempfile.mkstemp()
    print(f"📄 Created temp file: {path}")
    with os.fdopen(fd, 'w') as tmp:
        tmp.write("test content")
    yield path
    os.remove(path)
    print(f"🧹 Removed temp file: {path}")
```

```python
def test_read_temp_file(create_temp_file):
    with open(create_temp_file) as f:
        content = f.read()
    assert content == "test content"
```

> ⚠️ Note: Even though it’s autouse, you still **need to use the returned value** by matching the fixture name in the test function signature.

#### ✅ 2. **Mock HTTP Server with `http.server`**

Use Python's built-in mock server to simulate an HTTP endpoint.

```python
import pytest
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class MockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"mock response")

@pytest.fixture(scope="module", autouse=True)
def start_mock_server():
    server = HTTPServer(('localhost', 8081), MockHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    print("🌐 Started mock server at http://localhost:8081")
    yield
    server.shutdown()
    print("🧹 Stopped mock server")
```

```python
import requests

def test_mock_server_response():
    r = requests.get("http://localhost:8081")
    assert r.status_code == 200
    assert r.text == "mock response"
```

#### ✅ 3. **Dockerized Service Fixture with Autouse**

Simulate spinning up a Docker container (e.g., Redis, PostgreSQL, etc.) for integration tests.

```python
import pytest
import subprocess
import time

@pytest.fixture(scope="session", autouse=True)
def docker_redis():
    print("🐳 Starting Redis container...")
    subprocess.run(["docker", "run", "-d", "--name", "pytest-redis", "-p", "6379:6379", "redis:6"], check=True)
    time.sleep(3)  # Give it time to start
    yield
    print("🧹 Stopping Redis container...")
    subprocess.run(["docker", "rm", "-f", "pytest-redis"], check=True)
```

```python
import redis

def test_redis_connection():
    r = redis.Redis(host='localhost', port=6379)
    r.set("pytest", "works")
    assert r.get("pytest") == b"works"
```

---

## ✅ Summary

| Resource         | Fixture Tool               | Scope      | Autouse? | Use Case                              |
| ---------------- | -------------------------- | ---------- | -------- | ------------------------------------- |
| Temp file        | `tempfile`, `os`           | `function` | ✅        | File-based tests                      |
| Mock HTTP Server | `http.server`, `threading` | `module`   | ✅        | API client tests                      |
| Docker container | `subprocess`, Docker CLI   | `session`  | ✅        | Redis, Postgres, etc. for integration |


## patch.object
`patch.object` is a powerful tool in Python’s `unittest.mock` module, and it's especially useful when you're testing code that interacts with **class instances or external dependencies**.

#### 🔧 **What is `patch.object`?**

`patch.object(target, attribute, new=...)` temporarily **replaces an attribute of an object or class** with a mock or custom value **during a test**.

✅ It's typically used to:

* Mock a method or property of a class
* Intercept a call without changing the actual code
* Control behavior (e.g., force a return value)

#### ✅ Syntax

```python
from unittest.mock import patch

patch.object(target_object_or_class, 'method_or_property_name', new=mock_or_value)
```

#### 🧪 Example 1: Mock a method on a class

```python
class EmailClient:
    def send_email(self, to, subject):
        print(f"Sending email to {to} with subject {subject}")
        return True
```

##### Test using `patch.object`:

```python
from unittest.mock import patch

def test_send_email_called():
    client = EmailClient()
    with patch.object(EmailClient, 'send_email', return_value=False) as mock_method:
        result = client.send_email("user@example.com", "Hello")
        assert result is False
        mock_method.assert_called_once_with("user@example.com", "Hello")
```

#### 🧪 Example 2: Mock a property or constant

```python
class Config:
    ENV = "prod"

def test_override_constant():
    with patch.object(Config, 'ENV', 'test'):
        assert Config.ENV == 'test'
    assert Config.ENV == 'prod'  # Back to original
```


#### 🧪 Example 3: Patch instance method

```python
class DataFetcher:
    def fetch(self):
        return "real data"

def test_instance_method():
    df = DataFetcher()
    with patch.object(df, 'fetch', return_value="mocked data"):
        assert df.fetch() == "mocked data"
```

#### 🧠 When to Use `patch.object`

| Use Case                        | Why `patch.object` Helps                  |
| ------------------------------- | ----------------------------------------- |
| Mock instance/class method      | You can override just one method for test |
| Override class constant         | Temporarily change config                 |
| Patch method on one object only | More precise than `patch()`               |

#### 📝 Notes

* `patch.object` works as a **context manager (`with`)** or a **decorator**
* After the context ends, the original method is restored
* Works with both **classes and instances**

## pytest-mock vs unittest.mock
✅ **`pytest` fully supports `unittest.mock.patch`**, including:

* `patch`
* `patch.object`
* `patch.dict`
* `MagicMock`, `Mock`, etc.

Because `pytest` is **compatible with the standard library**, you can use `unittest.mock` tools directly — or, for even more convenience, use `pytest-mock`, a plugin that wraps `patch` into a more elegant format.


#### ✅ Option 1: Use `unittest.mock.patch` directly in pytest

```python
from unittest.mock import patch

class MyService:
    def get_status(self):
        return "live"

def test_patch_with_unittest():
    with patch.object(MyService, 'get_status', return_value="mocked"):
        service = MyService()
        assert service.get_status() == "mocked"
```

#### ✅ Option 2: Use `pytest-mock` plugin (`mocker` fixture)

Install it:

```bash
pip install pytest-mock
```

Use it in your test:

```python
def test_patch_with_mocker(mocker):
    mocker.patch.object(MyService, 'get_status', return_value="mocked")
    assert MyService().get_status() == "mocked"
```

No `with` block, and **scoped mocking is automatically cleaned up** after the test — cleaner and more pytest-native.

#### 🔁 When to Use Each

| Use                             | Tool                             |
| ------------------------------- | -------------------------------- |
| Traditional `with patch(...)`   | `unittest.mock.patch`            |
| Cleaner, pytest-native patching | `pytest-mock` (`mocker`)         |
| Complex class/function patching | Both are fine — preference-based |


#### 🧠 Summary

| Question                                  | Answer                             |
| ----------------------------------------- | ---------------------------------- |
| Can `pytest` use `patch` like `unittest`? | ✅ Yes                              |
| Is there a cleaner way with `pytest`?     | ✅ Yes – use `pytest-mock` plugin   |
| Do both restore after the test?           | ✅ Yes – both restore automatically |

