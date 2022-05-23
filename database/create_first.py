import sys
sys.path.append('./')
from model.BasicConfig import BasicConfig
from helper import *
import json
from app import *
class CreateDatabase():
    status = ''
    closed = ''
    messages =''
    conn = ''
    cursor = ''
    d = dict()
    
    def __init__(self):
        self.status , self.closed , self.messages = init_db.ConnectionToDB()
        if(self.status == 1) and (self.closed == 0):
            self.conn,self.cursor,self.closed,self.status,self.messages = init_db.connect()
    def createUser(self):
        self.cursor.execute('DROP TABLE IF EXISTS verification')
        self.conn.commit
        self.cursor.execute('DROP TABLE IF EXISTS users_roles;')
        self.conn.commit
        self.cursor.execute('DROP TABLE IF EXISTS users;')
        self.cursor.execute('CREATE TABLE users (id serial NOT NULL,'
                                        'first_name varchar (20) NOT NULL,'
                                        'last_name varchar (50) NOT NULL,'
                                        'email varchar(50) NOT NULL UNIQUE,'
                                        'username varchar(20) NOT NULL UNIQUE,'
                                        'password bytea NOT NULL,'
                                        'email_confirmed BOOL NOT NULL DEFAULT FALSE ,'
                                        'job varchar(100),'
                                        'bio text,'
                                        'phone varchar(15),'
                                        'avatar text,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP,'
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'unique_id varchar(100) NOT NULL UNIQUE,'
                                        'public_id varchar(50) NOT NULL UNIQUE,'
                                        'deleted bool NOT NULL DEFAULT FALSE,'
                                        'identity_card varchar(100) UNIQUE,'
                                        'PRIMARY KEY (id));'
                                        )
        self.conn.commit()
        self.cursor.execute('DROP TABLE IF EXISTS roles;')
        self.cursor.execute('CREATE TABLE roles (id serial NOT NULL,'
                                        'name varchar (20) NOT NULL,'
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'deleted bool NOT NULL DEFAULT FALSE,'
                                        'PRIMARY KEY (id));'
                                        )
        self.conn.commit()
        self.cursor.execute('CREATE TABLE users_roles (user_id serial NOT NULL,'
                                        'role_id serial NOT NULL,'
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'deleted bool NOT NULL DEFAULT FALSE,'
                                        'primary key (user_id, role_id),'
                                        'foreign key (user_id) references users(id) ON DELETE CASCADE,'
                                        'foreign key (role_id) references roles(id) ON DELETE CASCADE);'
                                        )

        self.cursor.execute('CREATE TABLE verification (id serial NOT NULL,'
                                        'user_id serial NOT NULL,'
                                        'verify_number integer DEFAULT 0,'
                                        'expired_time timestamp DEFAULT NOW(),'
                                        'created_at timestamp DEFAULT NULL,'
                                        'updated_at timestamp default current_timestamp,'
                                        'primary key (id),'
                                        'foreign key (user_id) references users(id));'
                                        )
        # Insert data into the table
        self.conn.commit()

        roledata = ["superadmin","administrator","developer","functional","qc","owner","unittest","user"]
        for rr in roledata:
            self.cursor.execute("INSERT INTO roles (name) VALUES ('"+rr+"')")
            self.conn.commit()
            

        qr = f"SELECT unique_id FROM users order by unique_id desc ;"
        self.cursor.execute(qr)
        row = self.cursor.fetchone()
        seq = ''
        pas = 'fajarsoegi'
        first_name = 'soegi'
        last_name='dev'
        email = 'soegidev.id@gmail.com'
        username = 'soegidev'
        if(self.cursor.rowcount == 0):
            seq = CreateUserUniqueID(None)
            hashed = CreatePassword(pas).decode('utf-8')
            qr = """
            WITH users as (
                INSERT INTO users(first_name, last_name, email,username,password,unique_id,public_id) 
                VALUES ('"""+first_name+"""','"""+last_name+"""','"""+email+"""','"""+username+"""',
                '"""+hashed+"""','"""+seq+"""','"""+str(uuid.uuid4())+"""') RETURNING *
            )
            INSERT INTO users_roles(user_id, role_id) 
                VALUES ((select users.id from users), 1);"""
            self.cursor.execute(qr)
            self.conn.commit()
        else:
            row = self.cursor.fetchone()[0]
            seq = CreateUserUniqueID(row)
            hashed = CreatePassword(pas).decode('utf-8')
            qr = """
            WITH users as (
                INSERT INTO users(first_name, last_name, email,username,password,unique_id,public_id) 
                VALUES ('"""+first_name+"""','"""+last_name+"""','"""+email+"""','"""+username+"""',
                '"""+hashed+"""','"""+seq+"""','"""+str(uuid.uuid4())+"""') RETURNING *
            ), 
        INSERT INTO users_roles(user_id, role_id) 
                VALUES ((select users.id from users), 1);"""
            self.cursor.execute(qr)
            self.conn.commit()
    def createMigrations(self):
        self.cursor.execute('DROP TABLE IF EXISTS migrations;')
        self.cursor.execute('CREATE TABLE migrations (id serial NOT NULL,'
                                        'name varchar (200) NOT NULL,'
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'PRIMARY KEY (id));'
                                        )
        migrateInsert = "INSERT INTO migrations(name)values(%s);"
        migrationame = "Initial Database With Table"
        self.cursor.execute(migrateInsert,[migrationame])
        self.conn.commit()
    def createConfiguration(self):
        self.cursor.execute('DROP TABLE IF EXISTS configuration;')
        self.cursor.execute('CREATE TABLE configuration (id serial NOT NULL,'
                                        'name varchar (200) NOT NULL,'
                                        'config text default NULL, '
                                        'active boolean default True, '
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'PRIMARY KEY (id));'
                                        )
        nameInsert = "Basic"
        configNew = "INSERT INTO configuration(name,config)values(%s,%s);"
        configinsert = """{"version":"v1.0.0","versioncode":1,"applicationname":"PythonDev","powered_by":"X_blocks","created_by":"Soegidev","created_year":"2022","license":"XLicence","github":"Soegidev","version_api":"1","version_server":"1","url_api":"http://localhost/api","endpoint":"/api"}"""
        self.cursor.execute(configNew,[nameInsert,configinsert])
        self.conn.commit()
        
    def cursorClose(self):
        return self.cursor.close()
    def connClose(self):
        return self.conn.close()
    def getDataConfig(self):
        name = "Basic"
        ss = str(BasicConfig().getConfig())
        query = f"SELECT {ss} FROM public.configuration WHERE name='{name}'"
        self.cursor.execute(query)
        if(self.cursor.rowcount == 0):
            self.cursor.close()
            self.conn.close()
        row = self.cursor.fetchone()
        parse = json.loads(row[1])
        PreconfigModel = BasicConfig()
        PreconfigModel.parsing(parse)
        print(PreconfigModel.result())
# if __name__ == "__main__":
#     run = CreateDatabase()
#     run.createUser()
#     run.createMigrations()
#     run.createConfiguration()
#     run.getDataConfig()
#     run.cursorClose()
#     run.connClose