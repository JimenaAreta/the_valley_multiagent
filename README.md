
# Proyecto Agno Playground con Agentes Especializados

Este proyecto es una implementación interactiva basada en Agno, integrando un conjunto de agentes especializados que realizan tareas específicas como planificación, análisis, investigación, edición y generación de contenido.

---

## 🚀 Objetivo del Proyecto

Proporcionar un entorno colaborativo con agentes automatizados para realizar tareas complejas mediante Inteligencia Artificial, facilitando su uso a través de una interfaz gráfica integrada.

---

## 📁 Estructura del Proyecto

```
.
├── agents/                     # Agentes especializados del proyecto
│   ├── __init__.py
│   ├── analyst.py              # Agente analista
│   ├── editor.py               # Agente editor
│   ├── planner.py              # Agente planificador
│   ├── researcher.py           # Agente investigador
│   ├── team.py                 # Coordinador de agentes
│   └── writer.py               # Agente redactor
│
├── agent-ui/                   # Interfaz de usuario personalizada (frontend)
├── playground.py               # Configuración principal del entorno Agno Playground
├── pyproject.toml              # Configuración del proyecto (dependencias y herramientas)
├── uv.lock                     # Archivo lock para dependencias (uv)
├── .env                        # Variables de entorno
├── .env.example                # Ejemplo de archivo de variables de entorno
├── .gitignore                  # Exclusión de archivos/directorios en git
└── README.md                   # Este archivo
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio:

```bash
git clone https://github.com/JimenaAreta/the_valley_multiagent.git
cd nombre_del_proyecto
```

### 2. Configurar entorno virtual con `uv`:

```bash
uv venv
source .venv/bin/activate - macos
sourve .venv\Scripts\activate - windows   
```

### 3. Instalar dependencias con `uv`:

```bash
uv pip install -r pyproject.toml
```

### 4. Configurar variables de entorno:

Crea el archivo `.env` tomando como referencia `.env.example`.

```env
OPENAI_API_KEY=tu_api_key
# otras variables según necesidades del proyecto
```

### 5. Ejecutar el proyecto localmente:

```bash
python playground.py
```

Una vez iniciado, visita la URL indicada en consola, usualmente:

```
http://127.0.0.1:8000
```

---

## 📌 Descripción de la carpeta `agents`

La carpeta `agents` contiene los agentes que conforman la inteligencia del proyecto:

- **`planner.py`**: Agente especializado en planificación estratégica.
- **`analyst.py`**: Realiza análisis profundo y crítico de información.
- **`researcher.py`**: Responsable de la búsqueda e investigación automatizada.
- **`editor.py`**: Mejora y corrige contenidos generados.
- **`writer.py`**: Genera contenido escrito original.
- **`team.py`**: Coordina y gestiona el trabajo en conjunto de todos los agentes.

---

## 🛠️ Tecnologías Utilizadas

- **Python**
- **Agno**
- **FastAPI**
- **OpenAI**
- **uv** (para gestión de dependencias y entorno virtual)
- **Dotenv**

---

## 📖 Documentación adicional

- [Agno Docs](https://github.com/agno-ai/agno)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [uv Docs](https://github.com/astral-sh/uv)
- [OpenAI API](https://platform.openai.com/docs/api-reference)

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, revisa el archivo `LICENSE`.

---

✨ **¡Disfruta desarrollando con Agno Playground!**
