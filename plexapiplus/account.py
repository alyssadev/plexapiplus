from plexapi.myplex import MyPlexAccount
from plexapi.exceptions import NotFound

from sys import stderr

class Account(MyPlexAccount):
    def mpservers(self):
        """ Returns a generator for MyPlexServerShare objects accessible from the authed account """
        for user in self.users():
            yield from user.servers

    def servers(self, verbose=False, *args, **kwargs):
        """ Returns a generator of tuples:
            ( (MyPlexResource, MyPlexResource.connect()), ... )
            Args are passed to MyPlexResource.connect(..), except for verbose, which prints progress to stderr
            Takes a while if some servers are hard to access, it will fall back to relay if necessary and
            return (resource, None) for servers to which it was unable to connect. """
        for resource in self.resources():
            try:
                _s = resource.connect(*args, **kwargs)
                if verbose: print(f"connected to {resource.name}", file=stderr)
                yield resource, _s
            except NotFound:
                if verbose: print(f"could not connect to {resource.name}", file=stderr)
                yield resource, None

