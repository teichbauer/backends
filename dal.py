from warnings import catch_warnings
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

    def insert1(self, dic, cname):
        try:
            if '_id' not in dic:
                ID = generate_id(self.db_name, cname)
            else:
                ID = dic['_id']

            # mongoDB _id contains onlt 24 bytes. 
            # APPDB-TS-1653531424212-KnfeDV has 26: 
            # _id should cut-off db-name: TS-1653531424212-KnfeDV (23 long)
            # -----------------------------------------------------
            if ID.startswith(self.db_name):
                dic['_id'] = ID[6:]
            # ret = self.db[cname].insert_one(dic)
            ret = self.db[cname].insert_one(dic)
            return bool(ret.acknowledged)
        except Exception as e:
            print(str(e))
            return False

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

    def find(self, cname, q):
        results = []
        coll = self.db[cname] 
        lst = list(coll.find(q))
        for e in lst:
            results.append(e)
            # print(e)
        return results

    def delete1(self, cname, the_id):
        self.db[cname].delete_many({'_id': the_id})
