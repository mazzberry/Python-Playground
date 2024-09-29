import asyncio

async def fetch_data(delay, id):
    # Simulate a delay in fetching data
    print(f'fetching data id : {id}')
    await asyncio.sleep(delay)  # شبیه‌سازی تأخیر
    print('data fetched, id:', id)
    return {'data': 'some data', 'id': id}

async def main():
    # ایجاد و اجرای وظایف همزمان
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)
    
    # همزمان هر دو وظیفه را اجرا کن
    result1, result2 = await asyncio.gather(task1, task2)
    
    print(f'Received result: {result1}')
    print(f'Received result2: {result2}')

asyncio.run(main())