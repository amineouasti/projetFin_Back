from api import db
from sqlalchemy.orm import relationship
class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    email = db.Column("email",db.String(30))
    password = db.Column("password",db.String(30))
    children = relationship("classification")
    def __init__(self,email,password):
        self.email = email
        self.password = password