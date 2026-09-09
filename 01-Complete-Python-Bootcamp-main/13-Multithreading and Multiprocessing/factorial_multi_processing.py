"""CPU-bound factorial work with a process pool.

The original inputs 5000, 6000, 700, and 8000 are preserved. Printing the full
integers floods the terminal and can dominate timing, so this version reports
digit counts and a bounded checksum instead.

Multiprocessing has startup/data-transfer cost. It is not automatically faster,
especially for small tasks. Measure the real workload with perf_counter().
"""

from __future__ import annotations

import math
import multiprocessing as mp
import os
import sys
import time


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(100_000)


def compute_factorial_summary(number: int) -> tuple[int, int, int, int]:
    """Return input, decimal digit count, checksum, and worker process ID."""
    if number < 0:
        raise ValueError("factorial is undefined for negative integers")
    digits = str(math.factorial(number))
    checksum = sum(int(character) for character in digits) % 10_000
    return number, len(digits), checksum, os.getpid()


def run_sequential(numbers: list[int]) -> list[tuple[int, int, int, int]]:
    return [compute_factorial_summary(number) for number in numbers]


def run_parallel(numbers: list[int], workers: int | None = None):
    with mp.Pool(processes=workers) as pool:
        return pool.map(compute_factorial_summary, numbers)


def main() -> None:
    numbers = [5000, 6000, 700, 8000]

    sequential_start = time.perf_counter()
    sequential_results = run_sequential(numbers)
    sequential_time = time.perf_counter() - sequential_start

    parallel_start = time.perf_counter()
    parallel_results = run_parallel(numbers, workers=min(4, mp.cpu_count()))
    parallel_time = time.perf_counter() - parallel_start

    for number, digits, checksum, process_id in parallel_results:
        print(f"{number}! has {digits} digits; checksum={checksum}; worker pid={process_id}")

    sequential_core = [result[:3] for result in sequential_results]
    parallel_core = [result[:3] for result in parallel_results]
    print("Results match:", sequential_core == parallel_core)
    print(f"Sequential: {sequential_time:.4f}s")
    print(f"Parallel:   {parallel_time:.4f}s")
    print("Faster in this run:", "parallel" if parallel_time < sequential_time else "sequential")


if __name__ == "__main__":
    mp.freeze_support()
    main()

