import asyncio
import schedule_maker
import execute_schedule
import website 
import data_collection
from os import path

def run() :
    if path.exists('schedule.json'):
        pass
    else:
        schedule_maker.make_schedule_for_all()
    
    asyncio.run(execute_schedule.execute_all())
    website.main()

if __name__ == "__main__":
    run()