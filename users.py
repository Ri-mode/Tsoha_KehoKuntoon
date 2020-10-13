from os import urandom
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
# Voiko session-muuttujia olla useita?
# Saakohan käyttäjänimen koodata tällä tavoin session aikana käytettäväksi?
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["user_id"]
# Tarvitseeko aiemmin luotu username-sessio poistaa?
    del session["username"]

def register_normal(username,password,current_weight,target_weight,height):
    hash_code = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (usertype,username,password,currentweight,targetweight,height,created,modified)" \
              "VALUES (1,:username,:password,:currentweight,:targetweight,:height,NOW(),NOW())"
        db.session.execute(sql, {"username":username,"password":hash_code,"currentweight":current_weight,
            "targetweight":target_weight,"height":height})
        db.session.commit()
    except:
        return False
    return login(username, password)

def register_coach(username,password):
    hash_code = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (usertype,username,password,created,modified)" \
              "VALUES (2,:username,:password,NOW(),NOW())"
        db.session.execute(sql, {"username":username,"password":hash_code})
        db.session.commit()
    except:
        return False
    return login(username, password)


def user_id():
    return session.get("user_id",0)

def username():
    return session.get("username",0)
