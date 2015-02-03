import MySQLdb
from DB_stat import db
from DB_stat import cursor

def update(Comb_sn,dire_comb, radiant_comb, radiant_win, duration):
    if Comb_sn==None:
        print "Update Comb None"
    
    sql="UPDATE ap_dec_2014 SET sample_size=sample_size+1, radiant_win=radiant_win+"+str(radiant_win)+", sample_game_time_sum=sample_game_time_sum+"+str(duration)+" WHERE sn="+str(Comb_sn)+""

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    
    except:
       # Rollback in case there is any error
       db.rollback()
       print 'update fail'
       #print sql

