import MySQLdb

def fetch(sn):
    db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_dataset_dec_2014")
    cursor=db.cursor()
    
    sql="SELECT * FROM ap_1_dec_2014 WHERE sn="+str(sn)

    try:
       # Execute the SQL command
       cursor.execute(sql)
       data=cursor.fetchone()
       # Commit your changes in the database
       db.commit()
       cursor.close()
       db.close()
    except:
       # Rollback in case there is any error
       db.rollback()
       cursor.close()
       db.close()
       print 'Exception Occured While Trying To Fetch From LocalDB'

    return data
