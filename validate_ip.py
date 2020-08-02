
def isIPv4(s):
    try: return str(int(s)) == s and 0 <= int(s) <= 255
    except: return False

def isIPv6(s):
    if len(s) > 4:
        return False
    try : return int(s, 16) >= 0 and s[0] != '-'
    except:
        return False

def validIPAddress(ip):
    """
    :type ip: str
    :rtype: str
    """
    if ip.count(".") == 3 and all(isIPv4(i) for i in ip.split(".")):
        return True
    if ip.count(":") == 7 and all(isIPv6(i) for i in ip.split(":")):
        return True
    return False

def validPortNumber(PORT):
    try:
        return str((int(PORT))) == PORT and 0 <= int(PORT) <= 65535
    except:
        return False
