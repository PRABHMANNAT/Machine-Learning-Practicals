"""Process pools, queues, pipes, shared memory, and synchronization.

Processes do not normally share Python objects. Data sent to a spawned process
must usually be pickled, so worker functions should be defined at module level.
Queues and pipes send messages; Value/Array/shared_memory deliberately share a
small region. Prefer message passing because shared state is harder to reason
about.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp
import os
import time


def square_number(number: int, delay: float = 0.05) -> str:
    """Preserved original pool task."""
    time.sleep(delay)
    return f"Square: {number * number} (pid={os.getpid()})"


def queue_worker(values: list[int], output: mp.Queue) -> None:
    output.put(sum(values))


def pipe_worker(connection) -> None:
    connection.send({"pid": os.getpid(), "message": "hello from child"})
    connection.close()


def increment_shared(counter: mp.Value, lock: mp.Lock, repetitions: int) -> None:
    for _ in range(repetitions):
        with lock:
            counter.value += 1


def process_pool_demo() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 2, 3, 12, 14]
    with ProcessPoolExecutor(max_workers=3) as executor:
        for result in executor.map(square_number, numbers):
            print(result)


def futures_demo() -> None:
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(square_number, n, 0.01): n for n in [3, 4, 5]}
        for future in as_completed(futures):
            number = futures[future]
            try:
                print(number, "->", future.result(timeout=3))
            except Exception as error:
                print(f"Task {number} failed: {error}")


def queue_pipe_shared_demo() -> None:
    result_queue = mp.Queue()
    queue_process = mp.Process(target=queue_worker, args=([1, 2, 3], result_queue))
    queue_process.start()
    print("Queue result:", result_queue.get(timeout=3))
    queue_process.join()
    result_queue.close()
    result_queue.join_thread()

    parent_end, child_end = mp.Pipe(duplex=False)
    pipe_process = mp.Process(target=pipe_worker, args=(child_end,))
    pipe_process.start()
    child_end.close()
    print("Pipe result:", parent_end.recv())
    parent_end.close()
    pipe_process.join()

    counter = mp.Value("i", 0)
    lock = mp.Lock()
    workers = [mp.Process(target=increment_shared, args=(counter, lock, 5_000)) for _ in range(2)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print("Shared counter:", counter.value)


if __name__ == "__main__":
    mp.freeze_support()
    process_pool_demo()
    futures_demo()
    queue_pipe_shared_demo()

# Other tools: multiprocessing.Pool, Array, Manager, shared_memory, Event,
# Semaphore, Condition, and Barrier. shared_memory owners must close(), and one
# owner must unlink() exactly once. Manager proxies are convenient but slower.

