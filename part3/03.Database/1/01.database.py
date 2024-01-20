import sqlite3 as db



#conn = ertebat ba database # ma niaz darim safhe code ro ba db match konim pass az connect 
#be onavan rabet db va safe code estefade mikonim
conn = db.connect('my_Database.db')

#c: cursur = vaghti code ro be db vasl kardim niaz be rabeti darim ke dasturat ro be amal biare to db
c = conn.cursor()

#c.exexute = ba estefade az rabet table ro too db dorost mikonim
#CREATE TABLE : Sakhtan miz baray gozashtan etelaat, IF NOT EXSISTS :Baray inke be error nakhorim hardafe 
#az in dastur estefade mikonim .
c.execute('''CREATE TABLE IF NOT EXISTS karmand(
    
    
    fname text,
    
    lname text,
    
    salary integer
         )
          
          ''')

#baray vared karan value dar class e karmand az dastur c.excute be soorat zir estefade mikonim:

##c.execute('INSERT INTO karmand VALUES ("Mohammad" , "Hosseini" , 30000)')





# baray save kardan az conn.commit() estefade mikonim
##conn.commit()

# mikhahim az table (karmand) select konim moredi ro .
# tarjome : entekhab kon (*= hamechi) hamechi ro (where = ke) obj = in "esm"
c.execute('SELECT * FROM karmand WHERE lname = "Hosseini"')

# alan moredi ke select kardim ra mikhahim namayesh dahim ke az :fitch... :estefade mikonim 
# va dar print qarar midim .
#fetchall = namayesh hame : khoruji = list
# ,  fetchmany= namayesh moredi ama chandtayi 
# ,  fetchone= namayesh yeki : khoruji = tuple
print(c.fetchone())


#va db ra mibandim ba dastur conn.close()
conn.close()