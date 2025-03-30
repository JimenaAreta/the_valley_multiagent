from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

"""
Agente: Investigador Experto (research_agent)

Este agente especializado tiene la función principal de llevar a cabo investigaciones profundas en la web, 
siguiendo un plan estructurado previamente generado. Su tarea incluye buscar información actualizada, verificar 
la credibilidad de fuentes seleccionadas, identificar actores relevantes y perspectivas diversas sobre un tema específico.

Atributos:
----------
model : OpenAIChat
    Modelo de lenguaje utilizado por el agente, específicamente GPT-4o.

tools : list
    Herramientas adicionales integradas al agente:
        - DuckDuckGoTools(): para ejecutar búsquedas profundas en la web y obtener resultados actualizados.

description : str
    Breve descripción del agente:
    "Investigador experto que realiza búsquedas profundas en la web y verifica fuentes relevantes."

instructions : str
    Conjunto detallado de instrucciones que indican paso a paso cómo debe llevar a cabo su proceso de investigación:
        1. Analizar y comprender el plan de investigación.
        2. Realizar búsquedas web profundas priorizando fuentes recientes y autorizadas.
        3. Seleccionar y verificar cuidadosamente la credibilidad de las fuentes encontradas.
        4. Identificar claramente actores clave y diversas perspectivas sobre cada subtema.
        5. Elaborar un informe estructurado y detallado conforme al formato requerido.

expected_output : str
    Plantilla estructurada en formato Markdown que especifica cómo debe ser presentado el informe final:
        - Título del informe y tema claramente indicado.
        - Hallazgos principales documentados detalladamente.
        - Análisis específico para cada fuente, incluyendo resúmenes, datos relevantes y citas textuales.
        - Tendencias generales y patrones observados entre fuentes.
        - Citación y referencia completa de cada fuente consultada.

markdown : bool
    Indica que la salida generada por el agente deberá presentarse utilizando formato Markdown.

show_tool_calls : bool
    Indica que se mostrarán explícitamente las llamadas realizadas por las herramientas integradas (DuckDuckGoTools).

add_datetime_to_instructions : bool
    Determina que la fecha y hora actual serán automáticamente añadidas a las instrucciones proporcionadas al agente 
    en cada ejecución, para garantizar precisión temporal del reporte generado.

Uso típico:
-----------
Este agente se utiliza inmediatamente después del agente de planificación (`research_planner`). Recibe una hoja 
de ruta estructurada y genera un informe completo, preciso y fundamentado sobre la investigación, proporcionando 
datos objetivos y contrastables.

Ejemplo de uso:
---------------
resultado = research_agent.run(plan_de_investigacion)

El resultado será un informe de investigación detallado, estructurado según la plantilla indicada, 
incluyendo fuentes confiables, hallazgos documentados y tendencias identificadas.

"""


# Luego úsala así:

research_agent = Agent(
    name="buscador_informacion",
    model=...,
    tools = ...,
    description="...",
    instructions=dedent("""
        ...
    """),
    expected_output=dedent("""
        ...
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)
