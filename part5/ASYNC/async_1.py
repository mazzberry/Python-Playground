import asyncio

async def fetch_data(delay, id):
    # Simulate a delay in fetching data
    print(f'fetching data id : {id}')
    await asyncio.sleep(delay)
    print('data fetched, id:',id)
    return {'data':'some data', 'id':id}

async def main():
    task1 = fetch_data(2,1)
    task2 = fetch_data(2,2)
    
    result = await task1
    print(f'Received result: {result}')
    
    result2 = await task2
    print(f'Received result2: {result2}')
    
asyncio.run(main())