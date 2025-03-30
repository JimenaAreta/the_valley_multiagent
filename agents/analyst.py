from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat

"""
Agente: Analista de Investigación (analysis_agent)

Este agente está especializado en realizar análisis críticos y detallados sobre informes de investigación previamente generados. Su objetivo es identificar patrones relevantes, evaluar perspectivas diversas, detectar posibles inconsistencias, y verificar la credibilidad de todas las fuentes utilizadas, generando finalmente un informe completo y fundamentado.

Atributos:
----------
model : OpenAIChat
    Modelo de lenguaje (GPT-4o) utilizado por el agente para llevar a cabo análisis profundos y detallados.

description : str
    Breve descripción del propósito del agente:
    "Analista de datos especializado en identificar patrones, evaluar perspectivas y detectar inconsistencias en investigaciones complejas."

instructions : str
    Instrucciones claramente estructuradas que guían el proceso analítico del agente, incluyendo:
        - Identificación y documentación de patrones y tendencias.
        - Evaluación crítica de las diferentes perspectivas.
        - Detección y aclaración de inconsistencias.
        - Evaluación minuciosa y crítica de la credibilidad de las fuentes utilizadas.
        - Elaboración de una síntesis fundamentada en datos estadísticos y contextuales.

expected_output : str
    Define claramente cómo debe ser el reporte de análisis crítico final, incluyendo:
        - Resumen ejecutivo claro del análisis.
        - Identificación detallada de patrones y tendencias.
        - Evaluación crítica de perspectivas documentadas.
        - Inconsistencias detectadas con recomendaciones específicas.
        - Evaluación rigurosa de fuentes.
        - Conclusiones respaldadas estadísticamente y con contexto adecuado.
        - Citación completa y clara según estándares académicos y profesionales.

markdown : bool
    Determina que el reporte generado debe utilizar formato Markdown, facilitando claridad, estructura y presentación visual.

show_tool_calls : bool
    Permite visualizar explícitamente cualquier herramienta adicional que el agente haya utilizado durante el análisis.

add_datetime_to_instructions : bool
    Garantiza que la fecha y hora actual sean incluidas automáticamente en cada ejecución, añadiendo precisión temporal al reporte analítico.

Uso típico:
-----------
Este agente se utiliza inmediatamente después del agente investigador (`research_agent`). Recibe un informe de investigación y genera un reporte analítico que facilita decisiones informadas sobre la calidad, fiabilidad y relevancia del material investigado.

Ejemplo de uso:
---------------
resultado = analysis_agent.run(informe_investigacion)

El resultado será un reporte crítico, detallado y claramente estructurado que facilitará una comprensión profunda, objetiva y precisa del tema investigado, sustentado por datos estadísticos, evaluaciones rigurosas y conclusiones bien fundamentadas.
"""

analysis_agent = Agent(
    name="analista_de_investigacion",
    model=...,
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
