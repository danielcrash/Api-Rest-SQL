# Api-Rest-SQL

### Aplicação REST com interação de banco de dados SQL e segurança JWT.

É importante informar que o mesmo foi feito com auxílio da ferramenta [Postman](https://www.postman.com/downloads/), então é sugerido a mesma para execução.

Instale os requirements:
```sh
$ pip install -r requirements.txt
```
Após isso, para rodar a aplicação execute o comando:
```sh
$ python app.py 
```
Use o Postman com a url localhost exposto na porta ```5000```. Após isso, é necessário fazer o Login para ter acesso aos endpoints, o mesmo deve ser constituido por:
```
{
    "login": "<username>",
    "password": "<password>"
} 
```
Utilize o endpoint ```/register```para cadastrar seu login e em seguida realizar o mesmo através do endpoint ```/login```.
Caso tenha feito tudo corredo até aqui, você obterá o token de acesso como saída:
```
{
    "acess_token": "<hash_token>"
}
```
Finalmente para ter acesso aos demais endpoints da aplicação, basta preencher no seu Postman a aba ```Headers``` utilizando duas keys, uma como **key:** ```Content-Type:``` o **value:** ```application/json``` e outra como **key:** ```Authorization:``` com **value:** ```Bearer <hash_token>``` no qual foi adquirido no seu login. 

### Endpoints

- ```GET /users/<user_id>```: endpoint para obter todos os usuários

- ```DEL /users/<user_id>```: endpoint para obter um usuário

- ```GET /contacts/<contacts_id>```:  endpoint para trazer um novo usuário pelo ID.

- ```GET /contacts/```:  endpoint para trazer todos os usuários no banco.

- ```POST /contacts/<contact_id>```:  endpoint para cadastrar novo contato utilizando o ```<contact_id>``` no qual quer cadastrar com o seguinte formato json:
```
{
    "name": <name>,
    "channel": <channel>,
    "value": <value>,
    "obs": <obs>
}
```
- ```PUT /contacts/<contact_id>```:  endpoint para alterar contato utilizando o mesmo formato de json do ```POST```.

- ```DEL /contacts/<contact_id>```:  endpoint para deletar contato apenas referindo o ```<contact_id>``` no seu path.

### Banco de dados
Foi utilizado o banco SQLite com a biblioteca ```flask_sqlalchemy>``` no qual irá criar o banco dentro da pasta raiz da aplicação assim que registar seu primeiro login.

### Ferramentas

 - Linguagem: Python 3.7
 - Consumo da API: Postman
 - Biblioteca: Flask & SQLite

autor: Daniel Nicácio
