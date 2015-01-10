import MySQLdb

def check(dire_comb,radiant_comb,radiant_win,duration):
    db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_statistics_2014")
    cursor=db.cursor()
    
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
                    sql_update="UPDATE ap_dec_2014 SET sample_size=sample_size+1, radiant_win=radiant_win+"+str(radiant_win)+", sample_game_time_sum=sample_game_time_sum+"+str(duration)+" WHERE sn="+str(row[0])+""
                    
                    try:
                        # Execute the SQL command
                        cursor.execute(sql_update)
                        # Commit your changes in the database
                        db.commit()
                        cursor.close()
                        db.close()
                        print "Update"
                        return None
                        
                    except:
                        # Rollback in case there is any error
                        db.rollback()
                        cursor.close()
                        db.close()
                        print "Excepting Occured whiling trying to update stat"
                        return None

        else:
            cursor.close()
            db.close()
            return False
        
    except:
        cursor.close()
        db.close()
        print "Excepting Occured whiling checking comb"
        
