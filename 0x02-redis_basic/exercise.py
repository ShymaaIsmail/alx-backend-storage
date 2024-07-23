#!/usr/bin/env python3
"""Exercise """


import redis
from typing import Optional, Callable, Union
import uuid


class Cache:
    """Cache Class"""
    def __init__(self):
        """Cache init"""
        self._redis = redis.Redis()

    def __del__(self):
        """Cache delete"""
        self._redis.flushdb()

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
            return value.decode('utf-8')
        return None

    def get_str(self, key) -> str:
        """get_str"""
        return self.get(key, lambda value: value.decode('utf-8'))

    def get_int(self, key) -> int:
        """get_int"""
        return self.get(key, lambda value: int(value.decode('utf-8')))
