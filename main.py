from sqlalchemy import text
import uvicorn
from fastapi import Depends, FastAPI
from database import get_db
from sqlalchemy.orm import Session
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession




app = FastAPI()

# create table using SQL function
@app.get("/create-table")
async def create_table(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(
            text(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL
                    );
                '''
            )
            
        )
        await db.commit()  # Commit the transaction
        return {"message": "Table created successfully"}

    except Exception as e:
        print(e)
        return {"error": str(e)}


# loop = asyncio.get_event_loop()
# if loop.is_running():
#     # If the loop is already running, use it to run the coroutine
#     loop.create_task(create_table())
# else:
#     # If no loop is running, use asyncio.run()
#     asyncio.run(create_table())

@app.get('/')
async def root():
    return {'message': 'Hello World'}




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host= '127.0.0.1', port=5000)
