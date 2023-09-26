
from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host='0.0.0.0', port=6379, decode_responses=True)


@app.get("/visit/{site}")
def visit(site: str):
    if r.get(site) == None:
        r.set(site, 1)
    else :
        r.set(site,int(r.get(site))+1)    
    return f'New visit, now is {r.get(site)}'

@app.get("/show/{site}")
def new_show(site : str):
    return r.get(site)
    