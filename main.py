from fastapi import FastAPI, HTTPException
import pymysql
import os

# Uncomment for Vercel Development
# rename example.env file to .env and update 
# with planetscale credentials and on vercel aswell
connection = pymysql.connect(
    host=os.environ.get('host'),
    database=os.environ.get('database'),
    user=os.environ.get('user'),
    password=os.environ.get('password',''),
    ssl_ca="cacert.pem"
)

# Uncomment for Local Development
# Only for use with local uvicorn hot reloading
# uvicorn main:app --reload
# connection = pymysql.connect(
#     host='aws.connect.psdb.cloud',
#     database='',
#     user='',
#     password='',
#     ssl_ca="cacert.pem"
# )

app = FastAPI()

@app.post("/walls",status_code=201)
async def add_wall(id: int, name: str, length: float, volume: float):
    # Execute an INSERT query to add the wall to the database
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO walls (id, name, length, volume) VALUES (%s, %s, %s, %s)", (id, name, length, volume))
        connection.commit()

    # Return a success message
    return {"message": "Wall added successfully"}

@app.get("/")
def HelloWorld():
    sum = 1 + 1
    return {"message": "Hello, World! (%s)" % sum}

@app.get("/walls")
async def get_walls():
    # Execute a SELECT query to retrieve all walls
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM walls")
        results = cursor.fetchall()

    # Return the results as JSON
    return {"walls": results}

@app.get("/walls/sum")
async def get_wall_sum():
    # Execute a SELECT query to retrieve the sum of wall volumes
    with connection.cursor() as cursor:
        cursor.execute("SELECT SUM(volume) FROM walls")
        result = cursor.fetchone()
        if result is not None:
            result = result[0]

    # Return the result as JSON
    return {"sum": result}

@app.delete("/walls/{wall_id}")
async def delete_wall(wall_id: int):
    # Execute a DELETE query to remove the wall from the database
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM walls WHERE id = %s", (wall_id,))
        connection.commit()

    # Return a success message
    return {"message": "Wall deleted successfully"}

