# engsoftware-pi-unifametro

### Requisitos
Verificar como instalar cada requisito no seu SO (Windows, Linux ou MacOS)
- Docker e Docker Compose
- Python 3.6+
- Virtualenv 20.4.3


### Instruções para rodar a API
Primeiro, instale o projeto e crie o ambiente virtual:
```
git clone https://github.com/IsaiasDimitri/engsoftware-pi-unifametro.git [NOME DO DIRETORIO]
cd [NOME DO DIRETORIO]
virtualenv -p python3 .env
```  
Agora, inicie o ambiente virtual. Caso esteja no Linux, rode
```
. .env/bin/activate #não esqueça do primeiro ponto, 'activate' é um executável.
```  
Caso esteja no Windows:
```
.env\Scripts\activate.bat
```  
Por ultimo, vamos criar o banco (sqlite3, por enquanto) e os containers e subi-los em http://localhost:8000:
```
python manage.py migrate  #criando o banco e a migração
docker-compose build  #demora um pouco, nao se assuste
docker-compose up
```  
Para derrubar o serviço, aperte CTRL+C.

### Usando a API
Ao acessar http://localhost:8000, você verá uma página com todas as requisições que pode fazer.
