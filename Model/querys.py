class Query:
    @staticmethod
    def query_create_table_tasks():
        return """
                    CREATE TABLE IF NOT EXISTS Task
                    (
                        task_id VARCHAR(15) NOT NULL PRIMARY KEY,
                        project_id VARCHAR(60) NOT NULL,
                        creation_date VARCHAR(30) NOT NULL, 
                        move_date VARCHAR(30),
                        stage VARCHAR(20) NOT NULL, 
                        text TEXT NOT NULL
                    );
                    """

    @staticmethod
    def query_save_data():
        return  """
                INSERT INTO Task (task_id, project_id, creation_date, move_date, stage, text)
                VALUES (?, ?, ?, ?, ?, ?)
                """

    @staticmethod
    def query_update_data():
        return  """
                UPDATE Task
                SET move_date = ?, stage = ?, text = ?
                WHERE task_id = ?;
                """

    @staticmethod
    def query_delete_data():
        return  """
                DELETE FROM Task WHERE task_id = ?
                """

    @staticmethod
    def query_get_tasks():
        return  """
                    SELECT * FROM Task WHERE project_id = ?
                """
    @staticmethod
    def query_delete_project():
        return  """
                DELETE FROM Task WHERE project_id LIKE ?
                """