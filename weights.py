from db import db
from flask import session

def add_weight(user_id, weight_now, date):
    try:
        sql = """INSERT INTO weights (user_id,weight_now,weight_date,created,modified,visible) 
                 VALUES (:user_id,:weight_now,:weight_date,NOW(),NOW(),1)"""
        db.session.execute(sql, {"user_id":user_id, "weight_now":weight_now, "weight_date":date})
        db.session.commit()
    except:
        return False
    return True

def get_weights(user_id):
#    try:
#    print("Kokeillaan")
    sql = "SELECT weight_date,weight_now FROM weights WHERE user_id=:user_id ORDER BY weight_date"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()
#    except:
 #       return 0

def check_date(user_id, date):
    sql = "SELECT 1 FROM weights WHERE user_id=:user_id AND weight_date=:weight_date AND visible=1"
    result = db.session.execute(sql, {"user_id":user_id, "weight_date":date})
    if result.fetchone() != None:
        return True
    else:
        return False