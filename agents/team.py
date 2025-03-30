from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat

from .planner import research_planner
from .researcher import research_agent
from .analyst import analysis_agent
from .writer import writing_agent
from .editor import editor_agent  

from . import editor
print(dir(editor)) 
"""
Agente: Equipo Periodístico Multi-agente (research_team)

Este agente actúa como coordinador general y responsable de ejecutar integralmente un flujo estructurado de investigación periodística profunda. Gestiona y coordina un equipo de sub-agentes especializados en planificación, investigación, análisis, redacción y edición, asegurando que cada etapa del proceso fluya eficazmente hacia la siguiente, culminando en un informe periodístico completo, riguroso y claramente estructurado.

Atributos:
----------
model : OpenAIChat
    Modelo GPT-4o, ideal para gestionar flujos de trabajo complejos con múltiples agentes.

name : str
    Identidad profesional del equipo:
    "Equipo periodístico multi-agente".

role : str
    Define claramente la función del agente en la coordinación del flujo de trabajo:
    "Ejecuta colaborativamente un flujo estructurado de investigación periodística profunda."

team : list
    Lista secuencial de agentes especializados gestionados:
        - research_planner: Planificador estratégico de la investigación.
        - research_agent: Investigador web profundo.
        - analysis_agent: Analista crítico del material investigado.
        - writing_agent: Redactor periodístico profesional.
        - editor_agent: Asistente editorial experto.

instructions : str
    Instrucciones claras sobre cómo gestionar el proceso:
        - Asignar tareas secuencialmente entre agentes.
        - Asegurar flujo de información consistente entre agentes.
        - Generar informe final completo basado en la edición final del artículo.
        - Garantizar la calidad y precisión de citas y referencias.

expected_output : str
    Formato detallado para la presentación del informe final, especificando claramente:
        - Titular atractivo.
        - Resumen ejecutivo.
        - Contexto histórico y panorama actual.
        - Principales hallazgos, citas y estadísticas.
        - Análisis claro del impacto.
        - Perspectivas futuras sustentadas por expertos.
        - Opiniones contrastantes de expertos.
        - Fuentes primarias claramente documentadas con enlaces.
        - Metodología general utilizada en la investigación.

markdown : bool
    Garantiza que el informe final esté estructurado en Markdown para claridad visual y organizativa.

show_tool_calls : bool
    Permite visibilizar explícitamente herramientas externas utilizadas durante la ejecución del flujo investigativo.

add_datetime_to_instructions : bool
    Incluye automáticamente fecha y hora actual en cada ejecución, aportando precisión temporal al informe generado.

Uso típico:
-----------
Este agente se emplea como coordinador general en procesos complejos de investigación periodística colaborativa, garantizando resultados consistentes, rigurosos y profesionales, listos para publicación inmediata.

Ejemplo de uso:
---------------
resultado = research_team.run("¿Qué impacto tienen las políticas económicas recientes en América Latina?")

El resultado será un informe completo, riguroso y estructurado sobre el tema consultado, elaborado colaborativamente por el equipo de agentes especializados, listo para su difusión pública inmediata.
"""


research_team = Agent(
    name="equipo_periodistico_multiagente",
    role="Ejecuta colaborativamente un flujo estructurado de investigación periodística profunda.",
    model=...,
    team=...,
    instructions=dedent("""
        ...
    """),
    expected_output=dedent("""...
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    debug_mode=True
)

