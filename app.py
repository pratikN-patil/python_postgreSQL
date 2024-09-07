import psycopg2
from queries import drop_table,create_table,insert_data,insert_value,update_data,fetch_data
from db_config import DATABASE_CONFIG
cursor=None
conn=None
try: 
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cursor=conn.cursor()
    
    cursor.execute(drop_table)
    
    cursor.execute(create_table)
    
    for record in insert_value:
        cursor.execute(insert_data,record)
    cursor.execute(update_data)
    cursor.execute(fetch_data)
    for record in cursor.fetchall():
        print(record)
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()