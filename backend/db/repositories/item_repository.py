import mysql.connector
from core.configs_core import DATABASE_PASSWORD


db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd= DATABASE_PASSWORD,
    database = 'wow_auction_house_analyzer_database'
)

mycursor = db.cursor()

def save_item(data):

    mycursor.execute(
        "INSERT INTO all_items_id (id) VALUES (%s)", (data,)
    )
    
    db.commit()
    return
