"""CRUD operations."""

from model import db, Org, Cat, Cause, connect_to_db

def create_org_with_cause_id(org_name, cause_id, mission):
    """Create and return a new organization."""

    org = Org(org_name=org_name, 
                  cause_id=cause_id,
                  mission=mission)

    db.session.add(org)
    db.session.commit()

    return org

### cause_obj parameter is a cause object not a string

def create_org_with_cause_obj(org_name, cause_obj, mission):
    """Create and return a new organization."""

    org = Org(org_name=org_name, 
                  cause=cause_obj,
                  mission=mission)

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

    return Org.query.get(org_name)


#def get_org_by_cause(cause_id):
 #   """Return a organization by cause."""

  #  return Org.query.filter(Org.cause == cause_name).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
