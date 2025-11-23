# agents/team.py

from textwrap import dedent
from agno.team import Team
from agno.models.openai import OpenAIChat

from .planner import research_planner
from .researcher import research_agent
from .analyst import analysis_agent
from .writer import writing_agent
from .editor import editor_agent

research_team = Team(
    name="equipo_periodistico_multiagente",
    role="Ejecuta colaborativamente un flujo estructurado de investigación periodística profunda.",
    model=OpenAIChat(id="gpt-4o-mini", temperature=0),
    members=[
        research_planner,
        research_agent,
        analysis_agent,
        writing_agent,
        editor_agent,
    ],
    instructions=dedent("""
        Tu función es coordinar y ejecutar de manera secuencial un flujo de trabajo de investigación periodística.
        El orden lógico del flujo es:

        1) Planificador de investigación
        2) Investigador web
        3) Analista
        4) Redactor
        5) Editor

        Pautas de coordinación:
        - El resultado de cada agente debe ser la entrada del siguiente.
        - No saltes pasos ni mezcles roles: cada agente cumple su función específica.
        - Asegúrate de que el redactor trabaje sobre el informe analítico consolidado.
        - El editor recibe el artículo periodístico ya redactado y lo devuelve anotado.
        - El informe final que presente este equipo debe basarse en la versión editada del artículo.

        El resultado que devuelva este equipo será un informe periodístico completo, claro y estructurado,
        listo para publicación, que incluya contexto, hallazgos, análisis de impacto, perspectivas futuras y fuentes.
    """),
    expected_output=dedent("""
        # {Titular atractivo y relevante}

        ## Resumen ejecutivo
        {Descripción breve de los hallazgos principales y por qué son importantes.}

        ## Contexto y antecedentes
        {Descripción del contexto histórico y del origen del problema o tema.}
        {Panorama actual claramente definido.}

        ## Hallazgos principales
        {Principales descubrimientos respaldados por datos y fuentes.}
        {Citas destacadas y opiniones de expertos relevantes.}

        ## Análisis del impacto
        {Implicaciones actuales del tema investigado: sociales, económicas, políticas o sectoriales.}
        {Perspectivas de actores clave o grupos afectados.}

        ## Perspectivas futuras
        {Tendencias emergentes identificadas.}
        {Escenarios plausibles a medio y largo plazo, si procede.}
        {Principales riesgos y oportunidades.}

        ## Opiniones y debates
        {Resumen de las principales posiciones en conflicto, si las hay.}
        {Puntos de consenso y desacuerdo entre expertos o fuentes.}

        ## Fuentes y metodología
        {Listado de las fuentes primarias más relevantes, con breve descripción.}
        {Descripción general del enfoque metodológico seguido por el equipo.}

        ---
        Informe elaborado por el Equipo Periodístico Multiagente IA.
        Fecha de publicación: {fecha_actual}
        Última actualización: {hora_actual}
    """),
    markdown=True,
    debug_mode=True
)
