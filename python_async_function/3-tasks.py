#!/usr/bin/env python3
# This shebang allows the script to be run directly from the command line.

import asyncio  # Import asyncio to create and manage asynchronous tasks.

# Import the wait_random coroutine from the previous task (0-basic_async_syntax.py).
# __import__ dynamically loads the module, and we access the wait_random function.
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A Task object that will execute wait_random asynchronously.
    """
    # Create and return the task without awaiting it.
    # This schedules the coroutine to run in the background.
    return asyncio.create_task(wait_random(max_delay))
