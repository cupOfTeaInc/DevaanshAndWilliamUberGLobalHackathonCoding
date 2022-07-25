import asyncio
import schedule_maker
import execute_schedule
import website 
import data_collection
from os import path

def run() :
    if path.exists('schedule.json'): # Check if schedule already exiss
        pass
    else:
        schedule_maker.make_schedule_for_all() # Create schedule if not
    
    asyncio.run(execute_schedule.execute_all()) # Run all schedules
    # website.main() # Begin website

if __name__ == "__main__":
    run()