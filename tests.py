####################################################################################################################

from unittest import TestCase
from model import Cause, Org, connect_to_db, db
from server import app
import server

#############################   Create sample_data for tests.py  #########################################

# Create a function called sample data


def sample_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Cause.query.delete()
    Org.query.delete()

    # Add sample Organizations
    womens_services= Cause(cause_name='Womens Services')
    swap = Org(org_name='Sistas with a purpose', cause=womens_services, mission='To support women escaping domestic abuse and homelessness and provide them with marketable skills')
    
    db.session.add_all([womens_services, swap])
    db.session.commit()

##################    Integration Test #1 - create a new org    ######################

class FlaskTestsNeworg(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///sample_data")

        db.create_all()
        sample_data()   

    def test_create_new_org(self):
        """Can we create a new organization and save it to the database?"""

        result = self.client.post('/createorg',
                                  data={'org_name':'DIVAS', 
                                  'cause_id': 5,
                                  'mission':'To educate, encourage, and empower women to be their best',
                                  'web_url':"",
                                  'tagline': 'All women succeeding'},
                                  follow_redirects=True)
        self.assertIn(b"Mighty Missions Registration", result.data)

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

############################  Unit Test #2 - return a profile page  #########################


class FlaskTestsProfile(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///sample_data")

        db.create_all()
        sample_data()

    def test_profilepage(self):
        """Can we retrieve the details of an organization?"""

        result = self.client.get('/profiles/DIVAS')
        self.assertIn(b"Mighty Missions Profile", result.data)

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()
    


####################  Unit Test #3 - search by cause  ##################

class FlaskTestsSearchbyname(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        
        connect_to_db(app, "postgresql:///sample_data")

        db.create_all()
        sample_data()

    

    def test_search_by_cause(self):
        """Can we search by cause and find a list of organization in the database?"""

        result = self.client.get('/cause',
                                data={'cause_name': 'Womens Services'},
                                follow_redirects=False)
        self.assertIn(b'Mighty Mission Organizations Related by Cause', result.data)
 
    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()
 


if __name__ == "__main__":
    import unittest
    connect_to_db(app, db_name='postgresql:///sample_data', echo=False)

    unittest.main()

