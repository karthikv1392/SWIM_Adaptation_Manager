_Author_ = "Karthik Vaidhyanathan"

# This will serve as the knowledge for the adaptation loop
# This stores the adaptation processes in a NoSQL database
# This class can also be used for storing the Q-Table required for the adaptation

import sqlite3
from sqlite3 import Error
from Custom_Logger import logger
from Initializer_Class import Initialize


init_obj = Initialize()

class Knowledge():
    def __init__(self):
        self.db_file = init_obj.adaptation_db

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        return conn


    def create_adaptation_record(self,conn, adaptation_record):
        # Insert the different values that needs to be stored while performing the adaptation
        sql = ''' INSERT INTO adaptations(timestamp,server_add_flag,server_remove_flag,action)
                      VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, adaptation_record)
        conn.commit()
        return cur.lastrowid

