import configparser

config = configparser.RawConfigParser()
config.read('/Users/utsav.jha/PycharmProjects/SlingApp/Configurations/configuration.ini')


class login_read:
    @staticmethod
    def getEmail():
        email = config.get("Login Info", "username")
        return email

    @staticmethod
    def getPass():
        password = config.get("Login Info", "password")
        return password
