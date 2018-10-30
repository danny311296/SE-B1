import psycopg2
import psycopg2.extras

class dbconnection:
    def __init__(self,host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host)
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
    def get_connection(self):
        return self.connection
    
    def get_cursor(self):
        return self.cursor
    
    def query(self,table,cols=['*'],**kwargs):
        query = "select " + ",".join(cols) + " from " + table 
        if(len(kwargs)>0):
            query += " where " + " and ".join([ column + "=" + str(value) if not(isinstance(value, str)) else column + "=" + "'"+ value + "'" for column,value in kwargs.items() ])
        print(query)
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert(self,table,**kwargs):
        query = "insert into " + table + "(" + ",".join([column for column,_ in kwargs.items()]) + ") " + "values(" + ",".join([str(value) if not(isinstance(value, str)) else "'"+ value + "'" for _,value in kwargs.items()]) + ")"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()