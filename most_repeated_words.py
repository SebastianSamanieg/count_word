from collections import defaultdict
import time

my_documents = [
    "La programación en Python es clave para el trabajo con datos",
    "Los programadores en Java tienen un alto interés en pasar a Python",
    "La optimización de algoritmos es fundamental en el desarrollo de software",
    "Las bases de datos relacionales son esenciales para muchas aplicaciones",
    "El paradigma de programación funcional gana popularidad",
    "La seguridad informática es un tema crucial en el desarrollo de aplicaciones web",
    "Los lenguajes de programación modernos ofrecen abstracciones poderosas",
    "La inteligencia artificial está transformando diversas industrias",
    "El aprendizaje automático es una rama clave de la ciencia de datos",
    "Las interfaces de usuario intuitivas mejoran la experiencia del usuario",
    "La calidad del código es esencial para mantener un proyecto exitoso",
    "La agilidad en el desarrollo de software permite adaptarse a cambios rápidamente",
    "Las pruebas automatizadas son cruciales para garantizar la estabilidad del software",
    "La modularización del código facilita la colaboración en equipos de programadores",
    "El control de versiones es necesario para rastrear cambios en el código",
    "La documentación clara es fundamental para que otros entiendan el código",
    "La programación orientada a objetos promueve la reutilización de código",
    "La resolución de problemas es una habilidad esencial en la programación",
    "La optimización prematura puede llevar a código complicado y difícil de mantener",
    "El diseño de interfaces de usuario atractivas mejora la usabilidad de las aplicaciones",
    "El código limpio es esencial para facilitar el mantenimiento",
    "Los patrones de diseño son soluciones probadas para problemas comunes",
    "Las pruebas unitarias garantizan el correcto funcionamiento de las partes del código",
    "El desarrollo ágil prioriza la entrega continua de valor al cliente",
    "Los comentarios en el código deben ser claros y útiles",
    "La recursividad es una técnica poderosa en la programación",
    "Las bibliotecas de código abierto aceleran el desarrollo de software",
    "La virtualización permite una mejor utilización de los recursos de hardware",
    "La seguridad en la programación web es fundamental para prevenir ataques",
    "Los principios SOLID son fundamentales para el diseño de software robusto",
    "La arquitectura de microservicios permite escalar componentes individualmente",
    "La refactorización mejora la calidad del código sin cambiar su comportamiento",
    "Los sistemas distribuidos presentan desafíos en la sincronización de datos",
    "El enfoque DevOps une el desarrollo y las operaciones para una entrega eficiente",
    "Las bases de datos NoSQL son útiles para manejar datos no estructurados",
    "La agilidad en el desarrollo permite adaptarse a cambios del mercado",
    "Las buenas prácticas en el control de versiones facilitan la colaboración",
    "La programación concurrente mejora la eficiencia en sistemas multiusuario",
    "Los marcos de trabajo MVC separan la lógica de la interfaz de usuario",
    "La interacción entre aplicaciones se logra a través de APIs",
    "El machine learning permite a las máquinas aprender de los datos",
    "La analítica de datos ayuda a tomar decisiones basadas en información",
    "El diseño responsivo garantiza una experiencia consistente en diferentes dispositivos",
    "Las pruebas de carga verifican el rendimiento de las aplicaciones",
    "El enfoque centrado en el usuario mejora la usabilidad de las aplicaciones",
    "La programación reactiva es útil para manejar flujos de datos asincrónicos",
    "Los contenedores facilitan la implementación y el despliegue de aplicaciones",
    "La gestión de dependencias es esencial para administrar las bibliotecas externas",
    "La integración continua automatiza la verificación de cambios en el código",
    "El aprendizaje profundo es una rama avanzada del machine learning",
    "La depuración es una habilidad crucial para encontrar y corregir errores",
    "La criptografía protege la información sensible en aplicaciones",
    "El desarrollo full-stack abarca tanto el frontend como el backend",
    "Las pruebas de seguridad ayudan a identificar vulnerabilidades en el software",
    "La agilidad cultural es clave para adoptar prácticas ágiles de manera efectiva",
    "La infraestructura como código permite automatizar la gestión de servidores",
    "Los patrones arquitectónicos guían la estructura general de una aplicación",
    "El análisis predictivo utiliza datos históricos para predecir tendencias",
    "Las interfaces API REST son ampliamente utilizadas para comunicarse con aplicaciones",
    "El rendimiento de las aplicaciones es esencial para brindar una buena experiencia",
    "La virtualización de servidores reduce costos y facilita la administración",
    "La ingeniería de software implica la aplicación de métodos sistemáticos",
    "El código autodocumentado es claro y fácil de entender para otros programadores",
    "La integración de sistemas conecta diferentes aplicaciones para trabajar juntas",
    "Las metodologías ágiles promueven la adaptación y la colaboración continua",
    "El monitoreo de aplicaciones permite identificar y resolver problemas en tiempo real",
    "El análisis de datos masivos (big data) abre oportunidades para obtener insights",
    "El diseño de interfaces de usuario es crucial para la experiencia del usuario",
    "La seguridad en el desarrollo es un proceso constante de mitigación de riesgos"
]


# Función para contar la frecuencia de palabras en un documento
def contar_palabras(documento):
    palabras = documento.split()
    frecuencias = defaultdict(int)
    for palabra in palabras:
        frecuencias[palabra] += 1
    return frecuencias


# Función principal para mostrar el ranking de palabras más repetidas
def ranking_palabras(documentos):
    # Iniciar temporizador
    start_time = time.time()

    # Diccionario para memoización de frecuencias de palabras por documento
    memo = {}
    # Diccionario para almacenar la frecuencia total de cada palabra en todos los documentos
    palabra_frecuencia = defaultdict(int)

    # Iterar a través de los documentos
    for documento in documentos:
        # Comprobar si las frecuencias del documento ya están calculadas
        if documento not in memo:
            # Si no, calcular las frecuencias y almacenarlas en memo
            memo[documento] = contar_palabras(documento)
        # Obtener las frecuencias del documento actual
        frecuencias_documento = memo[documento]

        # Actualizar la frecuencia total de las palabras
        for palabra, frecuencia in frecuencias_documento.items():
            palabra_frecuencia[palabra] += frecuencia

    # Detener temporizador
    end_time = time.time()

    # Calcular el tiempo de ejecución en segundos
    execution_time = end_time - start_time

    print(f"Tiempo de ejecución: {execution_time} segundos")

    # Ordenar las palabras por frecuencia en orden descendente
    ranking = sorted(palabra_frecuencia.items(), key=lambda x: x[1], reverse=True)

    return ranking


# Implementamos
ranking = ranking_palabras(my_documents)
for palabra, frecuencia in ranking:
    print(f"{palabra}: {frecuencia}")
