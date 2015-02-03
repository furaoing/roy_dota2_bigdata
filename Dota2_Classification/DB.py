import MySQLdb
db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_dataset_dec_2014")
cursor=db.cursor()
print "Db connection Established !"

def connection_close():
    cursor.close()
    db.close()
