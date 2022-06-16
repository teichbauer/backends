##############################################################################
# purpose: read *.py file, convert, save it as *.json file

# --How to use---------------------------------------------------------------
# example python file: naming.py
#       python convert.py naming.py
# there will be a new file created: naming.json
# if you give the json-file name:
#       python naming.py myjson.json
# this will save the json file into myjson.json
##############################################################################
import sys
import json, pdb


def get_lst(filename):
    data = open(filename, 'r', encoding='UTF-8').read()
    lst = eval(data)
    # pdb.set_trace()
    return lst


def convert2_json(lst, jfilename):
    with open(jfilename, 'w', encoding='UTF-8') as ofile:
        json.dump(
            lst,
            ofile,
            ensure_ascii=False,  # without this, unicoded chars -> \x23\xd34..
            indent=4,
            sort_keys=True
        )


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python convert.py <*.py file-name> <*.json file name>")
    else:
        python_filename = sys.argv[1]

        if len(sys.argv) == 3:
            json_filename = sys.argv[2]
        else:
            json_filename = python_filename.split('.')[0] + '.json'

        lst = get_lst(python_filename)
        convert2_json(lst, json_filename)

    print('Done')