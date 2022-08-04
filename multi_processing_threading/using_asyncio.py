import asyncio

# using async keyword we define a coroutine
# coroutines need to be executed inside an event loop
# coroutines are to be awaited with await keyword in order to execute them
import time
# asyncio is helpful for IO bound tasks only


async def main():
    print("our main entry point function to our program")
    # await suspends execution and gives control back to event loop to run some other task
    task = asyncio.create_task(print_something_async("Python"))
    returned_text = await task
    print(returned_text)
    print("done")


async def print_something_async(text):
    await asyncio.sleep(3)
    return "Hello " + text


asyncio.run(main())  # create an event loop and pass the main coroutine
