#!/usr/bin/env python3
"""Exercise """

from functools import wraps
from typing import Optional, Callable, Union
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """count_calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        self._redis.rpush(f"{method.__qualname__}:outputs", output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """replay to show call history of a function"""
    redis_cache = redis.Redis()
    name = method.__qualname__
    inputs = redis_cache.lrange(f"{method.__qualname__}:inputs", 0, -1)
    outputs = redis_cache.lrange(f"{method.__qualname__}:outputs", 0, -1)
    zipped_list = tuple(zip(inputs, outputs))
    print(f"{method.__qualname__} was called {len(zipped_list)} times:")
    for (i, o) in zipped_list:
        print(f"{name}(*{i.decode('UTF-8')},) -> {o.decode('UTF-8')}")


class Cache:
    """Cache Class"""
    def __init__(self):
        """Cache init"""
        self._redis = redis.Redis()

    def __del__(self):
        """Cache delete"""
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data"""
        random_id = str(uuid.uuid1())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable[[bytes], any]] = None) -> Optional[any]:
        """get value of key with correct original datatype"""
        value = self._redis.get(key)
        if value is not None:
            if fn:
                return fn(value)
            return value
        return None

    def get_str(self, key) -> str:
        """get_str"""
        return self.get(key, lambda value: value.decode('utf-8'))

    def get_int(self, key) -> int:
        """get_int"""
        return self.get(key, lambda value: int(value.decode('utf-8')))


if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
