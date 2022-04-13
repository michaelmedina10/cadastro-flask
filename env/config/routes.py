from controller.userController import UserRegister, Users, User, UserLogin, UserLogOut
class Routes:
    def setRoutes(api):
        api.add_resource(UserRegister, '/register')
        api.add_resource(UserLogin, '/login')
        api.add_resource(UserLogOut, '/logout')
        api.add_resource(Users, '/usuarios')
        api.add_resource(User, '/usuarios/<int:id>')