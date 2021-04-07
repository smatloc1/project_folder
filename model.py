##########################   SETUP FLASK  #################################

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##########################   SETUP DATABASE  #################################

class Org(db.Model):
    """ Organization Profile """

        __tablename__ = "orgs"

        org_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        org_name = db.Column(db.String(50), nullable=False, unique=True)
        #org_type = db.Column(db.String(2), default='NP')
        org_vision = db.Column(db.String(100))
        org_mission = db.Column(db.String(100))
        #mission_cat = db.Column(db.String(3), Foreign_key=True) 
        #ntsee_code = db.Column(db.String(3)), nullable=True)
        #project_type = db.Column(db.String(50))
        contact = db.Column(db.String(50))
        exec_sum = db.Column(db.String(50))
        #region = db.Column(db.Integer,nullable=False)
        address = db.Column(db.String(50),nullable=False )     
        city = db.Column(db.String(20), nullable=False)
        state = db.Column(db.String(2), nullable=False)
        

    def __repr__(self):
        return

class Mission(db.Model):
    """ Organization Missions """

        __tablename__ = "missions"

        mission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        mission_cat = db.Column(db.String(50), nullable=False, Foreign_key=True)
        ntsee_code = db.Column(db.String(3))
    
  db.create_all()

##########################   SETUP SQLALCHEMY   ###############################


def connect_to_db(app, orgs):   
    """ Connect to database """

    app config['SQLALCHEMY_DATABASE_URI'] = 'posgresql:///orgs
    app config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

connect_to_db(app, orgs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')