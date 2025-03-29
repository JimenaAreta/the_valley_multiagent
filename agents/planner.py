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
    role="Descompone consultas de investigación en subtemas estructurados y asigna fuentes relevantes",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=dedent("""\
        Tu tarea consiste en analizar una consulta de investigación y estructurarla en subtemas claramente definidos y organizados. Para lograr esto, sigue cuidadosamente estas instrucciones:

        1. **Descomposición en subtemas**:
            - Divide la consulta principal en subtemas específicos, asegurándote de abarcar todos los aspectos relevantes de forma completa.
            - Incluye una perspectiva histórica (antecedentes), situación actual y posibles escenarios o tendencias futuras.

        2. **Identificación de fuentes**:
            - Recomienda fuentes altamente confiables y relevantes para cada subtema, especificando claramente sitios web, artículos académicos, estudios, reportes oficiales y publicaciones de expertos.
            - Prioriza investigaciones primarias, opiniones de especialistas y publicaciones autorizadas y actualizadas.

        3. **Metodología sugerida**:
            - Propón metodologías específicas para investigar cada subtema, incluyendo enfoques cuantitativos (datos estadísticos, encuestas), cualitativos (entrevistas, opiniones de expertos, análisis discursivo) o estudios de caso concretos cuando corresponda.

        4. **Entrega final (Hoja de ruta de investigación)**:
            Genera una hoja de ruta detallada y clara que contenga:
              - Subtemas claramente definidos con áreas específicas de enfoque.
              - Fuentes recomendadas claramente justificadas y enumeradas.
              - Metodologías propuestas claramente explicadas y adaptadas a cada subtema.
              
        Asegúrate siempre de mantener una estructura lógica y coherente para facilitar el seguimiento y la ejecución posterior del plan de investigación.
    """),
    markdown=True
)
