#!/usr/bin/env python3
import requests
import time
from functools import wraps

# In-memory cache with expiration
cache = {}
cache_expiration = 10  # cache expiration time in seconds


def cache_decorator(func):
    @wraps(func)
    def wrapper(url):
        current_time = time.time()
        cache_key = f"count:{url}"
        # Check if the cached data is available and not expired
        if cache_key in cache:
            cache_entry, timestamp = cache[cache_key]
            if current_time - timestamp < cache_expiration:
                return cache_entry
        # Call the function and cache the result
        result = func(url)
        cache[cache_key] = (result, current_time)
        return result
    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()  # Ensure we handle HTTP errors
    return response.text


# Example usage (You can comment out this part when you run the code)
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))  # Fetch and cache the page
    time.sleep(5)  # Wait less than cache expiration time
    print(get_page(url))  # Return cached page
    time.sleep(6)  # Wait more than cache expiration time
    print(get_page(url))  # Fetch and cache the page again
