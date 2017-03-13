from banco import *
from Pessoa import *

def listaAttr(obj):
    return obj.__dict__.keys()
pass

def listaVal(obj):
    return obj.__dict__.values()
pass


conn = DataBase.getConnection('localhost','root','root','exemplos')

banco = DataBase.getCursor(conn)

#data = DataBase.ListAll(banco,'contatos')

#data = DataBase.ListOne(banco,'contatos','1')

#pessoa = Pessoa('ricardo','ricardo@uel.br', '4333333333','public','1')

#DataBase.Insert(banco,conn,'contatos',pessoa)

#DataBase.Insert(banco,conn,'contatos',pessoa)

#DataBase.Delete(banco,conn,'contatos',3)

#data = DataBase.ListAll(banco,'contatos')
#print(data)

banco.close()