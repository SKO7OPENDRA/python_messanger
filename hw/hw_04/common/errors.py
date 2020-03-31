class UsernameToLongError(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return 'Username {} should contain less than 26 symbols'.format(self.username)


class RCError(Exception):
    def __init(self, code):
        self.code = code

    def __str__(self):
        return 'Response code {} is not correct'.format(self.code)


class RCLenError(RCError):
    def __str__(self):
        return 'Response code {} length is not correct'.format(self.code)


class RCKeyError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'Mandatory attribute {} missing'.format(self.key)