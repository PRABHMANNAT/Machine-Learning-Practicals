"""Beginner-friendly introduction to multiprocessing.

A process is like a separate kitchen. It has its own Python interpreter and
memory. Separate kitchens can truly cook on different CPU cores, which helps
CPU-bound work. Creating and communicating between processes costs more than
using threads, so measure before choosing.

Windows and macOS commonly use "spawn". Child processes import the main module,
so process creation MUST be inside `if __name__ == "__main__":`.
"""

from __future__ import annotations

import multiprocessing as mp
import os
import time


def square_numbers(delay: float = 0.1) -> None:
    """Preserved original square worker."""
    for number in range(5):
        time.sleep(delay)
        print(f"Square: {number * number} | pid={os.getpid()}", flush=True)


def cube_numbers(delay: float = 0.15) -> None:
    """Preserved original cube worker."""
    for number in range(5):
        time.sleep(delay)
        print(f"Cube: {number ** 3} | pid={os.getpid()}", flush=True)


def run_demo() -> None:
    square_process = mp.Process(target=square_numbers, name="square-process")
    cube_process = mp.Process(target=cube_numbers, name="cube-process")

    started_at = time.perf_counter()
    square_process.start()
    cube_process.start()
    square_process.join(timeout=5)
    cube_process.join(timeout=5)

    for process in [square_process, cube_process]:
        if process.is_alive():
            process.terminate()  # Last resort; finally blocks may not run.
            process.join()
            raise RuntimeError(f"{process.name} did not finish in time")
        if process.exitcode != 0:
            raise RuntimeError(f"{process.name} exited with {process.exitcode}")

    print(f"Processes finished in about {time.perf_counter() - started_at:.2f}s")


if __name__ == "__main__":
    mp.freeze_support()
    run_demo()

