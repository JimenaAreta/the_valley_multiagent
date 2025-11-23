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
    model=OpenAIChat(id="gpt-4o-mini", temperature=0.4),
    members=[
        research_planner,
        research_agent,
        analysis_agent,
        writing_agent,
        editor_agent,
    ],
    add_team_history_to_members=True,
    num_team_history_runs=3,        # o más si quieres, p.ej. 5
    tool_call_limit=10,              # corta bucles de herramientas
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

        🔴 Reglas específicas para el EDITOR:
        - Solo llames al miembro 'editor' cuando YA exista un artículo redactado en el historial.
        - Cuando delegues al 'editor', incluye SIEMPRE el texto completo del artículo en la tarea, por ejemplo:
          "Revisa y anota el siguiente artículo:\n\n<<<ARTÍCULO>>>\n\nDevuélvelo con comentarios editoriales en línea."
        - Si el editor responde pidiendo el texto del artículo, significa que no lo ha recibido.
          En ese caso NO vuelvas a llamarle de nuevo con la misma tarea.
          En lugar de eso, pide tú explícitamente el texto del artículo al usuario.

        El resultado que devuelva este equipo será un informe periodístico completo, claro y estructurado,
        listo para publicación, que incluya contexto, hallazgos, análisis de impacto, perspectivas futuras y fuentes.
    """),
    expected_output=dedent("""
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
    debug_mode=True
)
