"""Server for mighty missions app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "2455lb"
app.jinja_env.undefined = StrictUndefined



###########   Returns the Homepage    #################

@app.route('/')
def homepage():
    """Welcome Page."""

    return render_template('homepage.html')




@app.route('/list_orgs')
def all_orgs():
    """ List all organizations by cause """

    orgs = crud.get_orgs()       

    return render_template('list_orgs.html', orgs=orgs)



##############   Returns a profile page   #################

@app.route('/orgs/<org_id>')
def show_org(org_name):
    """Show details on a particular organization."""

    org = crud.get_org_by_name(org_name)

    return render_template('org_profile.html', org=org)




###########   Create a new organization  ###################

@app.route('/login', methods=['POST'])
def register_new_org():
    """Create a new org."""

    org_name = request.form.get('org_name')
    mission = request.form.get('mission')
    #cause_id = request.form.get('cause_id')

    org = crud.get_org_by_name(org_name)
    if not org:
         
        flash('This organization does not exist in our database.')
        return redirect('/register')
 
    else:
        return redirect('/search')

#create a route to accept the information from register

##### this belongs to@app.route(handle registerdata)   
        #crud.create_org_with_cause_id(org_name, cause_id, mission)
        #flash('Congratulations! Your organization has been added to our database! You can now search for other organizations that have a similar mission and cause.')

   
        

    return redirect('/')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
