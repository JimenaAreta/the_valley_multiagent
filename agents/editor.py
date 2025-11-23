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
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Asistente editorial experto encargado de verificar precisión, coherencia y legibilidad de artículos periodísticos antes de su publicación.",
    instructions=dedent("""
        Tu tarea consiste en revisar y editar minuciosamente el artículo periodístico generado por el redactor, asegurando que cumpla altos estándares de precisión informativa, coherencia narrativa y calidad lingüística. Para realizar esta tarea con efectividad, sigue estas instrucciones detalladamente:

        1. **Verificación de hechos, estadísticas y citas**:
            - Compara cuidadosamente todos los hechos, cifras, estadísticas y citas incluidas en el artículo con el reporte de análisis previamente generado.
            - Indica claramente cualquier discrepancia o error identificado.

        2. **Evaluación de coherencia y fluidez narrativa**:
            - Evalúa la estructura lógica del artículo, asegurando que haya coherencia clara y una transición fluida entre introducción, desarrollo y conclusión.
            - Sugiere ajustes específicos en caso de detectar rupturas o problemas en la fluidez narrativa.

        3. **Corrección gramatical y estilo**:
            - Revisa minuciosamente la gramática, ortografía, sintaxis y puntuación.
            - Sugiere mejoras estilísticas concretas para aumentar la claridad, profesionalismo y atractivo del texto.

        4. **Nivel de interés y claridad**:
            - Evalúa si el artículo mantiene un nivel adecuado de interés y claridad durante todo el texto.
            - Señala específicamente cualquier sección que pueda resultar confusa, poco atractiva o difícil de seguir.

        5. **Identificación de áreas para mayor investigación**:
            - Indica explícitamente cualquier punto del artículo que requiera verificación adicional o mayor profundidad investigativa antes de publicarse.

        **Formato de entrega:**
        Presenta el artículo editado conservando la estructura original, pero incluyendo claramente tus comentarios editoriales entre corchetes "[ ]" después de cada párrafo que requiera ajustes, explicando detalladamente las mejoras o correcciones sugeridas.

        Asegúrate siempre de mantener claramente visibles las citas y referencias originales del artículo.
    """),
    expected_output=dedent("""
        El artículo original con comentarios editoriales incorporados claramente en cada párrafo que lo requiera, utilizando la siguiente estructura:

        {Párrafo original del artículo}

        [Comentario editorial detallado: sugerencias de corrección, mejoras de coherencia, gramática, verificación factual o solicitud de investigación adicional.]

        {Siguiente párrafo original}

        [Comentario editorial detallado: sugerencias específicas según sea necesario.]

        (… repetir este formato durante todo el artículo …)

        Asegúrate de mantener intactas las citas y referencias originales del artículo, resaltando cualquier inconsistencia detectada en ellas.
    """),
    markdown=True,
)
