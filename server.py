"""Server for mighty missions app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "2455lb"
app.jinja_env.undefined = StrictUndefined



################       Main Homepage        ####################

@app.route('/')
def homepage():
    """Welcome Page."""

    return render_template('homepage.html')



#################  Login to the Homepage  #################

@app.route('/login', methods=['POST'])
def login_org():
    """ Organization enters org_name and a search is completed """
      
    org_name = request.form.get('org_name')
    org = crud.get_org_by_name(org_name)
    
    
    if not org:
         
        flash('This organization does not exist in our database.')
        return redirect('/register.html')
    
    else:
        return redirect(f'/profiles/{org_name}')
 


###########   Retrieve data from register  ###################

@app.route('/formdata', methods=['POST'])
def new_org_formdata():
    """ Create a new org. """

    org_name = request.form.get('org_name')
    mission = request.form.get('mission')
    cause_id = request.form.get('cause_id')

    org = crud.get_org_by_name(org_name)
    if org:
         
        flash('Congratulations!  You have now been added to the Mighty Missions database.')
        return redirect('/homepage')



##############   Returns a profile page   #################

@app.route('/profiles/<org_name>')
def show_org(org_name):
    """ Show details on a particular organization."""

    org = crud.get_org_by_name(org_name)

    return render_template('profiles.html', org=org)



##############  Main Search Page ##########################

@app.route('/search', methods=['GET'])
def search():

    """ Render the Search page """

    return render_template('search.html')



##############   Returns a list of orgs page   #################

@app.route('/list')
def all_orgs():
    """ Search all organizations by name """

    orgs = crud.get_orgs()       

    return render_template('listoforgs.html', orgs=orgs)



##############   Search by Cause ##########################

@app.route('/searchbycause/<cause_obj>', methods=['GET'])
def same_orgs_by_cause():
    """ Search for organizations by cause """

    cause_obj = request.form.get('cause_obj')
    orgs = crud.get_orgs_by_cause(cause_obj)

    return render_template('searchbycause.html', orgs=orgs)



##############   Search by Name ##########################

@app.route('/searchbyname', methods=['POST'])
def org_by_name():
    """ Search for an organization by name """

    org_name = request.form.get('org_name')
    org = crud.get_org_by_name(org_name)

    return redirect(f'/profiles/{org_name}')



if __name__ == '__main__':
    connect_to_db(app)
    print("this is the server running")
    app.run(host='0.0.0.0', debug=True)
