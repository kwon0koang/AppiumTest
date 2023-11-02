import config

def is_aos():
    return "Android" == config.capabilities['platformName']
