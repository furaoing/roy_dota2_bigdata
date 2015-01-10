import MySQLdb

def check(dire_comb,radiant_comb,radiant_win):
    db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_statistics_2014")
    cursor=db.cursor()
    
    sql="SELECT * FROM ap_dec_2014 WHERE dire_comb="+str(dire_comb)

    try:
       # Execute the SQL command
       cursor.execute(sql)
       count=cursor.rowcount
       data=cursor.fetchall()
       # Commit your changes in the database
       db.commit()
       cursor.close()
       db.close()

       if count>0:
            for row in data:
                if row[2]==radiant_comb:
                    return row[0]
       else:
           return False

    except:
       # Rollback in case there is any error
       db.rollback()
       cursor.close()
       db.close()
       print "Excepting Occured whiling trying to query database"



