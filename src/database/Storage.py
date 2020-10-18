import psycopg2
from config.dev import ConfigDB

class Storage():
    """
    Management database
    """
    def __init__(self):
        
        super(Storage).__init__()
        self.configDB = ConfigDB()
        self.conn = None
        self.cursor = None

    def connect(self):
        """
        Connect Postgres database 
        """
        try:
            self.conn = psycopg2.connect(
                host = self.configDB.HOST,
                database = self.configDB.DATABASE,
                user = self.configDB.USER,
                password = self.configDB.PASSWORD)
            # Open a cursor to perform database operations
            self.cursor = self.conn.cursor()
            print(self.conn.get_dsn_parameters(), "\n")
            # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def get(self, query):
        """
        Select table in database
        paramters:
            query: SQL string for select in db
        return:
            rows: rows from table in db 
        example: 
            get("SELECT name, email FROM public.user WHERE ID=1088597617")
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        print("Select successfully")
        self.conn.close()
        return rows


    def insert(self, query):
        """
        Insert new tuple in to database table
        paramters:
            query: SQL string for Insert tuple
        return:
            count: number of insert tuples

        example:
            insert(INSERT INTO public.user(ID, userType, name, lastname, state, phone, email, password) VALUES(1085897621, 1, 'Pepe', 'Arteaga', true, 3164277878,'pepe@gmail.com','121d41s'))
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            count = self.cursor.rowcount
            print(count, "Record inserted successfully into table")
            self.conn.close()
        except :
            count = 0
            print(count, "Record inserted failed into table")

        return count
