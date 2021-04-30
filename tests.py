####################################################################################################################

from unittest import TestCase
from model import Cause, Org, connect_to_db, db, sample_data
from server import app
import server


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///sample_data")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

############################  Unit Test #1 - Homepage  #########################

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"Welcome to Mighty Missions Network!", result.data)



##################    Integration Test #2 - Create a new org    #######################

    def test_create_new_org(self):
        """Create a new organization"""

        result = self.client.post('/createorg',
                                  data="org_name",
                                  follow_redirects=True)
        self.assertIn(b"Type in your organization name", result.data)



####################  Integration Test #3 - Registration Form Page  ##################

    def test_registration_form(self):
        """Can we reach the registration page?"""

        result = self.client.get('/registrationform')
        self.assertIn(b'Mighty Missions Registration', result.data)










if __name__ == '__main__':
    unittest.main()
    