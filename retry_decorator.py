import time
import asyncio
import functools
import inspect

def retry(max_retries=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        is_coroutine = inspect.iscoroutinefunction(func)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return await func(*args, **kwargs)
                except exceptions:
                    attempts += 1
                    if attempts == max_retries:
                        raise
                    await asyncio.sleep(delay)

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempts += 1
                    if attempts == max_retries:
                        raise
                    time.sleep(delay)

        return async_wrapper if is_coroutine else sync_wrapper
    return decorator