from flask_restful import Resource, reqparse
from model.userRepository import UsuarioRepository
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from config.blacklist import BLACKLIST
import bcrypt

attr = reqparse.RequestParser()
attr.add_argument('login', type=str, required=True)
attr.add_argument('email', type=str)
attr.add_argument('senha', type=str, required=True, help="Senha Field is required")

class UserRegister(Resource):
    @jwt_required()
    def post(self):
        data = attr.parse_args()
        try:
            if not data.get('login') or data.get('login') is None:
                return {'Message': 'Campo Login é Obrigatório'}, 400
            
            if not data.get('email') or data.get('email') is None:
                return {'Message': 'Campo E-mail é Obrigatório'}, 400
            
            if not data.get('senha') or data.get('senha') is None:
                return {'Message': 'Campo Senha é Obrigatório'}, 400
            
            if UsuarioRepository.getByEmail(data['email']):
                return {'Message': 'Usuário Já Cadastrado'}, 400
            
            data.senha = bcrypt.hashpw(data.senha.encode('utf8'), bcrypt.gensalt())
            user = UsuarioRepository(**data)
            UsuarioRepository.insert(user)
            return {'Message': f'Usuário {user.email} cadastrado com sucesso'}, 201
              
        except :
            UsuarioRepository.delete()
            return {'Message': 'Um erro interno ocorreu'}, 400
        
class UserLogin(Resource):
    def post(self):
        data = attr.parse_args()
        try:
            if not data.get('login') or data.get('login') is None:
                    return {'Message': 'Campo Login é Obrigatório'}, 400
            
            if not data.get('senha') or data.get('senha') is None:
                return {'Message': 'Campo Senha é Obrigatório'}, 400
            
            user = UsuarioRepository.getByLogin(data['login'])
            if not user:
                return {'Message': 'Usuário não encontrado'}, 404
            
            isMatch = bcrypt.hashpw(data.senha.encode('utf8'), user.senha) == user.senha
            if isMatch:
                access_token = create_access_token(identity=user.id)
                return {
                    "login": user.id,
                    "email": user.email,
                    "token": access_token
                }, 200
        except Exception as error:
            return {'Message': 'Erro ao efetuar login: {}'.format(error)}, 400

class UserLogOut(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLACKLIST.add(jti)
        return {'Message': 'Token de acesso revogado.'}, 200
        
class Users(Resource):
    def get(self):
        try:
            users = UsuarioRepository.findAll()
            return [user.json() for user in users], 200
        except :
            return {'Message': 'Erro ao Retornar todos os usuários'}, 400
        
class User(Resource):
    def get(self, id):
        try:
            user = UsuarioRepository.getById(id)
            if user:
                return user.json(), 200
            return {'Message': 'Usuario {} não encontrado.'.format(id)}, 400
        except :
            return {'Message': 'Erro ao consultar usuario.'}, 400
    
    @jwt_required()  
    def delete(self, id):
        try:
            user = UsuarioRepository.getById(id)
            if user:
                user.delete()
                return {'Message': 'Usuário {} deletado com sucesso.'.format(id)}, 200
            return {'Message': 'Usuario {} não encontrado.'.format(id)}, 400
        except :
            return {'Message': 'Usuario {} não encontrado.'.format(id)}, 400
