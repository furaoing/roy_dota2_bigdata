import MySQLdb

def insert(dire_comb, radiant_comb, radiant_win, duration):
    db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_statistics_2014")
    cursor=db.cursor()
    
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO ap_dec_2014 (dire_comb,radiant_comb,sample_size,radiant_win,sample_game_time_sum) VALUES ("+str(dire_comb)+","+str(radiant_comb)+",1,"+str(radiant_win)+","+str(duration)+")"

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
       cursor.close()
       db.close()
    except:
       # Rollback in case there is any error
       db.rollback()
       cursor.close()
       db.close()
       print 'Exception Occured While Trying To Insert New Record'

