# Glosario de Ocre OS

**Estado:** Borrador  
**Versión:** 0.2

## 1. Propósito

Este documento establece el significado oficial de los términos utilizados en Ocre OS.

Su objetivo es evitar que una misma palabra represente conceptos diferentes y proporcionar un lenguaje común para operación, documentación, diseño y desarrollo.

Las definiciones describen conceptos del negocio. No implican todavía que cada concepto deba convertirse en una tabla, módulo o pantalla independiente.

---

# 2. Principios de terminología

## 2.1 Preferencia por español

Ocre OS utilizará términos en español siempre que exista una alternativa clara, precisa y natural.

Los términos técnicos universalmente aceptados podrán conservarse cuando su traducción genere mayor ambigüedad.

## 2.2 Una palabra, un concepto

Un mismo término no deberá utilizarse para representar objetos diferentes.

Ejemplo:

"Cliente" no deberá utilizarse indistintamente para referirse a una empresa, una persona de contacto y una ubicación.

## 2.3 El lenguaje del negocio precede al lenguaje técnico

Primero se define qué representa algo en la operación real.

Posteriormente se decide cómo representarlo en software.

---

# 3. Interacción

## Definición

Evento de comunicación entre una persona y Ocre, independientemente de que al momento de registrarlo se conozca o no con certeza la identidad, la Organización relacionada o el motivo completo del contacto.

Puede originarse mediante:

- llamada;
- WhatsApp;
- correo electrónico;
- formulario;
- mensaje desde el portal;
- referencia;
- contacto presencial;
- u otro medio.

Una Interacción existe como registro histórico desde que ocurre y puede posteriormente relacionarse con:

- un Contacto;
- una Organización;
- una Solicitud;
- un Caso;
- una Cita;
- un Servicio;
- o ningún elemento adicional si solamente requiere conservarse como antecedente.

## Importante

Una Interacción no significa automáticamente:

- una nueva persona;
- una nueva Solicitud;
- un nuevo Caso;
- una venta;
- ni un Servicio.

Una Interacción no debe eliminarse únicamente porque repita información ya existente. La repetición puede aportar información operativa sobre frecuencia de contacto, dificultades de seguimiento, uso de la plataforma o necesidades de capacitación.

---

## 3.1 Contacto 0 (C0)

## Definición

Clasificación provisional utilizada cuando existe una Interacción real, pero todavía no hay información suficiente para relacionarla de manera confiable con los elementos existentes de Ocre OS o para determinar qué proceso debe iniciar.

Contacto 0 no representa una persona, una Organización ni una Interacción adicional.

Puede utilizarse, por ejemplo, cuando todavía se desconoce:

- quién está contactando;
- a qué Organización pertenece;
- si ya existe en el sistema;
- si existe una Solicitud relacionada;
- si existe un Caso relacionado;
- cuál es la necesidad concreta;
- o qué acción debe realizarse.

## No significa

Un Contacto 0 no es necesariamente:

- un cliente;
- un prospecto;
- una venta;
- un servicio;
- una oportunidad comercial;
- ni una cita.

## Evolución

Contacto 0 deja de ser necesario cuando la Interacción puede clasificarse con suficiente certeza.

Al resolverse puede:

- relacionarse con un Contacto existente;
- relacionarse con una Organización existente;
- relacionarse con una Solicitud existente;
- relacionarse con un Caso existente;
- generar una nueva Solicitud;
- actualizar información existente;
- generar un Pendiente;
- o cerrarse sin acción posterior.

Resolver o cerrar C0 no elimina la Interacción que lo originó.

**Abreviatura de trabajo:** C0.

---

# 4. Contacto

## Definición

Persona identificada con la cual Ocre puede mantener comunicación.

Puede estar relacionada con una o varias organizaciones y desempeñar diferentes funciones.

Ejemplos de funciones:

- propietario;
- operador;
- encargado de compras;
- supervisor;
- mantenimiento;
- administración;
- contabilidad;
- responsable de pagos;
- responsable de facturación.

## Observación

Una persona no debe duplicarse únicamente porque desempeñe varias funciones.

---

# 5. Organización

## Definición

Entidad organizada con la cual Ocre mantiene una relación operativa o comercial.

Normalmente será una empresa, pero el término permite representar otras formas de organización sin atar el sistema exclusivamente al concepto jurídico de empresa.

Una organización puede tener:

- contactos;
- ubicaciones;
- equipos;
- información fiscal;
- solicitudes;
- servicios;
- documentos;
- pagos;
- y otros registros relacionados.

## Observación

"Organización" será inicialmente el término estructural recomendado.

En la interfaz para usuarios podrá mostrarse "Empresa" cuando resulte más natural.

---

# 6. Cliente

## Definición

Rol que adquiere una persona u organización cuando existe una relación comercial o de servicio con Ocre.

## Importante

"Cliente" describe una relación con Ocre; no necesariamente debe representar un objeto independiente.

Una organización puede existir en el sistema antes de convertirse en cliente.

Por esta razón, conceptualmente se distingue:

**qué es la organización**  
de  
**qué relación mantiene actualmente con Ocre**.

---

# 7. Prospecto

## Definición

Persona u organización identificada que presenta posibilidad razonable de convertirse en cliente.

## Uso

Este término podrá utilizarse para clasificación comercial, pero no sustituye a Contacto 0.

Una Interacción provisionalmente clasificada como C0 puede, al resolverse, identificar a una persona u Organización que posteriormente sea clasificada como prospecto.

## Observación

No toda Interacción ni todo C0 debe producir un prospecto.

---

# 8. Ubicación

## Definición

Lugar físico relevante para la operación de una organización o para la prestación de un servicio.

Puede corresponder a:

- planta;
- taller;
- oficina;
- almacén;
- sucursal;
- domicilio;
- obra;
- u otra instalación.

Una organización puede tener múltiples ubicaciones.

## Importante

Se prefiere "Ubicación" sobre "Sucursal" como concepto general porque no todas las instalaciones de un cliente son jurídicamente sucursales.

---

# 9. Necesidad

## Definición

Resultado, condición o problema que el cliente realmente necesita resolver.

La necesidad puede ser diferente de la falla técnica inicialmente reportada.

Ejemplos:

- recuperar producción;
- mejorar calidad;
- aumentar capacidad;
- reducir desperdicio;
- mantener una máquina operativa;
- reducir fallas;
- producir temporalmente mediante otro proveedor;
- corregir un problema de infraestructura.

## Principio

La necesidad constituye una de las referencias principales para evaluar si Ocre resolvió correctamente el trabajo.

---

# 10. Solicitud

## Definición

Expresión concreta de una necesidad que requiere análisis, respuesta, seguimiento o ejecución por parte de Ocre.

Una Solicitud puede originarse desde una Interacción, incluida una Interacción provisionalmente clasificada como C0, desde un cliente existente o desde otro proceso.

Ejemplos:

- "La máquina no enciende."
- "Necesitamos mantenimiento preventivo."
- "Queremos saber en qué condiciones se encuentra el equipo."
- "Necesitamos aumentar la producción."
- "Necesitamos una cotización."
- "Necesitamos capacitación."

## Importante

La solicitud debe conservar lo que originalmente expresó el solicitante aunque posteriormente el diagnóstico revele una causa o necesidad diferente.

---

# 11. Caso

## Definición provisional

Unidad de seguimiento que agrupa la información, acciones, comunicaciones y resultados relacionados con una necesidad determinada.

Un caso puede extenderse durante múltiples días y requerir:

- comunicaciones;
- diagnóstico;
- cotizaciones;
- pagos;
- citas;
- visitas;
- refacciones;
- pruebas;
- seguimiento;
- y múltiples reportes.

## Importante

La diferencia exacta entre "Solicitud" y "Caso" deberá validarse antes de diseñar el modelo de datos.

Conceptualmente:

**Solicitud = qué se está pidiendo.**

**Caso = todo el seguimiento necesario para atenderlo.**

Esta distinción queda provisionalmente aceptada, pero pendiente de validación mediante procesos reales.

---

# 12. Servicio

## Definición

Trabajo profesional proporcionado por Ocre para atender total o parcialmente una necesidad.

Ejemplos:

- diagnóstico;
- reparación;
- mantenimiento;
- instalación;
- calibración;
- modificación;
- capacitación;
- consultoría;
- puesta en marcha.

## Importante

Un servicio no es necesariamente equivalente a una visita.

Un servicio puede requerir varias visitas y una visita puede incluir varias actividades.

---

# 13. Diagnóstico General Inicial

## Definición

Evaluación estructurada realizada cuando Ocre interviene por primera vez un equipo.

Su propósito es establecer una línea base del equipo y comenzar formalmente su expediente técnico.

Puede coexistir con una reparación específica solicitada por el cliente.

**Abreviatura provisional:** DGI.

---

# 14. Diagnóstico

## Definición

Proceso mediante el cual se recopila evidencia, se formulan hipótesis, se realizan comprobaciones y se determina, con el nivel de certeza disponible, la causa o condición relacionada con una necesidad o falla.

## Principio

Una hipótesis técnicamente posible no constituye por sí misma un diagnóstico confirmado.

El sistema deberá permitir distinguir grados de certeza.

---

# 15. Síntoma

## Definición

Manifestación observable o reportada de un comportamiento no esperado.

Ejemplos:

- no enciende;
- pierde potencia;
- produce piezas fuera de medida;
- se detiene intermitentemente;
- presenta una alarma;
- pierde comunicación.

## Importante

El síntoma no debe confundirse con la causa.

---

# 16. Hallazgo

## Definición

Condición relevante descubierta durante una inspección, diagnóstico, servicio o análisis.

Un hallazgo puede estar relacionado o no con la solicitud original.

Ejemplos:

- cable deteriorado;
- ventilación obstruida;
- voltaje fuera de rango;
- componente con desgaste;
- respaldo inexistente;
- condición insegura.

Un hallazgo no implica automáticamente que sea la causa del problema investigado.

---

# 17. Hipótesis

## Definición

Explicación técnicamente posible que puede justificar uno o varios síntomas y que requiere comprobación.

Una hipótesis puede:

- mantenerse abierta;
- ganar evidencia;
- perder evidencia;
- descartarse;
- o confirmarse.

---

# 18. Causa

## Definición

Condición identificada que explica un síntoma o problema con evidencia suficiente.

## Causa raíz

Condición subyacente cuya corrección elimina o reduce de manera fundamental la posibilidad de repetición del problema.

Una pieza dañada no siempre constituye la causa raíz.

Ejemplo:

Un contactor quemado puede ser la causa inmediata de que una máquina no encienda, mientras que una conexión deficiente, sobrecarga o problema de alimentación puede constituir la causa raíz de que el contactor se haya dañado.

---

# 19. Evidencia

## Definición

Información utilizada para respaldar una observación, hipótesis, diagnóstico, actividad o conclusión.

Puede incluir:

- fotografía;
- video;
- medición;
- lectura;
- archivo;
- alarma;
- registro;
- captura de pantalla;
- documento;
- prueba funcional;
- testimonio;
- u otra observación.

## Importante

Ocre OS deberá distinguir, cuando sea relevante, entre información reportada por una persona y evidencia obtenida directamente mediante una prueba o medición.

---

# 20. Prueba

## Definición

Acción deliberada realizada para obtener evidencia, comprobar una condición o evaluar una hipótesis.

Ejemplos:

- medir voltaje;
- verificar corriente;
- ejecutar una pieza de prueba;
- inspeccionar temperatura;
- intercambiar temporalmente un componente;
- repetir una operación bajo condiciones controladas.

---

# 21. Actividad

## Definición

Acción realizada por Ocre dentro de un servicio.

Ejemplos:

- inspeccionar;
- medir;
- desmontar;
- limpiar;
- calibrar;
- configurar;
- reparar;
- reemplazar;
- respaldar;
- capacitar.

Una actividad no implica necesariamente una reparación.

---

# 22. Intervención

## Definición

Modificación física, eléctrica, electrónica, lógica o de configuración realizada sobre un equipo, sistema o infraestructura.

Puede ser:

- temporal;
- definitiva;
- reversible;
- correctiva;
- preventiva;
- de mejora.

Toda intervención relevante deberá ser trazable.

---

# 23. Solución temporal

## Definición

Intervención deliberadamente limitada cuyo objetivo principal es recuperar o mantener temporalmente la capacidad productiva mientras se prepara una solución definitiva.

## Principio

Una solución temporal no debe quedar registrada de forma que pueda confundirse posteriormente con una reparación definitiva.

Debe indicar:

- motivo;
- limitaciones;
- riesgos conocidos;
- duración o condición esperada;
- acción definitiva pendiente.

---

# 24. Solución definitiva

## Definición

Intervención destinada a corregir de manera estable la condición identificada, dentro de los alcances técnicos razonables del servicio.

Cuando sea posible, deberá considerar la causa raíz y no solamente el síntoma inmediato.

---

# 25. Visita

## Definición

Presencia física de uno o más integrantes de Ocre en una ubicación para realizar actividades relacionadas con uno o varios servicios.

Una visita tiene:

- fecha;
- ubicación;
- participantes;
- actividades;
- tiempos;
- y resultados.

## Importante

Visita y servicio no son sinónimos.

---

# 26. Cita

## Definición

Compromiso programado para realizar una interacción o actividad en una fecha y horario determinados.

Puede corresponder a:

- visita presencial;
- llamada;
- videollamada;
- diagnóstico remoto;
- capacitación;
- seguimiento.

Una cita puede estar relacionada con una solicitud, caso o servicio.

---

# 27. Equipo

## Definición

Activo físico identificable que participa en la operación o proceso productivo y cuya información técnica resulta relevante para Ocre.

Ejemplos:

- router CNC;
- cortadora láser;
- impresora;
- compresor;
- chiller;
- computadora industrial;
- sistema de extracción.

Cada equipo atendido deberá poder adquirir una identificación única dentro de Ocre OS.

---

# 28. Expediente técnico

## Definición

Conjunto acumulativo de información conocida sobre un equipo específico.

Puede contener:

- identificación;
- configuración;
- fotografías;
- componentes;
- historial;
- diagnósticos;
- intervenciones;
- servicios;
- documentación;
- respaldos;
- relaciones con otros equipos;
- operadores;
- y conocimiento específico.

## Importante

El expediente pertenece al equipo específico.

No debe confundirse con la base de conocimiento correspondiente al modelo o tecnología.

---

# 29. Modelo de equipo

## Definición

Representación de una familia o modelo técnico compartido por múltiples equipos físicos.

Ejemplo:

Dos clientes diferentes pueden poseer equipos del mismo fabricante y modelo.

Cada equipo tiene su propio expediente, pero ambos pueden compartir conocimiento del modelo.

---

# 30. Base de conocimiento

## Definición

Repositorio estructurado de conocimiento técnico reutilizable que no pertenece exclusivamente a un equipo individual.

Puede relacionarse con:

- fabricantes;
- modelos;
- tecnologías;
- componentes;
- fallas;
- síntomas;
- procedimientos;
- configuraciones;
- manuales;
- soluciones;
- herramientas;
- y experiencia comprobada.

## Diferencia fundamental

**Expediente técnico:** qué sabemos de ESTA máquina.

**Base de conocimiento:** qué sabemos que puede ser reutilizado para ESTA CLASE de máquinas, componentes, procesos o problemas.

---

# 31. Relación entre equipos

## Definición

Vínculo funcional, tecnológico o productivo existente entre dos equipos.

Puede representar:

- alimentación de material;
- salida hacia otro proceso;
- intercambio de información;
- dependencia;
- compatibilidad;
- tecnología compartida;
- o cualquier relación técnicamente relevante.

Una relación no requiere necesariamente que ambos equipos pertenezcan al mismo cliente.

---

# 32. Proceso productivo

## Definición

Conjunto de actividades, personas, equipos, materiales, información y recursos mediante los cuales el cliente genera un producto o resultado.

El proceso productivo constituye un nivel de análisis superior al equipo individual.

## Principio

Ocre busca preservar o mejorar el proceso productivo, no únicamente mantener máquinas encendidas.

---

# 33. Operador

## Definición

Persona que utiliza, controla o participa directamente en la operación de un equipo.

Un equipo puede tener múltiples operadores a lo largo del tiempo.

---

# 34. Perfil recomendado de operador

## Definición

Conjunto de capacidades, conocimientos y características operativas consideradas convenientes para utilizar correctamente un equipo determinado.

No representa una evaluación personal o laboral del individuo.

Su propósito es identificar necesidades de:

- capacitación;
- conocimiento;
- atención;
- destreza;
- criterio;
- fuerza;
- precisión;
- o experiencia.

---

# 35. Fabricante

## Definición

Organización responsable de fabricar o desarrollar un equipo, componente o sistema.

Puede constituir una fuente de:

- soporte;
- documentación;
- software;
- refacciones;
- capacitación;
- actualizaciones;
- y conocimiento técnico.

---

# 36. Distribuidor

## Definición

Organización o persona que comercializó, suministró o representa un equipo o producto.

Puede o no proporcionar soporte técnico.

El distribuidor no debe confundirse automáticamente con el fabricante.

---

# 37. Proveedor

## Definición

Persona u organización capaz de suministrar un producto, componente, servicio o recurso necesario para una operación.

Un fabricante o distribuidor puede también actuar como proveedor, pero los conceptos representan relaciones diferentes.

---

# 38. Refacción

## Definición

Componente físico destinado o potencialmente utilizable para sustituir otro componente dentro de un equipo o sistema.

Una refacción puede ser:

- nueva;
- usada;
- recuperada;
- reparada;
- temporal;
- de emergencia;
- específica;
- compatible con múltiples equipos.

---

# 39. Consumible

## Definición

Elemento cuyo desgaste, agotamiento o sustitución periódica forma parte normal de la operación.

Ejemplos:

- filtros;
- lubricantes;
- boquillas;
- cuchillas;
- lentes;
- gases;
- materiales de limpieza.

La distinción entre refacción y consumible dependerá de la función y ciclo de uso, no únicamente de su costo.

---

# 40. Inventario

## Definición

Conjunto de materiales, refacciones, consumibles, herramientas u otros activos cuya existencia y disponibilidad Ocre necesita conocer.

El inventario deberá permitir identificar no solamente cantidad, sino condición y posibles restricciones de uso cuando corresponda.

---

# 41. Pendiente

## Definición

Acción necesaria que todavía no ha sido completada.

Todo pendiente deberá, cuando sea posible, tener:

- responsable;
- motivo;
- prioridad;
- fecha objetivo o condición de ejecución;
- y estado.

## Principio

Los pendientes no deben depender exclusivamente de la memoria de una persona.

---

# 42. Seguimiento

## Definición

Actividad posterior destinada a verificar evolución, completar pendientes, obtener información o continuar la atención de una necesidad.

Un seguimiento puede realizarse sin generar una visita física.

---

# 43. Recomendación

## Definición

Acción sugerida por Ocre que no necesariamente forma parte del alcance ejecutado.

Debe poder distinguirse entre:

- recomendación inmediata;
- preventiva;
- de mejora;
- de seguridad;
- operativa;
- o futura.

---

# 44. Reporte de servicio

## Definición

Documento formal que comunica al cliente la información relevante de uno o varios trabajos realizados.

Debe generarse principalmente a partir de la información estructurada capturada durante la operación.

No debe depender de reconstruir posteriormente el servicio de memoria.

---

# 45. Cotización

## Definición

Propuesta económica y de alcance presentada para aprobación.

Puede incluir:

- servicios;
- materiales;
- refacciones;
- tiempos;
- condiciones;
- anticipos;
- vigencia;
- exclusiones.

Una cotización no significa que el trabajo haya sido autorizado.

---

# 46. Anticipo

## Definición

Pago parcial solicitado antes de ejecutar determinadas actividades.

El porcentaje o monto puede depender del servicio y no debe quedar rígidamente fijado en la definición del concepto.

## Observación

El 50 % actualmente contemplado es una regla comercial inicial, no parte de la definición universal de "anticipo".

---

# 47. Pago

## Definición

Registro de una transacción económica relacionada con uno o varios conceptos cobrados por Ocre.

Un pago no equivale a una factura fiscal.

---

# 48. Solicitud de facturación

## Definición

Registro mediante el cual se reúne y entrega la información necesaria para que se genere externamente una factura fiscal.

Puede contener:

- información fiscal;
- documentos;
- correo receptor;
- concepto;
- pago relacionado;
- instrucciones;
- estado;
- y responsable.

La emisión fiscal se encuentra inicialmente fuera de Ocre OS.

---

# 49. Estado

## Definición

Representación de la situación actual de un objeto o proceso.

## Principio

Los estados deberán representar situaciones reales del negocio y no únicamente necesidades visuales de una pantalla.

Ejemplos futuros podrían incluir:

- pendiente de información;
- pendiente de pago;
- agendado;
- en atención;
- esperando refacción;
- pendiente de validación;
- cerrado.

Las listas definitivas de estados se establecerán al modelar cada proceso.

---

# 50. Prioridad

## Definición

Nivel de importancia relativa utilizado para ordenar atención o recursos.

## Importante

Prioridad no es sinónimo de urgencia.

Un asunto puede ser urgente por tiempo y otro puede ser prioritario por impacto productivo, seguridad, compromiso comercial u otras razones.

---

# 51. Urgencia

## Definición

Grado en que una necesidad requiere atención dentro de un periodo reducido.

La urgencia debe evaluarse separadamente de otros criterios como impacto, riesgo y prioridad.

---

# 52. Trazabilidad

## Definición

Capacidad de reconstruir qué ocurrió con información suficiente para conocer:

- qué cambió;
- quién realizó el cambio;
- cuándo ocurrió;
- dentro de qué contexto;
- y, cuando sea relevante, por qué se realizó.

---

# 53. Regla de negocio

## Definición

Condición o principio operativo que Ocre OS debe respetar independientemente de la interfaz utilizada.

Ejemplo:

> El primer servicio sobre un equipo debe incluir un Diagnóstico General Inicial.

Las reglas de negocio deberán documentarse explícitamente y no quedar ocultas únicamente dentro del código.

---

# 54. Cierre

## Definición

Condición mediante la cual se determina que una solicitud, caso, servicio u otro proceso no requiere actualmente más acciones dentro de su alcance.

Cerrar no significa borrar.

La información y trazabilidad deben permanecer disponibles.

---

# 55. Reapertura

## Definición

Reactivación de un elemento previamente cerrado cuando surge una razón válida para continuar su atención.

La reapertura debe conservar el historial anterior.

---

# 56. Términos pendientes de validación

Los siguientes términos requieren validación adicional antes de considerarse definitivos:

- Contacto 0;
- Solicitud;
- Caso;
- Servicio;
- Orden de servicio;
- Trabajo;
- Visita;
- Incidencia;
- Oportunidad;
- Prospecto;
- Activo;
- Equipo;
- Expediente;
- cierre técnico;
- cierre administrativo;
- alcance;
- compromiso;
- entrega.

No deberán convertirse automáticamente en entidades independientes hasta definir claramente sus límites y relaciones.

---

# 57. Regla de mantenimiento del glosario

Cuando durante el diseño aparezca una palabra cuyo significado pueda interpretarse de más de una manera:

1. se detiene la decisión técnica;
2. se define el concepto;
3. se agrega o corrige este glosario;
4. se valida su relación con los conceptos existentes;
5. y posteriormente se continúa con el diseño.

El glosario es un documento vivo y podrá modificarse cuando una definición más precisa represente mejor la operación real de Ocre.
