"""Intermediate thread synchronization and ThreadPoolExecutor examples.

Threads share objects. Sharing is convenient, but two threads can change the
same object at the wrong time. That is a race condition. A Lock is like one
bathroom key: only its current holder may enter the critical section.

This file demonstrates ThreadPoolExecutor, Future objects, Lock, RLock,
Semaphore, Event, timeout-aware waiting, and clean shutdown.
"""

from __future__ import annotations

from concurrent.futures import Future, ThreadPoolExecutor, as_completed
import threading
import time


def print_number(number: int, delay: float = 0.1) -> str:
    """Preserved original pool task, with a short configurable wait."""
    time.sleep(delay)
    return f"Number: {number}"


class SafeCounter:
    """A counter whose read-change-write operation is protected by a lock."""

    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self, repetitions: int) -> None:
        for _ in range(repetitions):
            with self._lock:
                self.value += 1


def thread_pool_demo() -> None:
    """Use a reusable pool instead of manually creating many threads."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix="number") as executor:
        # map() preserves input order, even if tasks finish in another order.
        for result in executor.map(print_number, numbers):
            print(result)


def future_demo() -> None:
    """Process results in completion order and handle each task separately."""
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_number: dict[Future[str], int] = {
            executor.submit(print_number, number, 0.02 * (4 - number)): number
            for number in [1, 2, 3]
        }
        for future in as_completed(future_to_number):
            number = future_to_number[future]
            try:
                print(f"Task {number} -> {future.result()}")
            except Exception as error:
                print(f"Task {number} failed: {error}")


def lock_demo() -> None:
    counter = SafeCounter()
    workers = [threading.Thread(target=counter.increment, args=(10_000,)) for _ in range(4)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print("Safe counter:", counter.value)  # Always 40000.


def semaphore_and_event_demo() -> None:
    """Limit concurrent access and signal that setup is ready."""
    capacity = threading.Semaphore(2)
    ready = threading.Event()

    def worker(worker_id: int) -> None:
        if not ready.wait(timeout=2):
            print(f"Worker {worker_id}: setup timed out")
            return
        with capacity:
            print(f"Worker {worker_id}: entered limited section")
            time.sleep(0.05)

    workers = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
    for worker_thread in workers:
        worker_thread.start()
    ready.set()
    for worker_thread in workers:
        worker_thread.join()


def synchronization_notes() -> None:
    notes = [
        "Lock: one owner at a time; not re-entrant.",
        "RLock: the same thread may acquire it repeatedly.",
        "Semaphore: allows a limited number of simultaneous owners.",
        "Event: a one-to-many ready/stop signal.",
        "Condition: wait for a state change while coordinating around a lock.",
        "Barrier: a fixed group waits until everyone reaches the checkpoint.",
    ]
    print("\n".join(notes))


if __name__ == "__main__":
    thread_pool_demo()
    future_demo()
    lock_demo()
    semaphore_and_event_demo()
    synchronization_notes()

# Deadlock warning: if two threads acquire multiple locks in different orders,
# each can wait for the other forever. Keep critical sections short, acquire
# locks in one global order, prefer `with lock:`, and use timeouts when useful.

