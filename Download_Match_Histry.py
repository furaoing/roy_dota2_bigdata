import pycurl
import json
from StringIO import StringIO
import time
import MySQLdb

def curl(url):
    header=['Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding:gzip, deflate, sdch',
           'Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2,zh-TW;q=0.2',
           'Cache-Control:no-cache',
            'Connection:keep-alive',
            'Host:api.steampowered.com',
            'Pragma:no-cache',
            'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36']
    curl_start=time.time()
    buffer=StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.ENCODING, 'gzip')
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HTTPHEADER, header)
    c.setopt(c.CONNECTTIMEOUT, 2)           #set connection time limit to 2 second
    c.setopt(c.TIMEOUT,30)             #set transfering time limmit to 30 second, unfinished data transfering process will be aborted
    try:
        c.perform()
        c.close()
        curl_end=time.time()
        print 'Curl Time:'+str(curl_end-curl_start)
        return buffer.getvalue()
    except:
        return False

def update_db(match_id, match_seq_num, start_time, radiant_win, duration, lobby_type, cluster, game_mode, hero_ps):
    db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_dataset_dec_2014")
    cursor=db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO ap_1_dec_2014 (match_id,match_seq_num,start_time,hero_ps_1,hero_ps_2,hero_ps_3,hero_ps_4,hero_ps_5,hero_ps_6,hero_ps_7,hero_ps_8,hero_ps_9,hero_ps_10,radiant_win,duration,cluster,lobby_type,game_mode) VALUES ("\
          +str(match_id)+","+str(match_seq_num)+","+str(start_time)+","+str(hero_ps[0])+","+str(hero_ps[1])+","+str(hero_ps[2])+","+str(hero_ps[3])+","+str(hero_ps[4])+","+str(hero_ps[5])+","+str(hero_ps[6])+","+str(hero_ps[7])\
          +","+str(hero_ps[8])+","+str(hero_ps[9])+","+str(radiant_win)+","+str(duration)+","+str(cluster)+","+str(lobby_type)+","+str(game_mode)+")"

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # disconnect from server
    db.close()
    
#NEED ATTENTATION
def Match_Filter(human_players, game_mode, duration, lobby_type):
    if ((human_players==10) and (game_mode==1 or game_mode==22) and (lobby_type==0 or lobby_type==7) and (duration>1200 and duration<6000))==True:
        return True
    else:
        return False
#N

Init_match_seq_number=raw_input('Enter the init match_seq_number:')

start_time=time.time()

url='https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v001/?key=0128CDFDD3D826BEA17B01BCDDB73DA0&start_at_match_seq_num='+str(Init_match_seq_number)

most_recent_match_time=0

while most_recent_match_time<1417450537:
    content=curl(url)

    time.sleep(1)

    if content!=False:

        exec_time_start=time.time()

        S=json.loads(content)

        if S["result"]["status"]==1:

            for i in range(len(S["result"]["matches"])):

                human_players=S["result"]["matches"][i]["human_players"]

                game_mode=S["result"]["matches"][i]["game_mode"]

                duration=S["result"]["matches"][i]["duration"]

                lobby_type=S["result"]["matches"][i]["lobby_type"]

                #first_blood_time=S["result"]["matches"][i]["first_blood_time"]

                if Match_Filter(human_players, game_mode, duration, lobby_type)==True:

                    match_id=S["result"]["matches"][i]["match_id"]

                    match_seq_num=S["result"]["matches"][i]["match_seq_num"]

                    start_time=S["result"]["matches"][i]["start_time"]

                    cluster=S["result"]["matches"][i]["cluster"]

                    if S["result"]["matches"][i]["radiant_win"]==True:
                        radiant_win=1
                    else:
                        radiant_win=0

                    hero_ps=list()

                    for k in range(10):
                        
                        hero_ps.append(S["result"]["matches"][i]["players"][k]["hero_id"])

                    update_db(match_id, match_seq_num, start_time, radiant_win, duration, lobby_type, cluster, game_mode, hero_ps)
            
            start_at_match_seq_num=S["result"]["matches"][i]["match_seq_num"]+1

            most_recent_match_time=start_time 
            
            print 'OK:'+str(i)
            
            url='https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v001/?key=0128CDFDD3D826BEA17B01BCDDB73DA0&start_at_match_seq_num='+str(start_at_match_seq_num)
        else:
            print 'JSON Result Status Failure'


        exec_time_end=time.time()

        print 'Exec Time:'+str(exec_time_end-exec_time_start)
        
    else:
        
        print 'Connection Failure'

        time.sleep(1)


print 'Task Done'

        



