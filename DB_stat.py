import MySQLdb
db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_statistics_2014")
cursor=db.cursor()
print "Db_stat connection Established !"

def stat_connection_close():
    cursor.close()
    db.close()
