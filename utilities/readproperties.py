import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getapplicaionurl():
        url=config.get('common info','baseURL')
        return url


    @staticmethod
    def getusermail():
        username=config.get('common info','username')
        return username


    @staticmethod
    def getpasswod():
        password=config.get('common info','password')
        return password
