from sqlalchemy import Integer, String, Column
from db.database_db import Base

class Auctions(Base):
    __tablename__ = 'auctions'

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(50))
    item_icon = Column(String(100))
    auction_price = Column(Integer)




#item_name
# item_icon
# auction_price

