import MySQLdb
import Fetch_From_LocalDB
import Check_Comb_in_LocalDB
import Insert_New_Comb
import Update_Comb
import time

def process_data(sn):
    
    result=Fetch_From_LocalDB.fetch(sn)

    if result==None:
        return "None"

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

    Comb_sn=Check_Comb_in_LocalDB.check(dire_comb,radiant_comb,radiant_win)

    if Comb_sn==False:
        Insert_New_Comb.insert(dire_comb, radiant_comb, radiant_win, duration)
        #print "insert"
    else:
        Update_Comb.update(Comb_sn,dire_comb, radiant_comb, radiant_win, duration)
        #print "update"



for i in range(1,678533):
    try:
        process_data(i)
        #print 'OK'
        #time.sleep(0.1)
    except:
        time.sleep(10)
        process_data(i)

print 'Analysis Done'


