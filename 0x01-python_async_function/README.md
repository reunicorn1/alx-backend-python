# 0x01. Python - Async

Asynchronous I/O (async IO) in Python allows you to write programs that can handle multiple tasks at the same time without blocking the execution of the program. This is particularly useful for I/O-bound operations, such as network requests, file I/O, or interacting with a database, where you might need to wait for some time to get a response.

### Event Loop
The event loop is the core of every asyncio application. It runs in a single thread and manages the execution of asynchronous tasks.

### Coroutines
These are special functions that can have their execution paused and resumed because they maintain their state between pauses.

coroutines are the key ingredient to make asynchronous programming on concurrency.
When a coroutine calls await, it yields control back to the event loop, allowing other tasks to run.

### Tasks
Tasks are used to schedule the execution of coroutines.
asyncio.create_task can be used to run a coroutine concurrently as an asyncio Task.


## Tasks/Files

|    Tasks       |     Files                     |
|----------------|-------------------------------|
|0. The basics of async|``0-basic_async_syntax.py``|
|1. Let's execute multiple coroutines at the same time with async|`1-concurrent_coroutines.py`|
|2. Measure the runtime|`3-tasks.py`|
|3. Tasks|`3-to_str.py`|
|4. Tasks|`4-tasks.py`|

