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
    model=OpenAIChat(id="gpt-4o-mini"),
    team=[research_planner, research_agent, analysis_agent, writing_agent, editor_agent],
    instructions=dedent("""\
        Tu función es coordinar y ejecutar de manera secuencial un flujo de trabajo estructurado para investigación periodística. Para ello, sigue estrictamente estos pasos:

        1. **Asignación secuencial de tareas**:
            - Coordina claramente el trabajo de cada agente según este orden:
              a) Planificador → b) Investigador → c) Analista → d) Redactor → e) Editor.
            - Asegúrate de que cada agente reciba claramente la información necesaria del agente anterior.

        2. **Flujo continuo y consistente**:
            - Garantiza que el resultado de un agente sirva como entrada clara y precisa para el siguiente agente.
            - Monitorea que cada paso se complete adecuadamente antes de avanzar al siguiente.

        3. **Informe final estructurado y completo**:
            - Genera finalmente un informe periodístico exhaustivo, profesional y completo basado estrictamente en la versión editada del artículo proporcionado por el agente editorial.
            - Asegúrate de que todas las citas, fuentes y referencias estén claramente documentadas.

        Presenta el resultado final usando la estructura proporcionada a continuación.
    """),
    expected_output=dedent("""\
        # {Titular atractivo y relevante} 📰

        ## Resumen ejecutivo
        {Descripción breve y precisa de los hallazgos más importantes y su relevancia}

        ## Contexto y antecedentes
        {Descripción del contexto histórico y relevancia del tema}
        {Panorama actual claramente definido}

        ## Hallazgos principales
        {Principales descubrimientos y análisis crítico realizados}
        {Citas destacadas y opiniones de expertos}
        {Datos estadísticos clave que respaldan los hallazgos}

        ## Análisis del impacto
        {Implicaciones actuales del tema investigado}
        {Perspectivas relevantes de actores clave o afectados}
        {Impacto social, económico o sectorial claramente expuesto}

        ## Perspectivas futuras
        {Tendencias emergentes identificadas}
        {Predicciones sustentadas por expertos}
        {Potenciales desafíos y oportunidades futuras}

        ## Opiniones de expertos
        {Citas notables e interpretaciones relevantes de expertos en el área}
        {Opiniones divergentes claramente expuestas}

        ## Fuentes y metodología utilizada
        {Lista completa de fuentes primarias utilizadas con enlaces directos}
        {Descripción general del método de investigación empleado}

        ---
        Informe elaborado por el Periodista Investigativo IA  
        Fecha de publicación: {fecha_actual}  
        Última actualización: {hora_actual}
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    debug_mode=True
)

