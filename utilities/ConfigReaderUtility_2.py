from configparser import ConfigParser

"""
config = ConfigParser()
config.read("C:/Users/princ/PycharmProjects/pythonProject/config/config.ini")

print(config.get("locator","username"))
print(config.get("basic info","testsiteurl"))
"""

def readConfig(section,key):
    config = ConfigParser()
    config.read("C:/Users/princ/PycharmProjects/pythonProject/config/config.ini")
    return config.get(section,key)

