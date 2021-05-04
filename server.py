"""Server for mighty missions app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from pprint import pformat
import os
import requests
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "2455lbkjfgjhlllkfghkf"
app.jinja_env.undefined = StrictUndefined




################       Main Homepage        ####################

@app.route('/contact')
def contactpage():
    """Contact information Page"""

    return render_template('contact.html')


@app.route('/about')
def aboutpage():
    """information about Mighty Missions"""

    return render_template('about.html')




################       Main Homepage        ####################

@app.route('/')
def homepage():
    """Welcome Page and login."""

    return render_template('homepage.html')

#################  Display registration form ################################

@app.route('/registrationform')
def reg_form():
    
    causes= crud.get_all_causes()

    return render_template('register.html', causes=causes)



#################  Retrieve data from Homepage (login form)  #################

@app.route('/login', methods=['GET'])
def login_org():
    """ Organization enters org_name and a search is completed """
      
    org_name = request.args.get('org_name')
    org = crud.get_org_by_name(org_name)
    print('*'*20)
    print(org_name)
    print(org)
    
    if not org:
        flash('THIS ORGANIZATION IS NOT REGISTERED IN OUR DATABASE')
        return redirect('/registrationform')
    
    else:
        session['org_name'] = org.org_name
        session['org_id'] = org.org_id
        return redirect(f'/profiles/{org.org_id}')
 


###########   Retrieve data from register and create an org ###################

@app.route('/createorg', methods=['POST'])
def create_org_registration():
    """ Create a new org. """

    org_name = request.form.get('org_name')
    mission = request.form.get('mission')
    cause_id = request.form.get('cause_id')
    web_url = request.form.get('web_url')
    tagline = request.form.get('tagline')

    print('*'*20)
    print(org_name, mission, cause_id)
    org = crud.get_org_by_name(org_name)

    if not org:
        new_org = crud.create_org_with_cause_id(org_name, cause_id, mission, web_url, tagline)
        flash('CONGRATULATIONS!  YOU HAVE NOW BEEN ADDED TO THE MIGHTY MISSIONS NETWORK.')
        return redirect(f'/profiles/{new_org.org_id}')
    else: 
        flash('THIS ORGANIZATION ALREADY EXISTS IN OUR NETWORK.')
        return redirect(f'/profiles/{org.org_id}')        

   
@app.route('/logout') 
def logout():
    del session['org_id']
    del session['org_name']
    return redirect('/') 


##############   Returns a profile page   #################

@app.route('/profiles/<org_id>')
def show_org(org_id):
    """ Show details on a particular organization."""
    print("THIS IS FOR DEBUGGING\n\n\n\n\n\n")
    print(org_id)
    # org = crud.get_org_by_name(org_name)
    org = crud.get_org_by_id(org_id)
    print(org)
    return render_template('profiles.html', org=org)



##############  Main Search Page ##########################

@app.route('/search', methods=['GET'])
def search():


    causes=crud.get_all_causes()

    """ Render the Search page """

    return render_template('search.html', causes=causes)



##############   Returns a list of orgs page **UNIT TEST**  #################

@app.route('/list')
def all_orgs():
    """ Search all organizations by name """

    orgs = crud.get_orgs()       

    return render_template('listoforgs.html', orgs=orgs)



##############   Search by Cause ** INTEGRATION TEST*** ################################

@app.route('/cause', methods=['GET'])
def search_orgs_by_cause():
     """ Search for organizations by cause """

     cause_name = request.args.get('cause_name')
     cause_obj = crud.get_cause_by_name(cause_name)
     orgs = crud.get_orgs_by_cause(cause_obj)
    
     return render_template('searchbycause.html', cause_obj=cause_obj)

#@app.route('/test/', methods=["POST"])
#def show_orgs_by_cause():

 #   return "this url worked"


##############   Search by Name  INTEGRATION TEST  ##########################

@app.route('/searchbyname', methods=['POST'])
def org_by_name():
    """ Search for an organization by name """

    org_name = request.form.get('org_name')
    org = crud.get_org_by_name(org_name)

    if not org:
        flash('THIS ORGANIZATION IS NOT REGISTERED IN OUR DATABASE')
        return redirect('/search')

    return redirect(f'/profiles/{org.org_id}')



if __name__ == '__main__':
    connect_to_db(app)
    print("this is the server running")
    app.run(host='0.0.0.0', debug=True)
