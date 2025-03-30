
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

### 🔸 Paso 1: Clonar el repositorio

```bash
git clone https://github.com/JimenaAreta/the_valley_multiagent.git
cd the_valley_multiagent
```

### 🔸 Paso 2: Configurar entorno virtual con `uv`

```bash
uv venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
```

### 🔸 Paso 3: Instalar dependencias con `uv`

```bash
uv pip install -r pyproject.toml
```

### 🔸 Paso 4: Configurar variables de entorno

Crea el archivo `.env` usando `.env.example` como referencia:

```env
OPENAI_API_KEY=tu_api_key
# otras variables según necesidades del proyecto
```

### 🔸 Paso 5: Ejecutar Agno Playground

Antes de configurar la interfaz Agent UI, es necesario tener funcionando Agno Playground (ir antes a la sección Agno Agent UI)

```bash
python playground.py
```

Una vez iniciado, visita la URL indicada en consola (usualmente):

```
http://127.0.0.1:8000
```

---

## 🔷 Agno Agent UI

Una moderna interfaz de chat construida con Next.js, Tailwind CSS y TypeScript. Esta plantilla permite interactuar fácilmente con los agentes Agno.

### 🚦 Instalación de Agent UI

#### 🔹 Instalación automática (recomendada)

Si no tienes instalado Node.js y npm:

Para Windows - descargar en:
https://nodejs.org

Para MacOs:
```bash
brew install node
```

Una vez instalado:

```bash
npx create-agent-ui@latest
```

Luego entra al directorio generado y ejecuta:

```bash
cd agent-ui npm run dev
```

Una vez iniciado, visita:

```
http://localhost:3000
```

---

✨ **¡Disfruta desarrollando con Agno Playground y Agent UI!**
