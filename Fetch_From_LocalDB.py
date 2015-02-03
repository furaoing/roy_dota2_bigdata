import MySQLdb
from DB_dataset import db
from DB_dataset import cursor

def fetch(sn):
    sql="SELECT * FROM ap_1_dec_2014 WHERE sn="+str(sn)

    try:
       # Execute the SQL command
       cursor.execute(sql)
       data=cursor.fetchone()
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
       print 'Exception Occured While Trying To Fetch From LocalDB'

    return data
