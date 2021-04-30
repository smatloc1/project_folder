####################################################################################################################

from unittest import TestCase
from model import Cause, Org, connect_to_db, db, sample_data
from server import app
import server



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
                                  'tagline': 'All women succeeding',
                                  'image':""} 
                                  follow_redirects=False)
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

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_search_by_cause(self):
        """Can we search by cause and find a list of organization in the database?"""

        result = self.client.get('/searchbycause',
                                data='cause_id',
                                follow_redirects=False)
        self.assertIn(b', result.data)
 
 


if __name__ == "__main__":
    import unittest

    unittest.main()

