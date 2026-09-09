"""Threaded web fetching example with timeouts and error handling.

Web requests spend most of their time waiting, so this is I/O-bound work and a
good fit for threads. The original LangChain v0.2 URLs are retained as lesson
inputs. Websites change; HTTP errors are normal and must not crash the pool.

Install optional dependencies:
    python -m pip install requests beautifulsoup4

Be respectful: obey site terms and robots rules, identify your client when
appropriate, limit concurrency, retry gently, and never overload a server.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import time

import requests
from bs4 import BeautifulSoup


URLS = [
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/",
]


@dataclass(frozen=True)
class FetchResult:
    url: str
    status: int | None
    character_count: int
    error: str | None = None


def fetch_content(url: str, timeout: float = 10.0) -> FetchResult:
    """Fetch and parse one page; return data instead of printing in a worker."""
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "Python-learning-example/1.0"},
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(" ", strip=True)
        return FetchResult(url, response.status_code, len(text))
    except requests.RequestException as error:
        return FetchResult(url, None, 0, f"{type(error).__name__}: {error}")


def fetch_all(urls: list[str], max_workers: int = 3) -> list[FetchResult]:
    """Fetch pages concurrently and collect results in completion order."""
    results: list[FetchResult] = []
    with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="fetch") as pool:
        future_to_url = {pool.submit(fetch_content, url): url for url in urls}
        for future in as_completed(future_to_url):
            results.append(future.result())
    return results


def main() -> None:
    started_at = time.perf_counter()
    results = fetch_all(URLS)
    for result in results:
        if result.error:
            print(f"Could not fetch {result.url}: {result.error}")
        else:
            print(
                f"Fetched {result.character_count} characters "
                f"from {result.url} (HTTP {result.status})"
            )
    print(f"Finished {len(results)} requests in {time.perf_counter() - started_at:.2f}s")


if __name__ == "__main__":
    main()

