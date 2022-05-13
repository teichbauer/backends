from pydantic import BaseModel
Database_Name = 'APPDB'

# ------ collection_name:ES -----------------------------------
# physical entities put into a collection named ES
# -------------------------------------------------------------

# ------ collection_name:DS -----------------------------------
# document entities put into a collection named DS
# -------------------------------------------------------------

# ------ collection_name:CS -----------------------------------
# concepts/configuration entities put into a collection named CS
# -------------------------------------------------------------

# ------ collection_name:PS -----------------------------------
# persons/organizations put into a collection named PS
# -------------------------------------------------------------

# ------ collection_name:TS -----------------------------------
# time series (data) put into a collection named TS
# -------------------------------------------------------------

# ------ collection_name:US -----------------------------------
# only in META-DB
# unit definitions put into a collection named US
# -------------------------------------------------------------

# ------ collection_name:RS -----------------------------------
# only in META-DB
# definitions of relationship
# -------------------------------------------------------------


class MDB_Object(BaseModel):
    database_name: str = Database_Name
    collection_name: str = 'XX'
    category_name: str
    nick_name: str
    properties: dict
    relationships: dict

#################################################


class PLC_Object(BaseModel):
    plc_name = "Robot1"
    plc_ipaddr = "12.13.14.15"
    plc_topic = "abc"
    workpiece_id = "33087"
    work_post_id = "9"
