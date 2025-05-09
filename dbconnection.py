import oracledb as db
import os, sys


def readpath():
    filepath = open(file=f"{os.path.dirname(os.path.realpath(__name__))}/oracledb.txt", encoding='utf-8', mode='r')
    pwdfile = filepath.read()
    return pwdfile


def via_db():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    instantclient_path = os.path.join(base_path, "instantclient_23_6")
    db.init_oracle_client(lib_dir=instantclient_path)
    connection = db.connect(
        user='VIASOFT',
        password=readpath(),
        dsn="rac-scan/prod.cotriba",
        port=1521)
    return connection