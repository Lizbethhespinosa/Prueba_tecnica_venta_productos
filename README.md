# Prueba Técnica - Gestión de Productos

## Descripción

Este proyecto corresponde al desarrollo de una prueba técnica full stack para la gestión de productos, usuarios y compras.

La solución está compuesta por:

- **Backend** desarrollado con FastAPI
- **Frontend** desarrollado con React + Vite
- **Base de datos PostgreSQL local**
- **Docker** para contenerización del backend

La aplicación permite:

- Crear, consultar, actualizar y eliminar usuarios
- Crear, consultar, actualizar y eliminar productos
- Registrar compras asociando usuarios y productos
- Visualizar productos desde una interfaz web moderna
- Crear productos desde el frontend consumiendo la API REST

---

## Tecnologías Utilizadas

## Backend
-Python 3
-FastAPI
-SQLAlchemy
-PostgreSQL
-Pydantic
-Passlib
-Docker
-Uvicorn

## Frontend
-React
-Vite
-Bootstrap 5
-Axios
-React Router DOM
-HTML5
-CSS3

# Backend
## Funcionalidades Implementadas

## Usuarios

CRUD completo:
-Crear usuario
-Consultar usuarios
-Consultar usuario por ID
-Actualizar usuario
-Eliminar usuario

Campos:
-id
-nombre
-email
-password

Características:
-validación de email único
-hash seguro de contraseña con pbkdf2_sha256

## Productos

CRUD completo:
-Crear producto
-Consultar productos
-Consultar producto por ID
-Actualizar producto
-Eliminar producto

Campos:
-id
-nombre
-precio
-image_url

## Compras

Endpoint implementado:

-Registrar compra

Campos:
-usuario_id
-producto_id
-total_productos

## Configuración Backend
Variables de entorno

Archivo:
-backend/.env (SOLICITAR INFO BASE DE DATOS)

## Instalación Local

-Entrar al backend:
cd backend

-Crear entorno virtual:
python -m venv venv

-Activar entorno virtual:
Windows:
venv\Scripts\activate

Instalar dependencias:
pip install -r requirements.txt

Ejecutar servidor:
uvicorn app.main:app --reload

## Ejecución con Docker

-Entrar a backend:
cd backend

-Construir contenedor:
docker compose up --build

El backend quedará disponible en:
http://localhost:8000


# Frontend
Funcionalidades Implementadas

La interfaz web permite:

-Dashboard principal
-Navegación entre pantallas
-Formulario para registrar productos
-Visualización de productos en tarjetas
-Consumo de API REST mediante Axios

## Pantallas
Dashboard

Permite navegar a:
-Nuevo producto
-Listado de productos

## Crear Producto

Formulario con:
-nombre
-precio
-URL de imagen

Permite registrar nuevos productos consumiendo FastAPI.


## Productos

Visualización en formato cards mostrando:

-imagen
-nombre
-precio formateado

## Instalación Frontend

-Entrar a frontend:
cd frontend

-Instalar dependencias:
npm install

-Instalar librerías adicionales:
npm install bootstrap axios react-router-dom

-Ejecutar aplicación:
npm run dev

Disponible en:
http://localhost:5173

## Comunicación Frontend - Backend

Frontend consume la API REST del backend mediante Axios.

Endpoints utilizados:

GET /products
POST /products


## Seguridad Implementada
-Hash de contraseñas
-Validación de email único
-Separación por capas
-Manejo de esquemas con Pydantic
-ORM con SQLAlchemy


## Consideraciones Técnicas
-PostgreSQL se ejecuta localmente
-Docker contiene únicamente el backend
-El frontend se ejecuta localmente mediante Vite
-Arquitectura modular y escalable

# Arquitectura del Proyecto

```bash
proyecto/
│
├── backend/
│   ├── app/
│   │   ├── config/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── styles.css
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md

