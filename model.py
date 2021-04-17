""" Models for Organizational Profiles """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#class Cat(db.Model):
#   """ Organization category """

#  __tablename__ = "categories"

#   cat_id = db.Column(db.Integer, primary_key=True)
#   cat_name = db.Column(db.String(50), nullable=False)

    # orgs = a list of Org objects

#    def __repr__(self):
#         return f'<Cat cat_id = {self.cat_id}, cat_name = {self.cat_name}>'
  

class Cause(db.Model):
    """ Organization causes """

    __tablename__ = "causes"

    cause_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cause_name = db.Column(db.String(50), nullable=False)
    #cat_id = db.Column(db.Integer, db.ForeignKey('categories.cat_id'))
 
    # orgs = a list of Org objects

    def __repr__(self):
        return f'<Cause cause_id={self.cause_id}, cause_name={self.cause_name}>'
 
 
  
class Org(db.Model):
    """ Nonprofit Organization Profile """

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_name = db.Column(db.String(50), nullable=False, unique=True)
    mission = db.Column(db.String(200))
    cause_id = db.Column(db.Integer, db.ForeignKey('causes.cause_id'))
    #cat_id = db.Column(db.Integer, db.ForeignKey('categories.cat_id'))
    #web_url = db.Column(db.String(100)) - SPRINT 2
    #tagline = db.Column(db.String(100)) - SPRINT 2
    

    cause = db.relationship('Cause', backref='orgs')
    #cat = db.relationship('Cat', backref='orgs')



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
    

