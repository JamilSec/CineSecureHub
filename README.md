
![Logo](http://camarachp.cl/wp-content/uploads/2016/07/Logo-Cineplanet-1000x1000px-copia.png)

# CineSecureHub

CineSecureHub es un proyecto de encriptación y desencriptación de datos sensibles utilizando la lógica de una aplicación web para proteger la confidencialidad de la información. Este proyecto utiliza el algoritmo de encriptación AES (Advanced Encryption Standard) en modo CBC (Cipher Block Chaining) para garantizar la seguridad de los datos transmitidos.

## Características
- Encriptación de datos sensibles utilizando AES en modo CBC.
- Desencriptación segura de datos cifrados.
- Uso de claves y vectores de inicialización (IV) protegidos.
## Instalación
**1.-** Clona este repositorio en tu máquina local:
```bash
  $ git clone https://github.com/TU_USUARIO/CineSecureHub.git
```
**2.-** Asegúrate de tener Python 3.x instalado en tu sistema.

**3.-** Instala las dependencias requeridas:
```bash
  $ pip install -r requirements.txt
```
## Screenshots

- Desencriptación del payload de autenticación
![App Screenshot](https://i.ibb.co/XsC1Mqb/payload-Login.png)

- Desencriptación de la respuesta por parte del servidor
![App Screenshot]([https://i.ibb.co/n7TpVY9/informacion-User.png](https://i.ibb.co/n7TpVY9/informacion-User.png))
## Nota
La key de **encriptación** y el **iv** no estan puestas, ya que no pienso publicarlas.
