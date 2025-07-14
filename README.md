# 🛠️ Proyecto: CRUD con Django

Este repositorio contiene una investigación y una guía detallada sobre cómo desarrollar una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) utilizando el framework Django. Se abordan temas fundamentales como patrones de arquitectura, estructura de proyectos, flujo de datos, herramientas de Django y su panel de administración.

---

## 📌 1. ¿Qué es un CRUD y para qué sirve?

**CRUD** es el acrónimo de las operaciones básicas que toda aplicación web realiza sobre una base de datos:

| Operación | Acción | Método HTTP | Método Django (ORM) |
|-----------|--------|-------------|----------------------|
| Create    | Crear  | POST        | `Model.objects.create()` |
| Read      | Leer   | GET         | `Model.objects.get()` / `Model.objects.all()` |
| Update    | Actualizar | PUT/PATCH | `obj.save()` |
| Delete    | Eliminar | DELETE     | `obj.delete()` |

**Objetivo:** Permitir la gestión de datos de manera estructurada y segura entre el frontend y backend.

**Ejemplos de aplicaciones CRUD:**
- Redes sociales (Instagram, Facebook, BlueSky)
- Tableros de tareas (Trello, Jira, Odoo)

---

## 🧱 2. Patrones de arquitectura en desarrollo de software

###  ¿Qué son los patrones de arquitectura?

Son modelos que dividen una aplicación en componentes con responsabilidades claras, mejorando el mantenimiento, la escalabilidad y la reutilización.

---

###  ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?

El patrón **MVC** divide la lógica de una aplicación en tres componentes principales para **separar responsabilidades** de manera clara:

| Componente    | Responsabilidad                                                                 |
|---------------|----------------------------------------------------------------------------------|
| **Modelo**     | Gestiona los datos y la lógica del negocio. Accede y manipula la base de datos. |
| **Vista**      | Presenta los datos al usuario (HTML, JSON, interfaz gráfica, etc.).              |
| **Controlador**| Interpreta las peticiones del usuario, solicita datos al Modelo y muestra una Vista. |

#### 📈 Flujo típico de MVC:

```text
1. El usuario hace una petición (clic, URL, botón).
2. El Controlador interpreta esa petición.
3. Solicita datos al Modelo (leer, guardar, modificar).
4. Envía esos datos a la Vista.
5. La Vista genera la respuesta para el usuario.
```
---
### 🧩 ¿Qué es el patrón MVT (Modelo–Vista–Template)?

Django utiliza el patrón **MVT**, una variante del clásico patrón **MVC** (Modelo–Vista–Controlador), adaptada a su estructura interna. Aunque comparten el mismo objetivo (separación de responsabilidades), **Django renombra y organiza ligeramente los componentes**.

### 🧱 Comparación de Componentes: MVT vs MVC

| Componente MVT | Equivalente en MVC | Rol en Django                                                                 |
|----------------|--------------------|-------------------------------------------------------------------------------|
| **Modelo**      | Modelo              | Define la estructura y lógica de los datos. Usa el ORM de Django para comunicarse con la base de datos. |
| **Vista**       | Controlador         | Función o clase que procesa la solicitud HTTP, consulta el modelo y devuelve una respuesta. |
| **Template**    | Vista               | Archivo HTML que recibe datos de la vista y los presenta al usuario.         |

> ⚙️ **Nota:** Django automatiza parte del trabajo del “Controlador” tradicional. Por eso llama **Vista** a lo que en MVC se conoce como Controlador.

---
## 🔄 Diferencias clave entre MVC y MVT

Aunque tanto **MVC (Modelo–Vista–Controlador)** como **MVT (Modelo–Vista–Template)** buscan separar responsabilidades, Django adopta **MVT** con una estructura que automatiza parte del flujo tradicional.

### 📊 Comparación detallada

| **Aspecto**                     | **MVC**                                  | **MVT (Django)**                                                                |
|---------------------------------|------------------------------------------|---------------------------------------------------------------------------------|
| **Nombre de las piezas**        | Modelo, Vista, Controlador               | Modelo, Vista, Template                                                        |
| **Dónde va la lógica de negocio** | Modelo                                   | Modelo                                                                          |
| **Quién procesa la petición**   | Controlador                              | Vista (función o clase)                                                        |
| **Quién genera la salida final**| Vista (HTML, GUI, JSON, etc.)            | Template + motor de plantillas de Django                                       |
| **Quién maneja el enrutado**    | Normalmente el Controlador               | `urls.py` + la Vista                                                            |
| **Sensación para el desarrollador** | Escribes explícitamente Controlador y Vista | En muchos casos solo escribes Vistas y Templates; Django automatiza el flujo. |

---

### 🧠 Resumen
#### ¿Cual utiliza Django?
- Django utiliza el modelo MVT (Modelo–Vista–Template)**, una variante del clásico patrón MVC (Modelo–Vista–Controlador), adaptada para automatizar y simplificar el desarrollo web.
- En **ambos patrones**, los datos (Modelo), la lógica (Controlador/Vista) y la presentación (Vista/Template) están separados.
- Django **rebautiza** algunas piezas del patrón MVC:
  - Lo que en MVC sería el **Controlador**, en Django se llama **Vista**.
  - Lo que en MVC sería la **Vista**, en Django es un **Template**.
- El **motor de URLs y las vistas genéricas** permiten a Django actuar como un "mini-controlador" automático.

> ✅ **Conclusión**: MVT mantiene la separación de preocupaciones de MVC, pero hace que el flujo sea más directo y automatizado para el desarrollador.

---

## 📂 3. Estructura de un proyecto Django

Django organiza sus proyectos siguiendo la arquitectura **MVT (Modelo–Vista–Template)**. Cada componente cumple un rol específico para separar la lógica de negocio, la presentación y el manejo de peticiones.

---

### 📦 Estructura Básica
```plain text

mi_proyecto/
│
├── manage.py        # Script para comandos administrativos
├── mi_proyecto/     # Configuración general del proyecto
│ ├── settings.py    # Configuración del proyecto
│ ├── urls.py        # Enrutamiento global
│ └── ...
├── mi_aplicacion/   # Una "app" dentro del proyecto
│ ├── models.py      # Modelos (estructura de datos)
│ ├── views.py       # Vistas (lógica de respuesta)
│ ├── urls.py        # Enrutamiento local
│ ├── templates/     # Plantillas HTML
│ └── ...

```


---

### 🔍 Componentes Clave

| Componente     | Rol                                                                 |
|----------------|----------------------------------------------------------------------|
| **Modelos**     | Definen la estructura y el comportamiento de los datos. <br>Se crean en `models.py` usando clases de Python que representan tablas de la base de datos. |
| **Vistas**      | Procesan las peticiones del usuario. <br>Se definen en `views.py` como funciones o clases que consultan los modelos y devuelven una respuesta. |
| **Templates**   | Son archivos HTML que definen la presentación de los datos. <br>Utilizan el motor de plantillas de Django con etiquetas como `{% %}` y `{{ }}`. |
| **URLs**        | Asocian una ruta con una vista. <br>Se configuran en `urls.py`, permitiendo que Django sepa qué lógica ejecutar según la URL solicitada. |

---

### 🧩 ¿Cómo se conectan?

> 🔄 **Flujo típico de una petición en Django:**

1. El usuario hace una petición a una URL.
2. Django busca esa URL en `urls.py` y la asocia a una **vista**.
3. La vista consulta los **modelos** si necesita datos.
4. La vista devuelve una respuesta usando un **template** para mostrar los datos.
5. El navegador recibe la respuesta HTML final.

---

### 📝 Notas sobre templates

- `{% %}` → Se usa para lógica como condicionales o bucles.
- `{{ }}` → Se usa para mostrar valores de variables.

**Ejemplo:**
```html
{% if user.is_authenticated %}
  <p>Hola, {{ user.username }}!</p>
{% else %}
  <p>Bienvenido, visitante.</p>
{% endif %}
```
---

## 🔄 4. Flujo de Datos: De un Formulario HTML a la Base de Datos en Django

Cuando un usuario envía un formulario en una aplicación Django, los datos siguen un flujo específico que conecta el navegador con la base de datos mediante el backend.

### 📬 Flujo Paso a Paso

1. **Usuario llena el formulario en el navegador**  
   El formulario puede contener campos como nombre, correo, mensaje, etc.

2. **Formulario se envía mediante POST o GET**  
   Al hacer clic en "Enviar", los datos se envían al servidor a través del método especificado (`POST` normalmente).

3. **Vista en Django recibe la solicitud**  
   En `views.py`, una función o clase (`View`) recibe los datos. Esta vista valida, procesa y decide qué hacer con ellos.

4. **Validación y procesamiento de datos**  
   Se puede usar un formulario personalizado o un `ModelForm` para validar automáticamente según el modelo.

5. **Creación o modificación de un objeto del modelo**  
   Si los datos son válidos, se crea una instancia del modelo correspondiente (ej. `MiModelo(nombre="Ana", edad=25)`).

6. **Se guarda el objeto en la base de datos**  
   Con `.save()`, el objeto se almacena como un nuevo registro en la tabla correspondiente.

7. **Django responde con una nueva página o redirección**  
   Se puede mostrar un mensaje de éxito, redirigir al usuario o recargar la página.

---

### 💡 Ilustración Visual

```plaintext
[Navegador]
    ↓ (POST con datos del formulario)
[Vista en Django]
    ↓ (Valida y procesa los datos)
[Modelo]
    ↓ (.save())
[Base de datos]
    ↑
[Respuesta HTML o redirección]
```
---
## 🛠️ 5. Herramientas y Comandos de Django para Desarrollar un CRUD

Django incluye múltiples herramientas y comandos integrados que facilitan la creación de aplicaciones web con funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar).

### ⚙️ Comandos de Desarrollo

| Comando | Propósito |
|--------|-----------|
| `django-admin startproject nombre_proyecto` | Crea la estructura inicial de un proyecto Django. |
| `python manage.py startapp nombre_app` | Genera una nueva app dentro del proyecto. Aquí se define el CRUD. |
| `python manage.py makemigrations` | Crea archivos de migración basados en cambios en los modelos. |
| `python manage.py migrate` | Aplica las migraciones a la base de datos (crear o modificar tablas). |
| `python manage.py runserver` | Inicia el servidor de desarrollo local. |
| `python manage.py createsuperuser` | Crea un usuario administrador para acceder al panel de administración. |
| `python manage.py shell` | Abre una consola interactiva para ejecutar código y probar consultas. |

---

### 🧱 Componentes Esenciales para el CRUD

#### ✅ Model
Define la estructura de los datos. Cada modelo representa una tabla en la base de datos.

```python
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
```
### 📝 ModelForm
Genera formularios automáticamente a partir de un modelo, útil para crear y actualizar datos fácilmente.

```python
from django.forms import ModelForm

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']
```
### 🧑‍💻 Admin
Django genera un panel de administración funcional con solo registrar los modelos. Es una interfaz completa para operaciones CRUD sin necesidad de código adicional.

```python
from django.contrib import admin
from .models import Libro

admin.site.register(Libro)
```


### 🔁 Vistas Genéricas Basadas en Clases (CBV)

Django ofrece clases predefinidas que simplifican la implementación de operaciones CRUD. Estas vistas genéricas basadas en clases permiten crear funcionalidades completas con poco código.

| Clase        | Función                                  |
|--------------|-------------------------------------------|
| `ListView`   | Muestra una lista de objetos del modelo.  |
| `DetailView` | Muestra el detalle de un objeto específico. |
| `CreateView` | Permite crear nuevos objetos en la base de datos. |
| `UpdateView` | Permite modificar objetos existentes.     |
| `DeleteView` | Permite eliminar objetos de la base de datos. |

#### 🧩 Ejemplo de uso básico:

```python
from django.views.generic import ListView, CreateView
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = 'libros/lista.html'

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'autor']
    template_name = 'libros/crear.html'
    success_url = '/libros/'
```
---
## 🛡️ 6. ¿Cómo funciona el Admin de Django?

El **panel de administración de Django** es una interfaz web generada automáticamente a partir de los modelos del proyecto.  
Su propósito es permitir a administradores y editores **gestionar la base de datos sin escribir código**.

---

### ⚙️ ¿Cómo se construye?

#### 1. Usar modelos como base
Django toma las clases definidas en `models.py` como base para construir el panel.  
Cada clase representa una tabla de la base de datos y sus campos.

#### 2. Registrar el modelo en el panel
Para que un modelo aparezca en el panel, debes registrarlo en `admin.py`:

```python
# admin.py
from django.contrib import admin
from .models import MiModelo

admin.site.register(MiModelo)
```
#### 3. Crear un superusuario
Para acceder al panel de administración, necesitas un usuario con permisos especiales:
```
python manage.py createsuperuser
```
Luego accedes a la interfaz desde:
http://localhost:8000/admin

#### 4. Personalizar el panel
Puedes personalizar la visualización del modelo en el panel usando una clase ModelAdmin:

```python
# admin.py
@admin.register(MiModelo)
class MiModeloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')         # Campos mostrados en la lista
    search_fields = ('nombre',)                       # Habilita búsqueda por nombre
    list_filter = ('activo',)                         # Filtro por campo booleano
```
🧩 Características clave
- ✅ CRUD completo sin necesidad de programar vistas o formularios
- ✅ Interfaz intuitiva y amigable para administrar modelos
- ✅ Sistema de permisos: acceso solo para usuarios con rol staff
- ✅ Personalización de campos, filtros, orden y formularios
- ✅ Útil tanto para desarrollo como para la gestión de contenido en producción
---

## 👤 Autor

**Anthony Caceda**  
- Proyecto: CRUD con Django: https://github.com/Factoria-F5-madrid/proyecto-2-CRUD-Anthony_Caceda_Peralta
- Github: https://github.com/Anthonycpcode
