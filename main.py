from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class msgstuc(BaseModel):
    message: str

messages = []
@app.post('/post')

def msg(payload: msgstuc):
    m_id = uuid.uuid1()
    me = payload.dict()
    me['mid'] = str(m_id)
    messages.append(me)

    print(messages)
    

    return messages

@app.get('/secret/{m_id}')
def getmsg(m_id : str):
    for i in messages:
        if i['mid'] == m_id:
            found = i
            messages.remove(i)

            return found
        continue

    return {'Alert' : "This secret has already been burned or never existed."}