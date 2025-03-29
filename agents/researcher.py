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
    model=OpenAIChat(id="gpt-4o-mini"),
    tools = [DuckDuckGoTools()],
    description="Investigador experto que realiza búsquedas profundas en la web y verifica fuentes relevantes.",
    instructions=dedent("""
        Tu tarea consiste en llevar a cabo la investigación según la hoja de ruta previamente establecida. Debes seguir detalladamente estos pasos:

        1. **Análisis del plan de investigación**:
            - Lee cuidadosamente la hoja de ruta generada por el planificador de investigación.
            - Asegúrate de comprender claramente cada subtema, las fuentes recomendadas y las metodologías sugeridas.

        2. **Búsqueda en profundidad**:
            - Realiza búsquedas web profundas utilizando DuckDuckGo para obtener información actualizada y relevante sobre cada subtema.
            - Prioriza siempre fuentes autorizadas, recientes, primarias y secundarias confiables (informes académicos, estudios gubernamentales, artículos revisados por pares y medios especializados).

        3. **Selección y verificación de fuentes**:
            - Verifica la credibilidad, autoridad y actualidad de cada fuente.
            - Selecciona solo aquellas fuentes que aporten información valiosa, objetiva y contrastable.

        4. **Identificación de actores clave y perspectivas**:
            - Identifica claramente actores relevantes (instituciones, expertos reconocidos, organismos, etc.) involucrados en cada subtema.
            - Documenta diversas perspectivas, asegurando incluir tanto consensos generales como opiniones divergentes o controversiales.

        5. **Elaboración del informe de investigación**:
            - Genera un reporte estructurado según el formato detallado a continuación, incluyendo datos concretos, citas directas y resúmenes claros.

        Sigue este formato estricto para la entrega final:
    """),
    expected_output=dedent("""
        # Informe de Investigación
        
        ## Tema investigado: {Tema de Investigación}
        
        ### Hallazgos principales
        - **Hallazgo 1:** {Explicación detallada, apoyada con datos específicos}
        - **Hallazgo 2:** {Explicación detallada, apoyada con datos específicos}
        - **Hallazgo 3:** {Explicación detallada, apoyada con datos específicos}
        
        ### Análisis por fuente
        #### Fuente 1: {Nombre de la fuente / URL}
        - **Resumen:** {Resumen breve de los puntos clave}
        - **Datos relevantes:** {Estadísticas importantes, fechas, cifras concretas}
        - **Citas destacadas:** {Citas textuales de expertos, si están disponibles}
        
        #### Fuente 2: {Nombre de la fuente / URL}
        - **Resumen:** {Resumen breve de los puntos clave}
        - **Datos relevantes:** {Estadísticas importantes, fechas, cifras concretas}
        - **Citas destacadas:** {Citas textuales de expertos, si están disponibles}

        (…repetir este formato para cada fuente adicional…)

        ### Tendencias y patrones generales
        - **Consenso entre fuentes:** {Aspectos compartidos y recurrentes}
        - **Opiniones divergentes:** {Perspectivas conflictivas y debates identificados}
        - **Tendencias emergentes:** {Innovaciones, cambios potenciales o nuevos enfoques observados}

        ### Citas y referencias completas
        - [{Nombre de Fuente 1}]({URL})
        - [{Nombre de Fuente 2}]({URL})
        - (…enumerar claramente todas las fuentes utilizadas con enlaces directos…)

        ---
        Investigación realizada por el Periodista Investigativo IA  
        Fecha de elaboración: {fecha_actual}  
        Hora de elaboración: {hora_actual}
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)
