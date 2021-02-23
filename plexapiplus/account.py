from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.exceptions import NotFound

from sys import stderr
from collections import defaultdict

from .resource import HashableResource
from .result import Result

class Account(MyPlexAccount):
    _cached_connections = {}

    def mpservers(self):
        """ Returns a generator for MyPlexServerShare objects accessible from the authed account """
        for user in self.users():
            yield from user.servers

    def servers(self, verbose=False, *args, **kwargs):
        """ Returns a generator of tuples:
            ( (MyPlexResource, MyPlexResource.connect()), ... )
            Args are passed to MyPlexResource.connect(..), except for verbose, which prints progress to stderr
            Takes a while if some servers are hard to access, it will fall back to relay if necessary and
            return (resource, None) for servers to which it was unable to connect.
            Server connections are cached for reuse in self.search """
        for resource in self.resources():
            hr = HashableResource(resource)
            if hr in self._cached_connections:
                if verbose: print(f"found {resource.name} in cached connections")
                yield resource, self._cached_connections[hr]
                continue
            try:
                _s = resource.connect(*args, **kwargs)
                if verbose: print(f"connected to {resource.name}", file=stderr)
                self._cached_connections[hr] = _s
                yield resource, _s
            except NotFound:
                if verbose: print(f"could not connect to {resource.name}", file=stderr)
                yield resource, None

    def search(self, query, mediatype=None, limit=None, fetch=False, timeout=None, verbose=False):
        """ Returns a generator of tuples:
            ( (PlexServer, PlexServer.search(*args, **kwargs) ) """
        if not self._cached_connections and fetch:
            if verbose: print("Retrieving servers", file=stderr)
            _ = list(self.servers(verbose=verbose, timeout=timeout))
            servers = self._cached_connections
        elif not self._cached_connections and not fetch:
            if verbose: print("No servers provided, and fetch=False, so not retrieving servers with self.servers()", file=stderr)
        results = defaultdict(list)
        for hr,server in self._cached_connections.items():
            for result in server.search(query, mediatype=mediatype, limit=limit):
                g = f"{result.title}" + (f" ({result.year})" if hasattr(result, "year") else "") + " [{}]".format(result.guid.split("//")[1].split("?")[0])
                results[g].append(Result(server, result))
        return dict(results)
#            resource = hr.resource
#            relay = [c.relay for c in resource.connections if c.relay is not None][0]
#            yield (server, server.search(query, mediatype=mediatype, limit=limit))#, relay)
