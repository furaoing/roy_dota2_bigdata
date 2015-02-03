import MySQLdb
from DB_stat import db
from DB_stat import cursor

def check(dire_comb,radiant_comb,radiant_win,duration):
    
    sql="SELECT * FROM ap_dec_2014 WHERE dire_comb="+str(dire_comb)


    # Execute the SQL command
    cursor.execute(sql)
    count=cursor.rowcount
    data=cursor.fetchall()
    # Commit your changes in the database
    db.commit()

    try:
        if count>0:
            for row in data:
                if row[2]==radiant_comb:
                    return True
                else:
                    pass
            return False

        else:
            return False
        
    except:
        print "Excepting Occured whiling checking comb"
        
