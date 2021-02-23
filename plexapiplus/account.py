from plexapi.myplex import MyPlexAccount

class Account(MyPlexAccount):
    def servers(self):
        for user in self.users():
            yield from user.servers
