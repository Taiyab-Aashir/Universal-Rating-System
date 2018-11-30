from  django.db import connection
def update_gamerating(uid,gid,rating):
    nid=0
    with connection.cursor() as cursor :
        cursor.execute("Select * from gamerating where userid= %s and gameid=%s",[uid,gid])
        if len(cursor.fetchone())==0 :
            cursor.execute("Insert into gamerating values (%s,%s,%s,%s)",[nid,uid,gid,rating])
        else:
            cursor.execute("update gamerating set rating = %s where userid= %s and gameid= %s",[rating,uid,gid])


update_gamerating(3,4,10)