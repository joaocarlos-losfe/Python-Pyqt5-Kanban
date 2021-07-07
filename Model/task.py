import datetime
from generate_id import GenerateId
from Model.database import Database


class Task():
    #constantes
    NEW_TASK = "Nova Tarefa"
    IN_PROGRESS = "Em Progresso"
    CONCLUDED = "Concluida"

    def __init__(self):

        self._task_id = None
        self._project_id = None
        self._creation_date = None
        self._move_date = ""
        self._stage = None
        self._text = None

        self._able_to_update = False #apta a atualizar

    def create(self, project_id, text_info):
        if self._task_id is None:
            self._project_id = project_id
            self._text = text_info
            #auto generate
            self._task_id = GenerateId.generate(33,126)
            self._creation_date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            self._stage = Task.NEW_TASK
            self.local_database_update()

    def recovery(self, task_id, project_id, creation_date, move_date, stage, text):
        self._task_id = task_id
        self._project_id = project_id
        self._creation_date = creation_date
        self._move_date = move_date
        self._stage = stage
        self._text = text

        self._able_to_update = True

    def update_stage(self, stage_flag):
        if self._project_id is not None:
            if type(stage_flag) is int:
                if stage_flag == 1:
                    self._stage = Task.NEW_TASK
                elif stage_flag == 2:
                    self._stage = Task.IN_PROGRESS
                elif stage_flag == 3:
                    self._stage = Task.CONCLUDED

                if stage_flag >=1 and stage_flag <= 3:
                    self._move_date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                    self.local_database_update() #atualiza diretamente no bd

                return True #estagio do projeto atualizado com sucesso
        else:
            return False

    def get_all_details(self):
        details = []

        if self._task_id is not None:
            details.append(self._task_id)
            details.append(self._project_id)
            details.append(self._creation_date)
            details.append(self._move_date)
            details.append(self._stage)
            details.append(self._text)

        return details

    @property
    def get_stage_task(self):
        return self._stage

    @property
    def get_text(self):
        return self._text

    @property
    def get_id(self):
        return self._task_id

    def local_database_update(self):

        db = Database()

        if self._task_id is not None:
            if not self._able_to_update :
                db.save(self._task_id, self._project_id, self._creation_date, self._move_date, self._stage, self._text)
                self._able_to_update = True
            else:
                db.update(self._move_date, self._stage, self._text, self._task_id)

    def remove_from_data_base(self):
        db = Database()
        db.delete(self.get_id)