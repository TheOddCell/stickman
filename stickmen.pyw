import asyncio
# Grab the whole gang!

async def run_program(args):
    process = await asyncio.create_subprocess_exec(
        "python3", "stickman.pyw", *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

async def main():
    tasks = [
        ["alanOrange", "True"],
        ["alanRed", "False"],
        ["alanBlue", "False"],
        ["alanGreen", "False"],
        ["alanYellow", "False"],
        ["alanPurple", "False"]
    ]
    ddd = []
    for i, args in enumerate(tasks):
        ddd.append(asyncio.create_task(run_program(args)))
        await asyncio.sleep(6)  # Delay each task by 6 seconds
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
