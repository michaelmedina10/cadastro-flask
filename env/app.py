from flask import Flask
from flask_restful import Api
from config.routes import Routes
from flask import jsonify
from config.token_config import ACCESS_EXPIRES
from config.blacklist import BLACKLIST
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
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
    db.init_app(app)
    app.run(debug=True, port=3000)