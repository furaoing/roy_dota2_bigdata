import MySQLdb
from DB_stat import db
from DB_stat import cursor

def insert(dire_comb, radiant_comb, radiant_win, duration):
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO ap_dec_2014 (dire_comb,radiant_comb,sample_size,radiant_win,sample_game_time_sum) VALUES ("+str(dire_comb)+","+str(radiant_comb)+",1,"+str(radiant_win)+","+str(duration)+")"

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
       print 'Exception Occured While Trying To Insert New Record'

