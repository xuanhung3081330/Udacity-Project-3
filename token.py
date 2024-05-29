from sqlalchemy import Column, Integer, String

class Token(Base):
    __tablename__ = 'tokens'

    user_id = Column(String, primary_key=True)
    token = Column(String) 
    created_at = Column(DateTime)
    used_at = Column(DateTime, nullable=True)