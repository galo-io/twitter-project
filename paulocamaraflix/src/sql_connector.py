from sqlalchemy import create_engine, text
from sqlalchemy.types import Integer
import mypysql
import pandas as pd
import os

class sqlConnector():
    
    def __init__(self, username, password, server, port, database):
        
        self._username = username
        self._password = password
        self._server = str(server)
        self._port = str(port)
        self._engine = create_engine(f'mysql+pymysql://{self._username}:{self._password}@{self._server}:{self._port}')
        self._database = database
    
    def grantAcess(self):
        """
        
        """
        pass
        
    def createDataBase(self, table_name, schema_json):
        """
        Create a database into the MySQL Server

        Args:
            table_name: Name of the table
            schema_json: A JSON containing the {column_name:data_type}
        
        Authors:
            @marcuscardona
        
        Since:
            02-2023
        """

        # Create List to Save Schema
        var_to_create = []
        for var, var_type in schema_json.items():
            var_to_create.append(var+' '+var_type) 
        # Transform list to tuple
        
        
        with self._engine.connect() as conn:
           conn.execute(text(f"CREATE TABLE {self._database}.{table_name} ({','.join(var_to_create)})"))
           conn.commit()

    def insertInto(self, table_name, json):
        """
        Insert Data into the Table of the specified DB
        
        Args:
            table_name: Name of the table
            schema_json: A JSON containing the {column_name:data_type}
        
        Authors:
            @marcuscardona
        
        Since:
            02-2023
        """
        columns_list = []
        values_list = []
        for columns, values in json.items():
            columns_list.append(columns)
            values_list.append('"{}"'.format(values))
        
        columns = ','.join(columns_list)
        values = ','.join(values_list)
        with self._engine.connect() as conn:
            conn.execute(text(f'INSERT INTO {self._database}.{table_name} ({columns}) VALUES ({values});'))
            conn.commit()

    def showDatabases(self):
        with self._engine.connect() as conn:
            result = conn.execute(text('SHOW DATABASES'))
            print(result.all())

    def dropTable(self, table_name):
        with self._engine.connect() as conn:
            conn.execute(text(f"DROP TABLE {self._database}.{table_name}"))
            conn.commit()

    def importQuery(self, filename):
        """"""
        from pathlib import Path
        return Path('./queries/{0}.txt'.format(filename)).read_text(encoding='UTF-8')

    def queryData(self, query):
        import pandas as pd
        with self._engine.connect() as conn:
            result_proxy = conn.execute(text(query))
            results_dict = [r._asdict() for r in result_proxy]
            return results_dict