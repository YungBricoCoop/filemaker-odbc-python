import config
import pypyodbc

def connect_to_odbc():
    con_str = f'DSN={config.DSN};Database={config.DATABASE};UID={config.UID};PWD={config.PWD};'
    try:
        db = pypyodbc.connect(con_str)
        print("Connection to ODBC successful.")
    except pypyodbc.Error as e:
        db = None
        print("Connection to ODBC failed. \n" + str(e))
    return db

if __name__ == '__main__':
    db = connect_to_odbc()
    # get cursor¨
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT * FROM t_invoices")
    # get results
    results = cursor.fetchall()
    # print results
    print(results)
    # close connection
    db.close()