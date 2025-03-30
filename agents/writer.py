from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat

"""
Agente: Redactor Periodístico Profesional (writing_agent)

Este agente cumple la función de redactor profesional especializado en artículos periodísticos investigativos. 
Basándose en un reporte analítico previo, produce artículos estructurados, equilibrados y claros, siguiendo un estilo narrativo similar al empleado por medios prestigiosos como el New York Times.

Atributos:
----------
model : OpenAIChat
    Modelo GPT-4o-mini, optimizado para redacción periodística clara, breve y atractiva.

description : str
    Identidad profesional del agente:
    "Periodista profesional especializado en redacción al estilo del New York Times, orientado a artículos investigativos claros y cautivadores."

instructions : str
    Instrucciones detalladas que guían la creación del artículo periodístico:
        - Define claramente la estructura narrativa (introducción, desarrollo, conclusión).
        - Enfatiza la necesidad de mantener integridad periodística, neutralidad y equilibrio.
        - Destaca la importancia del uso de un lenguaje claro, atractivo y accesible.
        - Señala la necesidad de incluir citas textuales de expertos y referencias claramente verificables.
        - Especifica el formato final utilizando Markdown.

markdown : bool
    Garantiza que la presentación final del artículo use formato Markdown, facilitando la claridad visual y estructural del contenido generado.

show_tool_calls : bool
    Permite visualizar cualquier llamada realizada por herramientas externas integradas durante la generación del artículo.

add_datetime_to_instructions : bool
    Asegura la inclusión automática de fecha y hora actual, otorgando precisión temporal al artículo generado.

Uso típico:
-----------
Este agente se utiliza después del análisis crítico (`analysis_agent`). Recibe un reporte de análisis y lo convierte en un artículo periodístico listo para publicación, asegurando precisión informativa, objetividad y claridad narrativa.

Ejemplo de uso:
---------------
resultado = writing_agent.run(reporte_analitico)

El resultado será un artículo periodístico estructurado, atractivo, informativo y profesional, adecuado para difusión inmediata en medios digitales o impresos, adaptado al estilo riguroso y cautivador característico del periodismo investigativo de alta calidad.
"""

writing_agent = Agent(
    name="escritor",
    model=...,
    description="...",
    instructions=dedent("""
        ...
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)
