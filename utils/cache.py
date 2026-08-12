from cachetools import TTLCache

exchange_rate_cache = TTLCache(maxsize=500, ttl=300)
