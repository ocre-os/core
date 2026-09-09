# Reglas de Negocio de Ocre OS

**Estado:** Borrador  
**Versión:** 0.1

## 1. Propósito

Este documento concentra las reglas de negocio que Ocre OS debe respetar independientemente de la interfaz, tecnología o implementación utilizada.

Las reglas se identifican mediante un código estable `RN-XXX` para poder referenciarlas posteriormente desde procesos, modelo de datos, pruebas y código.

Una regla puede modificarse cuando el conocimiento del negocio demuestre que existe una representación mejor. Cuando esto ocurra, deberá conservarse trazabilidad del cambio.

---

## 2. Interacciones y clasificación

### RN-001 — Toda comunicación relevante se conserva

Toda Interacción registrada debe permanecer disponible como parte del historial, aunque posteriormente se determine que corresponde a información ya existente.

Una Interacción duplicada en contenido no es un registro inútil: puede aportar información sobre frecuencia de contacto, dificultades de seguimiento, capacitación requerida o comportamiento operativo.

### RN-002 — Una nueva Interacción no crea automáticamente una nueva Solicitud

Toda nueva comunicación debe clasificarse antes de concluir que representa una nueva necesidad.

Puede relacionarse con una Solicitud, Caso, Contacto u Organización existente sin crear objetos innecesarios.

### RN-003 — Contacto 0 es una clasificación provisional

Contacto 0 (C0) se utiliza cuando una Interacción todavía no puede clasificarse con suficiente certeza.

C0 no representa una persona, una Organización ni una Interacción adicional.

### RN-004 — Resolver Contacto 0 no elimina la Interacción

Cuando C0 queda clasificado, la Interacción que lo originó debe permanecer en el historial y relacionarse con los elementos identificados.

### RN-005 — No se inventan datos para completar un proceso

La plataforma debe admitir información incompleta cuando esa sea la realidad del negocio.

Los datos faltantes pueden completarse posteriormente sin obligar al usuario a introducir información falsa o provisional como si fuera definitiva.

---

## 3. Solicitudes y necesidades

### RN-006 — La expresión original del cliente se conserva

La Solicitud debe conservar lo que el solicitante expresó originalmente, aunque posteriormente el diagnóstico determine que la causa o incluso la necesidad real es diferente.

### RN-007 — La necesidad real puede diferir de la Solicitud original

Ocre debe poder registrar por separado:

- lo que el cliente expresó;
- la necesidad identificada;
- y la solución finalmente acordada.

La información posterior no debe sobrescribir el origen del Caso.

### RN-008 — El objetivo operativo es la capacidad productiva del cliente

La solución no debe evaluarse únicamente por el estado de una máquina.

Cuando el alcance contratado lo permita, el criterio superior es recuperar, mantener o mejorar la capacidad productiva necesaria para que el cliente pueda cumplir sus objetivos.

### RN-009 — El nivel de intervención debe respetar el alcance acordado

Ocre puede trabajar desde ejecución específica hasta acompañamiento integral.

Las recomendaciones adicionales no deben imponerse cuando el cliente haya definido expresamente un alcance limitado.

---

## 4. Casos y continuidad

### RN-010 — Un Caso representa continuidad de atención

Un Caso agrupa el seguimiento de una necesidad y puede extenderse a través de comunicaciones, Servicios, Visitas, cotizaciones, pagos, refacciones, Reportes y Pendientes.

No debe confundirse con una sola actividad o una sola Visita.

### RN-011 — La reincidencia no crea automáticamente un Caso nuevo

Cuando una nueva incidencia pueda estar lógica o técnicamente relacionada con una intervención reciente, primero debe evaluarse su relación con el Caso anterior.

### RN-012 — Presunción de continuidad ante posible reincidencia

Cuando exista duda razonable, Ocre OS debe favorecer provisionalmente la continuidad del Caso anterior hasta obtener evidencia suficiente para separar la nueva incidencia.

Esta regla no afirma que ambas fallas tengan la misma causa.

### RN-013 — La reapertura debe registrar motivo

Todo Caso reabierto debe conservar:

- fecha de reapertura;
- Interacción que la originó;
- motivo;
- responsable;
- y contexto disponible.

### RN-014 — Existe un estado de evaluación de reincidencia

Cuando un Caso sea reabierto sin certeza sobre la relación con la nueva incidencia, debe poder representarse explícitamente la incertidumbre.

Estado provisional de negocio:

`En evaluación de reincidencia`.

### RN-015 — La relación entre incidencias se decide con evidencia

La decisión de continuar un Caso o crear uno nuevo no debe basarse únicamente en:

- cercanía temporal;
- similitud superficial del síntoma;
- pertenecer al mismo Equipo;
- ni opinión no verificada.

Puede requerir clasificación técnica y diagnóstico.

### RN-016 — Un problema independiente genera un Caso relacionado

Si durante la evaluación se demuestra que la nueva incidencia es independiente, debe crearse un nuevo Caso conservando una relación explícita con el Caso que originó la investigación.

### RN-017 — Pueden existir problemas simultáneos

Si se confirma continuidad de la problemática anterior y además se descubre otra necesidad independiente, el Caso original puede continuar y debe poder crearse otro Caso relacionado.

### RN-018 — La decisión de separar Casos es trazable

Debe poder reconstruirse posteriormente:

1. qué reportó el cliente;
2. por qué se consideró una posible reincidencia;
3. qué se investigó;
4. qué evidencia se obtuvo;
5. y por qué se decidió continuar o separar la atención.

---

## 5. Equipos y expediente técnico

### RN-019 — Cada Equipo atendido desarrolla un expediente técnico

La información técnica obtenida sobre un Equipo específico debe acumularse en un expediente persistente y no quedar aislada únicamente dentro de Reportes individuales.

### RN-020 — El primer servicio sobre un Equipo incluye Diagnóstico General Inicial

Cuando Ocre interviene por primera vez un Equipo, debe realizarse un Diagnóstico General Inicial (DGI), aun cuando exista una reparación específica solicitada.

El alcance concreto del DGI puede adaptarse al tipo de Equipo y a las condiciones reales de la intervención.

### RN-021 — Una reparación menor puede integrarse al DGI

Cuando durante el DGI se identifica una corrección sencilla que no exige inversión, refacción significativa ni una ampliación material del tiempo o alcance, puede ejecutarse dentro del mismo Servicio.

Debe documentarse aunque no genere un cargo independiente.

### RN-022 — El Equipo debe analizarse dentro de su proceso productivo

Cuando resulte relevante, el expediente debe conservar relaciones de entrada, salida o dependencia con otros Equipos y procesos.

El análisis no debe limitarse artificialmente a una máquina aislada.

### RN-023 — Cada Equipo debe tener identificación única dentro de Ocre OS

La identificación interna debe permitir mantener continuidad histórica aun cuando cambie de Ubicación, operador u Organización responsable.

---

## 6. Diagnóstico y evidencia

### RN-024 — Síntoma no equivale a causa

El síntoma reportado u observado debe registrarse separadamente de las hipótesis, hallazgos, causas y causa raíz.

### RN-025 — Una hipótesis no es un diagnóstico confirmado

Una explicación técnicamente posible debe conservarse como hipótesis hasta que exista evidencia suficiente para elevar su nivel de certeza.

### RN-026 — Se valida antes de asumir

Antes de concluir que existe una falla interna compleja deben comprobarse las condiciones básicas y externas razonablemente relacionadas con el funcionamiento del sistema.

### RN-027 — Fenómeno antes que componente

El proceso de diagnóstico debe intentar comprender primero el fenómeno que produce el síntoma y posteriormente identificar qué componentes o condiciones pueden generarlo.

### RN-028 — De lo simple a lo complejo

Cuando varias hipótesis pueden explicar un mismo síntoma, deben priorizarse comprobaciones lógicas, de menor costo o menor intrusión antes de asumir fallas complejas o realizar sustituciones innecesarias.

### RN-029 — Las fallas dispersas obligan a investigar recursos compartidos

Cuando varios subsistemas presentan fallas aparentemente independientes, debe considerarse si comparten recursos como alimentación, tierra, comunicación, controladora o cableado común.

### RN-030 — Una prueba estática no descarta una falla bajo carga

Los resultados obtenidos sin carga no deben utilizarse como evidencia suficiente para descartar fenómenos que solo aparecen durante la operación real.

### RN-031 — Los testimonios y las mediciones se distinguen

La información reportada por operadores, supervisores o clientes debe conservarse como evidencia contextual, pero debe distinguirse de una medición o prueba realizada directamente.

### RN-032 — La experiencia orienta, pero no determina la conclusión

La experiencia técnica puede priorizar hipótesis, pero no debe impedir investigar explicaciones menos frecuentes cuando la evidencia lo requiera.

---

## 7. Servicios, Visitas y Reportes

### RN-033 — Servicio y Visita no son sinónimos

Un Servicio puede requerir múltiples Visitas y una Visita puede contener diversas actividades relacionadas con uno o más objetivos del Servicio.

### RN-034 — La documentación se captura durante la operación

Siempre que sea razonablemente posible, la información del Servicio debe registrarse durante su ejecución y no reconstruirse posteriormente desde la memoria del técnico.

### RN-035 — El Reporte se genera a partir de información estructurada

El Reporte debe reutilizar la información ya capturada en Solicitudes, Casos, Servicios y Visitas.

No debe exigir volver a escribir el Servicio desde cero.

### RN-036 — Todo Reporte debe preservar el alcance y resultado real

El Reporte debe distinguir como mínimo:

- qué solicitó el cliente;
- qué se encontró;
- qué se hizo;
- qué se comprobó;
- qué no pudo comprobarse;
- qué queda pendiente;
- y cuál es el estado final conocido.

### RN-037 — No se presenta incertidumbre como certeza

Cuando una falla intermitente o condición técnica no pueda comprobarse completamente, el Reporte debe expresar el nivel real de certeza y el seguimiento necesario.

---

## 8. Refacciones e inventario

### RN-038 — Una refacción puede tener múltiples clasificaciones

Las refacciones no deben limitarse a una categoría única.

Deben poder describirse mediante atributos independientes de función, condición, compatibilidad, estrategia de abastecimiento y restricciones de uso.

### RN-039 — Una pieza retirada no se considera automáticamente desperdicio

Una pieza retirada puede ser evaluada, reparada o conservada para uso temporal o de emergencia cuando sea técnicamente seguro.

### RN-040 — Las piezas temporales deben identificarse explícitamente

Una pieza reparada o recuperada que no sea adecuada para servicio permanente debe conservar una restricción visible que impida interpretarla posteriormente como refacción definitiva.

### RN-041 — Las compras pueden generar inventario excedente deliberado

Cuando el criterio operativo justifique mantener stock, una compra para un Caso puede incluir unidades adicionales que ingresen al inventario general después de reservar las necesarias para el trabajo específico.

---

## 9. Conocimiento técnico

### RN-042 — Cada Servicio debe poder enriquecer la base de conocimiento

Los hallazgos, procedimientos, configuraciones, documentación y soluciones reutilizables deben poder separarse del expediente individual y convertirse en conocimiento aplicable a otros Equipos cuando corresponda.

### RN-043 — Expediente técnico y base de conocimiento son diferentes

El expediente técnico describe lo conocido sobre un Equipo específico.

La base de conocimiento contiene información reutilizable sobre modelos, tecnologías, componentes, síntomas, procedimientos y soluciones.

### RN-044 — La documentación del fabricante debe preservarse oportunamente

Cuando se obtengan manuales, software, firmware, listas de partes, boletines, herramientas, capacitaciones u otra documentación relevante, debe conservarse aunque no exista una necesidad inmediata.

### RN-045 — Las configuraciones válidas deben poder respaldarse

Cuando se identifica o establece una configuración correcta, Ocre OS debe permitir conservarla junto con suficiente contexto para restaurarla posteriormente.

---

## 10. Personas, Organizaciones y Ubicaciones

### RN-046 — Persona y Organización no son sinónimos de Cliente

El sistema debe distinguir a la persona, la Organización y la relación comercial que mantienen con Ocre.

### RN-047 — Una persona puede desempeñar múltiples funciones

No debe duplicarse un Contacto únicamente porque actúe como operador, comprador, propietario, responsable de pagos u otro rol simultáneamente.

### RN-048 — Una Organización puede tener múltiples Ubicaciones

Los Equipos y Servicios deben poder relacionarse con la Ubicación física relevante sin asumir que toda instalación es jurídicamente una sucursal.

### RN-049 — El contexto del operador puede ser técnicamente relevante

Cuando corresponda, el expediente debe permitir conservar quién opera el Equipo, su relación con el proceso y las diferencias respecto del perfil recomendado de operación.

---

## 11. Seguimiento, agenda y administración

### RN-050 — Todo Pendiente debe aspirar a tener responsable y condición de seguimiento

Cuando sea posible, un Pendiente debe indicar responsable, motivo, prioridad y fecha objetivo o condición que determine cuándo debe retomarse.

Los Pendientes no deben depender exclusivamente de la memoria de una persona.

### RN-051 — Prioridad y urgencia son conceptos diferentes

La urgencia representa presión temporal.

La prioridad puede considerar además impacto productivo, seguridad, compromiso comercial, dependencia de otros trabajos u otros criterios.

### RN-052 — La facturación fiscal permanece inicialmente fuera de Ocre OS

Ocre OS no emitirá inicialmente la factura fiscal, pero debe controlar la Solicitud de facturación, reunir la información necesaria y conservar su estado hasta recibir el resultado correspondiente.

### RN-053 — Pago y factura son conceptos independientes

Registrar un Pago no implica que exista una factura fiscal emitida.

---

## 12. Trazabilidad y conservación

### RN-054 — Cerrar no significa borrar

Solicitudes, Casos, Servicios, Contactos 0 y demás procesos cerrados deben conservar su historial.

### RN-055 — Las decisiones relevantes deben ser trazables

Cuando una decisión cambie el estado, alcance o relación de un elemento importante, debe poder conocerse quién la tomó, cuándo, dentro de qué contexto y, cuando corresponda, por qué.

### RN-056 — La información se captura una vez y se reutiliza

Los datos existentes deben reutilizarse en expedientes, Reportes, cotizaciones, seguimiento y conocimiento para evitar duplicación y pérdida de consistencia.

### RN-057 — La fuente oficial del proyecto es el repositorio

Las conversaciones y herramientas de inteligencia artificial pueden utilizarse para analizar y proponer cambios, pero las decisiones aceptadas deben quedar reflejadas en la documentación o código versionado de Ocre OS.

---

## 13. Reglas pendientes de validación

Las reglas anteriores representan el conocimiento operativo capturado hasta esta versión.

Antes de considerarlas definitivas deben seguir probándose contra situaciones reales, especialmente en:

- límites entre Solicitud y Caso;
- criterios de cierre técnico y administrativo;
- garantías y responsabilidades por reincidencia;
- reglas comerciales de anticipos;
- múltiples Equipos dentro de una misma Solicitud;
- múltiples Organizaciones relacionadas con un mismo proceso productivo;
- asignación de técnicos externos;
- control de inventario temporal;
- permisos y visibilidad del portal del cliente.

Cuando aparezca una excepción real, primero deberá determinarse si:

1. la regla existente es incorrecta;
2. la regla necesita una excepción explícita;
3. o el caso pertenece a un concepto diferente.

No deberá agregarse complejidad al sistema únicamente para resolver una situación hipotética sin evidencia operativa.
