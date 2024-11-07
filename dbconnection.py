import cx_oracle as db
import os

def readpath():
    filepath = open(file=rf"{os.path.dirname(os.path.realpath(__name__))}\oracledb.txt", encoding='utf-8', mode='r')
    pwdfile = filepath.read()
    return pwdfile


def via_db():
    db.init_oracle_client(lib_dir='None')
    connection = db.connect(
        user='VIASOFT',
        password=readpath(),
        dsn="rac-scan/prod.cotriba",
        port=1521)
    return connection