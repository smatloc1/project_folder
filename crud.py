"""CRUD operations."""

from model import db, Org, Cat, Cause, connect_to_db

#def create_org(org_name, cause, category, mission):
    #"""Create and return a new organization."""

    #org = Org(org_name=org_name,
                  #cause=cause,
                  #category=category,
                  #mission=mission)

    #db.session.add(org)
    #db.session.commit()

    #return org


def get_orgs():
    """ Return all organizations."""

    return Org.query.all()


def get_org_by_name(org_name):
    """ Return an organization by name."""

    return Org.query.get(org_name)


def get_org_by_cause(cause_name):
    """Return a organization by cause."""

    return Org.query.filter(Org.cause == cause_name).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
