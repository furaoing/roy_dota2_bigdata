import MySQLdb
import Fetch_From_LocalDB
import Check_Comb_in_LocalDB
import Insert_New_Comb
import Update_Comb
from DB_dataset import dataset_connection_close
from DB_stat import stat_connection_close
import time
from timer import timer
		
t_db=timer()

t_all=timer()

def process_data(sn):

    t_db.timer_f(0)
    result=Fetch_From_LocalDB.fetch(sn)
    t_db.timer_f(1)

    if result==None:
        return

    dire_list=list()

    radiant_list=list()

    for i in range(4,9):
        dire_list.append(result[i])

    for i in range(9,14):
        radiant_list.append(result[i])

    dire_list.sort()

    radiant_list.sort()

    dire_comb=0

    radiant_comb=0

    for i in range(5):
        dire_comb+=dire_list[i]*(10**(3*i))

    for i in range(5):
        radiant_comb+=radiant_list[i]*(10**(3*i))

    radiant_win=result[14]

    duration=result[15]

    t_db.timer_f(0)
    Comb_sn=Check_Comb_in_LocalDB.check(dire_comb,radiant_comb,radiant_win,duration)
    t_db.timer_f(1)
    
    if Comb_sn==False:
        t_db.timer_f(0)
        Insert_New_Comb.insert(dire_comb, radiant_comb, radiant_win, duration)
        #print "insert"
        t_db.timer_f(1)
    else:
        t_db.timer_f(0)
        Update_Comb.update(Comb_sn,dire_comb, radiant_comb, radiant_win, duration)
        print "update"
        t_db.timer_f(1)

t_all.timer_f(0)
for i in range(1,100000):
    try:
        process_data(i)
        #print 'OK'
        #time.sleep(0.1)
    except:
        time.sleep(10)
        process_data(i)
t_all.timer_f(1)

dataset_connection_close()
stat_connection_close()

print 'Analysis Done'

t_db.print_time()

t_all.print_time()


