from aws_lambda_powertools.utilities.idempotency.persistence.base import BasePersistenceLayer
import psycopg2

class PostgresPersistenceLayer(BasePersistenceLayer):
    def __init__(self, dsn:str):
        self.dsn = dsn
        
    def _get_conn(self):
        return psycopg2.connect(self.dsn)
    
    def _get_record(self, idempotency_key: str):
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT status, response_data FROM idempotency WHERE idempotency_key = %s", (idempotency_key,))
                return cur.fetchone()
            
            
    def _put_record(self, idempotency_key: str, status: str, response_data: str):
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO idempotency (idempotency_key, status, response_data)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (idempotency_key) DO UPDATE SET status = EXCLUDED.status, response_data = EXCLUDED.response_data
                """, (idempotency_key, status, response_data))
                conn.commit()