#!/usr/bin/env python3
"""Exercise """


import redis
from typing import AnyStr, Union
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
