---
wingwing_chapter: 8
wingwing_unit: "B"
unit_title: "Weight and Balance"
faa_sources: ['PHAK - Chapter 10 - Weight and Balance.pdf']
estimated_read_time: 47
---

# Unit B: Weight and Balance

Imagina esto: estás preparándote para un vuelo de travesía con tres pasajeros y su equipaje, confiado en que tu aeronave puede manejar la carga, solo para descubrir durante tus cálculos de peso y balance que tu centro de gravedad está peligrosamente fuera de los límites. Este escenario destaca por qué el peso y balance no es solo papeleo—es una habilidad de seguridad crítica que puede significar la diferencia entre un vuelo exitoso y un accidente potencial. La gestión adecuada del peso y balance asegura que tu aeronave funcione de manera predecible, mantenga la controlabilidad y opere dentro de su envolvente de seguridad diseñada.

## Objetivos de Aprendizaje

Después de completar esta unidad, usted será capaz de:

- Explicar los principios fundamentales de peso y balance y su impacto en el rendimiento y la seguridad de la aeronave
- Definir centro de gravedad, momento y otra terminología esencial de peso y balance
- Identificar los efectos adversos de la distribución de peso y carga inadecuadas en la controlabilidad de la aeronave
- Aplicar los requisitos reglamentarios para el cumplimiento de peso y balance y el mantenimiento de registros
- Calcular el peso y balance de la aeronave utilizando métodos computacionales y fórmulas estándar
- Realizar cálculos de peso y balance para varios escenarios de carga, incluyendo consumo de combustible y cambios de pasajeros
- Determinar los efectos del desplazamiento de peso, adición o remoción de artículos en el balance de la aeronave y los límites del centro de gravedad

---

## FUNDAMENTOS DE PESO Y BALANCE

**El cumplimiento de peso y balance** representa una de las responsabilidades de seguridad más críticas para cualquier piloto. Operar una aeronave fuera de sus límites aprobados de peso y balance puede resultar en falla estructural catastrófica, características de vuelo irrecuperables o pérdida completa del control. A diferencia de muchos otros factores de seguridad de vuelo que pueden proporcionar cierto margen de error, las violaciones de peso y balance a menudo conducen directamente a accidentes con poca oportunidad de intervención o recuperación por parte del piloto.

La **Federal Aviation Administration (FAA)** establece los requisitos de peso y balance a través del Título 14 del Code of Federal Regulations (14 CFR). Aunque las operaciones bajo Part 91 no requieren cálculos formales de peso y balance antes de cada vuelo, 14 CFR 91.9 exige que los pilotos cumplan con todas las limitaciones operacionales especificadas en el Aircraft Flight Manual (AFM) aprobado o el Pilot's Operating Handbook (POH). Estas limitaciones incluyen explícitamente restricciones de peso y balance.

> **Nota Crítica de Seguridad**: Una aeronave que excede su peso máximo certificado compromete la integridad estructural y puede experimentar falla estructural completa durante operaciones de vuelo normales o turbulencia moderada.

### Introducción a la Importancia del Peso y Balance

Los fabricantes de aeronaves establecen los límites de peso y balance mediante extensas pruebas de vuelo y análisis estructural. Estos límites definen la envolvente operacional dentro de la cual la aeronave puede ser operada con seguridad. El **Type Certificate Data Sheet (TCDS)** contiene las limitaciones oficiales de peso y balance para cada modelo de aeronave, mientras que el AFM proporciona procedimientos detallados para calcular y verificar el cumplimiento.

**La integridad estructural** forma la base de las limitaciones de peso. Cada componente de la aeronave, desde largueros de ala hasta conjuntos de tren de aterrizaje, está diseñado para soportar factores de carga específicos al peso máximo certificado. Operar por encima de estos límites de peso somete la estructura de la aeronave a cargas que exceden las especificaciones de diseño. Durante encuentros con turbulencia, aterrizajes duros o maniobras de alta carga G, una aeronave con sobrepeso puede experimentar falla estructural sin advertencia.

**La degradación del desempeño** ocurre inmediatamente cuando el peso de la aeronave excede los parámetros de diseño. A diferencia de las reducciones graduales de desempeño observadas con cambios de altitud o temperatura, las penalizaciones de desempeño relacionadas con el peso son inmediatas y predecibles. Estos efectos se agravan con otros factores que reducen el desempeño, como altitud densidad alta, pistas contaminadas o condiciones atmosféricas.

**Las limitaciones de autoridad de control** presentan quizás el peligro más insidioso del peso y balance inadecuados. Una aeronave con su **centro de gravedad (CG)** fuera de los límites aprobados puede exhibir características de manejo normales durante condiciones de calma, pero volverse incontrolable durante fases críticas de vuelo como aproximación, aterrizaje o procedimientos de emergencia.

### Principios de Control de Peso y Relaciones de Sustentación

**El peso** representa la fuerza gravitacional que continuamente jala una aeronave hacia la Tierra. Como se establece en los principios aerodinámicos, el peso debe ser equilibrado por una **fuerza de sustentación** igual y opuesta para mantener vuelo nivelado. Esta relación fundamental gobierna todos los aspectos de la operación de aeronaves e impacta directamente cada parámetro de desempeño.

**La capacidad de generación de sustentación** de cualquier perfil aerodinámico es finita y depende de cuatro factores primarios: diseño del perfil aerodinámico, **ángulo de ataque (AOA)**, velocidad aerodinámica y densidad del aire. Los fabricantes de aeronaves diseñan las alas para producir sustentación suficiente al peso máximo certificado bajo condiciones atmosféricas estándar. Exceder este peso puede resultar en producción de sustentación insuficiente, haciendo imposible el vuelo sostenido.

**El ángulo de ataque crítico** se convierte en un factor limitante en operaciones de aeronaves con sobrepeso. A medida que aumenta el peso de la aeronave, se requieren ángulos de ataque más altos para generar sustentación suficiente para el vuelo. Este requisito de AOA aumentado reduce el margen entre actitudes de vuelo normales y condiciones de pérdida. Durante las fases de aproximación y aterrizaje, este margen reducido aumenta significativamente el potencial de accidentes por pérdida/barrena.

**Los cálculos de carga alar** ayudan a los pilotos a comprender las relaciones de sustentación. La carga alar es igual al peso de la aeronave dividido por el área del ala, típicamente expresada en libras por pie cuadrado. Cargas alares más altas requieren coeficientes de sustentación aumentados, logrados mediante ángulos de ataque más altos o velocidad aerodinámica aumentada. Cuando la carga alar excede los límites de diseño, la aeronave puede ser incapaz de generar sustentación suficiente para operaciones de vuelo seguras.

[Figura 8-1: Relación Sustentación-Peso en Vuelo - PHAK Cap 5, Fig 5-1]

**La curva de potencia requerida** cambia significativamente con los cambios de peso. Las aeronaves más pesadas requieren más potencia para todas las fases de vuelo, desde el despegue hasta el crucero. Este requisito de potencia aumentado puede exceder la potencia disponible del motor, particularmente en altitudes densidad altas o durante operaciones con un solo motor en aeronaves bimotores.

### Efectos del Peso en el Desempeño de la Aeronave

**El desempeño de despegue** sufre dramáticamente por exceso de peso. Las aeronaves con sobrepeso requieren **velocidades de despegue** más altas para generar sustentación suficiente, resultando en **carreras de despegue** más largas. La relación no es lineal: pequeños aumentos de peso pueden producir aumentos desproporcionadamente grandes en los requisitos de distancia de despegue. Las distancias de carrera en tierra pueden aumentar en 15-25% por aumentos de peso de solo 10% por encima de los límites máximos.

**La degradación del desempeño de ascenso** presenta serias implicaciones de seguridad, particularmente durante escenarios de franqueamiento de obstáculos. Las aeronaves con sobrepeso exhiben **régimen de ascenso** reducido y capacidades de **ángulo de ascenso** disminuidas. El **techo de servicio** (altitud máxima a la cual la aeronave puede mantener un régimen de ascenso de 100 pies por minuto) disminuye significativamente con exceso de peso. El desempeño de ascenso con un solo motor en aeronaves bimotores puede volverse negativo, haciendo imposible el vuelo con un solo motor.

> **Planificación de Desempeño**: Siempre verifique las tablas de desempeño durante la planificación de prevuelo para asegurar que existan márgenes adecuados para el peso real de despegue y las condiciones atmosféricas.

**Las penalizaciones de desempeño de crucero** incluyen **velocidad de crucero** reducida, **alcance** disminuido y tasas de consumo de combustible más altas. Las aeronaves con sobrepeso deben volar a ángulos de ataque más altos para mantener altitud, aumentando el arrastre inducido y reduciendo la eficiencia de combustible. El alcance máximo disminuye tanto por el aumento del arrastre como por las posibles reducciones de carga de combustible necesarias para cumplir con los límites de peso.

**El desempeño de aterrizaje** crea preocupaciones críticas de seguridad durante las fases de aproximación y aterrizaje. Las aeronaves con sobrepeso tienen **velocidades de pérdida** más altas, requiriendo velocidades de aproximación y aterrizaje más rápidas. Estas velocidades aumentadas resultan en **carreras de aterrizaje** más largas y márgenes de detención reducidos. Las velocidades de toma de contacto más rápidas también aumentan las cargas en los neumáticos y el calentamiento de los frenos, causando potencialmente falla de neumáticos o sobrecalentamiento del sistema de frenos.

**Las características de pérdida** se vuelven más peligrosas en aeronaves con sobrepeso. Las velocidades de pérdida más altas reducen el margen entre vuelo normal y condiciones de pérdida. La recuperación de pérdidas requiere más altitud, y la aeronave puede exhibir características de pérdida más agresivas. La recuperación de barrena, si está certificada, se vuelve más difícil y puede requerir técnicas fuera de los perfiles de entrenamiento normales.

**La maniobrabilidad** disminuye significativamente con exceso de peso. Las cargas alares más altas reducen la capacidad de la aeronave para cambiar de dirección rápidamente o responder a las entradas de control. Durante procedimientos de emergencia que requieren maniobras rápidas, como evasión de colisiones o encuentros con clima severo, la maniobrabilidad reducida puede impedir la recuperación exitosa.

### Cambios de Peso Durante Operaciones de Vuelo

**Los cálculos de peso de combustible** forman un componente fundamental de la planificación de peso y balance. **La gasolina de aviación (AVGAS) pesa 6 libras por galón**, haciendo que la carga de combustible sea un factor significativo en el peso total de la aeronave. Treinta galones de combustible equivalen a 180 libras, potencialmente más que un pasajero. Los pilotos deben contabilizar el peso del combustible al cargar pasajeros, equipaje y carga.

**Los pesos de combustible para turbinas** difieren de los pesos de AVGAS. **Jet A y Jet A-1 pesan 6.8 libras por galón**, mientras que **Jet B pesa 6.5 libras por galón**. Los operadores de aeronaves con turbina deben usar pesos de combustible apropiados para cálculos precisos. Las variaciones de temperatura pueden afectar la densidad del combustible, pero los pesos estándar proporcionan precisión adecuada para la mayoría de las operaciones.

**Los cálculos de consumo de combustible** requieren consideración cuidadosa de los desplazamientos del CG durante el vuelo. La mayoría de las aeronaves de aviación general llevan combustible en tanques de ala ubicados cerca del CG, minimizando el movimiento del CG a medida que se consume el combustible. Sin embargo, las aeronaves con tanques de combustible en el fuselaje o configuraciones de múltiples tanques pueden experimentar desplazamientos significativos del CG durante el consumo de combustible. Los pilotos deben verificar que el CG permanezca dentro de los límites durante todo el vuelo planificado.

**El combustible no utilizable** debe incluirse en los cálculos de peso vacío, pero no puede considerarse disponible para operaciones de vuelo. **El combustible utilizable** representa el combustible disponible para la planificación de vuelo. Los pilotos deben comprender la diferencia y asegurar reservas adecuadas de combustible utilizable mientras mantienen el cumplimiento de peso y balance.

> **Gestión de Combustible**: Monitoree los patrones de consumo de combustible para asegurar que el CG permanezca dentro de los límites durante todo el vuelo, especialmente en aeronaves con configuraciones de múltiples tanques de combustible.

**Las modificaciones de equipos** impactan significativamente el peso y balance de la aeronave. La instalación de radios, instrumentos o equipos opcionales adicionales cambia tanto el peso vacío como la ubicación del CG. Los **Supplemental Type Certificates (STCs)** para instalaciones de equipos incluyen información revisada de peso y balance que debe incorporarse en los registros de la aeronave.

**Los cambios de peso inducidos por mantenimiento** ocurren durante actividades de reparación y modificación. Las piezas de reemplazo pueden tener pesos diferentes a los componentes originales. Los esquemas de pintura, modificaciones interiores y reparaciones estructurales pueden alterar tanto las características de peso como de balance. **Advisory Circular (AC) 43.13-1** establece criterios para cambios de peso insignificantes que no requieren actualizaciones formales de peso y balance.

**Los criterios de peso estándar** para cambios insignificantes incluyen: una libra o menos para aeronaves que pesan menos de 5,000 libras de peso vacío; dos libras o menos para aeronaves con pesos vacíos entre 5,000 y 50,000 libras; y cinco libras o menos para aeronaves que exceden 50,000 libras de peso vacío. **Los cambios insignificantes del CG** se definen como menos de 0.05% de la **Mean Aerodynamic Chord (MAC)** para aeronaves de ala fija.

**Los requisitos de lastre** pueden ser necesarios cuando se retira equipo o cuando las condiciones operacionales requieren ajustes del CG. **El lastre permanente** se convierte en parte del peso vacío de la aeronave, mientras que **el lastre temporal** debe asegurarse y contabilizarse en cada cálculo de peso y balance. El lastre debe estar adecuadamente asegurado para evitar desplazamientos durante las operaciones de vuelo.

**Las consideraciones de secuencia de carga** se vuelven críticas en aeronaves con rangos amplios de CG o múltiples configuraciones de carga. Los pilotos deben verificar que el CG permanezca dentro de los límites durante todas las fases de carga y descarga. Las secuencias de carga de combustible, procedimientos de embarque de pasajeros y patrones de carga de carga afectan las ubicaciones provisionales del CG durante las operaciones en tierra.

---

## CENTRO DE GRAVEDAD Y CONCEPTOS DE BALANCE

El **centro de gravedad (CG)** representa el punto teórico donde se concentra todo el peso de una aeronave. Es el punto de equilibrio donde, si la aeronave estuviera suspendida, permanecería nivelada en todas direcciones. Comprender los conceptos del CG es fundamental para operaciones de vuelo seguras, ya que la ubicación del CG afecta directamente la estabilidad de la aeronave, la respuesta de los controles y las características generales de rendimiento.

El CG es un punto tridimensional con posicionamiento longitudinal, lateral y vertical dentro de la aeronave. Aunque las tres dimensiones son importantes, la posición longitudinal del CG recibe atención primaria en la mayoría de los cálculos de peso y balance debido a su impacto crítico en la estabilidad de cabeceo y la efectividad del elevador.

### Definición y Características del Centro de Gravedad

El **centro de gravedad** funciona como el punto de equilibrio de la aeronave y determina cómo la aeronave responderá a las entradas de control y fuerzas externas. A diferencia de un punto fijo, la ubicación del CG se desplaza a medida que cambia la distribución de peso dentro de la aeronave. Cuando los pasajeros se mueven, el combustible se consume o la carga se reposiciona, el CG se mueve en consecuencia.

La ubicación del CG se mide en pulgadas desde un punto de referencia llamado **datum**. Este datum es un plano vertical imaginario establecido por el fabricante de la aeronave y sirve como la estación cero para todos los cálculos de peso y balance. Todas las mediciones a popa del datum son valores positivos, mientras que las mediciones hacia adelante del datum son valores negativos.

Los cálculos del **momento** determinan la ubicación del CG mediante la fórmula: Peso × Brazo = Momento. El brazo representa la distancia horizontal desde el datum hasta el centro de gravedad del elemento. El momento total de la aeronave dividido por el peso total produce la ubicación del CG en pulgadas desde el datum.

> **Concepto Crítico**: El CG no necesariamente está ubicado en el centro geométrico de la aeronave. Los fabricantes posicionan el CG ligeramente adelante del centro de sustentación para asegurar la estabilidad longitudinal adecuada y la respuesta de control durante las operaciones de vuelo.

Los diseñadores de aeronaves establecen un **rango de CG** dentro del cual el punto de equilibrio debe caer para operaciones de vuelo seguras. Este rango está definido por límites adelante y atrás, típicamente especificados en pulgadas desde el datum. Estos límites aseguran estabilidad adecuada mientras mantienen autoridad de control suficiente a lo largo de la envolvente operacional de la aeronave.

### Consideraciones de Balance Longitudinal y Lateral

El **balance longitudinal** involucra el posicionamiento de proa a popa del CG a lo largo del eje longitudinal de la aeronave. Esto representa la preocupación principal en los cálculos de peso y balance, ya que el balance longitudinal inadecuado afecta significativamente la estabilidad de cabeceo y la efectividad del control del elevador.

Una **condición de CG adelantado** ocurre cuando el punto de equilibrio está posicionado delante del límite adelantado. Esto crea una condición de nariz pesada que requiere mayor presión de elevador hacia atrás para mantener vuelo nivelado. La carga con CG adelantado aumenta la estabilidad longitudinal pero requiere fuerzas de control más altas y reduce la autoridad del elevador para el flare durante el aterrizaje.

Una **condición de CG atrasado** se desarrolla cuando el punto de equilibrio se mueve detrás del límite de popa. Esta configuración de cola pesada reduce la estabilidad longitudinal y puede crear fuerzas de control extremadamente ligeras. Las condiciones de CG atrasado pueden llevar a una recuperación difícil de pérdidas y pérdida potencial de control debido a márgenes de estabilidad reducidos.

El **balance lateral** aborda la distribución de peso a través del eje lateral de la aeronave de punta de ala a punta de ala. Aunque no se calcula para la mayoría de las aeronaves de aviación general, los pilotos deben comprender los efectos del balance lateral en las características de vuelo y los procedimientos de gestión de combustible.

El desequilibrio lateral típicamente resulta del consumo desigual de combustible o carga asimétrica. Cuando el combustible se consume de manera desigual de los tanques de las alas, o cuando objetos pesados se posicionan en un lado de la aeronave, se desarrolla una condición de ala pesada. Esta condición requiere presión constante de alerón o ajuste de trim para mantener vuelo nivelado.

El piloto puede gestionar el balance lateral mediante procedimientos adecuados de gestión de combustible. La mayoría de los manuales de vuelo de aeronaves especifican procedimientos de consumo de combustible para mantener el balance lateral, tales como alternar el uso de tanques de combustible o requisitos específicos de programación de combustible para vuelos extendidos.

> **Alerta de Gestión de Combustible**: La gasolina pesa 6 libras por galón, haciendo de la distribución de combustible un factor significativo tanto en el balance longitudinal como lateral. La gestión inadecuada de combustible puede crear problemas serios de balance, particularmente en aeronaves con tanques en las puntas de las alas o múltiples sistemas de combustible.

### Límites de CG y Especificaciones de Rango

Los fabricantes de aeronaves establecen **límites de CG** mediante pruebas de vuelo extensivas para asegurar características de manejo seguras a lo largo de la envolvente operacional. Estos límites se publican en la **Type Certificate Data Sheet (TCDS)** y el **Aircraft Flight Manual (AFM)** aprobado o **Pilot's Operating Handbook (POH)**.

El **límite de CG adelantado** se establece típicamente basado en características de aterrizaje y autoridad de control del elevador. Este límite asegura efectividad suficiente del elevador para hacer flare en el aterrizaje a velocidades mínimas de aproximación. Cuando consideraciones estructurales no limitan la posición adelantada del CG, el límite se establece donde se requiere deflexión completa del elevador hacia arriba para obtener el ángulo de ataque necesario para el aterrizaje.

Los límites de CG adelantado también pueden establecerse para prevenir cargas excesivas en la rueda de nariz durante operaciones en tierra. Las aeronaves cargadas más allá del límite adelantado pueden experimentar sobrecarga de la rueda de nariz, velocidades aumentadas de despegue y dificultad potencial en la rotación durante el despegue.

El **límite de CG atrasado** representa la posición más hacia atrás donde existen márgenes de estabilidad adecuados para operaciones de vuelo seguras. Este límite se establece mediante pruebas de vuelo para asegurar capacidad de recuperación de pérdidas, estabilidad longitudinal adecuada y fuerzas de control aceptables a lo largo de la envolvente de vuelo.

Las **especificaciones de rango de CG** pueden variar con el peso bruto en algunas aeronaves. Las aeronaves ligeras a menudo tienen límites de CG constantes independientemente del peso, mientras que aeronaves más grandes pueden tener límites de CG que cambian a medida que el peso bruto aumenta o disminuye. Algunas aeronaves también especifican límites de CG diferentes para operaciones específicas tales como vuelo acrobático, operaciones de tren de aterrizaje retráctil o instalaciones de equipo especial.

La **Mean Aerodynamic Chord (MAC)** proporciona un método alternativo para expresar límites de CG en algunas aeronaves. La MAC representa la distancia promedio desde el borde de ataque hasta el borde de salida del ala. Los límites de CG expresados en porcentaje de MAC permiten una comparación más fácil entre diferentes configuraciones de aeronaves y ayudan a comprender los márgenes de estabilidad.

> **Requisito Regulatorio**: 14 CFR Part 91.9 requiere que los pilotos cumplan con las limitaciones operacionales en el AFM aprobado, incluyendo límites de peso y balance. Aunque Part 91 no requiere específicamente cálculos de peso y balance antes de cada vuelo, el cumplimiento con los límites de CG es obligatorio para operaciones de vuelo legales.

### Relaciones de Estabilidad y Control

La relación entre la ubicación del CG y la **estabilidad** de la aeronave es fundamental para operaciones de vuelo seguras. La **estabilidad longitudinal** disminuye a medida que el CG se mueve hacia atrás hacia el límite de popa. Una aeronave con carga de CG adelantado exhibe fuerte estabilidad longitudinal pero requiere fuerzas de control más altas y autoridad de control reducida.

La **estabilidad estática** se refiere a la tendencia inicial de la aeronave de retornar al equilibrio después de una perturbación. La carga con CG adelantado aumenta la estabilidad estática, haciendo que la aeronave sea más resistente a cambios de cabeceo pero requiriendo mayor entrada de control para maniobrar. La carga con CG atrasado reduce la estabilidad estática y puede resultar en estabilidad neutral o negativa en casos extremos.

La **estabilidad dinámica** involucra la respuesta de la aeronave a lo largo del tiempo después de una perturbación. Las condiciones de CG adelantado generalmente mejoran las características de estabilidad dinámica, mientras que la carga con CG atrasado puede llevar a respuestas oscilatorias o divergentes a entradas de control o encuentros con turbulencia.

La **autoridad de control** varía significativamente con la posición del CG. Las condiciones de CG adelantado requieren mayores fuerzas de control pero proporcionan respuesta de control predecible. Los pilotos pueden experimentar dificultad levantando la nariz durante el despegue y aterrizaje con carga de CG adelantado, potencialmente requiriendo ajustes de trim o modificaciones de técnica de control.

Las condiciones de CG atrasado crean fuerzas de control muy ligeras que pueden llevar a esfuerzo inadvertido excesivo de la estructura de la aeronave. Las fuerzas de control reducidas pueden sentirse placenteras inicialmente pero pueden resultar en situaciones peligrosas durante encuentros con turbulencia o maniobras de emergencia donde el control preciso es esencial.

Las **características de pérdida** cambian dramáticamente con la posición del CG. La carga con CG adelantado típicamente resulta en características de pérdida convencionales con advertencia adecuada y procedimientos de recuperación directos. La carga con CG atrasado puede producir características de pérdida violentas, advertencias de pérdida retrasadas y procedimientos de recuperación difíciles o imposibles.

> **Crítico para la Seguridad**: Las aeronaves cargadas más allá del límite de CG atrasado pueden ser irrecuperables de pérdidas o barrenas. La estabilidad longitudinal reducida puede resultar en condiciones de pérdida profunda donde la efectividad del elevador es insuficiente para la recuperación, independientemente de la técnica del piloto o altitud disponible.

Los **requisitos de trim** aumentan con posiciones de CG alejadas del centro de diseño. Las condiciones de CG adelantado requieren trim de nariz arriba para aliviar la presión de control, mientras que las condiciones de CG atrasado necesitan trim de nariz abajo. Los requisitos excesivos de trim reducen el recorrido disponible del elevador para maniobrar y pueden indicar condiciones de carga fuera de límites.

La relación entre la posición del CG y el **rendimiento de la aeronave** se extiende más allá de consideraciones de estabilidad. La carga con CG adelantado aumenta las distancias de despegue, reduce el rendimiento de ascenso y eleva las velocidades de pérdida. La carga con CG atrasado puede inicialmente parecer mejorar el rendimiento mediante resistencia de trim reducida pero crea márgenes de estabilidad inaceptables que comprometen la seguridad.

Comprender estas relaciones permite a los pilotos reconocer aeronaves cargadas inadecuadamente mediante observación de características de vuelo. Una aeronave que requiere fuerzas de control excesivas, ajustes de trim inusuales o que exhibe características de estabilidad pobres puede indicar problemas de peso y balance que requieren atención inmediata antes de operaciones de vuelo continuas.

---

## EFECTOS DEL DESEQUILIBRIO ADVERSO Y SEGURIDAD

Operar una aeronave con el centro de gravedad fuera de los límites aprobados crea condiciones de vuelo peligrosas que comprometen tanto la controlabilidad como la integridad estructural. Comprender estos efectos adversos es fundamental para la seguridad del vuelo, ya que **el balance inadecuado** puede transformar operaciones de vuelo rutinarias en situaciones que ponen en riesgo la vida. Las consecuencias de exceder los límites de CG son mucho más graves que una simple degradación del rendimiento.

Los efectos de las condiciones adversas de balance son acumulativos e interactúan con otros factores de rendimiento. Lo que podría ser manejable en condiciones ideales se vuelve catastrófico cuando se combina con situaciones de emergencia, clima adverso u operaciones a gran altitud de densidad.

### Efectos del Límite de CG Adelantado y Características de Aterrizaje

Cuando el centro de gravedad se desplaza hacia adelante de los límites aprobados, la aeronave desarrolla una pronunciada **condición de nariz pesada** que crea múltiples riesgos de seguridad. El límite de CG adelantado típicamente se establece basándose en las características de aterrizaje, ya que esto representa una de las fases más críticas del vuelo donde la autoridad de control es esencial.

**Las cargas excesivas en la rueda de nariz** representan una preocupación primaria con operaciones de CG adelantado. La fuerza descendente adicional sobre la rueda de nariz durante operaciones en tierra puede exceder los límites de diseño estructural, causando potencialmente falla del conjunto de la rueda o colapso del tren de nariz. Esta condición se vuelve particularmente peligrosa durante aterrizajes duros o al operar sobre superficies irregulares.

Las características de aterrizaje se deterioran significativamente con carga de CG adelantado. **La efectividad reducida del elevador** se hace evidente durante el flare de aterrizaje, donde los pilotos pueden encontrar difícil o imposible lograr la actitud de aterrizaje apropiada. El elevador puede carecer de autoridad suficiente para levantar la nariz adecuadamente, resultando en aterrizajes planos que imponen estrés excesivo sobre el tren de aterrizaje y la estructura del fuselaje.

**La dificultad del flare** se intensifica a medida que el CG se desplaza más hacia adelante. Los pilotos deben aplicar presión hacia atrás creciente para lograr la misma actitud de nariz arriba, y en casos extremos, la deflexión total del elevador puede ser insuficiente para ejecutar el flare apropiadamente. Esto fuerza ángulos de aproximación más pronunciados y velocidades de toma de contacto más altas, ambas comprometiendo los márgenes de seguridad del aterrizaje.

> **Consideración Crítica de Aterrizaje**: Las aeronaves cargadas en o cerca de los límites de CG adelantado requieren distancias de aterrizaje más largas y pueden exhibir rendimiento pobre de motor y al aire debido a la autoridad reducida del elevador durante operaciones de alto ángulo de ataque.

**Las tendencias de volcado hacia adelante** afectan particularmente de manera severa a las aeronaves con rueda de cola. Durante operaciones en tierra, especialmente al frenar u operar sobre superficies blandas, la carga de CG adelantado aumenta la probabilidad de que la aeronave se incline hacia adelante sobre su nariz. Este riesgo se agrava durante aterrizajes con viento cruzado donde las entradas de control direccional pueden desestabilizar la aeronave.

Fuerzas de control más altas a lo largo de todas las fases del vuelo caracterizan las operaciones de CG adelantado. Los pilotos experimentan mayor carga de trabajo y fatiga ya que se requiere presión hacia atrás continua para mantener vuelo nivelado. Esta condición reduce los márgenes de seguridad al hacer el control preciso más difícil y aumentar la carga de trabajo del piloto durante fases críticas del vuelo.

### Efectos del Límite de CG Atrasado y Preocupaciones de Estabilidad

**Las condiciones de CG atrasado** crean características de vuelo fundamentalmente diferentes pero igualmente peligrosas centradas alrededor de la estabilidad longitudinal reducida. A medida que el centro de gravedad se mueve hacia atrás, la aeronave se vuelve cada vez más inestable y difícil de controlar, con efectos que pueden rápidamente sobrepasar las capacidades del piloto.

**La estabilidad longitudinal reducida** se manifiesta como la tendencia disminuida de la aeronave a regresar a condiciones de vuelo trimado después de una perturbación. Las aeronaves normales están diseñadas con ligeras características de nariz pesada que proporcionan estabilidad inherente. La carga de CG atrasado reduce o elimina este margen de estabilidad, requiriendo atención constante del piloto para mantener el vuelo controlado.

La aeronave exhibe **fuerzas de control ligeras** que inicialmente pueden parecer deseables pero en realidad representan un riesgo serio de seguridad. Estas fuerzas de control reducidas hacen fácil para los pilotos sobre-controlar la aeronave o inadvertidamente exceder limitaciones de diseño. Pequeñas entradas de control producen grandes respuestas de la aeronave, haciendo el control preciso de la trayectoria de vuelo extremadamente difícil.

**La capacidad reducida de recuperación de pérdida** representa uno de los aspectos más peligrosos de la carga de CG atrasado. La carga descendente reducida sobre el estabilizador horizontal disminuye su efectividad al romper la pérdida. La recuperación puede requerir más altitud, entradas de control más agresivas, o puede ser imposible si el CG está suficientemente atrasado.

> **Advertencia de Estabilidad**: Las aeronaves cargadas más allá de los límites de CG atrasado pueden exhibir características de vuelo inestables que no pueden ser controladas independientemente del nivel de habilidad del piloto. Algunas configuraciones pueden ser imposibles de recuperar desde ciertas actitudes de vuelo.

La sensibilidad de cabeceo aumenta dramáticamente con la carga de CG atrasado. La aeronave responde más rápidamente a las entradas del elevador, haciéndola propensa a oscilaciones inducidas por el piloto y sobre-control. Esta sensibilidad es particularmente peligrosa durante aproximación y aterrizaje cuando el control preciso de la trayectoria de vuelo es esencial.

### Dificultad de Control y Características de Pérdida

**Las características de pérdida** cambian dramáticamente cuando la aeronave está cargada fuera de los límites de CG aprobados, con la carga atrasada creando las condiciones más peligrosas. La progresión normal desde buffet pre-pérdida hasta pérdida completa puede ser eliminada, reemplazada por salida súbita e incontrolable del vuelo controlado.

Con carga de CG atrasado, **las características violentas de pérdida** pueden incluir caídas súbitas de ala, momentos rápidos de cabeceo hacia abajo, o barrenas irrecuperables. La aeronave puede entrar en pérdida sin advertencia, eliminando la oportunidad del piloto de reconocer y responder a indicaciones pre-pérdida. Las técnicas de recuperación que funcionan con carga apropiada de CG pueden ser inefectivas o imposibles.

**Las características de barrena** se deterioran significativamente con carga inadecuada de balance. Las aeronaves cargadas más allá de los límites de CG atrasado pueden entrar en barrenas más fácilmente y exhibir características de barrena plana que hacen la recuperación extremadamente difícil o imposible. La efectividad reducida de los controles de vuelo en estas condiciones limita las opciones de recuperación.

La carga de CG adelantado crea dificultades de control diferentes pero igualmente problemáticas. **La autoridad reducida del elevador** afecta no solo las operaciones de aterrizaje sino todas las fases del vuelo que requieren actitudes de nariz arriba. Las operaciones de vuelo lento se vuelven particularmente peligrosas ya que el elevador puede carecer de poder suficiente para mantener vuelo controlado a velocidades normales de aproximación.

**Las operaciones de alto ángulo de ataque** sufren de efectividad de control reducida con carga de CG adelantado. Los procedimientos de motor y al aire, maniobras de libramiento de obstáculos y procedimientos de emergencia que requieren rendimiento máximo pueden estar comprometidos o ser imposibles de ejecutar de manera segura.

La interacción entre dificultad de control y procedimientos de emergencia crea riesgos de seguridad compuestos. Los procedimientos que son manejables con carga apropiada pueden volverse imposibles cuando la aeronave está cargada fuera de los límites aprobados. Este factor debe considerarse durante la planificación de prevuelo, ya que las emergencias no pueden esperar por redistribución de peso.

### Limitaciones Estructurales y Operacionales

**El potencial de sobreesfuerzo** aumenta significativamente con carga inadecuada de balance, particularmente con condiciones de CG atrasado donde las fuerzas de control ligeras hacen fácil exceder limitaciones de diseño. Las fuerzas de control reducidas pueden enmascarar la magnitud de las entradas de control, llevando a los pilotos a imponer inadvertidamente cargas G excesivas sobre la estructura del fuselaje.

**Las limitaciones de factor de carga** se vuelven más críticas con carga inadecuada de CG. Las aeronaves cargadas fuera de límites aprobados pueden experimentar falla estructural a cargas G más bajas que aquellas con balance apropiado. El diseño del fabricante asume carga apropiada de CG al establecer límites G operacionales.

Las limitaciones operacionales se extienden más allá de las operaciones normales de vuelo para incluir restricciones sobre maniobras aprobadas y operaciones de vuelo. Las aeronaves cargadas fuera de límites de CG pueden estar prohibidas de ciertas maniobras, aproximaciones o procedimientos operacionales que serían aceptables con carga apropiada.

**Las características de flutter y vibración** pueden cambiar con carga extrema de CG, particularmente cuando se combinan con altas velocidades aerodinámicas. La distribución de masa alterada puede cambiar frecuencias naturales y potencialmente inducir oscilaciones destructivas a velocidades aerodinámicas por debajo de los límites normales de diseño.

> **Realidad de Emergencia**: Las situaciones de emergencia que serían manejables con peso y balance apropiados pueden volverse no sobrevivibles cuando se combinan con condiciones adversas de balance. La planificación de prevuelo debe considerar este margen de seguridad reducido.

**La degradación del rendimiento** agrava los riesgos de seguridad de la carga inadecuada de balance. El rendimiento reducido de ascenso, distancias de despegue más largas y capacidad degradada de motor y al aire reducen las opciones disponibles para los pilotos durante situaciones de emergencia. Estas limitaciones son particularmente críticas en aeropuertos de gran altitud de densidad o al operar cerca de obstáculos.

**Las consideraciones de situación de emergencia** resaltan la importancia crítica de la carga apropiada de balance. Las fallas de motor, mal funcionamientos del sistema y encuentros con clima adverso todos requieren rendimiento y controlabilidad máximos de la aeronave. Las aeronaves cargadas fuera de límites aprobados pueden carecer de los márgenes de rendimiento necesarios para el manejo exitoso de emergencias.

El efecto acumulativo de las condiciones adversas de balance crea riesgos de seguridad que exceden la suma de las limitaciones individuales. Cuando se combinan con otros factores reductores de rendimiento tales como gran altitud de densidad, pistas contaminadas o condiciones de emergencia, la carga inadecuada de balance puede transformar situaciones manejables en accidentes. Esta realidad enfatiza por qué el cumplimiento con las limitaciones de peso y balance no es opcional sino que representa un requisito fundamental de seguridad que nunca debe ser comprometido.

---

## REQUISITOS REGLAMENTARIOS Y GESTIÓN

Comprender y cumplir con las regulaciones de peso y balance es una responsabilidad fundamental para todos los pilotos. La Federal Aviation Administration (FAA) ha establecido requisitos integrales que rigen cómo deben operarse las aeronaves dentro de sus limitaciones certificadas de peso y balance. Estas regulaciones, combinadas con la documentación apropiada y los procedimientos de verificación periódica, forman la base de las operaciones seguras de aeronaves.

### Requisitos de 14 CFR Parte 91 y Responsabilidades del Piloto

**14 CFR Sección 91.9** establece el requisito fundamental de que el piloto al mando (PIC) debe cumplir con los límites operacionales especificados en el **Aircraft Flight Manual (AFM)** aprobado, marcas y placas. Aunque la Parte 91 no requiere explícitamente que los pilotos realicen cálculos de peso y balance antes de cada vuelo, la regulación exige el cumplimiento de las limitaciones de peso y balance de la aeronave según se publican en el AFM.

El **piloto al mando** tiene la responsabilidad última de asegurar que la aeronave esté cargada dentro de los límites aprobados antes del vuelo. Esta responsabilidad no puede delegarse al personal de tierra, pasajeros u otras partes. El PIC debe verificar que tanto el peso total no exceda los límites máximos permitidos como que el centro de gravedad se encuentre dentro del rango aprobado.

Bajo operaciones de la Parte 91, los pilotos deben tener acceso a datos actuales de peso y balance de su aeronave. Esto incluye comprender el **peso vacío** actual de la aeronave y el **centro de gravedad**, que pueden haber cambiado desde la fabricación debido a modificaciones de equipo, reparaciones o alteraciones. El piloto debe poder calcular el peso cargado y el CG basándose en las condiciones reales de carga para cada vuelo.

> **Responsabilidad Crítica**: Incluso si el personal de tierra proporciona cálculos de peso y balance, el PIC permanece legalmente responsable de verificar la precisión y asegurar el cumplimiento de las limitaciones.

La regulación se extiende más allá del simple cumplimiento para abarcar el deber del piloto de comprender cómo el peso y balance afectan el desempeño de la aeronave y las características de manejo. Esto incluye reconocer cuándo condiciones como la altitud de densidad alta pueden requerir operación por debajo del peso máximo certificado para mantener márgenes de desempeño adecuados.

### Documentación de Aeronaves y Fuentes de Datos

Los cálculos precisos de peso y balance dependen de documentación fuente confiable. Las fuentes principales de información de peso y balance incluyen el **Type Certificate Data Sheet (TCDS)**, el AFM o **Pilot's Operating Handbook (POH)**, y los registros actuales de peso y balance de la aeronave.

El **Type Certificate Data Sheet** contiene los datos de certificación originales para el tipo de aeronave, incluyendo pesos máximos, rango de CG y otras limitaciones establecidas durante el proceso de certificación. El TCDS proporciona la base reglamentaria para todas las limitaciones de peso y balance y no puede excederse sin importar las circunstancias.

El **Aircraft Flight Manual** o POH contiene información detallada de peso y balance específica para la configuración de la aeronave. Esto incluye gráficas de carga, métodos computacionales y problemas de muestra para asistir a los pilotos en la determinación del peso cargado y la posición del CG. La sección de limitaciones del AFM contiene límites operacionales legalmente vinculantes que no deben excederse.

Los registros específicos de peso y balance de la aeronave mantienen el **peso vacío** actual y el **centro de gravedad en peso vacío** para la aeronave individual. Estos registros deben actualizarse siempre que modificaciones, reparaciones o cambios de equipo afecten el peso o balance de la aeronave. Los registros típicamente incluyen una lista de equipos detallando todos los artículos instalados y su contribución al peso vacío y momento.

Las placas de peso y balance instaladas en la aeronave proporcionan información de referencia rápida para cálculos de carga. Estas placas a menudo incluyen tablas de carga simplificadas o gráficas que permiten a los pilotos determinar si su configuración de carga está dentro de los límites sin cálculos detallados.

> **Vigencia de la Documentación**: Los documentos de peso y balance deben reflejar la configuración actual de la aeronave. Usar información desactualizada puede conducir a cálculos incorrectos y condiciones de carga potencialmente inseguras.

### Requisitos de Pesaje e Intervalos de Inspección

Los requisitos de pesaje de aeronaves varían significativamente según el tipo de operación y categoría de aeronave. Comprender estos requisitos es esencial para mantener datos precisos de peso y balance a lo largo del tiempo.

**Las operaciones de la Parte 125** requieren que las aeronaves con 20 o más asientos o capacidad de carga útil máxima de 6,000 libras o más sean pesadas cada **36 meses calendario**. Este requisito asegura que los efectos acumulados de modificaciones, reparaciones y cambios de equipo no alteren significativamente las características de peso y balance de la aeronave.

**Las aeronaves multimotores de la Parte 135** también están sujetas al requisito de pesaje de 36 meses a menos que operen bajo un programa aprobado de control de peso y balance especificado en las especificaciones de operaciones del operador. Estos programas aprobados pueden permitir métodos alternativos para rastrear cambios de peso y balance sin pesaje periódico.

Las operaciones de la Parte 91 no están sujetas a requisitos obligatorios de pesaje periódico. Sin embargo, **Advisory Circular 43.13-1** recomienda que los mecánicos de aeronaves aseguren la precisión de los datos de peso y balance durante las inspecciones anuales o de 100 horas. Esta verificación ayuda a identificar cualquier discrepancia que pueda haberse acumulado desde el último pesaje formal.

El proceso de pesaje debe realizarse utilizando básculas certificadas y procedimientos que consideren la cantidad de combustible, niveles de aceite y configuración de equipos. Las aeronaves típicamente se pesan en la condición de **peso vacío**, que incluye combustible inutilizable, aceite no drenado y todo el equipo instalado permanentemente.

El pesaje profesional de aeronaves requiere condiciones ambientales y procedimientos específicos. La aeronave debe estar en actitud nivelada, protegida del viento y posicionada para permitir lecturas precisas de las básculas. Todo el equipo removible debe ser contabilizado, y los tanques de combustible deben contener solo cantidades inutilizables de combustible.

> **Precisión del Pesaje**: Los procedimientos de pesaje inadecuados pueden introducir errores significativos en los cálculos de peso y balance. Solo el personal calificado usando equipo apropiado debe conducir operaciones de pesaje de aeronaves.

### Criterios de Cambio de Peso Despreciable

No toda modificación o reparación requiere un recálculo completo de peso y balance. **Advisory Circular 43.13-1** establece criterios específicos para determinar cuándo los cambios de peso se consideran despreciables y no requieren verificación formal de peso y balance.

Para **aeronaves de ala fija**, los criterios de cambio de peso despreciable se basan en categorías de peso vacío:
- **Una libra o menos** para aeronaves con peso vacío menor a 5,000 libras
- **Dos libras o menos** para aeronaves con peso vacío entre 5,000 y 50,000 libras
- **Cinco libras o menos** para aeronaves con peso vacío que exceda 50,000 libras

**El cambio despreciable del centro de gravedad** se define como cualquier cambio menor a **0.05 por ciento de Mean Aerodynamic Chord (MAC)** para aeronaves de ala fija o 0.2 por ciento para aeronaves de ala rotatoria. El **Mean Aerodynamic Chord** representa la distancia promedio desde el borde de ataque del ala hasta el borde de salida y proporciona una referencia estandarizada para cálculos de CG.

Las partes estándar como tuercas, tornillos, arandelas, remaches y herrajes similares típicamente caen dentro de los criterios de peso despreciable. Sin embargo, debe considerarse el efecto acumulativo de múltiples cambios pequeños. Si se realizan varias modificaciones menores a lo largo del tiempo, su cambio de peso combinado puede exceder los criterios despreciables.

Los estándares de peso despreciable se aplican solo a modificaciones o reparaciones individuales. No permiten exceder los límites de peso máximo de la aeronave o los límites de rango de CG. Incluso si un cambio de peso es despreciable, la aeronave debe operar aún dentro de sus limitaciones certificadas.

> **Efectos Acumulativos**: Múltiples cambios de peso despreciables pueden acumularse para crear errores significativos en los datos de peso y balance. La verificación periódica permanece importante incluso cuando los cambios individuales parecen menores.

Los criterios de peso despreciable proporcionan pautas prácticas para operaciones de mantenimiento mientras aseguran que la seguridad de vuelo no se vea comprometida. Los mecánicos y pilotos deben comprender estos estándares para tomar decisiones apropiadas sobre cuándo se requieren actualizaciones formales de peso y balance.

Los fabricantes de aeronaves pueden establecer criterios más restrictivos que aquellos especificados en AC 43.13-1. Cuando la guía del fabricante entra en conflicto con los estándares de circular consultiva, deben seguirse los requisitos más restrictivos. Algunos tipos de aeronaves, particularmente aquellos con características críticas de peso y balance, pueden requerir cálculos formales para cualquier cambio de peso.

Comprender los requisitos reglamentarios y los procedimientos apropiados de documentación forma la base para una gestión segura de peso y balance. Los pilotos que comprenden estos requisitos y mantienen datos actuales y precisos están mejor preparados para tomar decisiones sólidas de carga y operar sus aeronaves de manera segura dentro de las limitaciones aprobadas.

---

## TERMINOLOGÍA DE PESO Y BALANCE

Comprender la terminología adecuada de peso y balance es fundamental para la operación segura de aeronaves. La industria aeronáutica ha establecido definiciones estandarizadas a través de organizaciones como la **General Aviation Manufacturers Association (GAMA)** para asegurar consistencia entre fabricantes y operadores. Estos términos forman la base para todos los cálculos de peso y balance y el cumplimiento regulatorio.

### Definiciones Básicas de Peso y Estándares GAMA

La industria aeronáutica utiliza categorías específicas de peso que distinguen entre diferentes condiciones de carga de la aeronave. El **peso vacío básico** representa el peso vacío estándar más cualquier equipo opcional y especial instalado en la aeronave. Este término estandarizado por GAMA difiere del antiguo **peso vacío licenciado**, que algunos fabricantes utilizaban antes de los esfuerzos de estandarización de la industria.

El **peso vacío estándar** forma la línea base para todos los cálculos de peso. Este término definido por GAMA abarca la estructura, los motores y todo el equipo operativo instalado permanentemente con ubicaciones fijas. Incluye lastre fijo, fluido hidráulico, combustible no utilizable y aceite de motor completo. El peso vacío estándar excluye específicamente el combustible utilizable, el aceite que puede drenarse, la tripulación, los pasajeros y el equipaje.

La distinción entre peso vacío básico y peso vacío estándar es crucial para cálculos precisos. Mientras que el peso vacío estándar representa la aeronave principal con fluidos esenciales, el peso vacío básico agrega el equipo opcional instalado por el fabricante que varía entre aeronaves individuales del mismo modelo.

La **carga útil** representa el peso total disponible para elementos específicos de la misión, incluyendo piloto, pasajeros, equipaje y combustible utilizable. Este peso es igual al peso bruto máximo permitido menos el peso vacío básico. Comprender las limitaciones de carga útil es esencial ya que muchas aeronaves no pueden transportar simultáneamente pasajeros máximos, combustible completo y equipaje mientras permanecen dentro de los límites de peso.

La **carga de pago**, según lo definido por los estándares GAMA, se refiere específicamente al peso de los ocupantes, carga y equipaje, excluyendo el peso del combustible. Esta distinción ayuda a los pilotos a separar las consideraciones humanas y de carga de los requisitos de planificación de combustible.

### Cálculos de Momento y Brazo

El **momento** representa el cálculo fundamental en el trabajo de peso y balance, expresado como el producto del peso multiplicado por la distancia del brazo. Los momentos se miden en libras-pulgadas (in-lb) e indican la fuerza rotacional que el peso crea alrededor del punto de balance de la aeronave.

El **brazo** o brazo de momento mide la distancia horizontal en pulgadas desde la línea de referencia datum hasta el centro de gravedad de cualquier elemento. Los brazos llevan signos algebraicos: positivo (+) cuando se mide hacia popa del datum y negativo (-) cuando se mide hacia adelante. Esta convención de signos asegura precisión matemática en los cálculos de balance.

El **índice de momento** simplifica los cálculos dividiendo los momentos por constantes como 100, 1,000 o 10,000. Las aeronaves con componentes pesados y distancias de brazo largas generan números grandes y difíciles de manejar que se vuelven manejables mediante la indexación de momentos. Por ejemplo, un momento de 2,847,000 in-lb se convierte en 2,847 al usar un divisor de 1,000.

El momento total es igual al peso de la aeronave multiplicado por la distancia entre el datum y el centro de gravedad. Esta relación permite a los pilotos determinar el punto de balance de la aeronave dividiendo los momentos totales por el peso total, produciendo la ubicación del centro de gravedad en pulgadas desde el datum.

> **Cálculo Crítico**: Peso × Brazo = Momento. Esta relación fundamental impulsa todos los cálculos de peso y balance y debe aplicarse a cada elemento cargado a bordo de la aeronave.

### Conceptos de Datum de Referencia y Estación

El **datum** o datum de referencia establece un plano vertical imaginario desde el cual se originan todas las mediciones de brazo. Los fabricantes de aeronaves seleccionan este punto de referencia arbitrario, que permanece fijo durante toda la vida útil de la aeronave. Una vez establecido, todos los brazos de momento y rangos de centro de gravedad hacen referencia a este punto datum, identificado como estación cero.

Los números de **estación** identifican ubicaciones específicas dentro de la aeronave designando la distancia en pulgadas desde el datum. Un elemento ubicado en la estación +50 tiene un brazo de 50 pulgadas hacia popa del datum, mientras que la estación -20 indica una posición 20 pulgadas hacia adelante del datum. Este sistema de estaciones proporciona puntos de referencia precisos para los cálculos de peso y balance.

La **Cuerda Aerodinámica Media (MAC)** representa la distancia promedio desde el borde de ataque del ala hasta el borde de fuga. Aunque se utiliza principalmente en expresiones de centro de gravedad para aeronaves más grandes, el MAC se vuelve importante para determinar cambios de balance insignificantes. Según la Circular Asesor 43.13-1, los cambios menores al 0.05 por ciento del MAC para aeronaves de ala fija no requieren recalculación de peso y balance.

La ubicación del datum varía significativamente entre fabricantes y modelos de aeronaves. Algunos fabricantes colocan el datum en el cortafuegos, otros en el borde de ataque del ala, y algunos usan puntos adelante del morro de la aeronave. Independientemente de la ubicación, todos los cálculos deben hacer referencia al datum establecido por el fabricante para mayor precisión.

**Delta (Δ)** representa el cambio en los cálculos de peso y balance, utilizando el símbolo de letra griega para indicar cambios de valor. Por ejemplo, ΔCG indica movimiento del centro de gravedad, mientras que Δpeso muestra el cambio de peso durante las operaciones de vuelo.

### Pesos Estándar y Especificaciones de Combustible

La aviación utiliza **pesos estándar** establecidos para fluidos y materiales comunes cuando los pesos reales no están disponibles. Estos valores estandarizados aseguran consistencia en toda la industria, pero nunca deben reemplazar las mediciones reales cuando estén disponibles.

El **AVGAS** (gasolina de aviación) pesa 6.0 libras por galón estadounidense, lo que lo convierte en el peso de combustible más común para aeronaves con motor de pistón. Este peso se aplica a todos los grados de gasolina de aviación, incluyendo combustibles de 80/87, 100LL y 100 octanos utilizados en aviación general.

El combustible **Jet A y Jet A-1** pesa 6.8 libras por galón estadounidense, representando el estándar para aeronaves con motor de turbina. Estos combustibles mantienen características de peso consistentes en rangos de temperatura típicamente encontrados en operaciones de aviación.

El combustible **Jet B**, menos comúnmente utilizado, pesa 6.5 libras por galón estadounidense. El aceite pesa 7.5 libras por galón estadounidense, mientras que el agua pesa 8.35 libras por galón estadounidense. Estos pesos estándar permiten cálculos rápidos durante la planificación de vuelo y ajustes de peso.

> **Verificación de Realidad del Peso del Combustible**: Treinta galones de AVGAS pesan 180 libras, equivalente a un pasajero grande. El peso del combustible impacta significativamente tanto el peso total de la aeronave como los cálculos de balance.

La **carga de combustible** se refiere específicamente solo al combustible utilizable, excluyendo el combustible atrapado en líneas, sumideros o áreas de tanque no utilizables. Esta distinción evita que los pilotos cuenten el combustible no utilizable hacia los cálculos de carga de pago mientras aseguran reservas adecuadas para las operaciones de vuelo.

El **peso máximo en rampa** excede el peso máximo de despegue para tener en cuenta el combustible quemado durante el rodaje, la prueba de motores y las operaciones previas al despegue. Típicamente, las aeronaves queman de 10 a 30 libras de combustible antes del despegue, dependiendo del tiempo de rodaje y los requisitos de prueba de motor.

El **peso máximo de despegue** representa el peso máximo permitido al liberar los frenos para el despegue. Esta limitación considera cargas estructurales, requisitos de desempeño y estándares de certificación establecidos durante las pruebas de la aeronave.

El **peso máximo de aterrizaje** puede ser menor que el peso de despegue debido a consideraciones estructurales durante el impacto del aterrizaje. Las aeronaves que exceden el peso máximo de aterrizaje deben quemar combustible o descargar combustible (donde estén equipadas) antes del aterrizaje para prevenir daño estructural.

El **peso máximo sin combustible** limita el peso de la aeronave excluyendo el combustible utilizable. Esta limitación previene momentos de flexión excesivos en las estructuras del ala cuando los tanques de combustible están vacíos. El peso sin combustible se vuelve crítico durante las decisiones de carga de carga y ubicación de pasajeros.

Los **límites de carga del piso** especifican el peso máximo por pulgada o pie cuadrado que los pisos de la aeronave pueden sostener. Estos límites previenen daño estructural de cargas de carga concentradas y deben considerarse al cargar elementos densos como repuestos o maquinaria.

La relación entre estas categorías de peso crea limitaciones operacionales que los pilotos deben comprender. Una aeronave puede alcanzar el peso máximo sin combustible antes de alcanzar el peso máximo de despegue, requiriendo reducción de combustible para acomodar pasajeros o carga adicionales. Alternativamente, las limitaciones estructurales o de desempeño pueden prevenir operaciones de peso máximo de despegue bajo ciertas condiciones ambientales.

Comprender estos términos estandarizados y sus definiciones precisas permite a los pilotos realizar cálculos precisos de peso y balance, cumplir con los requisitos regulatorios y operar aeronaves de manera segura dentro de las limitaciones certificadas. Estos conceptos forman la base para todos los procedimientos y cálculos posteriores de peso y balance requeridos para operaciones de vuelo seguras.

---

## PRINCIPIOS DE CÁLCULO DE PESO Y BALANCE

La determinación exitosa de la condición de peso y balance de una aeronave se basa en la aplicación de principios matemáticos fundamentales y métodos computacionales sistemáticos. Estos principios forman la base para todos los cálculos de peso y balance, independientemente del tipo de aeronave o su complejidad. Comprender estos métodos computacionales es esencial para que los pilotos aseguren operaciones de vuelo seguras y el cumplimiento de los límites certificados.

El proceso computacional involucra tres elementos primarios: peso, brazo y momento. Estos elementos trabajan juntos a través de relaciones matemáticas básicas para determinar la ubicación del centro de gravedad de la aeronave. La precisión de estos cálculos impacta directamente la seguridad del vuelo, haciendo que el dominio de estos principios sea una habilidad crítica para el piloto.

### Principios Matemáticos Básicos y Cálculos de Momento

La base de todos los cálculos de peso y balance descansa en una fórmula simple pero crítica: **Peso × Brazo = Momento**. Esta relación expresa la fuerza gravitacional que causa una tendencia del peso a rotar alrededor de un punto o eje. En aplicaciones aeronáuticas, este punto es el centro de gravedad, y comprender esta tendencia rotacional es esencial para los cálculos apropiados de balance.

Los **momentos** son la expresión matemática de esta fuerza rotacional y se miden en **pulgadas-libra (in-lb)**. Para calcular un momento, multiplique el peso de cualquier elemento por su distancia desde el dato de referencia. Por ejemplo, un pasajero de 50 libras sentado a 85 pulgadas detrás del dato crea un momento de 4,250 in-lb (50 × 85 = 4,250).

El momento total de una aeronave representa la suma de todos los momentos individuales de los elementos. Este momento total, cuando se divide por el peso total de la aeronave, produce la ubicación del centro de gravedad. La expresión matemática es: **CG = Momentos Totales ÷ Peso Total**. Este cálculo proporciona la ubicación del punto de balance en pulgadas desde el punto de referencia del dato.

> **Fórmula Crítica**: La relación de peso y balance puede reorganizarse para resolver cualquier variable desconocida: Peso = Momento ÷ Brazo, o Brazo = Momento ÷ Peso. Estas variaciones resultan útiles al determinar desplazamientos de peso requeridos o al trabajar hacia atrás desde ubicaciones de CG deseadas.

Las aeronaves grandes o escenarios de carga complejos a menudo involucran números sustanciales que se vuelven difíciles de manejar en los cálculos. Para simplificar estos cómputos, los fabricantes pueden usar un sistema de **índice de momento**, dividiendo los momentos por constantes como 100, 1,000 o 10,000. Esta indexación reduce números grandes a cifras manejables sin afectar la precisión de los cálculos de CG. Al usar momentos indexados, todos los cálculos siguen los mismos principios, pero la determinación final del CG usa los valores indexados.

### Sistema de Referencia de Dato y Ubicaciones de Estación

El **dato** sirve como el punto de referencia fundamental para todas las mediciones de peso y balance. Este plano vertical imaginario es establecido por el fabricante de la aeronave y permanece fijo durante toda la vida operacional de la aeronave. La ubicación del dato varía entre modelos de aeronaves y se selecciona por conveniencia computacional más que por cualquier característica física específica.

Una vez establecido, el dato se convierte en la **estación cero**, y todas las demás ubicaciones se miden como distancias desde este punto de referencia. Estas mediciones crean el sistema de **estación**, donde cualquier ubicación en la aeronave se identifica por su distancia en pulgadas desde el dato. Por ejemplo, la estación 85 indica un punto ubicado a 85 pulgadas del dato de referencia.

El dato puede ubicarse en varias posiciones relativas a la estructura de la aeronave. Algunos fabricantes lo colocan en el cortafuegos, mientras que otros lo posicionan adelante de la nariz de la aeronave o en el borde de ataque del ala. En algunos casos, el dato se coloca bien adelante de la aeronave para asegurar que todas las mediciones resulten en números positivos, simplificando los cálculos.

Las estaciones de la aeronave típicamente se marcan a intervalos regulares a lo largo de la estructura, a menudo cada 10 o 20 pulgadas. Estas marcas asisten al personal de mantenimiento y a los pilotos en determinar la ubicación precisa de equipos, carga o pasajeros para propósitos de peso y balance. El sistema de estación proporciona un método estandarizado para identificar ubicaciones independientemente de cambios en la configuración de la aeronave.

### Métodos de Determinación del Punto de Balance

Determinar el punto de balance de la aeronave requiere el cálculo sistemático de todos los pesos y sus momentos correspondientes. El proceso comienza con establecer el **peso vacío** y el **momento de peso vacío** de los registros de peso y balance de la aeronave. Estos valores de referencia incluyen la estructura de la aeronave, motores, equipo requerido, combustible no utilizable y aceite completo.

El método computacional involucra enumerar el peso y brazo de cada elemento, luego calcular los momentos individuales. Considere una aeronave con la siguiente carga:

- Peso vacío: 2,100 libras en brazo 78.3 pulgadas = 164,430 in-lb
- Ocupantes delanteros: 340 libras en brazo 85.0 pulgadas = 28,900 in-lb  
- Ocupantes traseros: 350 libras en brazo 121.0 pulgadas = 42,350 in-lb
- Combustible: 450 libras en brazo 75.0 pulgadas = 33,750 in-lb
- Equipaje: 80 libras en brazo 150.0 pulgadas = 12,000 in-lb

El peso total es igual a 3,320 libras, y los momentos totales son iguales a 281,430 in-lb. La ubicación del CG es 281,430 ÷ 3,320 = 84.8 pulgadas detrás del dato.

> **Analogía de la Tabla de Balance**: Los cálculos de peso y balance reflejan un sistema simple de palanca y fulcro. Si coloca pesos en extremos opuestos de una tabla balanceada sobre un fulcro, la tabla se balanceará cuando los momentos en cada lado sean iguales. Este mismo principio se aplica al balance de aeronaves.

Los métodos alternativos incluyen soluciones gráficas proporcionadas por los fabricantes en el Aircraft Flight Manual. Estos gráficos eliminan la necesidad de cálculos manuales de momentos al proporcionar representaciones visuales de las relaciones entre peso y momento. El piloto ingresa cada condición de carga en el gráfico apropiado, lee el momento correspondiente y grafica los valores finales en una envolvente de centro de gravedad para verificar los límites aceptables.

### Cálculos de Brazo Positivo y Negativo

La convención de signo algebraico para las mediciones de brazo crea valores positivos o negativos dependiendo de la ubicación del elemento en relación con el dato. Las mediciones **detrás del dato** reciben **valores positivos (+)**, mientras que las mediciones **adelante del dato** reciben **valores negativos (-)** . Esta convención de signo afecta directamente los cálculos de momento y debe aplicarse cuidadosamente.

Cuando un elemento está ubicado adelante del dato, su brazo negativo crea un momento negativo que reduce la suma total de momentos. Por ejemplo, si el aceite de 11 libras está ubicado en la estación -31 (31 pulgadas adelante del dato), el cálculo del momento se convierte en: 11 × (-31) = -341 in-lb. Este momento negativo se resta del momento total al determinar la ubicación del CG.

La relación matemática sigue las reglas algebraicas estándar: peso positivo multiplicado por brazo positivo es igual a momento positivo, mientras que peso positivo multiplicado por brazo negativo es igual a momento negativo. Estas convenciones de signo aseguran la representación precisa del efecto del elemento en el punto de balance de la aeronave.

Los elementos ubicados adelante, como compartimentos de equipaje de nariz o accesorios del motor, comúnmente generan brazos y momentos negativos. Los depósitos de aceite, baterías y equipos de aviónica también pueden caer adelante del dato dependiendo de la selección del dato del fabricante. Los pilotos deben observar cuidadosamente las convenciones de signo al realizar cálculos para evitar errores que podrían resultar en determinaciones incorrectas del CG.

> **Verificación de Cálculo**: Al revisar cálculos de peso y balance, verifique que los elementos ubicados adelante del punto de balance aparente de la aeronave muestren brazos negativos, mientras que los elementos ubicados detrás muestren brazos positivos. Esto proporciona una verificación lógica contra errores de cálculo.

Considere una aeronave donde el aceite del motor está ubicado adelante del dato:
- Peso del aceite: 15 libras
- Brazo del aceite: -25 pulgadas (adelante del dato)  
- Momento del aceite: 15 × (-25) = -375 in-lb

Este momento negativo reduce el momento total de la aeronave, desplazando el CG hacia adelante. Al realizar el cálculo final del CG, este momento negativo se suma algebraicamente a (en realidad se resta de) los momentos positivos de otros elementos. El manejo apropiado de brazos positivos y negativos asegura la determinación precisa del CG y la operación segura de la aeronave.

El sistema de estación acomoda mediciones tanto positivas como negativas a través de una notación cuidadosa. Las estaciones adelante del dato pueden designarse como estaciones negativas o identificarse con notación específica indicando su ubicación delantera. Independientemente del método de notación, los valores de brazo utilizados en los cálculos de momento deben reflejar el signo algebraico apropiado para asegurar la precisión computacional.

---

## MÉTODOS DE CÁLCULO DE PESO Y BALANCE

Determinar el peso y balance de una aeronave requiere la aplicación sistemática de métodos de cálculo comprobados. Los pilotos deben dominar estos procedimientos para garantizar operaciones de vuelo seguras y el cumplimiento de los requisitos regulatorios. Los tres métodos principales para los cálculos de peso y balance son el **método computacional**, **método gráfico** y **método de tabla**, cada uno utilizando el principio fundamental de que la ubicación del centro de gravedad es igual al momento total dividido por el peso total.

Todos los métodos de cálculo se basan en la relación matemática básica entre peso, brazo y momento. El **momento** representa el producto del peso multiplicado por su distancia de brazo desde el datum. Cuando todos los momentos individuales se suman y se dividen por el peso total, el resultado determina la ubicación del centro de gravedad de la aeronave. Esta ubicación del CG debe estar dentro de la envolvente especificada por el fabricante para operaciones de vuelo seguras.

### Método Computacional con Procedimientos Paso a Paso

El método computacional proporciona el enfoque más directo para los cálculos de peso y balance utilizando operaciones matemáticas básicas. Este método requiere que los pilotos calculen manualmente los momentos para cada ítem de peso y determinen sistemáticamente el peso total de la aeronave y la ubicación del centro de gravedad.

El procedimiento paso a paso comienza con el establecimiento del peso vacío actual de la aeronave y el momento de los registros de peso y balance. El **peso vacío básico** incluye la estructura, los motores, el combustible inutilizable, el aceite no drenado y todo el equipo instalado permanentemente. Esta información aparece en la lista de equipamiento de la aeronave y la documentación de peso y balance.

**Paso 1: Listar todos los ítems de peso** incluyendo el peso vacío básico, ocupantes, combustible y equipaje. La gasolina de aviación pesa 6 libras por galón, mientras que el combustible Jet A pesa 6.8 libras por galón. Use pesos reales cuando estén disponibles en lugar de pesos estándar. Para los ocupantes, use pesos reales en lugar de asumir pesos estándar de 170 libras para adultos.

**Paso 2: Determinar el brazo para cada ítem de peso** utilizando la información de carga de la aeronave. Los brazos se miden en pulgadas desde el datum de referencia, con valores positivos hacia atrás del datum y valores negativos hacia adelante del datum. Los valores de brazo típicos para aeronaves pequeñas incluyen asientos del piloto y pasajero delantero a 85 pulgadas, asientos traseros a 121 pulgadas y áreas de equipaje entre 140-160 pulgadas.

**Paso 3: Calcular momentos para cada ítem** multiplicando peso por brazo (Peso × Brazo = Momento). Exprese los momentos en libras-pulgada. Por ejemplo, 340 libras de ocupantes del asiento delantero a brazo 85 pulgadas produce un momento de 28,900 libras-pulgada. Los brazos negativos producen momentos negativos que reducen el momento total.

**Paso 4: Sumar todos los pesos y momentos** para determinar los totales. Sume todos los pesos individuales para encontrar el peso total de la aeronave. Sume todos los momentos individuales (considerando signos algebraicos para momentos negativos) para determinar el momento total. Verifique que el peso total no exceda el peso bruto máximo permitido.

**Paso 5: Calcular la ubicación del centro de gravedad** dividiendo el momento total por el peso total (CG = Momento Total ÷ Peso Total). Exprese el resultado en pulgadas desde el punto de referencia del datum. Para el ejemplo anterior con peso total de 3,320 libras y momento total de 281,430 libras-pulgada: CG = 281,430 ÷ 3,320 = 84.8 pulgadas.

**Paso 6: Verificar que el CG esté dentro de los límites** comparando la ubicación del CG calculada con los límites de CG delantero y trasero especificados por el fabricante. Si el CG cae fuera de estos límites, el peso debe redistribuirse o removerse antes del vuelo. La aeronave es aceptable para el vuelo solo cuando tanto el peso como el CG están dentro de los límites aprobados.

> **Ventajas del Método Computacional**: Proporciona resultados de cálculo directos, no requiere gráficos o tablas especiales, funciona para cualquier configuración de aeronave y construye comprensión de las relaciones de peso y balance.

### Método Gráfico Usando Gráficos del Fabricante

El método gráfico simplifica los cálculos de peso y balance mediante el uso de gráficos proporcionados por el fabricante que eliminan los cálculos manuales de momento. Este método resulta particularmente útil para aeronaves complejas o cuando se realizan múltiples escenarios de carga de manera rápida y precisa.

**Los gráficos de carga** permiten a los pilotos determinar momentos trazando valores de peso contra componentes específicos de la aeronave [Figura 10-7: Gráfico de Carga - PHAK Cap 10, Fig 10-7]. Estos gráficos típicamente muestran el peso en un eje y el momento en el otro eje, con líneas o curvas separadas para diferentes componentes de la aeronave como ocupantes, combustible y equipaje.

Para usar gráficos de carga, localice el valor del peso en el eje horizontal y dibuje una línea vertical hacia arriba hasta que intersecte la línea del componente apropiado (piloto/pasajero delantero, pasajeros traseros, combustible o equipaje). Desde este punto de intersección, dibuje una línea horizontal hacia el eje vertical de momento para leer el valor del momento. El concepto de **índice de momento** a menudo divide los momentos por 1,000 para producir números más manejables.

Para cálculos de combustible, curvas separadas representan diferentes configuraciones de tanques de combustible. Los tanques estándar, tanques de largo alcance y tanques auxiliares cada uno tiene características de momento distintas basadas en sus ubicaciones físicas en la aeronave. Los pilotos deben seleccionar la línea de combustible apropiada que coincida con la configuración de tanques de su aeronave.

El **gráfico de envolvente de CG** proporciona verificación visual de los límites de carga [Figura 10-8: Envolvente de Momento del CG - PHAK Cap 10, Fig 10-8]. Trace el peso total de la aeronave en un eje y el momento total (o índice de momento) en el otro eje. El punto de intersección debe caer dentro del área de envolvente cerrada que representa combinaciones aceptables de peso y balance.

Las aeronaves de **categoría normal** y **categoría utilitaria** pueden tener diferentes límites de envolvente reflejando limitaciones operacionales. Las operaciones de categoría normal permiten maniobras estándar, mientras que la categoría utilitaria permite vuelo acrobático limitado. La envolvente de categoría utilitaria es típicamente más restrictiva, requiriendo un rango de CG más adelantado.

**Las técnicas de interpolación** se hacen necesarias cuando valores exactos de peso no aparecen en las líneas del gráfico. Para valores intermedios, estime proporcionalmente entre los puntos trazados más cercanos. Por ejemplo, si busca el momento para 325 libras cuando el gráfico muestra 300 y 350 libras, interpole a medio camino entre esos valores de momento.

> **Beneficios del Método Gráfico**: Representación visual de límites de carga, errores de cálculo reducidos, comparación rápida de múltiples escenarios de carga y verificación inmediata de envolvente.

### Método de Tabla y Placas de Programa de Carga

El método de tabla utiliza programas de carga proporcionados por el fabricante y tablas de momento para determinar peso y balance [Figura 10-9: Placa de Programa de Carga - PHAK Cap 10, Fig 10-9]. Estas tablas aparecen como placas en la cabina de la aeronave o dentro del manual de operación del piloto, proporcionando referencia rápida para cálculos de carga de rutina.

**Las placas de programa de carga** contienen valores de momento tabulados para incrementos de peso estándar de ocupantes, combustible y equipaje. Estas tablas eliminan la necesidad de cálculos manuales de momento al proporcionar valores precalculados. Los pilotos simplemente localizan el valor de peso apropiado y leen el momento correspondiente directamente de la tabla.

Las tablas de momento de ocupantes típicamente proporcionan momentos para rangos de peso en incrementos de 10 o 20 libras. Por ejemplo, una tabla de ocupantes del asiento delantero podría mostrar momentos para pesos desde 100 hasta 400 libras. Se requiere **interpolación** para pesos que caen entre valores tabulados. Al cargar 185 libras donde la tabla muestra 180 y 190 libras, calcule el momento proporcional entre esos valores.

**Las tablas de momento de combustible** contabilizan el peso del combustible a 6 libras por galón para gasolina de aviación. Estas tablas muestran tanto galones como pesos correspondientes con sus momentos asociados. Los pilotos deben asegurarse de que referencian la configuración de tanque de combustible correcta, ya que los tanques de ala y tanques auxiliares tienen diferentes distancias de brazo y características de momento.

**Los límites máximos de momento** aparecen en las tablas de carga, definiendo los límites de CG delantero y trasero para varios pesos de aeronave. Estos límites típicamente varían con el peso total de la aeronave, mostrando rangos de CG más restrictivos a pesos más altos. El formato de tabla presenta momentos mínimos y máximos permitidos para rangos de peso, típicamente en incrementos de 50 o 100 libras.

**Las limitaciones de peso sin combustible** aparecen en muchas tablas de aeronaves de categoría de transporte, restringiendo el peso máximo de la aeronave sin combustible. Esta limitación previene daño estructural por momentos de flexión de ala excesivos cuando los tanques de combustible están vacíos. El peso total de ocupantes, equipaje y carga no puede exceder el peso sin combustible especificado.

### Interpretación de la Envolvente del CG

La **envolvente del CG** representa las combinaciones aprobadas de peso de la aeronave y ubicación del centro de gravedad a lo largo del rango de peso operacional [Figura 10-8: Envolvente de Momento del CG - PHAK Cap 10, Fig 10-8]. Comprender la interpretación de la envolvente es crítico para determinar condiciones de carga aceptables y categorías operacionales.

**Los límites de CG delantero** típicamente siguen una línea recta o ligeramente curvada en el lado izquierdo de la envolvente. Estos límites aseguran autoridad adecuada del elevador para el redondeo en aterrizaje y previenen cargas excesivas en la rueda de nariz durante operaciones en tierra. El límite delantero puede volverse más restrictivo a pesos más altos debido a limitaciones de efectividad del elevador.

**Los límites de CG trasero** forman el límite derecho de la envolvente y pueden variar significativamente con el peso de la aeronave. Estos límites mantienen estabilidad longitudinal adecuada y previenen condiciones peligrosas de cola pesada. El límite trasero a menudo se vuelve más restrictivo a pesos más ligeros para preservar márgenes de estabilidad durante operaciones normales.

**Las limitaciones de peso** aparecen como límites horizontales en la envolvente. El límite superior representa el peso bruto máximo para la categoría de operación aplicable. Algunas aeronaves tienen diferentes pesos máximos para despegue, aterrizaje y condiciones sin combustible. El límite inferior típicamente representa el peso mínimo para cumplimiento de certificación.

**Las variaciones de forma de la envolvente** reflejan diferentes categorías operacionales y configuraciones. Las envolventes de categoría normal permiten operaciones de vuelo estándar, mientras que las envolventes de categoría utilitaria permiten maniobras acrobáticas limitadas con límites de CG más restrictivos. Las aeronaves de categoría de transporte pueden tener restricciones de envolvente adicionales para fases operacionales específicas.

**La verificación del punto de carga** requiere trazar el peso total de la aeronave y el momento (o índice de momento) como coordenadas en el gráfico de envolvente. El punto de intersección debe caer completamente dentro del área de envolvente cerrada. Los puntos en las líneas límite son aceptables, mientras que cualquier punto fuera de la envolvente representa una condición de carga insegura que requiere corrección antes del vuelo.

**La interpretación de múltiples envolventes** aplica a aeronaves con diferentes categorías operacionales o configuraciones de tren de aterrizaje. Algunas aeronaves tienen envolventes separadas para condiciones de tren arriba y tren abajo, reflejando el cambio de CG cuando el tren de aterrizaje se retrae. Los pilotos deben referenciar la envolvente apropiada para la fase de vuelo prevista.

> **Consideraciones Críticas de la Envolvente**: Siempre verifique que tanto las coordenadas de peso como de momento caigan dentro de los límites, comprenda las restricciones específicas de categoría, contabilice los efectos de consumo de combustible durante el vuelo y reconozca que los límites de la envolvente representan límites absolutos de seguridad que no deben excederse.

**La interpolación para valores intermedios** se hace necesaria cuando los valores de peso o momento de la aeronave caen entre líneas de cuadrícula impresas en el gráfico de envolvente. Use estimación proporcional para determinar la ubicación precisa relativa a los límites de la envolvente. En caso de duda, use interpretación conservadora que mantenga márgenes de seguridad adecuados de los límites de la envolvente.

El método de envolvente proporciona confirmación visual inmediata de la aceptabilidad de carga y ayuda a los pilotos a comprender la relación entre la distribución de peso y las limitaciones operacionales. La interpretación adecuada de la envolvente asegura el cumplimiento tanto de los requisitos regulatorios como de las limitaciones del fabricante mientras mantiene márgenes óptimos de seguridad de vuelo.

---

## ESCENARIOS DE CÁLCULO ESPECIALES

Los cálculos de peso y balance se vuelven más complejos cuando se manejan escenarios especiales que se desvían de las configuraciones de carga estándar. Estas situaciones requieren análisis cuidadoso y cálculos precisos para garantizar la seguridad de vuelo y el cumplimiento regulatorio. Los pilotos deben comprender cómo manejar los cálculos de brazos negativos, las limitaciones de peso sin combustible, las múltiples configuraciones de peso y los efectos de la quema de combustible durante el vuelo.

### Cálculos de Brazos Negativos

**Los brazos negativos** ocurren cuando los componentes o la carga están ubicados por delante del datum de referencia. Esto crea desafíos computacionales únicos que requieren atención cuidadosa a los signos algebraicos y precisión matemática.

Los elementos con brazos negativos incluyen más comúnmente los sistemas de aceite del motor, los compartimentos de equipaje montados en la nariz y ciertas instalaciones de equipos electrónicos. En la fórmula estándar de peso (Peso × Brazo = Momento), un peso positivo multiplicado por un brazo negativo produce un momento negativo que debe restarse de los momentos totales de la aeronave.

Considere una aeronave con aceite ubicado en la estación -31 (31 pulgadas por delante del datum). Seis cuartos de aceite que pesan 11 libras crean un momento de -341 in-lb (11 × -31 = -341). Este momento negativo reduce el momento total de la aeronave, moviendo efectivamente el centro de gravedad hacia adelante.

> **Punto Crítico**: Siempre verifique el signo algebraico al calcular momentos con brazos negativos. Un error de cálculo aquí afecta directamente la ubicación del CG y la seguridad de vuelo.

Al calcular los momentos totales con brazos negativos presentes, reste los momentos negativos de los momentos positivos. Por ejemplo, si los momentos positivos totalizan 125,000 in-lb y los momentos negativos totalizan -2,000 in-lb, el momento total real es 123,000 in-lb. El cálculo final del CG divide este momento neto por el peso total de la aeronave.

Algunas aeronaves tienen múltiples elementos con brazos negativos, particularmente instalaciones complejas con equipos montados hacia adelante. Cada momento negativo debe calcularse por separado y contabilizarse adecuadamente en la sumatoria de momentos totales antes de determinar la ubicación final del CG.

### Limitaciones de Peso Sin Combustible

**El peso máximo sin combustible (MZFW)** representa el peso máximo permitido de la aeronave excluyendo el combustible utilizable. Esta limitación protege la integridad estructural de la aeronave al prevenir cargas de flexión excesivas en las alas y el fuselaje durante las operaciones de vuelo.

Los cálculos de peso sin combustible requieren determinar el peso de la aeronave con todos los ocupantes, equipaje y carga, pero sin combustible utilizable. Este peso no debe exceder el MZFW especificado en el Type Certificate Data Sheet de la aeronave o en el manual de vuelo aprobado.

La secuencia de cálculo sigue este patrón: Comience con el peso vacío básico, agregue los pesos del piloto y los pasajeros, agregue los pesos del equipaje y la carga, luego verifique que este subtotal no exceda el MZFW publicado. Solo después de confirmar el cumplimiento del MZFW se puede agregar combustible para alcanzar el peso de despegue deseado.

Considere una aeronave con MZFW de 4,400 libras. Con un peso vacío básico de 3,230 libras, ocupantes que totalizan 885 libras y equipaje de 125 libras, el peso sin combustible es igual a 4,240 libras. Esto está dentro de la limitación de 4,400 libras, permitiendo la adición de combustible hasta los límites máximos de peso de despegue.

> **Nota Regulatoria**: Las aeronaves certificadas bajo 14 CFR Part 25 comúnmente especifican limitaciones de MZFW, mientras que muchas aeronaves más pequeñas bajo Part 23 pueden no tener esta restricción publicada.

Si el peso sin combustible excede el MZFW, se deben reducir los pasajeros o la carga antes del vuelo. La reducción de combustible no puede resolver las violaciones de MZFW ya que la limitación específicamente excluye el peso del combustible de la consideración.

### Múltiples Configuraciones de Peso

Las operaciones de aeronaves frecuentemente involucran múltiples configuraciones de peso a lo largo de un solo vuelo, requiriendo cálculos para **peso en rampa**, **peso de despegue** y **peso de aterrizaje**. Cada configuración tiene limitaciones específicas y consideraciones operacionales.

El peso en rampa (también llamado peso de taxi) representa el peso máximo para operaciones en tierra incluyendo procedimientos de rodaje y aceleración del motor. Este peso excede el peso de despegue por la cantidad de combustible consumido durante las operaciones en tierra, típicamente 20-30 libras para la mayoría de las aeronaves de aviación general.

La progresión del peso en rampa al peso de despegue implica restar la quema de combustible durante las operaciones de rodaje. El consumo estándar de combustible para procedimientos de arranque, rodaje y aceleración es aproximadamente 24 libras para operaciones típicas de aeronaves ligeras, aunque el consumo real varía con el tiempo en tierra y el tipo de motor.

El peso de despegue no debe exceder las limitaciones máximas de peso de despegue especificadas en la documentación de la aeronave. Este peso determina los cálculos de rendimiento de despegue incluyendo la distancia de carrera en tierra, los requisitos de franqueamiento de obstáculos y las capacidades de rendimiento de ascenso inicial.

Los cálculos de peso de aterrizaje restan el combustible consumido durante el vuelo del peso de despegue. Las limitaciones máximas de peso de aterrizaje, cuando se especifican, protegen contra cargas estructurales excesivas durante las operaciones de aterrizaje y garantizan un rendimiento de aterrizaje adecuado.

### Efectos de la Quema de Combustible Durante el Vuelo

El consumo de combustible durante el vuelo crea cambios continuos de peso y balance que afectan las características de manejo y el rendimiento de la aeronave. Comprender estos efectos es crucial para la planificación de vuelo y las decisiones de gestión en vuelo.

**El desplazamiento del CG durante el consumo de combustible** depende de las ubicaciones de los tanques de combustible en relación con el centro de gravedad de la aeronave. La mayoría de las aeronaves de aviación general posicionan los tanques de combustible cerca del CG, minimizando los cambios de balance a medida que se quema el combustible. Sin embargo, algunas aeronaves experimentan desplazamientos significativos del CG que requieren conciencia del piloto y posibles ajustes de carga.

El combustible ubicado por delante del CG causa movimiento del CG hacia atrás a medida que se quema, mientras que el combustible detrás del CG causa movimiento del CG hacia adelante durante el consumo. Las aeronaves con tanques en las alas posicionados en el CG típicamente experimentan cambios de balance mínimos a lo largo del vuelo.

Calcule los efectos de la quema de combustible determinando el cambio de momento a medida que disminuye el peso del combustible. Por ejemplo, si 30 galones (180 libras) de combustible se queman de tanques ubicados 6 pulgadas por delante del CG, el cambio de momento es igual a 1,080 in-lb, causando un desplazamiento del CG hacia atrás que debe permanecer dentro de los límites aprobados.

> **Consideración de Planificación de Vuelo**: Siempre verifique que el CG permanezca dentro de los límites aprobados tanto en el peso de despegue con combustible completo como en el peso de aterrizaje con combustible de reserva restante.

Los vuelos de largo alcance o las aeronaves con capacidad significativa de combustible requieren monitoreo cuidadoso de los cambios del CG a lo largo de las operaciones de vuelo. Algunos manuales de vuelo de aeronaves especifican límites de CG que varían con el peso, requiriendo verificación continua de cumplimiento a medida que se quema el combustible y disminuye el peso de la aeronave.

**Los cálculos de peso de aterrizaje** deben tener en cuenta el consumo de combustible planificado más las reservas requeridas. La ubicación final del CG en el aterrizaje debe estar dentro de los límites aprobados mientras se mantienen reservas adecuadas de combustible para aproximación, aterrizaje y requisitos de emergencia según lo especificado en 14 CFR 91.151 o 91.167.

---

## DESPLAZAMIENTO, ADICIÓN Y REMOCIÓN DE PESO

Comprender cómo calcular los efectos de los cambios de peso es esencial para la operación segura de la aeronave. Los pilotos frecuentemente enfrentan situaciones que requieren redistribución, adición o remoción de peso para lograr el balance adecuado. Estos cálculos aseguran que la aeronave permanezca dentro de los límites aprobados de centro de gravedad durante todas las fases del vuelo.

### Cálculos de Desplazamiento de Peso y Cambios en el CG

**El desplazamiento de peso** implica mover carga, pasajeros o equipo de una ubicación a otra sin cambiar el peso total de la aeronave. Los momentos totales cambian proporcionalmente a la dirección y distancia que se mueve el peso. Cuando el peso se mueve hacia adelante, los momentos totales disminuyen; cuando el peso se mueve hacia atrás, los momentos totales aumentan.

La **fórmula de proporción de desplazamiento de peso** proporciona un método directo para calcular los cambios en el centro de gravedad:

**Peso desplazado ÷ Peso total = ΔCG ÷ Distancia que se desplaza el peso**

Esta relación fundamental permite a los pilotos determinar el cambio exacto del CG sin recalcular los momentos totales. El **delta CG (ΔCG)** representa el cambio en la posición del centro de gravedad medido en pulgadas desde la ubicación original.

Considere una aeronave que pesa 8,000 libras con un CG en la estación 77. Si 100 libras se desplazan de la estación 30 a la estación 150, la distancia recorrida es igual a 120 pulgadas (150 - 30). Usando la fórmula de proporción:

100 ÷ 8,000 = ΔCG ÷ 120
ΔCG = (100 × 120) ÷ 8,000 = 1.5 pulgadas

La nueva ubicación del CG se convierte en 77 + 1.5 = 78.5 pulgadas hacia atrás del datum.

> **Punto Crítico**: Siempre verifique la dirección del movimiento del CG. El movimiento hacia atrás aumenta el número de estación del CG; el movimiento hacia adelante lo disminuye.

### Fórmulas Proporcionales para el Movimiento de Peso

La relación proporcional funciona en reversa para determinar los desplazamientos de peso requeridos para correcciones específicas del CG. Cuando el CG de la aeronave excede los límites, los pilotos pueden calcular el peso mínimo que debe redistribuirse para lograr el cumplimiento.

Para una aeronave que pesa 7,800 libras con CG en la estación 81.5, excediendo el límite trasero de 80.5, el movimiento hacia adelante requerido del CG es igual a 1.0 pulgada. Para desplazar carga de la estación 150 a la estación 30 (movimiento de 120 pulgadas):

Peso a desplazar ÷ 7,800 = 1.0 ÷ 120
Peso a desplazar = (7,800 × 1.0) ÷ 120 = 65 libras

Mover 65 libras hacia adelante reposiciona el CG exactamente en el límite trasero. Este cálculo previene la redistribución excesiva de peso mientras asegura el cumplimiento regulatorio.

**La redistribución de carga del compartimento de equipaje** comúnmente utiliza estos principios. Muchas aeronaves cuentan con áreas de equipaje delanteras y traseras con diferentes distancias de brazo desde el datum. La redistribución estratégica entre compartimentos proporciona un método efectivo para el control del CG sin reducir la carga útil.

La fórmula de proporción se aplica independientemente de las cantidades de peso o distancias involucradas. La relación permanece constante ya sea que se desplacen 10 libras o 500 libras, haciéndola universalmente aplicable a través de tipos de aeronaves y escenarios de carga.

### Adición de Peso y Desplazamiento del CG

**Agregar peso** a una aeronave cambia tanto el peso total como la ubicación del centro de gravedad. El CG se desplaza hacia la ubicación del peso agregado, con una magnitud de desplazamiento que depende de la cantidad de peso y su distancia desde el CG original.

La fórmula para los efectos de la adición de peso es:

**Peso agregado ÷ Nuevo peso total = ΔCG ÷ Distancia entre el peso agregado y el CG antiguo**

Considere una aeronave que pesa 6,860 libras con CG en la estación 80. Agregando 140 libras de equipaje en la estación 150:

Nuevo peso total = 6,860 + 140 = 7,000 libras
Distancia desde el CG antiguo = 150 - 80 = 70 pulgadas
140 ÷ 7,000 = ΔCG ÷ 70
ΔCG = (140 × 70) ÷ 7,000 = 1.4 pulgadas hacia atrás

La nueva ubicación del CG se convierte en 80 + 1.4 = 81.4 pulgadas hacia atrás del datum.

**La optimización de asientos de pasajeros** utiliza principios de adición de peso al determinar asignaciones de asientos con propósitos de balance. Cargar pasajeros pesados en asientos delanteros contrarresta condiciones de cola pesada, mientras que los asientos traseros ayudan a corregir situaciones de nariz pesada.

La carga de combustible representa el escenario más común de adición de peso. El peso del combustible afecta significativamente el balance de la aeronave, con la gasolina de aviación pesando 6 libras por galón. Agregar 50 galones aumenta el peso en 300 libras, potencialmente desplazando el CG dependiendo de las ubicaciones de los tanques de combustible relativas al punto de balance actual.

> **Consideración de Combustible**: La mayoría de las aeronaves pequeñas posicionan los tanques de combustible cerca del CG, minimizando los cambios de balance durante el consumo de combustible. Las aeronaves más grandes pueden experimentar desplazamientos significativos del CG que requieren ajustes de trim durante el vuelo.

### Remoción de Peso y Desplazamiento Hacia Adelante del CG

**La remoción de peso** causa que el centro de gravedad se desplace alejándose de la ubicación del peso removido. Esto crea un movimiento hacia adelante del CG cuando se remueve peso de posiciones traseras, o movimiento hacia atrás al remover peso delantero.

La fórmula de cálculo para la remoción de peso es:

**Peso removido ÷ Nuevo peso total = ΔCG ÷ Distancia entre el peso removido y el CG antiguo**

Para una aeronave que pesa 6,100 libras con CG en la estación 80, removiendo 100 libras de la estación 150:

Nuevo peso total = 6,100 - 100 = 6,000 libras
Distancia desde el CG antiguo = 150 - 80 = 70 pulgadas
100 ÷ 6,000 = ΔCG ÷ 70
ΔCG = (100 × 70) ÷ 6,000 = 1.17 pulgadas hacia adelante

La nueva ubicación del CG se convierte en 80 - 1.17 = 78.83 pulgadas hacia atrás del datum.

El consumo de combustible durante el vuelo representa el escenario principal de remoción de peso que los pilotos encuentran. A medida que el combustible se quema, la aeronave se vuelve más liviana y el CG se desplaza alejándose de las ubicaciones de los tanques de combustible. Para aeronaves con tanques montados en las alas cerca del CG, este desplazamiento permanece mínimo durante el vuelo.

**Las relaciones matemáticas para la corrección del CG** requieren comprender los efectos direccionales. Remover peso trasero mueve el CG hacia adelante; remover peso delantero mueve el CG hacia atrás. La magnitud depende de la relación proporcional entre el peso removido y el peso restante de la aeronave.

Las situaciones de emergencia pueden requerir remoción rápida de peso para mantener la controlabilidad o el rendimiento. Comprender estos cálculos permite a los pilotos tomar decisiones informadas sobre el lanzamiento de carga o el vaciado de combustible cuando los sistemas de la aeronave permiten tales acciones.

Las operaciones de carga y descarga de carga frecuentemente involucran cálculos de remoción de peso. Las tripulaciones de tierra y los pilotos deben verificar que las secuencias de descarga mantengan el CG dentro de los límites durante todo el proceso, previniendo condiciones peligrosas de desequilibrio durante estados intermedios de carga.

> **Alerta de Seguridad**: Siempre recalcule el peso y balance después de cualquier cambio de peso. Incluso ajustes menores pueden potencialmente colocar la aeronave fuera de los límites aprobados, comprometiendo la seguridad y la controlabilidad.

Estos cálculos de desplazamiento, adición y remoción de peso forman la base de la gestión práctica de peso y balance. El dominio de estos principios permite a los pilotos tomar decisiones de carga en tiempo real que mantienen la aeronave dentro de parámetros operativos seguros mientras maximizan la efectividad de la misión.

## Resumen

Revise los puntos clave de esta unidad:

- El cumplimiento de peso y balance es crítico para la seguridad de vuelo, ya que operar fuera de los límites aprobados puede resultar en falla estructural, características de vuelo irrecuperables o pérdida completa del control.
- El peso de la aeronave afecta directamente los requisitos de sustentación, con aeronaves más pesadas requiriendo ángulos de ataque mayores y potencialmente excediendo la capacidad del ala para generar suficiente sustentación.
- El exceso de peso degrada todos los aspectos del rendimiento incluyendo distancias de despegue más largas, tasas de ascenso reducidas, velocidades de pérdida más altas y distancias de aterrizaje aumentadas.
- La gasolina de aviación pesa 6 libras por galón mientras que el combustible para turbinas pesa 6.8 libras por galón (Jet A/A-1), haciendo que la carga de combustible sea un factor significativo en los cálculos de peso.
- El centro de gravedad representa el punto de balance teórico de la aeronave y afecta directamente la estabilidad, la respuesta de los controles y las características de rendimiento.
- Las condiciones de CG adelantado crean aeronaves pesadas de nariz con estabilidad aumentada pero efectividad del elevador reducida, particularmente peligroso durante el flare de aterrizaje.
- Las condiciones de CG atrasado resultan en estabilidad longitudinal reducida, fuerzas de control ligeras y características de pérdida potencialmente violentas o irrecuperables.
- Los límites de CG son establecidos por los fabricantes a través de pruebas de vuelo y publicados en el Type Certificate Data Sheet y el Aircraft Flight Manual.
- La carga con balance inadecuado puede causar sobreesfuerzo estructural, particularmente con condiciones de CG atrasado donde las fuerzas de control ligeras enmascaran entradas de control excesivas.
- Los procedimientos de emergencia se vuelven más difíciles o imposibles de ejecutar cuando las aeronaves están cargadas fuera de los límites aprobados de peso y balance.

---

## Términos Clave

| Término | Definición |
|------|------------|
| **Center of Gravity (CG)** | El punto teórico donde se concentra todo el peso de la aeronave y donde la aeronave estaría en equilibrio si se suspendiera |
| **Datum** | Un plano vertical imaginario establecido por el fabricante como punto de referencia cero para las mediciones de peso y balance |
| **Moment** | El producto del peso multiplicado por el brazo (distancia desde el datum), utilizado para calcular la ubicación del centro de gravedad |
| **Arm** | La distancia horizontal desde el datum hasta el centro de gravedad de un elemento, medida en pulgadas |
| **Forward CG Limit** | La posición más adelantada del centro de gravedad donde se pueden realizar operaciones de vuelo seguras |
| **Aft CG Limit** | La posición más atrasada del centro de gravedad donde existen márgenes de estabilidad adecuados para un vuelo seguro |
| **Type Certificate Data Sheet (TCDS)** | Documento oficial que contiene las limitaciones de peso y balance establecidas por la FAA para cada modelo de aeronave |
| **Wing Loading** | Peso de la aeronave dividido por el área del ala, típicamente expresado en libras por pie cuadrado |
| **Longitudinal Stability** | La tendencia de la aeronave a retornar al equilibrio después de una perturbación en cabeceo |
| **Mean Aerodynamic Chord (MAC)** | La distancia promedio desde el borde de ataque hasta el borde de fuga del ala, utilizada como referencia para los límites del CG |
| **Static Stability** | La tendencia inicial de la aeronave a retornar al equilibrio después de una perturbación |
| **Usable Fuel** | Combustible disponible para propósitos de planificación de vuelo, excluyendo el combustible no utilizable atrapado en los sistemas de tanques |
| **Ballast** | Peso agregado a la aeronave para lograr el balance apropiado, ya sea permanente (parte del peso vacío) o temporal |
| **Service Ceiling** | Altitud máxima donde una aeronave puede mantener una razón de ascenso de 100 pies por minuto |
| **Critical Angle of Attack** | El ángulo de ataque en el cual se genera la sustentación máxima antes de que la separación del flujo de aire cause una pérdida |

---

## Preguntas de Repaso

**Opción Múltiple**

1. ¿Cuál es el peso de la gasolina de aviación (AVGAS) utilizado para los cálculos de peso y balance?
   - A) 5.8 libras por galón
   - B) 6.0 libras por galón
   - C) 6.8 libras por galón
   - D) 7.2 libras por galón

2. Una aeronave cargada más allá del límite de CG de popa exhibirá:
   - A) Fuerzas de control pesadas y estabilidad aumentada
   - B) Fuerzas de control ligeras y estabilidad disminuida
   - C) Fuerzas de control normales y estabilidad neutra
   - D) Fuerzas de control variables dependiendo de la velocidad aerodinámica

3. El límite de CG delantero se establece principalmente con base en:
   - A) Requisitos de rendimiento en despegue
   - B) Características de aterrizaje y efectividad del elevador
   - C) Optimización del rendimiento en crucero
   - D) Limitaciones estructurales de los largueros del ala

4. ¿Qué regulación requiere que los pilotos cumplan con las limitaciones de peso y balance?
   - A) 14 CFR 91.103
   - B) 14 CFR 91.9
   - C) 14 CFR 61.87
   - D) 14 CFR 23.23

**Verdadero/Falso**

5. Verdadero o Falso: Las operaciones bajo Part 91 requieren cálculos formales de peso y balance antes de cada vuelo.

6. Verdadero o Falso: El combustible Jet A pesa más por galón que la gasolina de aviación.

7. Verdadero o Falso: El centro de gravedad de una aeronave permanece fijo independientemente del consumo de combustible durante el vuelo.

8. Verdadero o Falso: La carga con CG delantero típicamente resulta en características de pérdida mejoradas en comparación con la carga con CG de popa.

**Respuesta Corta**

9. Explique por qué operar una aeronave más allá del límite de CG de popa es particularmente peligroso durante condiciones de pérdida.

10. Describa tres efectos específicos de rendimiento que resultan de operar una aeronave por encima del peso máximo certificado.

**Emparejamiento**

11. Empareje cada condición de CG con su característica principal:

**Condiciones de CG:**
- A) CG Delantero
- B) CG de Popa
- C) CG dentro de los límites

**Características:**
- 1) Fuerzas de control ligeras, estabilidad reducida
- 2) Fuerzas de control pesadas, estabilidad aumentada
- 3) Fuerzas de control normales, estabilidad apropiada

12. Calcule el momento para un pasajero que pesa 180 libras sentado en una estación 85 pulgadas a popa del datum. Muestre su trabajo e incluya las unidades apropiadas.

---

## Referencias FAA

- PHAK Capítulo 8: Rendimiento de Aeronaves, secciones de Peso y Balance
- PHAK Capítulo 5: Aerodinámica del Vuelo, Cuatro Fuerzas del Vuelo
- 14 CFR Part 91.9: Manual de Vuelo de Aeronaves Civiles, Requisitos de Marcado y Placas
- AC 43.13-1: Métodos, Técnicas y Prácticas Aceptables - Inspección y Reparación de Aeronaves