import psycopg2
from datetime import datetime

class PipelineLogger:
    def __init__(self, db_params):
        self.conn = psycopg2.connect(**db_params)
        
    def start_run(self, pipeline_name: str) -> int:
        query = """
            INSERT INTO pipeline_runs (pipeline_name, status, start_time)
            VALUES (%s, 'RUNNING', %s)
            RETURNING id;
        """
        
        with self.conn.cursor() as cursor:
            cursor.execute(query, (pipeline_name, datetime.now()))
            run_id = cursor.fetchone()[0] 
            self.conn.commit()
            
        return run_id

    def complete_run(self, run_id: int, total_records: int):
        now = datetime.now()
        
        query = """
            UPDATE pipeline_runs
            SET status = 'SUCCESS',
                end_time = %s,
                duration_seconds = EXTRACT(EPOCH FROM (%s - start_time)),
                total_records = %s
            WHERE id = %s;
        """
        
        with self.conn.cursor() as cursor:
            cursor.execute(query, (now, now, total_records, run_id))
            self.conn.commit()

    def fail_run(self, run_id: int, error_message: str):
        now = datetime.now()
        
        query = """
            UPDATE pipeline_runs
            SET status = 'FAILED',
                end_time = %s,
                duration_seconds = EXTRACT(EPOCH FROM (%s - start_time)),
                error_message = %s
            WHERE id = %s;
        """
        
        with self.conn.cursor() as cursor:
            cursor.execute(query, (now, now, error_message, run_id))
            self.conn.commit()
            
    def close(self):
        if self.conn:
            self.conn.close()