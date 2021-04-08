##########################   SETUP FLASK  #################################

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##########################   SETUP DATABASE  #################################

class Org(db.Model):
    """ Organization Profile """

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_name = db.Column(db.String(50), nullable=False, unique=True)
    org_type = db.Column(db.String(2), default='NP')
    org_vision = db.Column(db.String(100))
    org_mission = db.Column(db.String(100))
    mission_cat = db.Column(db.String(3), foreign_key=True) 
    ntsee_code = db.Column(db.String(3), nullable=True)
    project_type = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    exec_sum = db.Column(db.String(50))
    region = db.Column(db.String, nullable=True)
    address = db.Column(db.String(50),nullable=False )   
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(2), nullable=False)
        

    def __repr__(self):
        return f'<Org org_id = {self.org_id}, org_name = {self.org_name}>'

class Mission(db.Model):
    """ Organization Missions """

    __tablename__ = "missions"

    mission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_cat = db.Column(db.String(50), nullable=False, foreign_key=True)
    ntsee_code = db.Column(db.String(3))
    
    def __repr__(self):
        return f'<Mission mission_id = {self.mission_id}, mission_cat = {self.mission_cat}>'
  
 

##########################   SETUP SQLALCHEMY   ###############################



def connect_to_db(app, db_name='postgresql:///orgs', echo=True):
    """Connect to database """

    app.config['SQLALCHEMY_DATABASE_URI'] = db_name
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.app = app
    db.init_app(app)

    print('connected to db')

if __name__ == '__main__':
    from server import app
    

    db.create_all()