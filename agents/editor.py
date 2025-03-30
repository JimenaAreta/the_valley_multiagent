from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat

"""
Agente: Asistente Editorial Experto (editor_agent)

Este agente cumple la función de asistente editorial profesional especializado en verificar y mejorar artículos periodísticos generados previamente. Su responsabilidad incluye asegurar precisión informativa, coherencia narrativa, corrección lingüística y claridad general del texto, proporcionando recomendaciones detalladas para ajustes antes de su publicación final.

Atributos:
----------
model : OpenAIChat
    Modelo GPT-4o, óptimo para edición detallada y precisa.

description : str
    Identidad profesional del agente:
    "Asistente editorial experto encargado de verificar precisión, coherencia y legibilidad de artículos periodísticos antes de su publicación."

instructions : str
    Instrucciones precisas y estructuradas sobre cómo llevar a cabo el proceso de edición del artículo:
        - Verificación rigurosa de hechos, estadísticas y citas.
        - Evaluación y mejora de coherencia narrativa y fluidez textual.
        - Revisión detallada de gramática, sintaxis, puntuación y estilo lingüístico.
        - Evaluación del nivel de claridad y atractivo del contenido.
        - Identificación clara de puntos que requieren mayor investigación o verificación adicional.
        - Formato específico de entrega: artículo original con comentarios editoriales claramente indicados.

expected_output : str
    Describe explícitamente cómo se espera recibir el artículo editado:
        - El artículo original preservado completamente.
        - Comentarios editoriales integrados claramente entre corchetes "[ ]" después de cada párrafo que requiera ajustes.
        - Explicaciones específicas y detalladas para cada sugerencia realizada.
        - Conservación explícita de citas y referencias originales con énfasis en correcciones o inconsistencias detectadas.

markdown : bool
    Asegura que la presentación final del artículo editado y comentarios editoriales utilicen formato Markdown, facilitando una revisión clara, organizada y visualmente atractiva.

show_tool_calls : bool
    Permite visualizar explícitamente cualquier herramienta adicional que haya sido utilizada durante el proceso editorial.

add_datetime_to_instructions : bool
    Incluye automáticamente fecha y hora actual en cada ejecución, proporcionando precisión temporal al proceso de edición.

Uso típico:
-----------
Este agente se utiliza como paso final antes de la publicación del artículo periodístico. Recibe un artículo previamente generado por el `writing_agent`, revisa detalladamente cada aspecto del texto, y devuelve una versión anotada con sugerencias explícitas que facilitan su mejora inmediata antes de la difusión pública.

Ejemplo de uso:
---------------
resultado = editor_agent.run(articulo_periodistico)

El resultado será un artículo completamente revisado con comentarios editoriales claros, específicos y prácticos, garantizando que el artículo final esté listo para publicación y cumpla altos estándares de calidad informativa, narrativa y lingüística.
"""

editor_agent = Agent(
    name="editor",
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
