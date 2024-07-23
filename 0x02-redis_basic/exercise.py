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
            fn: Optional[Callable[[object], str]] = None) -> str:
        """get value of key with correct original datatype"""
        value = self._redis.get(key)
        if value and fn:
            return fn(value)
        elif value and fn is None:
            return value.decode('utf-8')
        else:
            return fn(value)
