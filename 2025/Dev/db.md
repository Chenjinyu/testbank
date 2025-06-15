## Table of Contents
- [PostgreSQL](#postgresql)

---
## PostgreSQL

### How does **PostgreSQL + asyncpg** handle async?

#### ✅ What is `asyncpg`?

* `asyncpg` is a **high-performance asynchronous PostgreSQL driver** for Python (built on `asyncio`)
* It’s used when you want to **query your Postgres database without blocking** the event loop (e.g., in FastAPI or an async GraphQL server like Strawberry)

#### ⚙️ How It Works (Internally)

1. **`asyncpg` opens an async TCP connection** to PostgreSQL.
2. Every query you run (e.g., `await conn.fetch(...)`) is **non-blocking**.
3. While waiting for Postgres to respond, your app can do **other work** (e.g., handle other requests).
4. Once the response comes back, your coroutine resumes.

#### 🔁 Typical Usage

```python
import asyncpg
import asyncio

async def fetch_users():
    conn = await asyncpg.connect(user='postgres', database='testdb')
    rows = await conn.fetch('SELECT * FROM users')
    await conn.close()
    return rows
```

> This allows you to handle **thousands of concurrent DB requests** more efficiently than using blocking drivers like `psycopg2`.

#### 🚀 Benefits of asyncpg

| Feature              | Benefit                              |
| -------------------- | ------------------------------------ |
| Async I/O            | No thread-blocking                   |
| Fast binary protocol | Faster than traditional drivers      |
| Connection pooling   | Supported with `asyncpg.create_pool` |

---
