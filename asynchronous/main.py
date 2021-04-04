import asyncio

async def fetch():
    print('Start to fetch')
    await asyncio.sleep(2)
    print('Finish to fetch')
    return {'data': 'Sekardayu Hana Pradiani'}

async def print_numbers():
    for i in range(20):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    fetch_task = asyncio.create_task(fetch())
    print_task = asyncio.create_task(print_numbers())

    value = await fetch_task
    print(value)
    await print_task


asyncio.run(main())