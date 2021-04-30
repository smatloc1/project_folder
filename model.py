""" Models for Organizational Profiles """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###################################  Create Cause Class   #############################################  

class Cause(db.Model):
    """ Organization causes """

    __tablename__ = "causes"

    cause_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cause_name = db.Column(db.String(50), nullable=False)
  

    def __repr__(self):
        return f'<Cause cause_id={self.cause_id}, cause_name={self.cause_name}>'
 
 
 #####################################   Create Org Class  ########################################### 


class Org(db.Model):
    """ An Organization Profile """

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_name = db.Column(db.String(50), nullable=False, unique=True)
    mission = db.Column(db.String(200))
    cause_id = db.Column(db.Integer, db.ForeignKey('causes.cause_id'))
    image = db.Column(db.String)
    web_url = db.Column(db.String) 
    tagline = db.Column(db.String)
   

    cause = db.relationship('Cause', backref='orgs')

    def __repr__(self):
        return f'<Org org_id={self.org_id}, org_name={self.org_name}, misssion={self.mission}, cause_id={self.cause_id}>'



def connect_to_db(app, db_name='postgresql:///mmdata', echo=False):
    """Connect to database """

    app.config['SQLALCHEMY_DATABASE_URI'] = db_name
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


    print('connected to db!')



if __name__ == '__main__':
    from server import app

    connect_to_db(app)
   
