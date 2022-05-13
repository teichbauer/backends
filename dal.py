from pymongo import MongoClient
from tools.gen_id import generate_id
import pdb

Database_Name = "APPDB"


class DB:
    def __init__(self, db_name=Database_Name):
        self.db_name = db_name
        self.db_client = MongoClient()
        self.db = self.db_client[db_name]

    def drop_db(self, db_name=None):
        if not db_name:
            db_name = self.db_name
        self.db.drop_database(db_name)

    def drop_collection(self, collection_name):
        self.db.drop_collection(collection_name)

    def get_names(self, dic):
        if 'database_name' in dic:
            dbname = dic.pop('database_name')
        else:
            dbname = self.db_name
        if 'collection_name' in dic:
            colname = dic.pop('collection_name')
        else:
            colname = 'XX'
        return dbname, colname

    def insert_one(self, dic):
        try:
            # pdb.set_trace()
            dname, cname = self.get_names(dic)
            if '_id' not in dic:
                the_id = generate_id(dname, cname)
                dic['_id'] = the_id
            ret = self.db[cname].insert_one(dic)
            if ret.acknowledged:
                return 'inserted'
            else:
                return 'not inserted'
        except:
            return 'failed'

    def insert_many(self, dics, cname):
        # -----------------------------------------------------
        # dics is a list of Python/dicts.
        # every dict in this list must have _id in it
        # all dicts inserted into a collection named cname
        # -----------------------------------------------------
        try:
            ret = self.db[cname].insert_many(dics)
            if ret.acknowledged:
                return 'all inserted'
            else:
                return 'not inserted'
        except:
            return 'failed'
