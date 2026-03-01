---
wingwing_chapter: 9
wingwing_unit: "B"
unit_title: "VOR Navigation"
faa_sources: ['PHAK - Chapter 16 - Navigation.pdf']
estimated_read_time: 42
---

# Unidad B: Navegación VOR

Antes de que el GPS revolucionara la aviación, los pilotos navegaban vastas distancias utilizando una red de radiofaros terrestres que pintaban carreteras invisibles a través del cielo. El sistema VHF Omnidirectional Range (VOR) permanece como una de las herramientas de navegación más confiables de la aviación, proporcionando guía direccional precisa que ha guiado con seguridad millones de vuelos durante más de siete décadas. Comprender la navegación VOR es esencial para cada piloto, ya que sirve tanto como método de navegación primario como respaldo crítico cuando los sistemas modernos fallan.

## Objetivos de Aprendizaje

Después de completar esta unidad, usted será capaz de:

- Explicar los principios fundamentales de transmisión y recepción de señales VOR
- Operar el equipo VOR aerotransportado e interpretar con precisión las indicaciones de la presentación en cabina
- Aplicar los conceptos de radial y rumbo para determinar la posición de la aeronave en relación con las estaciones VOR
- Ejecutar procedimientos estándar de navegación VOR incluyendo identificación de estación y seguimiento de curso
- Demostrar técnicas prácticas de navegación VOR para interceptación de curso, seguimiento y paso de estación
- Utilizar sistemas VOR-DME para obtener fijaciones de posición precisas y navegar usando información de distancia
- Identificar las limitaciones del sistema VOR y compensar las fuentes de error comunes
- Realizar las verificaciones requeridas del sistema VOR y reconocer malfuncionamientos del equipo

---

## PRINCIPIOS Y FUNDAMENTOS DEL VOR

### Qué es el VOR y su papel en la radionavegación

**Very High Frequency Omnidirectional Range (VOR)** es un sistema de radionavegación terrestre que proporciona información precisa de marcación magnética a aeronaves equipadas con equipo receptor compatible. El sistema VOR representa una de las ayudas a la navegación más confiables y ampliamente utilizadas en la aviación, sirviendo como componente fundamental de la navegación tanto VFR como IFR.

La naturaleza **omnidireccional** del VOR significa que transmite señales de navegación en todas las direcciones desde la estación terrestre, creando 360 **radiales** individuales que se extienden hacia afuera como los rayos de una rueda. Cada radial representa una marcación magnética específica desde la estación, numerados del 001° al 360°, donde cada grado corresponde a una línea de marcación magnética que se extiende hacia afuera desde la instalación VOR.

El VOR desempeña un papel crucial en la radionavegación al proporcionar a los pilotos la capacidad de determinar su posición relativa a un punto de referencia terrestre conocido y navegar a lo largo de rutas precisas entre puntos de referencia. A diferencia del pilotaje, que se basa en la referencia visual a puntos de referencia, o la navegación a estima, que depende de cálculos de tiempo, velocidad y dirección, la navegación VOR ofrece precisión electrónica que permanece efectiva independientemente de las condiciones meteorológicas o limitaciones de visibilidad.

El sistema habilita tres funciones primarias de navegación: fijación de posición, guía de rumbo e identificación de paso sobre la estación. Los pilotos pueden determinar en qué radial se encuentran, seguir un rumbo de entrada o salida de una estación, e identificar cuándo pasan sobre la instalación. Esta capacidad hace que el VOR sea particularmente valioso para la navegación de travesía, procedimientos de aproximación y mantenimiento de trayectorias de vuelo precisas en espacio aéreo controlado.

> **Integración de Navegación**: El VOR sirve como piedra angular del National Airspace System, proporcionando la base para muchos procedimientos de aproximación por instrumentos, aerovías y fijos de navegación utilizados en operaciones de vuelo tanto VFR como IFR.

### Bandas de frecuencia VOR e identificación de estaciones

Las estaciones terrestres VOR operan dentro de la **banda de frecuencia VHF de 108.0 a 117.95 MHz**, con frecuencias asignadas en incrementos de 0.05 MHz (50 kHz). Esta asignación de frecuencia coloca al VOR en el espectro de Very High Frequency, que proporciona varias ventajas operacionales incluyendo resistencia a interferencias atmosféricas y transmisión de señal relativamente clara.

La banda de frecuencia VHF es compartida con otros sistemas de navegación aérea, con rangos de frecuencia específicos designados para diferentes propósitos. Las frecuencias de 108.0 a 111.95 MHz pueden estar emparejadas con frecuencias de localizador del Instrument Landing System (ILS), mientras que el rango de 112.0 a 117.95 MHz se usa exclusivamente para operaciones VOR.

La **identificación de estación** se logra mediante dos métodos primarios: **identificación en código Morse** e **identificación por voz**. Cada estación VOR transmite un identificador único de tres letras en código Morse internacional al menos una vez cada 30 segundos. Esta identificación codificada típicamente consiste en dos o tres letras que corresponden a la ubicación o nombre de la estación. Por ejemplo, el VOR de Oklahoma City podría transmitir "OKC" en código Morse.

Muchas estaciones VOR también proporcionan identificación por voz, donde un anuncio grabado indica el nombre de la estación seguido de la palabra "VOR". Esta identificación por voz hace que la verificación de la estación sea más accesible para pilotos que pueden no ser competentes en la interpretación del código Morse. Sin embargo, los pilotos no deben depender únicamente de transmisiones de voz para una identificación positiva, ya que las Flight Service Stations frecuentemente transmiten mensajes de voz sobre múltiples frecuencias VOR, potencialmente causando confusión.

Los **procedimientos críticos de identificación** requieren que los pilotos identifiquen positivamente cada estación VOR antes de usarla para navegación. Cuando una estación VOR está fuera de servicio por mantenimiento o calibración, la identificación en código Morse se remueve de la transmisión. Esta ausencia de identificación sirve como advertencia clara a los pilotos de que la estación no debe ser usada para propósitos de navegación.

Las Flight Service Stations transmiten frecuentemente información meteorológica, NOTAMs y otros datos operacionales sobre frecuencias VOR. Aunque estas transmisiones proporcionan información valiosa, no constituyen identificación positiva de la estación y no deben usarse como medio primario para confirmar la instalación VOR correcta.

> **Ayuda Memoria**: El mnemotécnico "Very High Frequency - Very Helpful Flying" puede ayudar a recordar que el VOR opera en la banda VHF y proporciona asistencia de navegación esencial.

### Componentes básicos y operación de estaciones terrestres VOR

Las estaciones terrestres VOR consisten en varios componentes críticos trabajando juntos para generar y transmitir señales de navegación omnidireccionales precisas. El **transmisor primario** genera la onda portadora en la frecuencia asignada y la modula con la información de navegación que los receptores de aeronaves decodifican para determinar información de marcación.

El **sistema de antena** representa el componente más visible y crucial de una instalación VOR. El arreglo de antena típicamente consiste en una antena central rodeada por una disposición circular de antenas más pequeñas, frecuentemente llamada **contrapeso**. Esta configuración crea el patrón de señal rotatoria que permite a las aeronaves determinar su posición radial relativa a la estación.

Las estaciones VOR emplean dos métodos distintos de transmisión de señal: **Conventional VOR (CVOR)** y **Doppler VOR (DVOR)**. Las estaciones CVOR usan un sistema de antena mecánicamente rotatoria o arreglos de antenas conmutadas electrónicamente para crear la señal de referencia rotatoria. El sistema de antena rota físicamente a 1,800 revoluciones por minuto (30 Hz), creando la señal de fase variable que los receptores de aeronaves interpretan como información de marcación.

Las estaciones DVOR utilizan el principio del efecto Doppler, empleando un arreglo circular de típicamente 48 a 50 antenas fijas dispuestas alrededor de una antena de referencia central. La conmutación electrónica activa secuencialmente estas antenas en un patrón rotatorio, creando una fuente de señal aparente que se mueve en un círculo a 30 Hz. Esto crea la misma información de navegación que CVOR pero con precisión mejorada y requisitos de mantenimiento reducidos.

Los **sistemas monitores** verifican continuamente la precisión y operación del equipo terrestre VOR. Estos sistemas automatizados verifican la fuerza de la señal, estabilidad de frecuencia, precisión de rumbo y transmisión de identificación. Si algún parámetro excede las tolerancias aceptables, el sistema monitor automáticamente remueve la señal de identificación de la estación y puede apagar completamente el transmisor.

La **potencia de salida** de las estaciones VOR varía según su clasificación y área de servicio prevista. Los VOR terminales típicamente operan a niveles de potencia más bajos (200-2000 watts), mientras que los VOR de alta altitud pueden transmitir con niveles de potencia hasta 2000 watts o más. La potencia radiada efectiva determina el volumen de servicio de la estación y el alcance operacional a varias altitudes.

Los **sistemas de energía de respaldo** aseguran operación continua durante fallas de energía comercial. La mayoría de las instalaciones VOR incluyen generadores de emergencia o sistemas de respaldo de batería que se activan automáticamente cuando se interrumpe la energía primaria, manteniendo servicios de navegación para operaciones de aeronaves.

> **Nota Técnica**: Las instalaciones VOR modernas frecuentemente incorporan capacidades de monitoreo remoto, permitiendo a los técnicos verificar la operación de la estación y parámetros de rendimiento desde ubicaciones distantes, mejorando la eficiencia de mantenimiento y confiabilidad del servicio.

### Principios de transmisión de señal VOR y cobertura

La transmisión de señal VOR opera en el principio de **comparación de fase** entre dos señales de referencia distintas de 30 Hz transmitidas simultáneamente desde la estación terrestre. Comprender este principio es esencial para que los pilotos utilicen efectivamente la navegación VOR y reconozcan las limitaciones del sistema.

La **señal de referencia** permanece constante en fase independientemente de la posición de la aeronave relativa a la estación VOR. Esta señal es modulada en frecuencia sobre una subportadora de 9960 Hz, que luego es modulada en amplitud sobre la onda portadora VHF principal. La señal de referencia proporciona una línea base estable para cálculos de marcación.

La **señal variable** cambia la relación de fase mientras rota alrededor de la estación a 30 Hz (1800 RPM). Cuando esta señal rotatoria pasa a través del norte magnético relativo a la estación, se alinea exactamente en fase con la señal de referencia. A medida que la señal variable continúa rotando, progresivamente cambia la relación de fase con la señal de referencia a una tasa de 360° por revolución.

Los receptores VOR de aeronaves decodifican información de navegación al **comparar la diferencia de fase** entre estas dos señales. Cuando las señales variable y de referencia están exactamente en fase (diferencia de fase cero), la aeronave está posicionada en el radial de 360° (norte magnético desde la estación). A medida que la aeronave se mueve a diferentes posiciones radiales, la diferencia de fase cambia proporcionalmente, con cada grado de posición radial correspondiendo a un grado de diferencia de fase.

Las **limitaciones de línea de vista** afectan significativamente la cobertura VOR debido a las características de frecuencia VHF. Las señales VOR viajan en líneas rectas y no pueden doblarse alrededor de la curvatura de la Tierra o penetrar obstáculos de terreno significativos. Esta limitación significa que el alcance VOR aumenta con la altitud de la aeronave, siguiendo la fórmula del horizonte de radio.

A 1,000 pies AGL, el alcance típico de recepción VOR se extiende aproximadamente 40-45 millas náuticas bajo condiciones atmosféricas normales. Este alcance aumenta sustancialmente con la altitud: una aeronave a 10,000 pies AGL podría recibir señales VOR desde 120 millas náuticas o más, dependiendo del terreno y condiciones atmosféricas.

Los **volúmenes de servicio** se establecen para cada clasificación VOR para definir el espacio aéreo dentro del cual se garantizan señales de navegación confiables. Estos volúmenes se definen por rangos específicos de altitud y distancias desde la estación, teniendo en cuenta el enmascaramiento del terreno, requisitos de fuerza de señal y estándares de precisión.

El blindaje del terreno puede crear **zonas muertas** donde las señales VOR son bloqueadas por montañas, colinas u otras obstrucciones. Estas áreas pueden existir incluso dentro del volumen de servicio publicado, particularmente en regiones montañosas. Los pilotos deben ser conscientes de que la recepción VOR puede ser poco confiable o completamente no disponible en áreas enmascaradas por el terreno.

Las **condiciones atmosféricas** pueden afectar la propagación de señal VOR, particularmente durante períodos de propagación anómala o canalización atmosférica. Estas condiciones pueden causar que las señales sean recibidas a distancias más allá del alcance normal pero con precisión reducida. Por el contrario, estática por precipitación, tormentas eléctricas u otros fenómenos meteorológicos pueden degradar la calidad de recepción de la señal.

La **referencia magnética** para todos los radiales VOR se establece durante la calibración de la estación y permanece fija relativa al norte magnético en la ubicación de la estación. Sin embargo, los pilotos deben recordar que la variación magnética cambia a través de áreas geográficas, por lo que la marcación magnética a una estación VOR desde la posición de la aeronave puede diferir del radial en el que está la aeronave debido a la convergencia de meridianos magnéticos.

> **Planificación de Cobertura**: Al planificar navegación VOR, los pilotos deben considerar que existe cobertura efectiva dentro de los volúmenes de servicio publicados, pero la recepción real puede extenderse más allá de estos límites a altitudes más altas. Sin embargo, la precisión de navegación puede degradarse a rangos extendidos, haciendo aconsejables métodos de navegación de respaldo.

---

## EQUIPOS Y PANTALLAS VOR A BORDO

El sistema de navegación VOR requiere equipos sofisticados a bordo para recibir e interpretar señales de estaciones VOR terrestres. Comprender la operación y el uso adecuado de este equipo es esencial para una navegación VOR precisa. Los componentes principales trabajan en conjunto para proporcionar orientación precisa de rumbo e información de distancia a los pilotos que vuelan bajo condiciones VFR e IFR.

Los receptores VOR modernos se integran perfectamente con la instrumentación de la aeronave para mostrar información de navegación en formatos que son intuitivos y fáciles de interpretar durante las operaciones de vuelo. La confiabilidad y precisión del sistema lo han convertido en una piedra angular de la radionavegación durante décadas.

### Componentes y Controles del Receptor VOR

El **receptor VOR** es el corazón del sistema de navegación VOR a bordo. Esta unidad recibe señales VHF transmitidas en frecuencias entre 108.0 y 117.95 MHz desde estaciones VOR terrestres. El receptor debe estar sintonizado y operado correctamente para asegurar información de navegación precisa.

La **selección de frecuencia** se realiza mediante un control de sintonización que permite a los pilotos seleccionar la frecuencia deseada de la estación VOR. La mayoría de los receptores modernos muestran la frecuencia seleccionada digitalmente, aunque las unidades más antiguas pueden usar pantallas analógicas. La frecuencia debe seleccionarse cuidadosamente y verificarse contra las cartas actuales, ya que la selección incorrecta de frecuencia es una fuente común de errores de navegación.

El **control de volumen** ajusta el nivel de audio para la identificación de la estación VOR. Este control es crítico porque se requiere una identificación positiva de la estación mediante código Morse o anuncio de voz antes de usar cualquier estación VOR para navegación. El volumen debe establecerse en un nivel que permita una recepción clara de la señal de identificación sin interferir con otras comunicaciones en cabina.

Los **interruptores de encendido** controlan la operación del receptor y típicamente están integrados con el interruptor maestro de aviónica de la aeronave o controles individuales de equipos de navegación. Algunas instalaciones incluyen controles separados para diferentes funciones del receptor, permitiendo a los pilotos personalizar la configuración de su equipo según los requisitos de vuelo.

> **Verificación del Equipo**: Siempre verifique la operación adecuada del receptor VOR antes del vuelo sintonizando una estación cercana y confirmando identificación clara e indicaciones normales del instrumento.

Los receptores VOR modernos a menudo incluyen **indicadores de intensidad de señal** o **banderas de alarma** que alertan a los pilotos cuando las señales recibidas son demasiado débiles para una navegación confiable. Estos indicadores son esenciales para determinar cuándo la posición o altitud de la aeronave puede estar limitando la capacidad de recepción VOR.

### Operación del Selector Omnidireccional de Rumbo (OBS)

El **Selector Omnidireccional de Rumbo (OBS)** es un control giratorio que permite a los pilotos seleccionar cualquier curso magnético hacia o desde una estación VOR. También conocido como selector de curso, el OBS está calibrado en grados de 001° a 360°, representando todos los rumbos magnéticos posibles relativos a la estación VOR.

La **rotación del OBS** ajusta mecánica o electrónicamente la referencia contra la cual el receptor VOR compara las señales entrantes. Cuando el OBS se gira a un curso específico, el sistema determina la posición de la aeronave relativa a ese curso seleccionado. Esta operación fundamental permite a los pilotos interceptar y rastrear cualquier radial o curso deseado.

La **técnica de selección de curso** implica rotar el OBS hasta que el curso de entrada o salida deseado se muestre en la marca de índice superior. Por ejemplo, para rastrear el radial 090° saliendo de una estación VOR, el piloto rotaría el OBS hasta que 090° aparezca en el índice de curso. El curso recíproco (270°) aparecería automáticamente en la parte inferior del dial del OBS.

La **relación entre radiales y cursos** es crítica de entender. Un radial se extiende hacia afuera desde la estación VOR, mientras que un curso representa la dirección de vuelo prevista. Al volar hacia afuera en el radial 090°, la aeronave sigue un curso magnético de 090°. Al volar hacia la estación en la misma línea, la aeronave sigue un curso magnético de 270°, que es el recíproco del radial.

Las **configuraciones del OBS para diferentes tareas de navegación** varían según la operación prevista. Para intercepción de curso, el OBS debe establecerse al curso deseado antes de comenzar el procedimiento de intercepción. Para determinación de posición, el OBS se gira hasta que la aguja del Indicador de Desviación de Curso se centre, revelando la posición de la aeronave relativa a los radiales VOR.

> **Consejo de Navegación**: Siempre establezca el OBS al curso que pretende volar, no necesariamente al radial que está rastreando. Esto asegura una interpretación adecuada de la aguja y reduce la confusión durante la navegación.

### Interpretación del Indicador de Desviación de Curso (CDI)

La aguja del **Indicador de Desviación de Curso (CDI)** proporciona información de guía lateral relativa al curso VOR seleccionado. Comprender la operación e interpretación del CDI es fundamental para una navegación VOR exitosa. La aguja muestra la posición de la aeronave relativa a la línea central del curso deseado.

La **deflexión de la aguja del CDI** indica la dirección hacia el curso seleccionado, no la dirección para girar la aeronave. Cuando la aguja se desvía hacia la derecha, el curso seleccionado se encuentra a la derecha de la posición actual de la aeronave. Para interceptar el curso, el piloto debe volar hacia la dirección de la aguja, pero el rumbo de intercepción depende de factores que incluyen el ángulo de intercepción y las condiciones de viento.

La **sensibilidad del CDI** está estandarizada en todas las instalaciones VOR. La **deflexión de escala completa** ocurre cuando la aeronave está a 10° o más del curso seleccionado cuando se mide desde la estación VOR. Esta medición angular significa que el ancho del curso varía con la distancia desde la estación - a 60 millas náuticas de un VOR, la deflexión de escala completa representa aproximadamente 10 millas náuticas de desplazamiento lateral.

La **interpretación de puntos y deflexión** ayuda a los pilotos a comprender su posición relativa al curso deseado. Cada punto en la escala del CDI típicamente representa 2° de desviación de curso. A 60 millas náuticas de una estación VOR, cada punto representa aproximadamente 2 millas náuticas de desplazamiento lateral. Esta relación cambia proporcionalmente con la distancia desde la estación.

La **técnica de centrado del CDI** requiere que los pilotos vuelen rumbos que hagan que la aguja se mueva hacia el centro. Las correcciones pequeñas de rumbo son generalmente más efectivas que los cambios grandes de curso, especialmente cuando están cerca del curso deseado. El objetivo es lograr y mantener el centrado de la aguja del CDI mientras se establecen las correcciones apropiadas de deriva del viento.

Los **procedimientos de seguimiento de curso** implican usar el CDI para mantener el curso seleccionado. Cuando la aguja comienza a desviarse del centro, las correcciones prontas pero medidas ayudan a minimizar las desviaciones de curso. La sobrecorrección a menudo conduce a oscilación alrededor del curso deseado, resultando en navegación ineficiente y mayor tiempo de vuelo.

> **Nota de Precisión**: La sensibilidad del CDI permanece constante independientemente de la distancia de la aeronave desde la estación VOR, pero el ancho geográfico representado por cada grado de deflexión aumenta con la distancia.

### Indicaciones y Significados de la Bandera TO/FROM

La **bandera TO/FROM** proporciona información esencial sobre la relación entre la posición de la aeronave, el curso seleccionado y la ubicación de la estación VOR. Este indicador elimina la ambigüedad sobre si seguir el curso seleccionado conduce hacia o lejos de la estación.

La **indicación de bandera TO** aparece cuando el curso OBS seleccionado, si se intercepta y vuela correctamente, llevaría a la aeronave hacia la estación VOR. La bandera muestra que la aeronave está posicionada en el hemisferio opuesto al curso seleccionado relativo a la estación. Por ejemplo, si se selecciona 090° en el OBS y aparece una bandera TO, la aeronave está al oeste de la estación.

La **indicación de bandera FROM** muestra que seguir el curso seleccionado llevaría a la aeronave lejos de la estación VOR. Esto indica que la aeronave está posicionada en el mismo hemisferio que el curso seleccionado. Con 090° seleccionado y una indicación FROM mostrándose, la aeronave está al este de la estación y volaría más hacia el este al seguir el curso seleccionado.

Las **indicaciones ambiguas de bandera** ocurren en situaciones específicas que los pilotos deben reconocer. Cuando una aeronave pasa directamente sobre o muy cerca de una estación VOR, la bandera TO/FROM puede fluctuar o desaparecer completamente. Este **cono de confusión** típicamente se extiende desde la superficie hasta aproximadamente 3,000 pies sobre la estación, con el ancho del cono dependiendo de la altitud.

La **interpretación de bandera durante cambios de curso** requiere comprender cómo la indicación TO/FROM se relaciona con la posición de la aeronave en lugar del rumbo de la aeronave. La indicación de bandera depende únicamente de la posición geográfica de la aeronave relativa a la estación y al curso OBS seleccionado, independientemente de la dirección en que la aeronave esté volando realmente.

Los **sistemas de advertencia de bandera NAV** alertan a los pilotos cuando la intensidad de la señal VOR es insuficiente para una navegación confiable. La bandera NAV aparece cuando la aeronave está más allá del alcance utilizable de la estación, cuando la estación está fuera del aire, o cuando ocurre un mal funcionamiento del receptor. Esta bandera roja típicamente cubre o reemplaza la indicación TO/FROM, advirtiendo claramente que la información de navegación no es confiable.

Diferentes instalaciones de aeronaves pueden mostrar banderas de advertencia en varios formatos. Algunos sistemas usan banderas rojas que cubren la pantalla de navegación, mientras que otros usan anunciadores de advertencia separados o sistemas de advertencia integrados. Independientemente del método de visualización específico, los pilotos deben reconocer inmediatamente y responder apropiadamente a las indicaciones de bandera NAV.

> **Alerta de Seguridad**: Nunca intente navegación VOR cuando se muestren banderas de advertencia NAV. La información de navegación no es confiable y podría conducir a desviaciones peligrosas de curso o errores de posición.

Los **parámetros de deflexión de escala completa** definen los límites de operación del CDI. Cuando la aeronave está a más de 10° del curso seleccionado según se mide desde la estación VOR, la aguja del CDI alcanza deflexión de escala completa y permanece allí hasta que la aeronave regrese dentro del ancho total del curso de 20° (10° a cada lado de la línea central). Comprender estos parámetros ayuda a los pilotos a reconocer cuando están muy fuera del sobre de guía de curso y necesitan tomar acción correctiva para reestablecer el seguimiento adecuado del curso.

---

## RADIALES VOR Y CONCEPTOS DE MARCACIÓN

Comprender la relación entre **radiales** y **marcaciones** constituye la base de la navegación VOR precisa. Si bien estos términos a menudo son confundidos por pilotos principiantes, dominar sus significados y aplicaciones distintos es esencial para el posicionamiento preciso de la aeronave y el seguimiento de curso. La estructura de radiales de 360 grados del sistema VOR proporciona a los pilotos un marco de navegación integral que permite tanto la navegación simple punto a punto como técnicas complejas de fijación de posición.

### Comprendiendo Radiales vs Marcaciones

La distinción fundamental entre radiales y marcaciones radica en su referencia direccional y uso previsto. Un **radial** se define como una línea de curso magnético que se extiende hacia afuera DESDE una estación VOR. Piense en los radiales como rayos que irradian desde el centro de una rueda, con la estación VOR en el centro. Cada radial representa una marcación magnética específica DESDE la estación, numerados desde 001° hasta 360°.

Por el contrario, una **marcación** representa la dirección magnética HACIA una estación VOR desde la posición actual de la aeronave. Si una aeronave está ubicada en el radial 090° de una estación VOR, la marcación HACIA esa estación sería 270° (el recíproco del radial). Esta relación recíproca es constante: radial más marcación siempre es igual a 360° (o marcación más radial es igual a 360°).

Por ejemplo, si usted determina que está en el radial 045° DESDE la estación VOR ABC, su marcación magnética HACIA esa estación es 225°. Esta distinción se vuelve crítica durante la planificación y ejecución de la navegación, ya que seleccionar la referencia incorrecta puede conducir a errores de navegación de 180°.

> **Ayuda Memoria de Navegación**: Recuerde "Radiales Radian DESDE" - los radiales siempre se extienden hacia afuera desde la estación VOR, mientras que las marcaciones apuntan hacia la estación.

La aplicación práctica de este concepto aparece constantemente en la navegación VOR. Cuando se dirige HACIA una estación, los pilotos seleccionan la marcación de entrada en el OBS y siguen la guía del CDI. Cuando se dirige DESDE una estación, los pilotos seleccionan el radial deseado en el OBS y mantienen ese curso de salida.

### Sistema de Radiales Magnéticos (360 Radiales)

El sistema VOR transmite exactamente 360 radiales individuales, cada uno separado por un grado de marcación magnética. El **radial 000°** (también referenciado como el radial 360°) se extiende hacia el norte magnético desde la estación, mientras que el radial 180° se extiende hacia el sur magnético. Esta cobertura completa de 360 grados proporciona a los pilotos referencias direccionales precisas para cualquier curso deseado.

Cada radial mantiene su orientación magnética independientemente de los cambios en la variación magnética a través de regiones geográficas. El radial 090° de una estación VOR siempre se extiende hacia el este magnético desde esa estación, ya sea que la estación esté ubicada en un área de 10° de variación este o 15° de variación oeste. Esta consistencia simplifica los cálculos de navegación y asegura una guía de curso confiable.

El sistema de numeración de radiales sigue la convención estándar de la brújula, aumentando en sentido horario desde el norte magnético. El radial 090° apunta al este, 180° apunta al sur, 270° apunta al oeste, y 360°/000° apunta al norte. Los radiales intermedios proporcionan referencias direccionales precisas: el radial 045° se extiende hacia el noreste, el radial 225° se extiende hacia el suroeste, y así sucesivamente.

Comprender el espaciado de radiales se vuelve importante para la precisión de navegación. Los radiales adyacentes (como 090° y 091°) están separados por exactamente un grado. A una distancia de 60 millas náuticas de la estación, esta separación de un grado equivale a aproximadamente una milla náutica en tierra. Más cerca de la estación, los radiales convergen; más lejos, divergen proporcionalmente.

> **Nota de Precisión**: La precisión del radial VOR es generalmente dentro de ±1° bajo condiciones normales, proporcionando una excelente alineación de curso para la navegación de travesía.

La referencia magnética de los radiales VOR elimina la necesidad de correcciones de variación durante la navegación básica. Dado que los radiales ya están orientados al norte magnético, los pilotos pueden relacionar directamente las indicaciones VOR con los rumbos de brújula magnética y los cursos magnéticos trazados en cartas seccionales.

### Determinando la Posición de la Aeronave Usando VOR

Una sola estación VOR proporciona una línea de posición - el radial en el cual la aeronave está ubicada actualmente. Determinar este radial requiere el uso adecuado del sistema CDI y OBS. El procedimiento estándar implica rotar el OBS hasta que la aguja CDI se centre con una indicación FROM. La configuración del OBS en este punto indica el radial DESDE la estación.

Para encontrar su radial DESDE una estación VOR, primero sintonice e identifique la frecuencia VOR deseada. Rote el OBS lentamente mientras observa tanto la aguja CDI como el indicador TO/FROM. Cuando la aguja se centre perfectamente y muestre FROM, lea el radial directamente desde la ventana del OBS. Este radial representa su línea de posición actual que se extiende hacia afuera desde la estación VOR.

Para el posicionamiento práctico, considere tanto el radial como su distancia aproximada desde la estación. Mientras que el radial proporciona la posición direccional, estimar la distancia completa la fijación de posición. La distancia se puede estimar a través de varios métodos: verificaciones de tiempo-distancia usando cambios de marcación, equipo DME si está disponible, o referencia visual a puntos de referencia cartografiados.

La precisión de la determinación de posición con un solo VOR depende de varios factores. La intensidad de la señal afecta la precisión - las señales débiles al alcance máximo pueden proporcionar información de radial menos precisa que las señales fuertes recibidas cerca de la estación. La sensibilidad de la aguja también varía con la distancia; los movimientos pequeños de la aeronave causan deflexiones más grandes de la aguja cuando están cerca de la estación.

La verificación de posición se vuelve crucial cuando se depende de un solo VOR para la navegación. Verifique su posición determinada contra puntos de referencia visibles, cálculos de navegación a estima, o información GPS cuando esté disponible. Esta verificación ayuda a identificar posibles errores en la interpretación del VOR o mal funcionamiento del equipo.

> **Verificación de Precisión**: Verifique periódicamente la precisión del VOR usando puntos de verificación en tierra aprobados, puntos de verificación en el aire, o instalaciones VOT para asegurar información de navegación confiable.

Practique el procedimiento de determinación de radiales regularmente para desarrollar competencia. Los pilotos principiantes a menudo tienen dificultades con el concepto inicialmente, pero la práctica consistente construye la comprensión intuitiva necesaria para una navegación VOR eficiente. Recuerde que la indicación FROM es esencial - una aguja centrada con indicación TO muestra la marcación HACIA la estación, no el radial DESDE ella.

### Técnicas de Intersección de Radiales

**La determinación de posición por marcaciones cruzadas** usando dos o más estaciones VOR proporciona fijaciones de posición precisas de la aeronave a través de la intersección de radiales. Esta técnica implica identificar su radial desde cada una de dos estaciones VOR diferentes y trazar estos radiales en una carta seccional. El punto de intersección de estos radiales marca su posición actual.

El proceso comienza con la sintonización de la primera estación VOR y la determinación de su radial usando el procedimiento estándar de centrado. Registre este radial, luego sintonice una segunda estación VOR (preferiblemente de 45° a 90° de distancia de la primera para una precisión óptima) y determine su radial desde esa estación. Trace ambos radiales en su carta seccional - su intersección revela su posición.

La geometría óptima de intersección de radiales ocurre cuando los dos radiales se cruzan en ángulos entre 45° y 135°. Los radiales que se intersectan en ángulos poco profundos (menos de 30°) o ángulos casi perpendiculares cercanos a 180° crean patrones de error alargados que reducen la precisión de la posición. Seleccione estaciones VOR que proporcionen una buena separación geométrica para las fijaciones de posición más confiables.

Por ejemplo, si usted determina que está en el radial 090° DESDE el VOR ABC y simultáneamente en el radial 180° DESDE el VOR XYZ, trace estas dos líneas en su carta. El radial 090° del VOR ABC se extiende hacia el este desde esa estación, mientras que el radial 180° del VOR XYZ se extiende hacia el sur desde su estación. Donde estas líneas se cruzan marca su posición actual.

**La intersección de múltiples radiales** usando tres estaciones VOR crea un triángulo de líneas de posición. Idealmente, estas tres líneas se intersectan en un solo punto. En la práctica, pequeños errores de navegación típicamente crean un triángulo pequeño. Su posición real se encuentra dentro de este triángulo, con la ubicación más probable en el centro del triángulo.

La precisión de las técnicas de intersección de radiales depende de varios factores: precisión de estaciones VOR individuales, identificación adecuada de estaciones, determinación correcta de radiales, y trazado preciso en la carta. Errores sistemáticos en cualquiera de estas áreas pueden desplazar toda la fijación de posición. La intensidad de la señal y la distancia desde las estaciones también afectan la precisión - señales más fuertes y estaciones más cercanas generalmente proporcionan mejores resultados.

> **Técnica Profesional**: Siempre verifique las intersecciones de radiales contra referencias de posición conocidas tales como aeropuertos, puntos de referencia distintivos, o coordenadas GPS cuando estén disponibles.

Las consideraciones de tiempo afectan la precisión de la intersección de radiales durante el vuelo. Dado que las aeronaves se mueven continuamente, determine los radiales de ambas estaciones tan rápidamente como sea práctico para minimizar los cambios de posición entre mediciones. Para aeronaves de alta velocidad o cuando se usan estaciones distantes, este factor de tiempo se vuelve cada vez más importante.

Las aeronaves modernas equipadas con múltiples receptores VOR pueden determinar intersecciones de radiales simultáneamente, eliminando errores de tiempo. Sin embargo, muchas aeronaves de entrenamiento tienen solo un receptor VOR, lo que requiere sintonización secuencial de estaciones. Desarrolle procedimientos eficientes para cambiar rápidamente entre estaciones para minimizar errores de posición relacionados con el tiempo.

---

## PROCEDIMIENTOS DE NAVEGACIÓN VOR

Comprender los principios y equipos VOR proporciona la base para la navegación por radio, pero la aplicación práctica requiere dominar procedimientos específicos para usar este sistema de manera efectiva en vuelo. Estos procedimientos constituyen las habilidades fundamentales que permiten a los pilotos navegar con precisión desde la salida hasta el destino utilizando estaciones terrestres VOR. Cada procedimiento se basa en los demás, creando una metodología de navegación integral que sirve como respaldo a los sistemas GPS y permanece esencial para el entrenamiento de vuelo por instrumentos.

### Sintonización e Identificación de Estaciones VOR

**La sintonización de estación** representa el primer paso crítico en los procedimientos de navegación VOR. El receptor VOR debe sintonizarse en la frecuencia correcta para la estación deseada, que típicamente se encuentra en las cartas seccionales dentro del símbolo de rosa de los vientos de la estación. Las frecuencias VOR van desde 108.0 hasta 117.95 MHz, con frecuencias de números pares que terminan en décimas impares (como 108.1, 108.3) reservadas para estaciones VOR, mientras que las décimas pares se usan para sistemas de aterrizaje por instrumentos.

Después de sintonizar la frecuencia deseada, **la identificación positiva de la estación** se vuelve obligatoria antes de usar cualquier estación VOR para navegación. Cada transmisor VOR difunde su identificación en código Morse, típicamente cada 10 segundos. Algunas estaciones también incluyen identificación de voz grabada indicando el nombre de la estación seguido de "VOR". Los pilotos deben escuchar y confirmar que esta identificación coincide con la estación prevista.

> **Seguridad en Navegación**: Nunca use una estación VOR para navegación sin identificación positiva. Si no se escucha identificación, la estación puede estar fuera de servicio por mantenimiento, haciéndola no confiable para propósitos de navegación.

**El proceso de identificación de estación** requiere que los pilotos consulten la carta seccional para el identificador de tres letras y la secuencia de código Morse correspondiente. Por ejemplo, el VOR de Oklahoma City (OKC) transmite raya-raya-raya, raya-punto-raya, raya-punto-raya-punto en código Morse. Muchos pilotos encuentran útil anotar la secuencia Morse de la carta y compararla con la señal recibida.

**La verificación de intensidad de señal** ocurre a través de la **bandera NAV** o **bandera OFF** en el CDI. Cuando existe intensidad de señal adecuada, esta bandera desaparece de la vista. Si la bandera permanece visible, la aeronave puede estar demasiado lejos de la estación, demasiado baja para recepción de línea de vista, o la estación puede estar inoperativa. Las señales VOR están limitadas por restricciones de línea de vista, típicamente proporcionando 40-45 millas de alcance a 1,000 pies AGL, aumentando con la altitud.

La identificación de estación también incluye verificar cualquier **transmisión de voz** de las Estaciones de Servicio de Vuelo que puedan operar en la misma frecuencia. Aunque estas transmisiones proporcionan información de vuelo valiosa, no deben usarse para identificación de estación ya que las instalaciones FSS frecuentemente transmiten sobre múltiples estaciones VOR con diferentes identificadores.

### Intercepción y Seguimiento de Cursos VOR

**La intercepción de curso** implica maniobrar la aeronave para interceptar un radial específico o línea de curso que conduce hacia o desde una estación VOR. Esta habilidad fundamental requiere comprender la relación entre el rumbo de la aeronave, el curso deseado y el ángulo de intercepción necesario para alcanzar ese curso eficientemente.

**El proceso de intercepción de curso** comienza determinando el curso deseado usando el OBS. Gire el OBS hasta que el radial deseado (para seguimiento saliente) o su recíproco (para seguimiento entrante) aparezca en el índice de curso, asegurando que aparezca la indicación TO/FROM apropiada. La posición de la aguja CDI entonces indica la posición de la aeronave relativa al curso deseado.

**La interpretación del CDI** para intercepción de curso sigue reglas específicas. Cuando la aguja CDI se desvía hacia la derecha, el curso deseado está a la derecha de la posición actual de la aeronave. Cuando la aguja se desvía a la izquierda, el curso está a la izquierda. El grado de desviación indica la distancia aproximada desde la línea central del curso, con desviación de escala completa representando aproximadamente 10-12 grados desde el radial.

**La selección de rumbo de intercepción** requiere elegir un rumbo que cree el ángulo apropiado entre la trayectoria de la aeronave y el curso deseado. Este ángulo de intercepción debe ser lo suficientemente grande para asegurar captura positiva del curso pero no tan grande como para causar sobrepaso. El rumbo seleccionado también debe tener en cuenta las condiciones de viento conocidas que podrían afectar la trayectoria sobre el terreno de la aeronave.

**El seguimiento de curso** comienza una vez que la aeronave alcanza el curso deseado, indicado por el centrado de la aguja CDI. En este punto, el piloto debe hacer la transición del rumbo de intercepción a un **rumbo de seguimiento** que mantenga la aeronave en el curso deseado. El rumbo de seguimiento inicial típicamente equivale al rumbo del curso, pero probablemente serán necesarios ajustes de corrección de viento.

**La corrección de viento durante el seguimiento** se hace evidente cuando la aguja CDI comienza a moverse fuera del centro a pesar de mantener el rumbo del curso. Si la aguja se mueve a la derecha, la aeronave está desviándose a la izquierda del curso y requiere una corrección de rumbo hacia la derecha. Si la aguja se mueve a la izquierda, la aeronave está desviándose a la derecha del curso y necesita una corrección de rumbo hacia la izquierda.

### Técnicas de Intercepción de Curso

**Los ángulos de intercepción estándar** van desde **30 a 45 grados** para la mayoría de las situaciones de navegación. Estos ángulos proporcionan captura efectiva del curso sin sobrepaso excesivo. Ángulos menores de 15-20 grados funcionan bien cuando se está cerca del curso deseado, mientras que ángulos mayores de hasta 60 grados pueden ser necesarios cuando se está posicionado lejos del curso o cuando se requiere intercepción rápida.

**La técnica de intercepción de 30 grados** ofrece el método más comúnmente usado para intercepción de curso. Calcule el rumbo de intercepción sumando o restando 30 grados del curso deseado, dependiendo de en qué lado del curso está posicionada la aeronave. Por ejemplo, si intercepta el radial de 360 grados desde una posición al este del curso, vuele con rumbo de 330 grados (360 - 30).

**La intercepción de 45 grados** proporciona captura de curso más rápida cuando la aeronave está posicionada bien alejada del curso deseado. Esta técnica resulta especialmente útil durante la captura inicial del curso después del despegue o cuando se hacen cambios de curso significativos. El ángulo mayor crea movimiento más rápido de la aguja CDI, proporcionando indicaciones claras de aproximación al curso deseado.

**El ajuste del ángulo de intercepción** depende de varios factores incluyendo distancia desde la estación VOR, velocidad de la aeronave y condiciones de viento. Cuando está cerca de la estación, ángulos de intercepción menores previenen el sobrepaso debido al movimiento rápido de la aguja. A mayores distancias de la estación, pueden usarse ángulos mayores ya que el movimiento de la aguja es más gradual.

**El procedimiento de intercepción de curso** sigue una secuencia específica: primero, determine la posición de la aeronave relativa al curso deseado centrando la aguja CDI con la indicación TO/FROM apropiada. Segundo, gire al rumbo de intercepción calculado. Tercero, monitoree el movimiento de la aguja CDI hacia el centro. Cuarto, comience el viraje al rumbo del curso cuando la aguja se aproxime al centro. Finalmente, ajuste finamente el rumbo para mantener la línea central del curso.

**Los efectos de distancia a la estación** influyen significativamente en las técnicas de intercepción. Cerca de la estación, los radiales convergen rápidamente, causando movimiento rápido de la aguja y requiriendo control preciso de rumbo. Lejos de la estación, los radiales están ampliamente espaciados, resultando en movimiento más lento de la aguja y permitiendo cambios de rumbo más graduales.

### Mantenimiento de la Línea Central del Curso

**El mantenimiento de línea central** requiere monitoreo continuo de la aguja CDI y hacer pequeñas correcciones de rumbo para mantener la aguja centrada. Rara vez ocurre centrado perfecto debido a variaciones de viento, turbulencia y desviaciones menores de rumbo, pero el objetivo es minimizar las desviaciones de curso mientras se mantiene un vuelo suave.

**La sensibilidad de la aguja** varía con la distancia desde la estación VOR. Cerca de la estación, pequeños cambios de rumbo producen movimiento rápido de la aguja, requiriendo entradas de control suaves. A mayores distancias, pueden necesitarse cambios de rumbo mayores para producir movimiento notable de la aguja. La desviación CDI de escala completa representa aproximadamente 10-12 grados a cada lado del radial seleccionado.

**El método de horquillado** proporciona la técnica más efectiva para mantener la línea central del curso en condiciones de viento variables. Este método implica hacer correcciones de rumbo que son mayores que la desviación de curso esperada, permitiendo a la aeronave recapturar la línea central del curso, luego reducir la corrección a un rumbo que debería mantener el curso.

**Los virajes de régimen estándar** de 3 grados por segundo resultan ideales para la mayoría de las correcciones de curso. Estos virajes proporcionan cambios de rumbo controlados sin ángulos de inclinación excesivos o cambios de trayectoria de vuelo abruptos. Para correcciones menores, virajes de medio régimen estándar de 1.5 grados por segundo ofrecen control más preciso.

**Las técnicas de corrección de rumbo** siguen el principio de virar hacia la aguja CDI. Si la aguja se desvía a la derecha, vire a la derecha para regresar al curso. Sin embargo, la cantidad de viraje debe ser apropiada para el grado de desviación y la distancia desde la estación. Una regla general sugiere virar 10-20 grados hacia la aguja para desviaciones pequeñas y hasta 30 grados para desviaciones mayores.

**La anticipación del curso** se vuelve importante cuando se aproxima a puntos de recorrido o cambios de curso. Comience a planificar el siguiente segmento de curso antes de alcanzar el punto de recorrido actual para asegurar transiciones suaves. Esto es particularmente importante cuando se aproxima a la estación VOR, donde ocurren fluctuaciones rápidas de la aguja CDI durante el paso de estación.

### Corrección de Viento en Cursos VOR

**La determinación del ángulo de corrección de viento (WCA)** requiere observación sistemática de los efectos del viento en la trayectoria de la aeronave. El WCA representa la diferencia angular entre el rumbo de la aeronave y la trayectoria del curso deseado, compensando la deriva del viento para mantener la trayectoria sobre el terreno prevista.

**La indicación de deriva de viento** aparece como movimiento gradual de la aguja CDI alejándose del centro a pesar de mantener un rumbo constante igual al curso deseado. Si se mantiene un rumbo de 360 grados para seguir el radial 360 saliente, pero la aguja CDI se mueve lentamente a la derecha, el viento está causando que la aeronave derive a la izquierda del curso (hacia el oeste).

**El método de ensayo y error** para determinar la corrección de viento funciona efectivamente cuando las condiciones de viento son desconocidas. Comience estableciendo una corrección de rumbo en la dirección opuesta a la deriva observada. Si la aguja dejó de moverse a la derecha en el ejemplo anterior, pruebe un rumbo de 005 grados (5 grados de corrección a la derecha). Monitoree la aguja durante varios minutos para determinar si esta corrección mantiene la línea central.

**La técnica de horquillado** para corrección de viento implica sobrecorregir deliberadamente para determinar los límites de corrección requerida. Si una corrección de 5 grados resulta insuficiente y la aguja continúa moviéndose a la derecha, pruebe una corrección de 10 grados (rumbo 010). Si la aguja entonces se mueve a la izquierda, la corrección requerida está entre 5 y 10 grados. Pruebe 8 grados y ajuste finamente desde ahí.

**La evaluación de corrección de viento** requiere paciencia ya que los efectos del viento se desarrollan gradualmente. Permita al menos 2-3 minutos después de cada cambio de rumbo antes de evaluar su efectividad. Las correcciones prematuras conducen a cambios constantes de rumbo y seguimiento pobre del curso. Monitoree las indicaciones de velocidad sobre el terreno si están disponibles, ya que los vientos de frente y de cola afectan las estimaciones de tiempo y el consumo de combustible.

**La compensación de viento variable** requiere atención continua ya que las condiciones de viento cambian con la altitud, ubicación geográfica y movimiento del sistema meteorológico. Esté preparado para ajustar el ángulo de corrección de viento a lo largo del vuelo. La actividad térmica, pasajes frontales y efectos del terreno pueden alterar significativamente las condiciones de viento a lo largo de la ruta.

> **Regla de Corrección de Viento**: El ángulo de corrección de viento debe aplicarse en la dirección opuesta a la deriva del viento. Si el viento causa deriva hacia la izquierda (hacia el oeste), aplique corrección de rumbo a la derecha (hacia el este). Si ocurre deriva hacia la derecha (hacia el este), aplique corrección de rumbo a la izquierda (hacia el oeste).

**Los procedimientos sistemáticos de corrección de viento** ayudan a asegurar resultados consistentes. Primero, establezca el rumbo del curso deseado y note la posición inicial de la aguja CDI. Segundo, observe el movimiento de la aguja durante 2-3 minutos para determinar la dirección y velocidad de deriva. Tercero, aplique una corrección inicial de 5-10 grados hacia la dirección necesaria para detener la deriva. Cuarto, monitoree durante 2-3 minutos para evaluar la efectividad de la corrección. Quinto, ajuste la corrección según sea necesario usando incrementos menores de 2-3 grados. Finalmente, note el ángulo de corrección de viento final para uso en cursos similares durante el vuelo.

---

## TÉCNICAS Y APLICACIONES DE NAVEGACIÓN VOR

La navegación VOR se extiende mucho más allá del seguimiento básico de curso para abarcar técnicas sofisticadas que permiten una navegación precisa en diversos escenarios de vuelo. Esta sección examina aplicaciones avanzadas de VOR que incluyen **procedimientos de navegación directa**, **correcciones fuera de curso**, **reconocimiento de paso de estación**, y **cálculos de tiempo-distancia**. Estas técnicas forman la base para la navegación práctica de travesía y proporcionan capacidades de respaldo esenciales para los sistemas modernos de navegación electrónica.

Comprender la distinción entre **homing** y **seguimiento de curso** representa un concepto fundamental que separa la navegación VOR novata de la competente. Aunque ambos métodos pueden conducir a un destino, solo el seguimiento de curso adecuado garantiza trayectorias de vuelo eficientes y tiempos de llegada predecibles bajo condiciones de viento variables.

### Navegación Directa Hacia y Desde Estaciones VOR

La navegación VOR directa implica volar cursos en línea recta entre su punto de partida y una estación VOR, o desde una estación VOR hasta su destino. Esta técnica requiere una consideración cuidadosa de los efectos del viento y la aplicación apropiada de **ángulos de corrección de viento** para mantener la trayectoria sobre el suelo deseada.

Al navegar **directo hacia una estación VOR**, comience determinando su posición actual en relación con la estación. Gire el OBS hasta que la aguja CDI se centre con una indicación "TO". El curso mostrado en el OBS representa el **rumbo magnético hacia la estación**. Sin embargo, simplemente volar este rumbo magnético rara vez resulta en una trayectoria directa hacia la estación debido a los efectos del viento.

Para establecer una intercepción adecuada, vuele inicialmente un rumbo aproximadamente 10-30 grados hacia el lado de barlovento del curso directo. Esto crea un ángulo de intercepción controlado que le permite observar los efectos de la deriva del viento. A medida que se aproxima al curso deseado, reduzca el ángulo de intercepción y establezca un **ángulo de corrección de viento** que mantenga la línea central del curso.

> **Consejo de Navegación**: Use la "Regla de 60" para estimaciones rápidas de corrección de viento. Si se desvía 1 grado fuera de curso en 60 millas, aplique un ángulo de corrección de viento de 1 grado. Para distancias más cortas, aumente proporcionalmente el ángulo de corrección.

**La navegación directa desde una estación VOR** sigue principios similares pero requiere configurar el radial de salida deseado en el OBS. Después del paso de estación, la bandera TO/FROM cambia a "FROM", confirmando que está siguiendo el radial seleccionado en salida. Mantenga las mismas técnicas de corrección de viento para permanecer en el radial deseado durante todo el vuelo de salida.

Al volar rutas directas sobre largas distancias, considere los efectos de **convergencia de radiales**. Los radiales VOR convergen en la estación, lo que significa que dos radiales que están separados 10 grados a 60 millas de la estación están solo a 5 millas náuticas de distancia. Esta convergencia afecta la geometría de intercepción y los ángulos de corrección requeridos a medida que se aproxima a la estación.

### Navegación Fuera de Curso y Correcciones de Curso

Las situaciones fuera de curso ocurren frecuentemente en la navegación VOR debido a cambios de viento, errores de navegación o requisitos de intercepción de curso. Las **técnicas de corrección de curso** efectivas minimizan el tiempo de vuelo y el consumo de combustible mientras mantienen un control de navegación positivo.

El **proceso de corrección en cuatro pasos** proporciona un enfoque sistemático para las correcciones de curso. Primero, determine su posición en relación con el curso deseado centrando la aguja CDI y anotando los grados de desviación. Cada punto en un CDI estándar representa aproximadamente 2 grados de desviación de curso, con una deflexión a escala completa que típicamente indica 10-12 grados fuera de curso.

Segundo, calcule el **ángulo de intercepción** requerido basándose en su distancia desde la estación y la tasa deseada de retorno al curso. Una regla general sugiere usar un ángulo de intercepción igual al doble del número de grados fuera de curso, más la mitad del ángulo de corrección de curso deseado. Por ejemplo, si está 6 grados a la derecha del curso, use un ángulo de intercepción de aproximadamente 15-20 grados a la izquierda.

Tercero, vuele el rumbo de intercepción hasta que la aguja CDI se acerque al centro, luego reduzca gradualmente el ángulo de intercepción. A medida que la aguja se centra, establezca un nuevo rumbo que incluya el ángulo de corrección de viento original más cualquier corrección adicional sugerida por el patrón de deriva.

Cuarto, monitoree el CDI durante varios minutos para confirmar que el nuevo rumbo mantiene el curso deseado. Realice pequeños ajustes de rumbo según sea necesario, típicamente en incrementos de 2-5 grados.

Las técnicas de **seguimiento paralelo** resultan útiles al navegar paralelo pero desplazado de un radial VOR. Seleccione el radial VOR que sea paralelo a su trayectoria sobre el suelo deseada, luego mantenga un rumbo constante a ese radial usando procedimientos estándar de seguimiento de curso. Esta técnica es particularmente valiosa al evitar espacio aéreo restringido o mantener separación de otras aeronaves.

Al realizar **correcciones de curso grandes** (mayores de 30 grados), considere interceptar primero un radial intermedio, luego proceder a su curso final deseado. Este enfoque escalonado proporciona mejor control de navegación y reduce el riesgo de exceder las correcciones.

### Reconocimiento de Paso de Estación VOR

Reconocer el **paso de estación VOR** es crucial para temporizar cambios de curso, fijar la posición e iniciar procedimientos de navegación de salida. Varios indicadores confirman el paso de estación, cada uno proporcionando diferentes niveles de precisión y confiabilidad.

El indicador principal es la **inversión de la bandera TO/FROM**. A medida que pasa sobre o al través de una estación VOR, el indicador TO/FROM cambia de "TO" a "FROM" (o viceversa cuando sigue en salida). Esta inversión ocurre dentro de aproximadamente 1-2 millas náuticas de la estación, dependiendo de su altitud y las características del cono de confusión de la estación.

Las **fluctuaciones de la aguja CDI** proporcionan la indicación de paso de estación más sensible. A medida que se aproxima a la estación, la aguja CDI se vuelve cada vez más sensible a pequeños cambios de rumbo. Directamente sobre la estación, la aguja fluctúa rápidamente o se vuelve poco confiable debido al **cono de confusión** - un área pequeña directamente sobre la estación donde las señales son débiles o poco confiables.

> **Técnica de Paso de Estación**: Al usar un RMI para el paso de estación, observe el movimiento rápido de la aguja de marcación. La aguja girará rápidamente pasando el punto de 180 grados a medida que pasa la estación, proporcionando una indicación precisa de paso.

El **equipo medidor de distancia (DME)**, cuando está disponible, proporciona la indicación de paso de estación más precisa. La lectura DME alcanza su valor mínimo en el paso de estación, típicamente mostrando 0.0 a 0.5 millas náuticas dependiendo de su altitud sobre la estación.

Para **pasos de estación a gran altitud**, el cono de confusión se extiende más lejos de la estación. Las aeronaves que vuelan por encima de 10,000 pies AGL pueden experimentar fluctuaciones de aguja a varias millas de la estación. Planifique cambios de curso basándose en la distancia en lugar del comportamiento de la aguja cuando vuele a grandes altitudes.

**Temporizar el paso de estación** se vuelve crítico para la precisión de la planificación de vuelo. Anote su tiempo exacto de paso para usar en cálculos de velocidad sobre el suelo y actualizaciones de ETA. Al volar sobre un VOR a 5,000 pies AGL, el paso de estación típicamente ocurre cuando la aeronave está dentro de 1-2 millas náuticas de la estación horizontalmente.

### Cálculos de Tiempo y Distancia Usando VOR

La navegación VOR permite **cálculos de tiempo y distancia** precisos, esenciales para la planificación de vuelo, la gestión de combustible y la fijación de posición. Estos cálculos usan tasas de cambio de marcación y parámetros conocidos de rendimiento de la aeronave para determinar la posición y la temporización de navegación.

El **método de cambio de marcación** proporciona cálculos de distancia y tiempo a la estación usando lecturas del indicador de desviación de curso. Para realizar este cálculo, primero establezca un rumbo constante perpendicular al radial deseado (90 grados al curso). Anote el tiempo cuando la aguja CDI se centre en su radial de referencia, luego continúe en el mismo rumbo hasta que la aguja se centre nuevamente después de girar el OBS 10 grados en la dirección de su giro.

Aplique la fórmula: **Tiempo a la estación (minutos) = (60 × tiempo transcurrido en minutos) ÷ grados de cambio de marcación**. Para el cálculo de distancia, use: **Distancia a la estación (NM) = (TAS en NM por minuto × tiempo transcurrido en minutos) ÷ grados de cambio de marcación**.

Por ejemplo, si vuela a 120 nudos TAS (2 NM por minuto) y requiere 90 segundos para un cambio de marcación de 10 grados, el tiempo a la estación es igual a (60 × 1.5) ÷ 10 = 9 minutos. La distancia a la estación es igual a (2 × 1.5) ÷ 10 = 0.3 × 10 = 3 millas náuticas.

Las **verificaciones de tiempo-distancia con RMI** ofrecen cálculos simplificados cuando están disponibles. Gire para colocar la aguja de marcación en la posición del extremo del ala (90 grados), anote el tiempo y mantenga el rumbo hasta que la aguja se mueva 10 grados. El tiempo a la estación en minutos es igual al tiempo transcurrido en segundos con el punto decimal movido una posición a la izquierda. A 75 segundos de tiempo transcurrido, la estación está a 7.5 minutos de distancia.

Los **procedimientos de inversión de curso** requieren una planificación cuidadosa al usar navegación VOR. La inversión de curso estándar implica volar pasando la estación, ejecutar un giro de 180 grados e interceptar el curso recíproco. Planifique el giro de inversión para comenzar aproximadamente 1-2 minutos después del paso de estación, dependiendo de su velocidad sobre el suelo y la geometría de intercepción deseada.

Para **entradas de registro de navegación**, registre los tiempos de paso VOR, cambios de rumbo e información de marcación sistemáticamente. Las entradas de registro esenciales incluyen: identificación de estación y frecuencia, tiempo de paso, rumbo magnético volado, cálculos de velocidad sobre el suelo y datos de consumo de combustible. Estas entradas proporcionan información de navegación de respaldo y respaldan el cumplimiento del plan de vuelo.

> **Nota de Precisión**: Los cálculos de tiempo-distancia VOR proporcionan valores aproximados afectados por las condiciones del viento, la precisión de la temporización y la geometría de la estación. Use estos cálculos como estimaciones y verifique con otros métodos de navegación cuando la precisión sea crítica.

La **determinación de velocidad sobre el suelo** usando VOR requiere volar una distancia conocida entre dos radiales o fijos identificables. Registre el tiempo requerido para volar entre los fijos, luego calcule la velocidad sobre el suelo usando la fórmula: **Velocidad Sobre el Suelo = Distancia ÷ Tiempo**. Esta técnica resulta particularmente valiosa cuando los vientos reales difieren significativamente de las condiciones pronosticadas.

Al realizar **múltiples fijos VOR** para determinación de posición, use estaciones separadas por al menos 30 grados en marcación para una precisión óptima. Sintonice simultáneamente dos receptores VOR en diferentes estaciones, centre ambas agujas CDI y trace la intersección de los dos radiales en su carta aeronáutica. Esta intersección representa su posición actual con una precisión típicamente dentro de 1-2 millas náuticas.

Las **aplicaciones de computadora de vuelo electrónica** mejoran los cálculos de tiempo-distancia VOR al proporcionar soluciones rápidas a problemas complejos de triángulo de viento. Las calculadoras modernas pueden resolver condiciones de viento desconocidas usando la velocidad sobre el suelo derivada de VOR y valores conocidos de velocidad verdadera del aire, permitiendo actualizaciones de plan de vuelo en tiempo real y una precisión de navegación mejorada.

---

## SISTEMAS Y OPERACIÓN VOR-DME

La navegación VOR proporciona una excelente guía direccional, pero los pilotos frecuentemente necesitan conocer su distancia desde una estación para determinar fijaciones de posición, calcular velocidad respecto al suelo o estimar tiempos de llegada. El **Equipo Medidor de Distancia (DME)** llena este vacío crítico al proporcionar información precisa de distancia cuando se empareja con estaciones VOR. Los sistemas combinados VOR-DME representan una de las ayudas a la navegación más versátiles y ampliamente utilizadas en la aviación general.

### Principios del Equipo Medidor de Distancia

El **DME** opera mediante un **sistema de interrogación y respuesta** utilizando señales de radio de frecuencia ultra alta (UHF) en la banda de 962-1213 MHz. El equipo DME aerotransportado envía pares de pulsos codificados a un transpondedor DME basado en tierra, el cual responde automáticamente con pares de pulsos codificados en una frecuencia diferente. El receptor DME mide el tiempo entre la interrogación y la respuesta, luego calcula y muestra la distancia a la estación.

El sistema funciona bajo el principio de que las ondas de radio viajan a una velocidad constante de 186,000 millas por segundo. Dado que la señal debe viajar desde la aeronave a la estación terrestre y regresar, la computadora DME divide el tiempo total entre dos y lo multiplica por la velocidad de la luz para determinar la distancia. Este proceso ocurre continuamente, con el equipo aerotransportado enviando 150 pares de pulsos de interrogación por segundo cuando busca una estación y 24-30 pares por segundo cuando está sincronizado.

El DME muestra la distancia en **millas náuticas** con una precisión típicamente dentro de ±0.2 millas náuticas o ±3 por ciento de la distancia medida, lo que sea mayor. La mayoría de los indicadores DME muestran la distancia a la décima de milla náutica más cercana cuando se encuentran dentro de 100 millas náuticas de la estación. El sistema puede proporcionar información confiable de distancia hasta 199 millas náuticas y a altitudes de hasta 40,000 pies, aunque el alcance real depende de las limitaciones de línea de vista.

> **Nota Importante**: El DME mide **distancia de alcance oblicuo**, no distancia horizontal sobre el terreno. Esta distinción se vuelve crítica al volar a grandes altitudes cerca de la estación.

### Capacidades de las Estaciones VOR-DME

Las **estaciones VOR-DME** combinan la información de rumbo del VOR con la capacidad de medición de distancia del DME. Estas instalaciones proporcionan fijación completa de posición con una sola estación terrestre: los pilotos pueden determinar tanto su rumbo magnético desde la estación (usando VOR) como su distancia desde la estación (usando DME). Esta combinación elimina la necesidad de múltiples estaciones VOR para establecer fijaciones de posición.

Las estaciones VOR-DME se identifican con el mismo identificador de tres letras utilizado para la porción VOR, transmitido en código Morse cada 30 segundos. La porción DME se empareja automáticamente con la frecuencia VOR: cuando un piloto sintoniza una frecuencia VOR, el receptor DME selecciona automáticamente el canal DME correspondiente. Este sistema de **emparejamiento de frecuencias** asegura que tanto la información de rumbo como de distancia provengan de la misma instalación terrestre.

El **alcance efectivo** de las estaciones VOR-DME sigue las mismas clasificaciones que las instalaciones VOR independientes. Las estaciones clase Terminal (T) proporcionan servicio dentro de 25 millas náuticas a altitudes de 12,000 pies y por debajo. Las estaciones clase baja altitud (L) sirven a aeronaves por debajo de 18,000 pies dentro de 40 millas náuticas. Las estaciones clase alta altitud (H) proporcionan cobertura extendida hasta 130 millas náuticas entre 18,000 pies y FL 450.

Las estaciones VOR-DME se someten a las mismas verificaciones de precisión que las instalaciones VOR independientes. La porción VOR mantiene precisión dentro de ±1°, mientras que la porción DME proporciona precisión de distancia dentro de las especificaciones mencionadas anteriormente. Los pilotos deben realizar verificaciones regulares de precisión VOR utilizando instalaciones VOT, puntos de verificación terrestres certificados o puntos de verificación aéreos certificados según se enumeran en el Chart Supplement U.S.

### Cálculos de Distancia DME y Velocidad Respecto al Suelo

Las lecturas de distancia DME requieren interpretación cuando se utilizan para planificación de navegación y cálculos de velocidad respecto al suelo. El factor más significativo es comprender **alcance oblicuo versus distancia sobre el terreno**. El DME mide la distancia en línea recta desde la aeronave a la estación, la cual incluye tanto distancia horizontal como separación vertical.

La **distancia de alcance oblicuo** se vuelve significativamente diferente de la distancia horizontal sobre el terreno al volar a grandes altitudes cerca de la estación DME. Por ejemplo, una aeronave volando directamente sobre una estación DME a 6,076 pies AGL recibe una lectura de distancia de 1.0 milla náutica, aunque la distancia horizontal es cero. La fórmula para calcular la distancia horizontal es: Distancia sobre el Terreno = √(Distancia DME² - Altitud²), donde la altitud debe convertirse a millas náuticas (6,076 pies = 1 milla náutica).

Para propósitos prácticos de navegación, el error de alcance oblicuo se vuelve insignificante cuando la distancia a la estación excede diez veces la altitud de la aeronave sobre la estación. Una aeronave a 6,000 pies AGL debe estar al menos a 10 millas náuticas de la estación para que el error de alcance oblicuo sea menor a 0.5 millas náuticas.

Los **cálculos de velocidad respecto al suelo** usando DME proporcionan datos precisos de rendimiento en tiempo real. La mayoría de las unidades DME modernas muestran la velocidad respecto al suelo directamente midiendo la tasa de cambio de distancia a lo largo del tiempo. El equipo típicamente promedia cambios de distancia durante períodos de 1-3 minutos para proporcionar lecturas estables de velocidad respecto al suelo. Los cálculos manuales de velocidad respecto al suelo utilizan la fórmula: Velocidad Respecto al Suelo = (Cambio de Distancia ÷ Tiempo) × 60, donde el cambio de distancia está en millas náuticas y el tiempo en minutos.

Los **cálculos de tiempo a la estación** se vuelven simples con DME: Tiempo a la Estación (minutos) = Distancia DME ÷ Velocidad Respecto al Suelo × 60. Por ejemplo, si el DME muestra 30 millas náuticas y la velocidad respecto al suelo es 120 nudos, el tiempo a la estación es igual a 15 minutos. Muchas unidades DME muestran el tiempo a la estación automáticamente cuando la velocidad respecto al suelo excede 30 nudos.

> **Consejo de Navegación**: Las lecturas de velocidad respecto al suelo del DME son más precisas al volar directamente hacia o desde la estación. La precisión de la velocidad respecto al suelo disminuye al volar en trayectorias que cruzan la estación en ángulos distintos a 90°.

### Sistemas TACAN y VORTAC

**TACAN (Tactical Air Navigation)** es un sistema de navegación militar que proporciona información tanto de rumbo como de distancia, similar al VOR-DME civil pero usando principios operativos diferentes. El TACAN opera en la banda UHF y utiliza un sistema de antena rotativa que crea información de rumbo a través de patrones de modulación de amplitud. La porción de medición de distancia del TACAN opera de manera idéntica al DME civil.

Las **estaciones VORTAC** representan la combinación de equipo VOR civil con equipo TACAN militar en la misma ubicación. Este emparejamiento permite que tanto aeronaves civiles como militares utilicen la instalación simultáneamente. Las aeronaves civiles reciben información de rumbo VOR e información de distancia TACAN (que es idéntica al DME), mientras que las aeronaves militares pueden usar el sistema TACAN completo tanto para rumbo como para distancia.

Desde la perspectiva de un piloto civil, las estaciones VORTAC funcionan exactamente como estaciones VOR-DME. El receptor VOR proporciona información de rumbo magnético, mientras que el receptor DME muestra información de distancia del sistema TACAN. Todos los procedimientos para seguimiento de curso, fijación de posición y navegación permanecen idénticos ya sea usando instalaciones VOR-DME o VORTAC.

Las estaciones VORTAC se identifican con el identificador estándar de tres letras transmitido en código Morse. En las cartas seccionales, las instalaciones VORTAC se representan con un símbolo que muestra capacidades tanto VOR como TACAN. El Chart Supplement U.S. enumera estas instalaciones como VORTAC y proporciona información completa de frecuencia, horarios de operación y cualquier limitación especial.

Las **áreas de cobertura y estándares de precisión** para las instalaciones VORTAC coinciden con las de las estaciones VOR-DME. La porción VOR proporciona precisión de rumbo dentro de ±1°, mientras que el componente de medición de distancia TACAN proporciona la misma precisión que el equipo DME estándar. Los pilotos utilizan el mismo sistema de emparejamiento de frecuencias: sintonizar la frecuencia VOR selecciona automáticamente el canal correspondiente de medición de distancia TACAN.

### Emparejamiento de Frecuencia DME con VOR

El **sistema de emparejamiento de frecuencia DME** elimina la necesidad de que los pilotos sintonicen manualmente el equipo medidor de distancia por separado. Cuando se selecciona una frecuencia VOR en el receptor de navegación, el DME se sintoniza automáticamente a la frecuencia UHF correspondiente utilizada por la instalación DME o TACAN emparejada. Este emparejamiento está estandarizado en todo el mundo y asegura que la información de rumbo y distancia siempre provengan de la misma estación terrestre.

Las frecuencias VOR operan en la banda VHF de 108.00 a 117.95 MHz, mientras que el DME opera en la banda UHF de 962 a 1213 MHz. Cada frecuencia VOR tiene una frecuencia DME específica emparejada. Por ejemplo, la frecuencia VOR 108.00 MHz se empareja con el canal DME 17X (978 MHz interrogación, 1041 MHz respuesta). El emparejamiento continúa secuencialmente a través de todas las frecuencias VOR disponibles.

El sistema de emparejamiento utiliza **canales X e Y** para acomodar el número de frecuencias VOR disponibles dentro del espectro de frecuencias DME. Los canales X se emparejan con frecuencias VOR que terminan en .00, .05, .20, .25, .40, .45, .60, .65, .80 y .95 MHz. Los canales Y se emparejan con frecuencias VOR que terminan en .10, .15, .30, .35, .50, .55, .70, .75, .90 y .95 MHz. Este arreglo proporciona suficientes canales DME para todas las frecuencias VOR mientras mantiene separación entre frecuencias de interrogación y respuesta.

La mayoría del equipo DME de aviación general opera automáticamente: los pilotos simplemente sintonizan la frecuencia VOR deseada y la porción DME se sincroniza con la frecuencia emparejada sin acción adicional. El equipo típicamente indica la sincronización DME con una bandera que desaparece o una anunciación específica en la pantalla de distancia. La sincronización inicial puede tomar 30-60 segundos mientras el receptor DME se sincroniza con el transpondedor terrestre.

Los sistemas de navegación integrados modernos muestran tanto la información VOR como DME en un solo instrumento, simplificando la gestión de cabina y reduciendo la carga de trabajo del piloto. Estos sistemas mantienen el emparejamiento de frecuencias automáticamente y proporcionan indicaciones de respaldo si se pierden las señales VOR o DME. Comprender este sistema de emparejamiento ayuda a los pilotos a verificar que están recibiendo información de navegación de la instalación prevista y a solucionar cualquier discrepancia entre las pantallas de navegación esperadas y reales.

---

## LIMITACIONES DEL VOR Y FUENTES DE ERROR

Aunque la navegación VOR proporciona excelente precisión y confiabilidad para la navegación de aeronaves, los pilotos deben comprender sus limitaciones inherentes y fuentes potenciales de error para usar el sistema de manera efectiva y segura. Estas limitaciones pueden afectar la precisión de navegación, la recepción de señal y la seguridad general del vuelo, haciendo que el conocimiento de estos factores sea crítico para operaciones VOR exitosas.

### Limitaciones de Línea de Vista y Alcance

Las transmisiones VOR operan en ondas de radio de muy alta frecuencia (VHF) entre 108.0 y 117.95 MHz, las cuales están sujetas a **restricciones de línea de vista**. A diferencia de las señales de frecuencia más baja que pueden doblarse alrededor de obstáculos o seguir la curvatura de la Tierra, las señales VHF viajan en líneas rectas y no pueden penetrar características significativas del terreno ni curvarse más allá del horizonte.

El **volumen de servicio** de una estación VOR define el espacio aéreo tridimensional dentro del cual la instalación proporciona señales de navegación confiables. Este volumen varía significativamente con la altitud de la aeronave, ya que el alcance de recepción aumenta con la altura sobre el nivel del suelo. A 1,000 pies AGL, la recepción típica del VOR se extiende de 40 a 45 millas náuticas desde el transmisor. Esta distancia aumenta sustancialmente con la altitud, siguiendo la relación matemática de la geometría de línea de vista.

Las instalaciones VOR se clasifican en tres categorías operacionales con limitaciones específicas de volumen de servicio. Los VOR **clase Terminal (T)** proporcionan servicio dentro de 25 millas náuticas a altitudes hasta 12,000 pies MSL. Las estaciones **clase baja altitud (L)** sirven aeronaves por debajo de 18,000 pies MSL dentro de un radio de 40 millas náuticas. Los VOR **clase alta altitud (H)** ofrecen la cobertura más extensa, proporcionando servicio dentro de 40 millas náuticas por debajo de 14,500 pies MSL, extendiéndose a 100 millas náuticas entre 14,500 y 17,999 pies MSL, y alcanzando 130 millas náuticas desde 18,000 pies MSL hasta FL 450.

> **Limitación Crítica**: El terreno montañoso puede crear **áreas de sombra** significativas donde las señales VOR son bloqueadas, incluso dentro del volumen de servicio publicado. Los pilotos que operan en regiones montañosas deben planificar métodos alternativos de navegación para áreas donde pueda ocurrir enmascaramiento por terreno.

Las limitaciones de distancia se vuelven particularmente importantes durante la planificación de vuelo. Las aeronaves que vuelan a altitudes bajas pueden perder la recepción VOR mucho antes de alcanzar los límites de volumen de servicio publicados debido al terreno intermedio. El **cono de confusión** directamente sobre una estación VOR crea otra limitación, donde la intensidad de la señal se vuelve poco confiable dentro de aproximadamente 2-3 millas náuticas de la instalación, causando comportamiento errático de la aguja CDI e indicaciones TO/FROM poco confiables.

### Estándares de Precisión y Tolerancia del VOR

La Federal Aviation Administration establece estándares específicos de precisión para los sistemas de navegación VOR para asegurar un desempeño de navegación confiable. El **estándar de precisión de ±4 grados** representa la desviación máxima permitida para las instalaciones terrestres VOR cuando están debidamente calibradas y mantenidas. Este estándar se aplica a los radiales transmitidos desde la estación VOR misma.

Los receptores VOR de aeronaves deben cumplir requisitos adicionales de precisión durante la certificación y verificaciones periódicas. Para operaciones de vuelo por instrumentos, las regulaciones especifican tolerancias máximas de **±4 grados para verificaciones VOR terrestres** usando puntos de chequeo certificados o instalaciones VOT (VOR Test), y **±6 grados para verificaciones en vuelo** realizadas usando puntos de chequeo aéreos certificados. Aunque estas verificaciones no son obligatorias para operaciones VFR, proporcionan una valiosa verificación de precisión.

La precisión de la navegación VOR se degrada con la distancia desde la estación transmisora. En el alcance máximo de servicio, pequeños errores angulares se traducen en desplazamiento lineal significativo. Un error de 4 grados a 100 millas náuticas de la estación resulta en aproximadamente 7 millas náuticas de desplazamiento lateral del curso previsto. Esta relación matemática enfatiza la importancia de correcciones periódicas de curso y verificación cruzada con otras fuentes de navegación.

La precisión del receptor puede deteriorarse debido a componentes envejecidos, variaciones de temperatura e interferencia electrónica. Efectos de **cambio Doppler** pueden ocurrir en aeronaves de alta velocidad, aunque este factor afecta principalmente a jets en lugar de aeronaves típicas de aviación general. Las verificaciones regulares de precisión ayudan a identificar problemas en desarrollo del receptor antes de que comprometan la seguridad de navegación.

> **Nota sobre Equipos**: Los receptores VOR digitales modernos generalmente proporcionan mejor precisión y estabilidad que las unidades analógicas antiguas, pero todos los receptores requieren verificación periódica para asegurar confiabilidad continua dentro de las tolerancias publicadas.

### Efectos del Terreno y Obstáculos

Las características del terreno impactan significativamente la propagación de señal VOR y la calidad de recepción. El **enmascaramiento por terreno** ocurre cuando montañas, colinas u otro terreno elevado bloquean el camino de línea de vista entre el transmisor VOR y el receptor de la aeronave. Este fenómeno puede crear zonas muertas de navegación incluso dentro del volumen de servicio publicado de una instalación VOR.

La **reflexión de señal** y **propagación de trayectorias múltiples** presentan desafíos adicionales en terreno montañoso. Las señales VOR pueden rebotar en características del terreno, creando múltiples trayectorias de señal al receptor de la aeronave. Esto resulta en distorsión de señal, fluctuaciones del indicador de desviación de curso (CDI) y errores potenciales de rumbo. Los valles orientados perpendicularmente a los radiales VOR a menudo experimentan los efectos de trayectorias múltiples más severos.

Las grandes características del terreno pueden crear efectos de **curvatura de señal**, donde los cursos VOR parecen desviados de sus rumbos magnéticos publicados. Este fenómeno ocurre más comúnmente en áreas con relieve significativo del terreno en relación tanto con el transmisor VOR como con la altitud de la aeronave receptora. Los pilotos deben ser particularmente cautelosos al navegar a través de pasos estrechos o valles profundos donde los efectos del terreno son más pronunciados.

Las **condiciones atmosféricas** también pueden afectar la propagación de señal VOR. Inversiones de temperatura, precipitación y canalización atmosférica pueden causar refracción de señal o crear patrones de propagación inusuales. Aunque estos efectos son generalmente menos significativos que el enmascaramiento por terreno, pueden contribuir a errores de navegación, particularmente a largas distancias de la estación VOR.

Las áreas urbanas con concentraciones densas de edificios grandes pueden crear efectos similares de enmascaramiento y reflexión. Los pilotos que operan cerca de áreas metropolitanas importantes deben ser conscientes de que la precisión del VOR puede verse degradada por estructuras hechas por el hombre, particularmente cuando vuelan a altitudes más bajas.

### Limitaciones de Equipo y Fallas

El equipo de navegación VOR en aeronaves puede experimentar varios tipos de fallas y mal funcionamientos que comprometen la precisión de navegación y la seguridad. Comprender estos problemas potenciales permite a los pilotos reconocer fallas de equipo rápidamente y tomar acción correctiva apropiada.

Las **fallas de suministro de energía** representan el mal funcionamiento de equipo más obvio. La pérdida completa de energía eléctrica al receptor VOR resulta en pérdida de toda capacidad de navegación. La degradación parcial de energía puede causar operación errática, recepción débil de señal o función intermitente del equipo que puede ser más peligrosa que la falla completa porque el mal funcionamiento puede no ser inmediatamente aparente.

La **degradación de sensibilidad del receptor** ocurre gradualmente a medida que los componentes electrónicos envejecen. Esto se manifiesta como alcance de recepción reducido, mayor susceptibilidad a interferencia y calidad de señal deficiente a distancias normales de operación de las estaciones VOR. La **bandera NAV** o **bandera OFF** debe aparecer cuando la intensidad de la señal cae por debajo de niveles aceptables, alertando a los pilotos sobre información de navegación poco confiable.

Los **problemas del sistema de antena** pueden impactar significativamente la recepción VOR. Elementos de antena dañados, conexiones corroídas o cables coaxiales sueltos crean atenuación y distorsión de señal. La acumulación de hielo en antenas VOR durante el vuelo en condiciones de formación de hielo puede degradar severamente la recepción hasta que el hielo sea removido o se derrita.

Los **mal funcionamientos internos del receptor** pueden causar errores de rumbo, cambios de sensibilidad del CDI o problemas de indicación TO/FROM. Estas fallas pueden ser particularmente insidiosas porque pueden proporcionar información de navegación consistente pero incorrecta. Las verificaciones regulares de precisión usando puntos de chequeo VOR publicados ayudan a identificar estos problemas en desarrollo.

> **Reconocimiento de Mal funcionamiento**: Los pilotos deben sospechar inmediatamente mal funcionamiento del equipo VOR cuando experimenten: comportamiento errático de la aguja CDI, apariciones frecuentes de bandera NAV en áreas de recepción buena esperada, incapacidad para identificar transmisiones de la estación, o indicaciones de navegación que entran en conflicto con otras fuentes de navegación o referencias visuales.

El **cono de confusión** sobre las estaciones VOR crea limitaciones operacionales incluso con equipo funcionando perfectamente. Dentro de aproximadamente 2-3 millas náuticas de la estación y extendiéndose hacia arriba, las señales VOR se vuelven poco confiables debido a las características del patrón de radiación de la antena. Las agujas CDI pueden oscilar rápidamente, las indicaciones TO/FROM pueden fluctuar, o el equipo puede mostrar banderas OFF durante el paso de la estación.

La **interferencia eléctrica** de otros sistemas de la aeronave puede afectar la operación del receptor VOR. Las luces estroboscópicas, sistemas de radar y algunos dispositivos electrónicos pueden causar patrones de interferencia que degradan la calidad de señal VOR o crean indicaciones falsas. Los pilotos deben ser conscientes de estas fuentes potenciales de interferencia y considerar apagar equipos electrónicos no esenciales cuando experimenten problemas inexplicables de recepción VOR.

Las aeronaves modernas con múltiples sistemas de navegación proporcionan oportunidades para verificar cruzadamente las indicaciones VOR contra GPS u otras fuentes de navegación. Esta redundancia ayuda a identificar mal funcionamientos de equipo y proporciona capacidad de navegación de respaldo cuando los sistemas primarios fallan. Sin embargo, los pilotos deben comprender las limitaciones y fuentes de error de todos los sistemas de navegación instalados para usarlos efectivamente para verificación mutua y navegación de respaldo.

---

## VERIFICACIONES Y MANTENIMIENTO DEL SISTEMA VOR

La precisión del sistema VOR es crítica para la navegación segura, ya sea operando bajo condiciones VFR o IFR. Las verificaciones regulares y el mantenimiento adecuado aseguran que el receptor VOR proporcione guía de rumbo confiable e información de marcación precisa. Aunque las verificaciones VOR no son requeridas para vuelo VFR, comprender estos procedimientos es esencial para cualquier piloto que utilice navegación VOR y obligatorio para operaciones de vuelo por instrumentos.

### Verificaciones de Precisión VOR Requeridas

Las Regulaciones Federales de Aviación requieren verificaciones de precisión VOR para aeronaves operadas bajo Reglas de Vuelo por Instrumentos (IFR). De acuerdo con **14 CFR 91.171**, ninguna persona puede operar una aeronave bajo IFR utilizando equipo VOR a menos que el **equipo VOR haya sido verificado operacionalmente dentro de los 30 días precedentes** y se haya encontrado dentro de los límites prescritos.

Este **requisito de verificación VOR de 30 días** aplica específicamente a operaciones IFR, pero los pilotos VFR también deben realizar verificaciones de precisión regulares para asegurar que su equipo de navegación funcione correctamente. La regulación establece que la verificación VOR debe realizarse mediante uno de cuatro métodos: VOR Test Facility (VOT), punto de verificación en tierra, punto de verificación en vuelo, o verificación de receptor VOR dual.

El piloto al mando debe asegurar que las verificaciones de precisión VOR estén documentadas apropiadamente. **Cada verificación VOR debe registrarse en el libro de mantenimiento de la aeronave u otro registro permanente**, incluyendo la fecha, lugar, error de marcación y firma de la persona que realiza la verificación. Este requisito de documentación asegura responsabilidad y proporciona un historial de mantenimiento para el equipo de navegación.

> **Importante**: Las verificaciones de precisión VOR son requeridas cada 30 días para operaciones de vuelo IFR. Aunque no son requeridas para VFR, las verificaciones regulares aseguran confiabilidad en la navegación y deben ser parte de las buenas prácticas operacionales.

### Procedimientos VOT (VOR Test Facility)

Una **VOR Test Facility (VOT)** es un transmisor de prueba basado en tierra que proporciona un método conveniente para verificar la precisión del receptor VOR. Las instalaciones VOT transmiten una señal de prueba en 108.0 MHz que simula una estación VOR ubicada directamente sobre la aeronave. La señal VOT está específicamente diseñada para verificaciones de equipo y no puede ser usada para navegación.

Al realizar una verificación VOT, sintonice el receptor VOR a 108.0 MHz e identifique la señal VOT mediante su serie continua de puntos o la identificación grabada que dice "VOT". Con la aeronave posicionada en cualquier lugar del aeropuerto con servicio VOT, la **aguja del Course Deviation Indicator (CDI) debe centrarse cuando el Omni Bearing Selector (OBS) esté ajustado a 0 grados con indicación "FROM" o 180 grados con indicación "TO"**.

El **error máximo de marcación permisible al usar un VOT es ±4 grados**. Si el CDI se centra en cualquier ajuste diferente a 0 grados (FROM) o 180 grados (TO), dentro de esta tolerancia de 4 grados, el receptor VOR requiere ajuste o reparación. Por ejemplo, si el CDI se centra con el OBS ajustado a 002 grados mostrando FROM, o 182 grados mostrando TO, el equipo está dentro de límites aceptables ya que el error es solo de 2 grados.

Los procedimientos VOT requieren atención cuidadosa al detalle. Asegure que la identificación de audio sea confirmada antes de realizar la prueba, ya que otras señales pueden ser recibidas en 108.0 MHz. La prueba debe realizarse con los sistemas eléctricos normales de la aeronave operando para simular condiciones reales de vuelo. Registre el error de marcación, incluso si está dentro de límites, ya que esto proporciona información de tendencias para propósitos de mantenimiento.

> **Resumen de Verificación VOT**: Sintonice 108.0 MHz, identifique señal VOT, centre aguja CDI. Debe leer 000° FROM o 180° TO dentro de ±4°. Disponible en aeropuertos seleccionados - consulte Chart Supplement U.S. para ubicaciones.

### Métodos de Puntos de Verificación en Tierra y en Vuelo

Los **puntos de verificación en tierra** proporcionan un método alternativo para verificaciones de precisión VOR cuando las instalaciones VOT no están disponibles. Estos puntos de verificación consisten en radiales certificados de estaciones VOR cercanas que pueden recibirse en tierra en ubicaciones específicas en superficies aeroportuarias. El **error máximo de marcación permisible para puntos de verificación en tierra es ±4 grados**, la misma tolerancia que las verificaciones VOT.

Para realizar una prueba de punto de verificación en tierra, posicione la aeronave en la ubicación del punto de verificación designado mostrada en el Chart Supplement U.S. Sintonice e identifique la estación VOR apropiada, luego ajuste el radial publicado en el OBS. La aguja CDI debe centrarse con la indicación TO o FROM apropiada dentro de 4 grados del radial publicado. Los puntos de verificación en tierra típicamente están ubicados en plataformas de aeropuertos, calles de rodaje o pistas donde existe línea de vista clara a la estación VOR.

Los **puntos de verificación en vuelo** se utilizan cuando las instalaciones en tierra no están disponibles o no son prácticas. Estos puntos de verificación consisten en radiales específicos de estaciones VOR que pueden verificarse mientras se vuela sobre puntos de referencia designados a altitudes especificadas. El **error máximo de marcación permisible para puntos de verificación en vuelo es ±6 grados**, proporcionando tolerancia ligeramente mayor que las verificaciones en tierra debido a la naturaleza dinámica de las operaciones de vuelo.

Los procedimientos de puntos de verificación en vuelo requieren volar sobre el punto de referencia designado a la altitud publicada mientras sintoniza la estación VOR especificada. Ajuste el radial publicado en el OBS y anote la indicación CDI. La aguja debe centrarse dentro de 6 grados de la marcación publicada. Los puntos de verificación en vuelo son particularmente útiles para aeronaves basadas en aeropuertos sin instalaciones de verificación en tierra.

Las **verificaciones de receptor VOR dual** pueden realizarse cuando la aeronave está equipada con dos receptores VOR independientes. Sintonice ambos receptores a la misma estación VOR y compare las marcaciones indicadas cuando ambas agujas CDI estén centradas en el mismo radial. La **variación máxima permisible entre los dos receptores es 4 grados**. Este método puede realizarse en tierra o en vuelo y proporciona verificación de que ambos sistemas de navegación funcionan correctamente.

### Requisitos de Registro de Verificaciones VOR

La documentación apropiada de verificaciones de precisión VOR es obligatoria para operaciones IFR y representa una buena práctica para todos los pilotos que utilizan navegación VOR. Los **requisitos de entrada en el libro de registro** especificados en 14 CFR 91.171 deben incluir información específica para satisfacer el cumplimiento regulatorio y proporcionar seguimiento de mantenimiento.

Cada entrada de verificación VOR debe contener la **fecha de la verificación, lugar donde se realizó la verificación, error de marcación encontrado y firma de la persona que realiza la verificación**. Por ejemplo: "15 ENE 2024, Oklahoma City VOT, +2°, Juan Pérez". Esta información proporciona un registro completo de la precisión del equipo y cualquier tendencia en el error de marcación a lo largo del tiempo.

El error de marcación debe registrarse incluso cuando esté dentro de límites aceptables. Una verificación VOT que muestre exactamente 0 grados FROM debe registrarse como "0° error", mientras que una lectura de 002 grados FROM debe registrarse como "+2° error". Esta documentación ayuda al personal de mantenimiento a identificar deterioro gradual en la precisión del receptor antes de que exceda los límites permitidos.

Los registros de verificaciones VOR deben mantenerse en los registros permanentes de la aeronave, típicamente en el libro de mantenimiento de la aeronave o un registro separado de equipo de navegación. Los registros deben conservarse y estar disponibles para inspección por personal de FAA. Algunos operadores mantienen registros electrónicos, pero los mismos requisitos de información aplican independientemente del método de registro.

Para aeronaves operadas bajo IFR, el piloto al mando es responsable de asegurar que las verificaciones VOR vigentes sean realizadas y registradas apropiadamente. Operar IFR con verificaciones VOR vencidas es una violación de las Regulaciones Federales de Aviación y podría resultar en acción sobre el certificado. Incluso los pilotos VFR deben mantener registros precisos de verificaciones de equipo de navegación como parte de una buena práctica aeronáutica y preparación para potencial entrenamiento de instrumentos u operaciones de vuelo.

> **Requisitos de Documentación**: Cada verificación VOR debe incluir: Fecha, Ubicación, Error de marcación, Firma. Requerido cada 30 días para operaciones IFR. Mantenga registros en libro de aeronave o registro permanente de equipo de navegación.

## Resumen

Revise los puntos clave de esta unidad:

- VOR (Very High Frequency Omnidirectional Range) es un sistema de navegación por radio terrestre que opera en frecuencias VHF de 108.0 a 117.95 MHz y proporciona información precisa de marcación magnética a través de 360 radiales individuales que se extienden hacia afuera desde cada estación.
- Las estaciones VOR transmiten señales omnidireccionales utilizando comparación de fase entre señales de referencia y variables de 30 Hz, con cobertura limitada por características de línea de vista que aumentan el alcance con la altitud de la aeronave.
- Cada estación VOR debe ser identificada positivamente mediante código Morse o identificación por voz antes de su uso, y las estaciones eliminan las señales de identificación cuando están fuera de servicio por mantenimiento.
- El equipo VOR aerotransportado incluye el receptor, el Selector de Marcación Omni (OBS) para selección de rumbo, el Indicador de Desviación de Rumbo (CDI) para guía lateral, y la bandera TO/FROM para indicación de relación de rumbo.
- El CDI proporciona guía lateral de rumbo con deflexión a escala completa que ocurre a 10° o más del rumbo seleccionado, representando cada punto típicamente 2° de desviación.
- Los radiales se extienden DESDE las estaciones VOR y representan rumbos magnéticos hacia afuera desde la instalación, mientras que las marcaciones representan direcciones magnéticas HACIA la estación desde la posición de la aeronave.
- Un solo VOR proporciona una línea de posición al determinar qué radial ocupa la aeronave mediante el centrado de la aguja del CDI con una indicación FROM.
- Las técnicas de marcación cruzada utilizando dos o más estaciones VOR permiten fijaciones de posición precisas mediante intersección de radiales, logrando una precisión óptima cuando los radiales se intersectan en ángulos entre 45° y 135°.

---

## Términos Clave

| Término | Definición |
|------|------------|
| **VOR (Very High Frequency Omnidirectional Range)** | Sistema de radionavegación terrestre que proporciona información precisa de marcación magnética a través de 360 radiales que se extienden desde cada estación |
| **Radial** | Línea de rumbo magnético que se extiende hacia afuera DESDE una estación VOR, numerada de 001° a 360° |
| **Bearing** | Dirección magnética HACIA una estación VOR desde la posición actual de la aeronave |
| **OBS (Omni Bearing Selector)** | Control rotatorio que permite a los pilotos seleccionar cualquier rumbo magnético hacia o desde una estación VOR |
| **CDI (Course Deviation Indicator)** | Indicador de aguja que muestra la posición de la aeronave en relación con el rumbo VOR seleccionado |
| **TO/FROM Flag** | Indicador que muestra si seguir el rumbo seleccionado conduce hacia (TO) o alejándose de (FROM) la estación VOR |
| **Full-Scale Deflection** | Posición de la aguja CDI cuando la aeronave está a 10° o más del rumbo seleccionado según lo medido desde la estación VOR |
| **Phase Comparison** | Principio de transmisión de señal VOR que utiliza señales de referencia y variables de 30 Hz para determinar la marcación de la aeronave |
| **Line of Position** | Línea de referencia de navegación única, como un radial VOR, que indica la ubicación de la aeronave a lo largo de esa línea |
| **Cross-Bearing** | Técnica de navegación que utiliza radiales de dos o más estaciones VOR para determinar la posición precisa de la aeronave |
| **Cone of Confusion** | Área directamente sobre una estación VOR donde las indicaciones TO/FROM se vuelven poco confiables |
| **Service Volume** | Espacio aéreo definido alrededor de una estación VOR donde se garantizan señales de navegación confiables |
| **NAV Flag** | Indicación de advertencia que aparece cuando la intensidad de la señal VOR es insuficiente para navegación confiable |
| **Station Identification** | Transmisión en código Morse o por voz utilizada para identificar positivamente las estaciones VOR antes del uso de navegación |
| **Reciprocal** | Marcación que difiere de otra marcación por exactamente 180°, utilizada en conversiones de radial a marcación |

---

## Preguntas de Repaso

**Opción Múltiple**

1. ¿Dentro de qué rango de frecuencia operan las estaciones VOR?
   - A) 108.0 a 117.95 MHz
   - B) 118.0 a 136.975 MHz
   - C) 121.5 a 135.0 MHz
   - D) 225.0 a 399.975 MHz

2. Si una aeronave está en el radial 090° DESDE una estación VOR, ¿cuál es el rumbo magnético HACIA esa estación?
   - A) 090°
   - B) 180°
   - C) 270°
   - D) 360°

3. La deflexión de escala completa de la aguja CDI ocurre cuando la aeronave está a cuántos grados del curso seleccionado?
   - A) 5° o más
   - B) 10° o más
   - C) 15° o más
   - D) 20° o más

4. ¿Qué significa una indicación de bandera FROM?
   - A) La aeronave debe volar alejándose de la estación VOR
   - B) Seguir el curso seleccionado llevaría a la aeronave hacia la estación VOR
   - C) Seguir el curso seleccionado llevaría a la aeronave alejándose de la estación VOR
   - D) La señal VOR es demasiado débil para la navegación

**Verdadero/Falso**

5. Los radiales VOR están referenciados al norte verdadero en lugar del norte magnético.

6. Una estación VOR que está fuera de servicio por mantenimiento eliminará su señal de identificación en código Morse.

7. La aguja CDI siempre apunta hacia la estación VOR independientemente del ajuste del OBS.

8. La cobertura VOR aumenta con la altitud de la aeronave debido a las limitaciones de línea de vista.

**Respuesta Corta**

9. Explique la diferencia entre la operación de estaciones terrestres CVOR y DVOR.

10. Describa el procedimiento apropiado para determinar en qué radial se encuentra DESDE una estación VOR.

**Emparejamiento**

11. Empareje cada componente con su función principal:
    - A) OBS               1) Proporciona guía lateral de curso
    - B) CDI               2) Advierte de intensidad de señal insuficiente
    - C) Bandera TO/FROM   3) Selecciona el curso magnético deseado
    - D) Bandera NAV       4) Muestra la relación del curso con la estación

12. Una aeronave determina que está en el radial 045° desde VOR-A y en el radial 315° desde VOR-B. Si ambas estaciones están correctamente identificadas y los radiales se intersectan en un ángulo de 90°, ¿qué técnica de navegación se está utilizando y por qué la geometría es favorable para la precisión?

---

## Referencias de la FAA

- PHAK Capítulo 16: Navegación, Secciones 16-1 a 16-15
- AIM Capítulo 1: Ayudas Radioeléctricas para la Navegación Aérea, Sección 1-1-3