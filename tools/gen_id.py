from datetime import datetime   # for getting utc time
import sys
import string
import random

DB_name = 'APPDB'


def _MD_gen_randomstr(length=6) -> str:
    letters = string.ascii_letters  # lower/upper letters
    m = ''.join(random.choice(letters) for i in range(length))
    return m


def _MD_msec_now_str() -> str:
    """ 13 digits number-str: epoch time (UTC) in miliseconds """
    utc_ts_in_milisecs = round(datetime.now().timestamp() * 1000)
    return str(utc_ts_in_milisecs)


def generate_id(db_name, coll_name) -> str:
    return f"{db_name}-{coll_name}-{_MD_msec_now_str()}-{_MD_gen_randomstr()}"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"python gen_id.py <collection-name>")
    else:
        the_id = generate_id(DB_name, sys.argv[1])
        print(the_id)
