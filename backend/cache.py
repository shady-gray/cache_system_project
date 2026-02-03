#Author: Basil Bassey

import time

# In-memory cache dictionary
cache_store = {}

# TTL (seconds)
TTL = 60

# Stats
hits = 0
misses = 0

def get(key):
    """Get data from cache"""
    global hits, misses

    if key in cache_store:
        value, expiry = cache_store[key]

        if time.time() < expiry:
            hits += 1
            return value
        else:
            # expired
            del cache_store[key]

    misses += 1
    return None

def set(key, value):
    """Set data in cache with TTL"""
    expiry = time.time() + TTL
    cache_store[key] = (value, expiry)

def clear():
    """Clear cache"""
    global cache_store
    cache_store = {}

def stats():
    return {
        "hits": hits,
        "misses": misses,
        "items": len(cache_store)
    }
