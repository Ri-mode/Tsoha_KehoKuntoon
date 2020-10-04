from db import db
from flask import session

def add_weight(user_id,weight_now,fat_now,muscle_now):
    try:
        sql = "INSERT INTO weights (user_id,weight_now,fat_now,muscle_now,weight_date,created,modified) VALUES \
              (:user_id,:weight_now,:fat_now,:muscle_now,NOW(),NOW(),NOW())"
        db.session.execute(sql, {"user_id":user_id,"weight_now":weight_now,"fat_now":fat_now,"muscle_now":muscle_now})
        db.session.commit()
    except:
        return False
    return True

def get_weights(user_id):
#    try:
#    print("Kokeillaan")
    sql = "SELECT weight_now FROM weights WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()
#    except:
 #       return 0