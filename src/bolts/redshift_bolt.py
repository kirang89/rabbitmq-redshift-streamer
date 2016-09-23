import json
import os
import psycopg2
from streamparse import Bolt


class RedshiftBolt(Bolt):

    def initialize(self, conf, ctx):
        columns = ['id', 'name']
        self.query = self._generate_query("users", columns)
        self.conn = psycopg2.connect(database=os.environ.get('RS_DBNAME'),
                                     host=os.environ.get('RS_HOST'),
                                     port=os.environ.get('RS_PORT'),
                                     user=os.environ.get('RS_USER'),
                                     password=os.environ.get('RS_PASS'))
        self.cursor = self.conn.cursor()

    def _generate_query(self, table, columns):
        if not table or not columns:
            return

        col_string = (', ').join(columns)
        values = ["'{" + col + "}'" for col in columns]
        values_str = (",").join(values)
        query = "INSERT INTO {} ({}) VALUES ({});".format(table, col_string, values_str)  # noqa
        return query

    def process(self, tuple):
        user_data = json.loads(tuple.values[0])
        query = self.query.format(**user_data)
        self.cursor.execute(query)
        self.conn.commit()
