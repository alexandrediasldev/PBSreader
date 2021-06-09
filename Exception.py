class UnknownPBSName(Exception):
    def __init__(self, message):
        self.message = message


class EnvironmentLoadingException(Exception):
    def __init__(self, message):
        self.message = message
