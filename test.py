host = "localhost"
user = "root"
passwd = "cemcem99"

import mysql.connector as mysql

db = mysql.connect(
    host = host,
    user = user,
    passwd = passwd
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE mydb") #create db


db.database = "mydb"
cursor.execute('''
    create table user_data(
    ID INT NOT NULL AUTO_INCREMENT,
    nama_merk VARCHAR(100) NOT NULL,
    kota_asal TEXT NOT NULL,
    jenis_bisnis TEXT NOT NULL,
    PRIMARY KEY (ID)
    );
''')
db.commit() #commit the variables of table

# #INSERT table contents
cursor.execute("INSERT INTO user_data (nama_merk,kota_asal,jenis_bisnis) VALUES ('Nike','Beavertown','Sports Apparel')")

# #ALTER table contents
cursor.execute("ALTER TABLE user_data RENAME brand_list;")

# #UPDATE table contents
cursor.execute("UPDATE brand_list SET nama_merk ='Adidas', kota_asal = 'Herzogenaurach' WHERE ID = '2' ")
cursor.execute("UPDATE brand_list SET nama_merk ='', kota_asal = '', jenis_bisnis = '', WHERE ID = '' ")

# #DELETE table contents
cursor.execute("DELETE FROM brand_list WHERE ID > '3'")
db.commit()
# #show data after INSERT/DELETE/DROP/ALTER/UPDATE neccesary changes

cursor.execute("SELECT * FROM brand_list")


#cursor.execute("SHOW TABLES")
data = cursor.fetchall()
for row in data:
    print(row)
