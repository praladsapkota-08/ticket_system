import sqlite3
import datetime
import pandas as pd


def create_table():
        conn = sqlite3.connect('parking_system.db')
        c = conn.cursor()
        c.execute("""
                CREATE TABLE IF NOT EXISTS ticket_system 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                phone TEXT,
                vehicle_number TEXT,
                entry_time TEXT,
                exit_time TEXT,
                total_price INTEGER,
                vehicle TEXT
                );
        """)

        conn.commit()
        conn.close()



def checking_table():
        conn = sqlite3.connect('parking_system.db')
        c = conn.cursor()

        c.execute(f"""
    SELECT * FROM sqlite_master WHERE type='table' AND name='ticket_system';
    """)
        result = c.fetchone()
        if result:
                return True

        else:
                return False


def inserting_value(username, phone , vehicle_number , entry_time , vehicle):
        conn = sqlite3.connect('parking_system.db')
        c = conn.cursor()
        c.execute('''INSERT INTO ticket_system 
        (username,
        phone ,
        vehicle_number ,
        entry_time ,
        vehicle) 
        VALUES (?,?,?,?,?)''' ,(username, phone , vehicle_number, entry_time, vehicle))
        
        conn.commit()
        conn.close()

def create_slip():
        conn = sqlite3.connect('parking_system.db')
        c = conn.cursor()

        c.execute("SELECT id, username, vehicle_number ,entry_time FROM ticket_system ORDER BY id DESC LIMIT 1")
        user_id,username,vehicle_number,entry_time = c.fetchone()
        conn.commit()
        conn.close()

        data = {
                "id" : user_id,
                "username" : username,
                "vehicle_number" : vehicle_number,
                "entry_time" : entry_time
        }

        df = pd.DataFrame(data , index = [0])
        df.to_csv(f'E:\\data_science\\ticket_system\\data\\{username}_{user_id}.csv' , index = False)


#create_table()
#inserting_value('john', '123', 'ds1','null','1')
#checking_table()
#create_slip()

