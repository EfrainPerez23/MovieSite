from werkzeug.security import safe_str_cmp
from DataAccessLayer.DataAccessObject.IDAO.UserDAO import UserDAO

import hashlib
import sys

hashlib.sha256()

def authenticate(email, password):
    userDao = UserDAO()
    user = userDao.findUserByEmail(email)
    encryptedPasword = hashlib.sha224(password.encode('utf-8')).hexdigest()
    if user and safe_str_cmp(user.password, encryptedPasword):
        return user


def identity(payload):
    userDao = UserDAO()
    return userDao.read(payload['identity'])
