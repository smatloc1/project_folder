"""CRUD operations."""

from model import db, Org, Cause, connect_to_db

def create_org_with_cause_id(org_name, cause_id, mission, web_url, tagline, image):
    """Create and return a new organization."""

    org = Org(org_name=org_name.lower(), 
                  cause_id=cause_id,
                  mission=mission,
                  web_url=web_url,
                  tagline=tagline,
                  image=image)

    db.session.add(org)
    db.session.commit()

    return org

### cause_obj parameter is a cause object not a string

def create_org_with_cause_obj(org_name, cause_obj, mission, web_url, tagline, image):
    """Create and return a new organization."""

    org = Org(org_name=org_name.lower(), 
                  cause=cause_obj,
                  mission=mission,
                  web_url=web_url,
                  tagline=tagline,
                  image=image)

    db.session.add(org)
    db.session.commit()

    return org

def create_cause(cause_name):
    """Create and return a new cause."""

    cause = Cause(cause_name=cause_name) 
                  
    db.session.add(cause)
    db.session.commit()

    return cause


def get_orgs():
    """ Return all organizations."""

    return Org.query.all()


def get_org_by_name(org_name):
    """ Return an organization by name."""

    return Org.query.filter(Org.org_name == org_name).first()


def get_orgs_by_cause(cause_name):
   """Return a list of organizations by cause."""
 
   return Org.query.filter(Org.cause == cause_name)


def get_cause_by_name(cause_name):
    """ Return a cause by name."""

    return Cause.query.filter(Cause.cause_name == cause_name).first()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
