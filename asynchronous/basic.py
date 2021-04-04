import asyncio

async def sekar():
    print('Sekardayu Hana Pradiani')
    calling_task = asyncio.create_task(calling())
    yelling_task = asyncio.create_task(yelling())
    await yelling_task
    await calling_task
    print('Finished')

async def calling():
    print('Calling....')
    await asyncio.sleep(5)

async def yelling():
    print('Yelling')
    await asyncio.sleep(2)

asyncio.run(sekar())