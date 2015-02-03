import MySQLdb
db = MySQLdb.connect("localhost","root","mysqlphotoshare","ap_dataset_dec_2014")
cursor=db.cursor()
print "Db_dataset connection Established !"

def dataset_connection_close():
    cursor.close()
    db.close()
