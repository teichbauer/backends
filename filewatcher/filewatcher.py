# -----------------------------------------------------------------------------
# pip install file_read_backwards
# ----------------------------------
''' test.txt
000
111
222
'''
import time
import os
from file_read_backwards import FileReadBackwards
from hashlib import md5
import pdb
filename = 'test.txt'

record = {
    'sig': ' ',
    'ts': 0
}


def find_newlines(filename):
    newlines = []
    new_sig = None

    rfile = FileReadBackwards("./test.txt", encoding='utf-8')
    for line in rfile:
        sig = md5(line.encode()).digest().hex()
        if sig != record['sig']:
            newlines.append(line)
            if not new_sig:
                new_sig = sig
        else:
            break
    record['sig'] = new_sig

    return newlines


def test_time(filename):
    time_stamp = os.stat(filename).st_mtime
    if time_stamp > record['ts']:
        return time_stamp
    else:
        return None


if __name__ == '__main__':
    while True:
        time.sleep(2)
        # pdb.set_trace()
        new_timestamp = test_time(filename)
        if new_timestamp:
            record['ts'] = new_timestamp
            new_lines = find_newlines(filename)
            print(f' new lines:')
            for line in new_lines:
                print(f'\t{line}')
        else:
            print("Nothing new")
