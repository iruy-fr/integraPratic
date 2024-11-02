import oracledb as db

def readpath():
    filepath = open(file=r"\\172.16.0.70\c$\bd\oracledb.txt", encoding='utf-8', mode='r')
    pwdfile = filepath.read()
    return pwdfile


def via_db():
    connection = db.connect(
        user='VIASOFT',
        password=readpath(),
        dsn="rac-scan/prod.cotriba",
        port=1521)
    return connection