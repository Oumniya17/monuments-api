# 🏛️ Monument API  
### 🌍 Gestión de monumentos con Django REST + JWT

---

## ✨ Descripción

**Monument API** es una API REST desarrollada con Django que permite gestionar monumentos históricos de una ciudad, incluyendo operaciones completas de CRUD, filtrado avanzado y autenticación segura mediante JWT.

> 🚀 Proyecto enfocado en buenas prácticas de desarrollo backend y arquitectura REST.

---

## 🧰 Tecnologías

- 🐍 Python
- 🎯 Django
- ⚡ Django REST Framework
- 🔐 JWT (SimpleJWT)
- 🔍 django-filter

---

## ⚙️ Funcionalidades principales

### 🏛️ CRUD de Monumentos

| Método | Endpoint | Descripción |
|--------|--------|------------|
| GET | `/api/monuments/` | Listar monumentos |
| GET | `/api/monuments/<id>/` | Obtener detalle |
| POST | `/api/monuments/` | Crear monumento |
| PUT | `/api/monuments/<id>/` | Actualizar |
| DELETE | `/api/monuments/<id>/` | Eliminar |

---

### 🔎 Filtros y ordenación

- 🔍 Búsqueda por nombre:
```

/api/monuments/?search=Coliseo

```

- 📊 Ordenación:
```

/api/monuments/?ordering=name
/api/monuments/?ordering=-year_built

```

- 📄 Paginación automática:
```

PAGE_SIZE = 5

````

---

### 🔐 Autenticación JWT

| Acción | Endpoint |
|------|--------|
| Registro | `/api/register` |
| Login | `/api/login` |
| Refresh | `/api/refresh` |

---

### 🧠 Token personalizado

El token JWT incluye:

```json
{
"username": "user1",
"email": "user1@test.com"
}
````

---

## 🚀 Instalación

```bash
# Clonar repositorio
git clone https://github.com/TU_USUARIO/monuments-api.git

cd monuments-api

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver
```

---

## 🧪 Uso

Accede a la API en:

```
http://127.0.0.1:8000/api/monuments/
```

Puedes interactuar directamente desde el navegador gracias a la interfaz de Django REST Framework.

---

## 🛡️ Seguridad

* Autenticación mediante JWT
* Tokens con información personalizada
* Preparado para proteger endpoints sensibles

---

## 📂 Estructura del proyecto

```
monuments-api/
│
├── monumentapp/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── monumentproject/
│   ├── settings.py
│   └── urls.py
│
├── requirements.txt
└── manage.py
```

---

## 🎯 Objetivo académico

Este proyecto forma parte de una práctica de desarrollo de API REST con Django, cumpliendo los siguientes requisitos:

* CRUD completo
* Paginación, filtrado y ordenación
* Autenticación JWT
* Token personalizado
* Gestión de dependencias

---

## 👨‍💻 Autor

<p align="center">
  <img src="https://github.com/user-attachments/assets/d549c019-35bb-4af8-8e61-8d6885c6cd9b" width="200">
</p>

**Oumniya Chahidi — Developer**<br>

Desarrollado como proyecto académico de backend con Django REST.

---

