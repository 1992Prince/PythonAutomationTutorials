from utilities.ConfigReaderUtility_2 import readConfig
from utilities.LogUtility_1 import getLogger

# calling logger utility fun, similarly we can call this in our scripts
logger = getLogger()
logger.info("This is second info")
logger.critical("I am critical resource")

print("***********************************************************")
# calling configReader function
siteurl = readConfig("basic info","testsiteurl")
username = readConfig("locator","username")
print("Site URl is :",siteurl," Username is :",username)