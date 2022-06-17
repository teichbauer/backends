# -----------------------------------------------------------------------------
# imports for running fastAPI
# -----------------------------------------------------------------------------
from fastapi import FastAPI
import uvicorn
import pdb

# -----------------------------------------------------------------------------
# imports for python-mongo lib api, database/object-models
# -----------------------------------------------------------------------------
from models import MDB_Object, PLC_Object
from dal import DB

# -----------------------------------------------------------------------------
# imports for connecting to mosquitto
# -----------------------------------------------------------------------------
from mqtt import MQTTClient

db0 = DB("META")    # META-DB
db = DB()           # use default DB-name in dal
mqtt_client = MQTTClient(db, 'FAPI-DB')

# -----------------------------------------------------------------------------
# set ups for running FastAPI server
# -----------------------------------------------------------------------------
app = FastAPI()
fapi_port = 5001

from bloc import convert_dict
@app.get("/")
async def index():
    return {'hello': "World!"}


@app.get("/hkhget/{param}")
async def get_id(param):
    queries = param[1:].split('&')
    qdic = {}
    for q in queries:
        key, value = q.split('=')
        key = 'properties.' + key
        if value.isdigit():
            value = eval(value)
        qdic[key] = value
    res = db.find('TS', qdic)[0]
    new_dic = convert_dict(res)
    return new_dic


@app.post("/plcmsg")
async def pub_plcmsg(msg: PLC_Object):
    # pdb.set_trace()
    dic = msg.dict()
    ret = mqtt_client.publish(dic, "sng/test")
    return {"result": "plc-msg published", "ret-code": str(ret)}


@app.post("/addo")
async def add_object(data: MDB_Object):
    # pdb.set_trace()
    dic = data.dict()
    ret = db.insert_one(dic)
    dic.update({'db-code': str(ret)})
    return dic


@app.get("/loadmeta")
async def load_meta_data():
    ''' read a python file containing a list of dicts
        parse all that into json array of object, and insert 
        them to META-DB.
        '''
    from data.formats import data as formats
    from data.units import data as units
    from data.relationships import data as relationships
    # pdb.set_trace()
    try:
        # put into database 'META/DS' and 'META/US'
        for pair in [
            (formats, 'CS'),
            (units, 'US'),
            (relationships, 'RS'),
        ]:
            # first drop the collection
            db0.drop_collection(pair[1])

            # insert-many into the now empty collection
            ret = db0.insert_many(pair[0], pair[1])
            return {'result': ret}
    except:
        return {'result': 'error'}

if __name__ == '__main__':
    # -----------------------
    mqtt_client.subscribe()
    mqtt_client.subscribe('sng/test')
    mqtt_client.start()
    # -----------------------

    print(f"FastAPI server running on prt {fapi_port}")
    uvicorn.run(app, host='0.0.0.0', port=fapi_port)

    # -----------------------
    mqtt_client.stop()
    # -----------------------
