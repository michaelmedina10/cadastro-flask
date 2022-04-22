from flask import Flask
from flask_restful import Api
from config.routes import Routes
from flask import jsonify
from config.token_config import ACCESS_EXPIRES
from config.blacklist import BLACKLIST
from sql_alchemy import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_user import UserManager
from model.userRepository import UsuarioRepository
from dotenv import load_dotenv
import os
load_dotenv('.env')



app_web = Flask(__name__)
app_web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
# Criando um banco de dados vazio para inicializar as migrations em um projeto existente
# app_web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app_web.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app_web.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app_web.config["JWT_BLACKLIST_ENABLED"] = True
app_web.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
# Flask User
app_web.config["USER_ENABLE_EMAIL"] = False
app_web.config["SECRET_KEY"] = "teste"
app_web.config["USER_ENABLE_CONFIRM_EMAIL"] = False
app_web.config["USER_ENABLE_USERNAME"] = False

api = Api(app_web)
jwt = JWTManager(app_web)
db.init_app(app_web)
migrate = Migrate(app_web, db)
 # Setup Flask-User and specify the User data-model
user_manager = UserManager(app_web, db, UsuarioRepository)

@app_web.before_first_request
def createDataBase():
    db.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
        return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'Message': 'Log Out feito com sucesso.'}), 401
Routes.setRoutes(api)

if __name__ == '__main__':
    from sql_alchemy import db
    # db.init_app(app_web)
    app_web.run(debug=True, port=3000, host='0.0.0.0')