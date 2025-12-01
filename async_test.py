#!/usr/bin/env python3

"""
Testing Asynchronous I/O
"""

import asyncio

async def sample_async_function():
    for i in range(5):
        print("Hello!")

    for i in range(5):
        print("World")

    await asyncio.sleep(2)

async def second_sample_async_function():
    for i in range(5):
        print("Hello!")
        await asyncio.sleep(2)
        print("World!")



def main():
    asyncio.run(second_sample_async_function())


if __name__ == "__main__":
    main()
