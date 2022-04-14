# cadastro-flask
Esta aplicação é simples, mas completa em relação a um backend feito em python, usando o mini-framework flask, e o ORM sqlalchemy. Com o Objetivo de fazer um CRUD de usuários, com direito a autenticação, login e logout, para isso foi usado a bibilioteca **flask_jwt_extended**  e para encriptar a senha cadastrada foi usado a biblioteca **flask-bcrypt**.

Também fiz uso de design patterns como MVC (No caso só o MC) e o padão repository para desacoplar código o tornando mais manutenível.
Estou usando a versão 3.6 do python para você que queira clonar esse projeto.

Caso você só queira testar o projeto, não precisa se preocupar com preparação de ambiente, versão de software etc..
Basta:
* Instalar o Docker caso você não tenha instalado
* copiar o arquivo **docker-compose.yaml** para qualquer pasta do seu computador
* Executar o comando **docker compose up**
* Para encerrar a aplicação basta pressionar as teclas  CTRL+C.
* Caso as teclas de atalho não funcione e o docker continue executando basta digitar no terminal **docker compose down**

![image](https://user-images.githubusercontent.com/68739172/163392411-844a9219-f0f2-47f9-9860-5bfc1d767bec.png)

Agora, caso você tenha o postman ou qualquer outro software para fazer requisições, basta abrir e usar a URL: **http://localhost:3000**, OU, caso o docker compose já esteja rodando, clique ou cole as urls abaixo para visualizar os resultados no seu browser.

URL's dísponíveis:
* http://localhost:3000/usuarios - GET
* http://localhost:3000/usuarios/id - GET (ID será numérico e gerado automáticamente)
* http://localhost:3000/usuarios/id - DEL (Lembrando que precisa de autenticação para deletar ou registrar alguém)
* http://localhost:3000/register - POST
* http://localhost:3000/login - POST
* http://localhost:3000/logout - POST

Para autenticar faça o login com o seguinte usuário:
{
    "login": "testeLogin",
    "senha": "123456"
}

Será gerado um token:
![image](https://user-images.githubusercontent.com/68739172/163393733-27e60604-dacf-4c54-9d80-f728546d4c52.png)

Copie esse token e cole nas requisições para deletar e para registrar, na parte de **Headers**:
![image](https://user-images.githubusercontent.com/68739172/163393917-92a06f44-b3c6-417e-9e1f-b5100e6f8a44.png)

Não se esqueça de escrever Bearer antes de colar o token, Bearer significa "portador", ou seja, portador do token.
Obs. O token expira a cada 3 horas

Caso queira somente pegar a imagem criada, você pode acessar a página oficial do docker na qual fiz o upload da imagem do container:
https://hub.docker.com/repository/docker/medina10/flask_sqlalchemy_application
