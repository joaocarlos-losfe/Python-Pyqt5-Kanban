import datetime
import os

from generate_id import GenerateId



print(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
"""
print("Teste de colisao: ")
while True:
    anterio_gerada = GenerateId.generate(33, 126)
    segunda_gerada = GenerateId.generate(33, 126)

    if anterio_gerada == segunda_gerada:
        print(anterio_gerada + " = " + segunda_gerada)
        break

    print(anterio_gerada + " = " + segunda_gerada)

"""

from Model.task import Task


"""
from  Model.database import Database

db = Database()

print(db.get_db_path)

if not os.path.isfile(db.get_db_path):
    print("database created")
else:
    print("database existente")


#db.save("3saddsad", "projeto 2", "22/06/2021 09:32", "", "Nova Tarefa", "teste de adicçao")

db.update("22/06/2021 09:32", "Em progresso", "teste de movimentação para em progresso - ok", "3saddsad")

print(db.get_tasks("projeto 2"))

db.delete("3")
"""

