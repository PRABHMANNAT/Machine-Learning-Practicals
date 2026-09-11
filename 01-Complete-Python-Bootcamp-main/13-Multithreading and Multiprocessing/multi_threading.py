"""Beginner-friendly introduction to Python threads.

Explain it like I am 5
-----------------------
A thread is like one helper inside a kitchen. Several helpers share the same
kitchen (memory). While one helper waits for the oven, another can wash dishes.
That makes threads useful for I/O-bound work: waiting for files, networks, or
databases.

Threads provide concurrency. In regular CPython, the Global Interpreter Lock
(GIL) usually lets only one thread execute Python bytecode at a time. Therefore,
threads normally do not speed up pure Python CPU-heavy calculations. Use
processes for CPU-bound work when measurement shows that parallelism helps.

Run this file directly:
    python multi_threading.py

Importing it is safe: the demo only runs under the main guard.
"""

from __future__ import annotations

import threading
import time


def print_numbers(delay: float = 0.2) -> None:
    """Print five numbers, pausing to imitate an I/O wait."""
    for number in range(5):
        time.sleep(delay)
        print(f"Number: {number} | thread={threading.current_thread().name}")


def print_letters(delay: float = 0.2) -> None:
    """Print five letters, pausing to imitate an I/O wait."""
    for letter in "abcde":
        time.sleep(delay)
        print(f"Letter: {letter} | thread={threading.current_thread().name}")


def run_demo() -> None:
    """Create, start, and join two threads.

    start() asks the thread to begin. join() makes the main thread wait for it.
    Output order can change between runs; that is normal concurrent behavior.
    """
    number_thread = threading.Thread(target=print_numbers, name="number-worker")
    letter_thread = threading.Thread(target=print_letters, name="letter-worker")

    started_at = time.perf_counter()
    number_thread.start()
    letter_thread.start()
    number_thread.join()
    letter_thread.join()

    elapsed = time.perf_counter() - started_at
    print(f"Both threads finished in about {elapsed:.2f} seconds.")
    print("Sequential waiting would take about 2.00 seconds.")


if __name__ == "__main__":
    run_demo()

