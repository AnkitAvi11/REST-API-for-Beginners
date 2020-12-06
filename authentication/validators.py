import re

def isemail(email) : 
    regex = re.compile('^([a-zA-Z0-9\-\.\_])+\@([a-zA-Z0-9\-\.\_])+\.([a-zA-Z0-9]{2,4})$')
    if regex.match(email) : return True
    return False


def isvalid_password(username, password) : 
    username = username.lower()
    if username in password : 
        return False
    
    if len(password) < 8 : 
        return False

    return True


def isvalid_username(username) : 
    regex = re.compile('^([a-zA-Z0-9\_]{8,})$')
    if regex.match(username) : 
        return True

    return False
