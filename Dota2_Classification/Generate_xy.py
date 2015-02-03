import Fetch_From_LocalDB
from DB import connection_close

def generate_xy():
    
    def process_data(sn,x,y):

        local_x=list()
        
        result=Fetch_From_LocalDB.fetch(sn)

        if result==None:
            return "None"

        for i in range(4,9):
            local_x.append(result[i])

        for i in range(9,14):
            local_x.append(result[i])

        local_x.append(result[15]) #push the value of game duration (feature) into the x list

        x.append(local_x)   #push local_x list (one individual sample) into the x list (sample array/dataset)

        #print x

        y.append(result[14]) #push the value of radiant_win (label) into the y list (sample label array)

        #print y
        
    x=list()

    y=list()

    for i in range(1,500):
        try:
            process_data(i,x,y)
        except:
            time.sleep(10)
            process_data(i,x,y)
            
    connection_close()

    return [x,y]
