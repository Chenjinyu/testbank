"""
pytest-benchmark(https://pytest-benchmark.readthedocs.io/en/latest/index.html)
used to test the performance of code snippets and functions in Python.

pytest-benchmark is a plugin for measuring and comparing the performance of Python code inside your pytest test suite. you can use it on many types of applications, anywhere performance matters and you want repeatable benchmarks

the common applications areas where pytest-benchmark is used are:
1. web applications & APIs
 - measure response time to Flask/Django/FastAPI endpoints (without full load testing, more about code path efficienty).
 - Example: Comparing JSON serialization speed between `ujson` vs `orjson` in a Falsk API.

2. Microservices & distributed systems
 - Benchmark Kafka or RabbitMQ message processing handlers.
 - Example: How many messages per second can your consumer handle before slowing down?
 
3. Data processing pipelines
 - Benchmark ETL jobs: reading CVS/JSON/Parquet, transforming data, loading into DB.
 - Example: 
   - measuring time taken to process 1 million records with Pandas vs Dask.
   - measuring time takes from grouping a pandas datagrame with 1 million rows by different columns.
   
4. Database interactions
 - Measure query perforamance vs psycopg2, sqlalchemy, or syyncpg.
 - Example: Compare ORM vs raw SQL query execution times.
 
5. Algorithms & scientific computing
 - Test performance of algorithms: sorting, graph traversal, ML preprocessing.
 - Example: Compare performance of NumPy vectorized operations vs pure Python loops.

etc.

DO NOT USE FOR:
- Full load testing or stress testing (use Locust, JMeter, or k6 instead).
- End-to-end distributed system benchmarking under real user traffic.
- Long-running performance monitoring (use Prometheus, Grafana, Datadog).

```sh
pytest 2025/TEST/perf/pytest_benchmark_eg.py --benchmark-only 

pytest 2025/TEST/perf/pytest_benchmark_eg.py --benchmark-only --benchmark-histogram=./2025/TEST/perf/reports/perf.png
```

"""

# simple example to benchmark a fibonacci function
def fib(n: int) -> int:
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

def test_fib_benchmark(benchmark):
    result = benchmark(fib, 20)
    assert result == 10946
