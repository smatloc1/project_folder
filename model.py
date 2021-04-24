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


#############################   Create sample_data for tests.py  #########################################

#    """Create some sample data."""

    # In case this is run more than once, empty out existing data
#    Cause.query.delete()
#    Org.query.delete()

   # Add sample causes and organizations
#    animal_rescue= Cause(dept_code='fin', dept='Finance', phone='555-1000')
#    women_crisis= Cause(dept_code='legal', dept='Legal', phone='555-2222')
#    senior_svcs= Cause(dept_code='mktg', dept='Marketing', phone='555-9999')

#    leonard = Employee(name='Leonard', dept=dl)
#    liz = Employee(name='Liz', dept=dl)
#    maggie = Employee(name='Maggie', dept=dm)
#    nadine = Employee(name='Nadine')

#    db.session.add_all([df, dl, dm, leonard, liz, maggie, nadine])
#    db.session.commit()







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
    

