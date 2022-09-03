# Imports
from scholarly import scholarly
from scholarly import ProxyGenerator
from fastapi import FastAPI

# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

# Intitialize fast API
app = FastAPI()

@app.get("/")
async def root():
    return {"response": "Welcome to AcademusFeed"}

@app.get("/auth/{name}")
async def read_item(name):
    name = name.replace('_', ' ')
    search_query = scholarly.search_author(name)
    first_result = next(search_query)
    # Retrieve all the details for the author
    author = scholarly.fill(first_result)
    return {"author": author}