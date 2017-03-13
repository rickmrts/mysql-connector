import MySQLdb


class DataBase(object):
    def getConnection(end,usr,passwd,name):
        db = MySQLdb.connect(end,usr,passwd,name)
        return db
    pass

    def getCursor(db):
        cursor = db.cursor()
        return cursor
    pass

    def ListAll(crs,table):
        crs.execute("SELECT * FROM "+table)
        return crs.fetchall()
    pass

    def ListOne(crs,table,id):
        crs.execute ("SELECT * FROM %s WHERE id=%s " % (table,id))
        return crs.fetchone()
    pass

    def Insert(crs,bd,table,obj):
        try:
            st = "INSERT INTO %s" % table
            crs.execute(st+"(nome,email,telefone,grupo,autorizacao) VALUES (%s,%s,%s,%s,%s) " , (obj.nome,obj.email,obj.telefone,obj.grupo,obj.autorizacao))
            bd.commit()
        except:
            bd.rollback()
    pass

    def Delete(crs,bd,table,id):
        try:
            crs.execute ("DELETE FROM %s WHERE id=%s " % (table,id))
            bd.commit()
        except:
            bd.rollback()
    pass    
