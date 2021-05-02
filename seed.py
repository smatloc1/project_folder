"""Script to seed database."""

import os
#import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb mmdata')
os.system('createdb mmdata')

model.connect_to_db(server.app)
model.db.create_all()


###########    #1. Create a new cause        #########################

cause1 = crud.create_cause('Religious Activities')
cause2 = crud.create_cause('Scholarship and Financial Support')
cause3 = crud.create_cause('Youth Development, Shelter, and Crisis Services')
cause4 = crud.create_cause('Youth Education Programs and Services')
cause5 = crud.create_cause('Social Services')
cause6 = crud.create_cause('Women, Children and Family Services')
cause7 = crud.create_cause('Animal Protection and Welfare')

###########    #2. Create a new org using cause_obj    ###############

org1=crud.create_org_with_cause_obj(org_name='I Have a Dream Foundation', cause_obj=cause2, 
                mission="Empowering children in low-income communities to achieve higher education",
                web_url="http://www.ihaveadreamfoundation.org", 
                tagline="Empowering children in low-income communities to achieve higher education")

org2=crud.create_org_with_cause_obj(org_name='18Doors', cause_obj=cause1, 
                mission='Empower people in interfaith relationships to engage in Jewish life',
                web_url="https://18doors.org/", tagline='Unlocking Jewish')

org3=crud.create_org_with_cause_obj(org_name='100 Black Men of America', cause_obj=cause3,
                mission='To improve the quality of life within our communities and enhance educational and economic opportunities for all African Americans.',
                web_url="http://www.100blackmen.org/", tagline="Improving the quality of life within our communities")



################   #3. Create a new org using a cause_id    ###################

org4=crud.create_org_with_cause_id(org_name='After-School All-Stars', cause_id=3, 
                mission='To provide comprehensive after-school programs that keep children safe and help them succeed in school and life',
                web_url='http://www.afterschoolallstars.org/', tagline='After-school and summer programs for underserved youth.')

org5=crud.create_org_with_cause_id(org_name='4 Paws for Ability', cause_id=5,
                mission='4 Paws for Ability strives to be the leading provider of service dogs for children regardless of disability',
                web_url='http://www.4pawsforability.org/', tagline='Providing service dogs to people with disabilities worldwide')

org6=crud.create_org_with_cause_id(org_name='AdoptAClassroom.org', cause_id=4, 
                mission='To give teachers a hand by providing needed classroom materials so that students can succeed',
                web_url='http://www.adoptaclassroom.org', tagline='We give teachers a hand')

org7=crud.create_org_with_cause_id(org_name='AAUW - American Association of University Women', cause_id=4,
                mission='To advance equity for women and girls through advocacy, education, philanthropy, and research.',
                web_url='http://www.aauw.org', tagline='Empowering women since 1881')
 

 
