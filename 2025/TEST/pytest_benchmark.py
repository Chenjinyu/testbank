"""
pytest-benchmark(https://pytest-benchmark.readthedocs.io/en/latest/index.html)
used to test the performance of code snippets and functions in Python.

"""

import pytest
from fastapi.testclient import TestClient
from my.app import app

client = TestClient(app)
