# Desafio CIID
  <p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="100" src="https://vuejs.org/images/logo.png" alt="Vue logo"></a></p>
<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="100" src="https://pbs.twimg.com/profile_images/1417542931209199621/fWMEIB5j_400x400.jpg" alt="Vue logo"></a></p>

BIenvenido al repositorio del desafio de personas y provincias(BACKEND), desarrollado con vuejs y fastApi.

## Recomendaciones de Instalacion

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and desactivar Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Creacion de un entorno virtual

Para ejecutar este proyecto , opcionalmente se puede usar un entorno virtual,para no instalar de manera global todas la dependencias del proyecto.
El comando para crear es:

```sh
py -m venv nombredelentorno
```
Luego, antes de instalar las dependencias hay entrar en el entorno con el siguiente comando:

```sh
source ./nombredelentorno/bin/activate
```
Sabremos que el entorno esta activado cuando nos muestra de la siguiente manera: 

Por ejemplo (venv) PS C:\develorp\CIID\Desafio-Ciid\backend>

Luego una vez dentro del entorno, podremos instalar las dependencias.


## Configuracion del proyecto

Ademas del VsCode ,se requeriran las siguientes dependencias con sus respectivas versiones:

    anyio==3.6.2
    cffi==1.15.1
    click==8.1.3
    colorama==0.4.6
    cryptography==39.0.0
    fastapi==0.88.0
    greenlet==2.0.1
    h11==0.14.0
    idna==3.4
    MarkupSafe==2.1.1
    mysql-connector-python==8.0.31
    mysqlclient==2.1.1
    protobuf==3.20.1
    pycparser==2.21
    pydantic==1.10.4
    PyJWT==2.6.0
    PyMySQL==1.0.2
    sniffio==1.3.0
    SQLAlchemy==1.4.46
    starlette==0.22.0
    typing_extensions==4.4.0
    uvicorn==0.20.0
    Werkzeug==2.2.2


### Como descargar las versiones


```sh
Se instala con el comando pip install dependencia===version
Por ejemplo: pip install SomePackage==1.0.4   

```


### Base de datos

Sera necesario tener un gestor de base de datos, para ello se debera crear una base de datos llamada logincat.En caso de querer otro nombre, se debe revisar la linea :
engine = create_engine("mysql+pymysql://root:@localhost:3306/logincat")  , ubicada en el archivo db.py en donde ademas del usuario, debera controlar el puerto que se usa.


### Compilacion del proyecto

Una vez instalado todo , se procede a dar de alta el servideo con el comando: 
```sh
uvicorn main:app --reload
```

El siguiente paso sera pasar al frontend.








