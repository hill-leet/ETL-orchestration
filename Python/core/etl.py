class ETLDB:
    def __init__(self, target_table, target_schema, src_table=None, src_schema=None):
        self.target_table = target_table
        self.target_schema = target_schema
        self.src_table = src_table
        self.src_schema = src_schema

    def insert_to_clickhouse(self, dwh_con, src_con, sql):
        clickhouse_conn = dwh_con
        conn = src_con

        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        clickhouse_conn.execute(
            f'TRUNCATE TABLE {self.target_schema}.{self.target_table}'
        )

        clickhouse_conn.execute(
            f'INSERT INTO {self.target_schema}.{self.target_table} VALUES',
            ((cur,) for cur in data)        # позже проверить по доке
        )

        cursor.close()

        
