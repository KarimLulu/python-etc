import asyncio


bg_tasks = set()


async def child():
    print('started child')
    # When child hits await, the scheduler switches to another task, which is main
    await asyncio.sleep(1)
    print('finished child')


async def main():
    task = asyncio.create_task(child())
    # hold the reference to the task
    # in a global set
    bg_tasks.add(task)
    # automatically remove the task
    # from the set when it's done
    task.add_done_callback(bg_tasks.discard)
    # When create_task is called, it is scheduled but not yet executed.
    print('before sleep')
    # When main hits await, the scheduler switches to child.
    await asyncio.sleep(0)
    print('after sleep')
    await task

asyncio.run(main())
