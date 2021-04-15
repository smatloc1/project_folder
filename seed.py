"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb mmdata')
os.system('createdb mmdata')

model.connect_to_db(server.app)
model.db.create_all()



###########    #1. Create a new cause        #########################

test_cause3 = create_cause('youth development')

cause4 = create_cause('Religious Activities')

cause5 = create_cause('Scholarship and Financial Support')



###########    #2. Create a new org using cause_obj    ###############

test_org2 = create_org_with_cause_obj(org_name='100 Men', cause_obj=test_cause2, mission='To help youth in crisis')

org4=create_org_with_cause_obj(org_name='I Have a Dream Foundation', cause_obj=cause5, 
                mission="Empowering children in low-income communities to achieve higher education")

org5=create_org_with_cause_obj(org_name='18 Doors', cause_obj=cause4, 
                mission='Empower people in interfaith relationships to engage in Jewish life')



###########   #3. Create a new org using a cause_id    ###############

test_org3 = create_org_with_cause_id(org_name='FBTB,inc', cause_id=3,
                mission='Helping families with youth in crisis')

org6=create_org_with_cause_id(org_name='After-School All-Stars', cause_id=3, 
                mission='To provide comprehensive after-school programs that keep children safe and help them succeed in school and life')
 

 
######## EX: How to use the cause relationship from an org to call the cause_name #####

# test_org2.cause.cause_name  
#'youth development'
   
######## EX:  How to query for all orgs with that have test_cause2; it returns a list of all the orgs ####### 

#  test_cause2.orgs    
#[<Org org_id=2, org_name=100 Men, misssion=To help youth in crisis, cause_id=3>, <Org org_id=3, org_name=FBTB,inc, misssion=Helping families with youth in crisis, cause_id=3>]
 
######## EX:  How to modify an attibute once its been created

#test_cause2.cause_name='youth and family support'
#db.session.add(test_cause2)
#db.session.commit()