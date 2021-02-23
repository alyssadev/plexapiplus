from plexapi.myplex import MyPlexResource

class HashableResource(MyPlexResource):
    resource = None
    def __init__(self, resource):
        self.resource = resource
    def __hash__(self):
        return hash(self.resource.clientIdentifier)
    def __repr__(self):
        return repr(self.resource) + "#"
