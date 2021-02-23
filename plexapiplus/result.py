

class Result:
    def __init__(self, server, result):
        self.server = server
        self.result = result
        self.guid = result.guid.split("//")[1].split("?")[0]
    def __repr__(self):
        return f"{self.server.friendlyName}:{self.result.title}:{self.guid}"
