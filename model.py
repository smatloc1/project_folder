""" Models for Organizational Profiles """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Mission(db.Model):
    """ Organization Missions """

    __tablename__ = "missions"

    mission_id = db.Column(db.Integer)
    mission_cat = db.Column(db.String(50), nullable=False, primary_key=True)
    ntsee_code = db.Column(db.String(3))
    
    def __repr__(self):
        return f'<Mission mission_id = {self.mission_id}, mission_cat = {self.mission_cat}>'
  


class Cause(db.Model):
    """ Organization cause """

    __tablename__ = "causes"

    cause_id = db.Column(db.Integer, autoincrement=True)
    cause_name = db.Column(db.String(50), nullable=False, primary_key=True)
    
    def __repr__(self):
        return f'<Cause cause_id = {self.cause_id}, cause_name = {self.cause_name}>'
 
 
  #####################################################################################################3




































  #####################################################################################################


class Org(db.Model):
    """ Nonprofit Organization Profile """

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_name = db.Column(db.String(50), nullable=False, unique=True)
    org_mission = db.Column(db.String(100))
    mission_cat = db.Column(db.String(3), db.ForeignKey('missions.mission_cat'))
    interest_id = db.Column(db.Integer, db.ForeignKey('interests.interest_id'))
    contact = db.Column(db.String(50))
    exec_sum = db.Column(db.String(50))
    region = db.Column(db.String, nullable=True)
    address = db.Column(db.String(50),nullable=False )   
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(2), nullable=False)
        

    def __repr__(self):
        return f'<Org org_id = {self.org_id}, org_name = {self.org_name}>'

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


