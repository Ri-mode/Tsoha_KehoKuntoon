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
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]

def register_normal(username,password,target_weight,height):
    hash_code = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (usertype,username,password,targetweight,height,created,modified,visible)
                 VALUES (1,:username,:password,:targetweight,:height,NOW(),NOW(),1)"""
        db.session.execute(sql, {"username":username,"password":hash_code,
            "targetweight":target_weight,"height":height})
        db.session.commit()
    except:
        return False
    return login(username, password)

def register_coach(username,password, target_weight,height):
    hash_code = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (usertype,username,password,targetweight,height,created,modified,visible)
                 VALUES (2,:username,:password,:targetweight,:height,NOW(),NOW(),2)"""
        db.session.execute(sql, {"username":username,"password":hash_code,
            "targetweight":target_weight,"height":height})
        db.session.commit()
    except:
        return False
    return login(username, password)

def is_user():
    return user_id() != 0

def is_coach(id):
    sql = "SELECT 1 FROM users WHERE id=:id AND usertype=2"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone() != None

def user_id():
    return session.get("user_id",0)

def username():
    return session.get("username",0)

def user_info(id):
    sql = "SELECT username,targetweight,height FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def add_coach(coach_id, trainer_id):
    try:
        sql = """INSERT INTO coaches (coach_id,trainer_id,created,modified,visible) 
                 VALUES (:coach_id,:trainer_id,NOW(),NOW(),1)"""
        db.session.execute(sql, {"coach_id":coach_id,"trainer_id":trainer_id})
        db.session.commit()
    except:
        return False
    return True

