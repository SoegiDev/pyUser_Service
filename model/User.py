import bcrypt
class User():
    nm_id = "id"
    nm_firstname = "first_name"
    nm_lastname = "last_name"
    nm_email = "email"
    nm_username = "username"
    nm_password = "password"
    nm_email_confirmed = "email_confirmed"
    nm_job = "job"
    nm_bio = "bio"
    nm_phones = "phone"
    nm_avatar = "avatar"
    nm_added = "date_added"
    nm_created = "created_at"
    nm_updatedat = "updated_at"
    nm_unique_id = "unique_id"
    nm_public = "public_id"
    nm_deleted = "deleted"
    nm_identity = "identity_card"
    
    id = None
    public_id = None
    unique_id = None
    email =None
    username = None
    password = None
    firstname = None
    lastname = None
    created = None
    updated =None
    added = None
    deleted = False
    identity = None
    phone = None
    avatar = None
    job =None
    bio = None
    email_confirmed =False
    
    def __init__(self):
        pass
    
    def set_id (self,fname):
        self.id = fname
    def set_first_name(self, fname):
        self.firstname = fname
    def set_last_name(self, fname):
        self.lastname = fname
    def set_email(self, fname):
        self.email = fname
    def set_username(self, fname):
        self.username = fname
    def set_password(self, param):
        self.password = param
    def set_email_confirmed(self, fname):
        self.email_confirmed = fname
    def set_job(self, fname):
        self.job = fname
    def set_bio(self, fname):
        self.bio = fname
    def set_phone(self, fname):
        self.phone = fname
    def set_avatar(self, fname):
        self.avatar = fname
    def set_date_added(self, fname):
        self.added = fname
    def set_created(self, fname):
        self.created = fname
    def set_updated(self, fname):
        self.updated = fname
    def set_unique_id(self, fname):
        self.unique_id = fname
    def set_public_id(self, fname):
        self.public_id = fname
    def set_deleted(self, fname):
        self.deleted = fname
    def set_identity_card(self, fname):
        self.identity = fname

        
    def __repr__(self):
        return repr(self.__dict__)
    
    def checkPassword(self, password: str)->bool:
        ''' Check if the provided password is equal to user password '''
        return bcrypt.checkpw(bytes(password, 'utf-8'), self.password)

    def set_pw(self, password: str):
        '''
        Set current user passowed.

        password is hashed first before getting assigned to user
        '''
        self.password = bcrypt.hashpw(
            bytes(password, 'utf-8'), bcrypt.gensalt(12))
    def format_login(self):
       return {
        "id": self.id,
        "public_id": self.public_id,
        "unique_id": self.unique_id,
        "email": self.email,
        "username":self.username
        }