from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat

"""
Agente: Planificador de Investigación

Este agente se encarga de descomponer consultas de investigación generales en subtemas claros y estructurados, 
facilitando la organización lógica del proceso investigativo. Además, asigna fuentes relevantes y sugiere metodologías específicas adaptadas a cada subtema, generando finalmente una hoja de ruta detallada para guiar la investigación.

Atributos:
----------
name: str
    Identifica el nombre del agente, en este caso "Planificador de Investigación".

role: str
    Describe brevemente la función general del agente dentro del sistema:
    "Descompone consultas de investigación en subtemas estructurados y asigna fuentes relevantes".

model: OpenAIChat
    Modelo específico de lenguaje utilizado (GPT-4o) para la ejecución inteligente del agente.

instructions: str
    Instrucciones detalladas en formato Markdown que guían paso a paso al agente sobre cómo descomponer
    y organizar una consulta de investigación, cómo recomendar fuentes y metodologías, y cómo estructurar
    el resultado final.

Uso típico:
-----------
El agente se emplea cuando se desea transformar una consulta compleja o amplia en un plan de investigación bien estructurado, asegurando que se cubran integralmente los aspectos históricos, presentes y futuros del tema, además de identificar claramente las fuentes más relevantes y confiables junto con las metodologías óptimas para cada caso.

Ejemplo de uso:
---------------
resultado = research_planner.run("¿Qué efectos tienen las políticas económicas recientes en América Latina?")

El resultado será una hoja de ruta completa con subtemas definidos, fuentes recomendadas con justificación, y metodologías propuestas para llevar a cabo una investigación profunda y organizada sobre la consulta planteada.
"""

research_planner = Agent(
    name="planificador_investigacion",
    role="...",
    model=...,
    instructions=dedent("""...
    """),
    markdown=True
)
