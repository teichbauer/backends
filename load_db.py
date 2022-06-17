# ---------------------------------------------------------------------
# Purpose: 
#   load the dict data in every *.py file into mongodb 
#   overwriting old content in the collections
# ------------ How to use:
#  1. cd to the location under "backends"
#  2. python3 load_db.py
# ---------------------------------------------------------------------

from glob import glob
from dal import DB

_allowed_collection_names = ('ES', 'CS', 'TS', 'DS')

def get_dics(dirname):
    cns = []
    dics = {}
    lst = glob(f'./{dirname}/*')
    for dr in lst:
        cn = dr.split('/')[-1]
        if cn in _allowed_collection_names:
            cns.append(cn)
            filenames = glob(dr + '/*')
            # db.drop_collection(cn)
            for file_name in filenames:
                fn = file_name.split('/')[-1]
                # fn must start with capital-letter, ends with .py
                if fn.endswith('py') and fn[0].isupper():
                    data = eval(open(file_name).read())
                    dics[(cn, file_name)] = data
    return dics, cns


def insert_db(db, collection_names, dics):
    # clear all collections to be empty
    for collection_name in collection_names:
        db.drop_collection(collection_name)

    # pumping in
    for (cn, fn), dic_lst in dics.items():
        for dic in dic_lst:
            inserted = db.insert1(dic, cn)
            if not inserted:
                ID = dic.get('_id','000')
                print(f'cry: {fn}-{ID}')


if __name__ == '__main__':
    db = DB()
    lst_dic, cns = get_dics('concrete_model_HKH')
    insert_db(db, cns, lst_dic)
    print('Done')
