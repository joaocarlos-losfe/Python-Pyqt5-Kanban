import os
import pathlib
import sqlite3

from Model.querys import Query
from singleton import Singleton

class Database(Query, metaclass = Singleton):
    def __init__(self):
        self._db_path = pathlib.Path(__file__).parent.absolute()
        self._db_path = os.path.join(self._db_path, "DB")

        if not os.path.isfile(self.get_db_path):
            conn = sqlite3.connect(self.get_db_path)
            exec = conn.cursor()
            exec.execute(super().query_create_table_tasks())

    @property
    def get_db_path(self):
        return self._db_path + "local.db"

    def get_tasks(self, project_id):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_get_tasks(), (project_id,))
        data = exec.fetchall()

        data_table = {}
        task_info = []

        for task in data: #itera no conjunto
            for t in task:
                task_info.append(t)
            data_table[task[0]] = task_info #id da tarefa
            task_info = []

        return data_table

    def save(self, task_id, project_id, creation_date, move_date, stage, text):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_save_data(), (task_id, project_id, creation_date, move_date, stage, text,))
        conn.commit()

    def update(self, move_date, stage, text, task_id ):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_update_data(), (move_date, stage, text, task_id, ))
        conn.commit()

    def delete(self, task_id):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_delete_data(), (task_id,))
        conn.commit()

    def delete_project(self, project_id):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_delete_project(), ("%"+project_id+"%",))
        conn.commit()