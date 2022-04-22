from sql_alchemy import db
class UsuarioRepository(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key= True)
    login = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    senha = db.Column(db.String(80), nullable=False)
    roles = db.relationship('Role', secondary='user_roles')
     
    def __init__(self, login,  email, senha ):
        self.login = login
        self.email = email
        self.senha = senha
                
    def json(self):
        print([role for role in self.roles])
        return {
            "id": self.id,
            "login": self.login,
            "email": self.email,
        }
            
    @classmethod
    def getByEmail(cls, email):
        user = cls.query.filter_by(email = email).first()
        if user:
            return user
        return None
    
    @classmethod    
    def findAll(cls):
        users = cls.query.all()
        if users:
            return users
        return None
    
    
    @classmethod
    def getById(cls, user_id):
        user = cls.query.filter_by(id = user_id).first()
        if user:
            return user
        return None
    
    @classmethod
    def getByLogin(cls, login):
        user = cls.query.filter_by(login = login).first()
        if user:
            return user
        return None
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
 # Define the Role data-model
class Role (db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    def __init__(self, name):
        self.name = name

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
