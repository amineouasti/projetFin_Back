from api import db
from sqlalchemy.orm import relationship
class classification(db.Model):
    id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column("name",db.String(30))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __init__(self,name,id_user):
        
        self.name = name
        self.id_user = id_user