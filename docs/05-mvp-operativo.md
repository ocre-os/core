# MVP Operativo de Ocre OS

**Estado:** Borrador  
**Versión:** 0.1

## 1. Propósito

Definir la primera versión utilizable de Ocre OS que debe generar valor operativo y económico real antes de incorporar toda la visión futura de la plataforma.

El MVP no busca demostrar tecnología. Busca resolver los problemas actuales más urgentes:

- servicios realizados que no quedan documentados adecuadamente;
- reportes que no se entregan oportunamente;
- trabajos y pendientes que dependen de memoria;
- dificultad para dar seguimiento a lo realizado;
- cobros que se retrasan por falta de control;
- información técnica que se dispersa o se pierde.

El MVP debe ser suficientemente útil para comenzar a utilizarse en servicios reales y suficientemente estructurado para no convertirse en un prototipo desechable.

---

# 2. Resultado mínimo esperado

La primera versión debe permitir completar de principio a fin este escenario:

1. Registrar una nueva Interacción.
2. Identificar o crear Contacto y Organización.
3. Registrar la Solicitud original.
4. Abrir un Caso.
5. Relacionar uno o varios Equipos cuando corresponda.
6. Crear un Servicio.
7. Programar y ejecutar una Visita.
8. Capturar desde campo actividades, fotografías, mediciones, hallazgos, diagnóstico, intervenciones y Pendientes.
9. Generar un Reporte profesional sin volver a escribir el trabajo realizado.
10. Entregar o dejar listo el Reporte para el cliente.
11. Registrar el estado económico del trabajo.
12. Generar, cuando corresponda, una Solicitud de facturación.
13. Mantener visible cualquier Pendiente posterior.

Si Ocre OS puede ejecutar este ciclo con confiabilidad, la plataforma ya genera valor aunque todavía no tenga toda la inteligencia diagnóstica futura.

---

# 3. Principios del MVP

## 3.1 Utilizable en campo

Las funciones críticas deben operar correctamente desde teléfono, tableta o computadora.

La captura en campo debe requerir la menor cantidad razonable de escritura repetitiva.

## 3.2 Captura progresiva

No se exigirá completar todo el expediente antes de comenzar una atención.

La información debe crecer conforme avanza el proceso.

## 3.3 Capturar una vez

Los datos introducidos durante la operación deben reutilizarse en:

- expedientes;
- Reportes;
- seguimiento;
- cobro;
- y posteriormente base de conocimiento.

## 3.4 El MVP no debe bloquear excepciones reales

El flujo normal será guiado, pero debe ser posible atender casos como:

- Solicitud sin Equipo conocido;
- Caso de infraestructura;
- cliente existente con Equipo nuevo;
- reincidencia;
- varias Visitas para un Servicio;
- Servicio concluido con Pendientes administrativos;
- solución temporal pendiente de reemplazo definitivo.

## 3.5 Valor operativo antes que automatización avanzada

La primera versión debe priorizar control, Reportes, seguimiento y cobro.

La IA diagnóstica será construida sobre los datos reales capturados por la operación.

---

# 4. Usuarios iniciales

## 4.1 Administrador / técnico principal

En la primera versión deberá poder:

- administrar Organizaciones y Contactos;
- registrar Interacciones;
- abrir y administrar Casos;
- administrar Equipos;
- ejecutar Servicios y Visitas;
- generar Reportes;
- administrar Pendientes;
- consultar el estado económico;
- preparar Solicitudes de facturación.

Inicialmente este rol podrá concentrar la mayoría de permisos.

## 4.2 Técnico

Debe poder, según permisos:

- consultar los Casos asignados;
- consultar historial técnico relevante;
- registrar Visitas;
- capturar diagnóstico y Evidencias;
- registrar actividades e Intervenciones;
- crear Pendientes;
- preparar el contenido de Reportes.

## 4.3 Cliente

El portal completo no es requisito para la primera entrega interna, pero la arquitectura debe permitir incorporarlo sin rediseñar el dominio.

La primera versión del portal deberá posteriormente permitir:

- iniciar sesión;
- ver Equipos autorizados;
- consultar Casos y su estado;
- consultar Reportes emitidos;
- aportar documentación;
- consultar pagos o instrucciones de pago;
- solicitar facturación.

---

# 5. Módulos funcionales del MVP

## 5.1 Inicio y tablero operativo

Debe responder rápidamente:

- ¿qué debo atender hoy?;
- ¿qué Casos están abiertos?;
- ¿qué Visitas están programadas?;
- ¿qué Reportes faltan?;
- ¿qué trabajos están pendientes de cobro?;
- ¿qué Pendientes necesitan atención?;
- ¿qué Casos están esperando información, refacción o cliente?

### Criterio de aceptación

El técnico no debe depender de recordar personalmente qué quedó pendiente al terminar el día.

---

## 5.2 Interacciones y clasificación

Debe permitir registrar rápidamente:

- canal;
- fecha y hora;
- teléfono, correo u otro identificador disponible;
- nombre si se conoce;
- mensaje o resumen;
- archivos o Evidencias iniciales.

Debe permitir después:

- relacionar con Contacto;
- relacionar con Organización;
- relacionar con Solicitud o Caso existente;
- crear nueva Solicitud;
- dejar temporalmente como Contacto 0.

### Criterio de aceptación

Registrar una llamada o WhatsApp nuevo no debe obligar a crear un cliente ficticio ni perder la comunicación si ya existía un Caso.

---

## 5.3 Organizaciones y Contactos

### Organización

Debe incluir inicialmente:

- nombre comercial;
- razón social cuando exista;
- teléfonos;
- correos generales;
- observaciones;
- estado de relación;
- roles relevantes;
- información fiscal disponible.

### Contacto

Debe incluir inicialmente:

- nombre;
- teléfonos;
- WhatsApp;
- correos;
- Organizaciones relacionadas;
- funciones o roles dentro de cada Organización;
- notas relevantes.

### Criterio de aceptación

Una persona que sea operador y encargado de compras no debe necesitar dos registros diferentes.

---

## 5.4 Ubicaciones

Debe permitir registrar:

- Organización;
- nombre identificable de la instalación;
- dirección;
- referencias de acceso;
- horarios;
- contactos relevantes;
- observaciones técnicas del entorno.

### Criterio de aceptación

Una Organización debe poder tener varios talleres, plantas o instalaciones sin duplicarse como cliente.

---

## 5.5 Equipos

Debe permitir crear un Equipo con información incompleta e ir enriqueciéndolo.

### Datos mínimos iniciales sugeridos

- identificador interno Ocre OS;
- Organización responsable actual;
- Ubicación actual;
- tipo o familia;
- marca si se conoce;
- modelo si se conoce;
- número de serie si se conoce;
- descripción libre inicial;
- fotografías principales.

### Información progresiva

- placas;
- características técnicas;
- componentes;
- alimentación eléctrica;
- software;
- configuraciones;
- operador;
- fabricante y distribuidor;
- documentos;
- relaciones con otros Equipos.

### Criterio de aceptación

El sistema debe poder identificar inequívocamente un Equipo aun cuando el cliente tenga varias máquinas del mismo modelo.

---

## 5.6 Diagnóstico General Inicial

Debe implementarse como un tipo de Servicio configurable.

La primera versión debe permitir capturar, cuando corresponda:

- identificación y fotografías;
- estado general;
- instalación eléctrica;
- condiciones ambientales;
- componentes relevantes;
- estado mecánico;
- software y configuraciones;
- pruebas funcionales;
- pruebas dimensionales o de calidad;
- operador actual;
- perfil recomendado;
- objetivo operativo del cliente;
- función del Equipo dentro del proceso productivo;
- documentación disponible y faltante.

No todos los campos serán obligatorios para todos los tipos de Equipo.

### Criterio de aceptación

El DGI debe generar información reutilizable para el Expediente técnico y no quedar encerrado solamente en un PDF.

---

## 5.7 Solicitudes y Casos

### Solicitud

Debe conservar como mínimo:

- expresión original;
- solicitante;
- Organización;
- urgencia;
- necesidad percibida;
- Equipos relacionados si se conocen;
- Evidencias iniciales.

### Caso

Debe permitir:

- estado;
- prioridad;
- responsable;
- relación con Solicitudes;
- Organización y Ubicación;
- Equipos afectados;
- Interacciones;
- Servicios;
- Visitas;
- Pendientes;
- Reportes;
- relaciones con otros Casos.

### Criterio de aceptación

Debe poder abrirse un Caso aun cuando el problema finalmente sea la instalación eléctrica y no el Equipo inicialmente reportado.

---

## 5.8 Reincidencias

Debe existir la capacidad de:

- reabrir un Caso;
- registrar el motivo;
- entrar en `En evaluación de reincidencia`;
- conservar la nueva Interacción;
- continuar el Caso anterior;
- o crear un nuevo Caso relacionado después de la evaluación.

### Criterio de aceptación

El sistema nunca debe obligar a decidir prematuramente que una nueva falla es igual o diferente de la anterior.

---

## 5.9 Servicios

Debe permitir crear Servicios dentro de un Caso.

### Tipos iniciales

- Diagnóstico General Inicial;
- diagnóstico específico;
- reparación;
- mantenimiento preventivo;
- mantenimiento correctivo;
- calibración;
- instalación;
- modificación;
- capacitación;
- consultoría.

Los tipos deberán ser configurables posteriormente.

### Criterio de aceptación

Un Caso debe poder contener más de un Servicio sin convertirse en varios Casos artificialmente.

---

## 5.10 Citas y agenda

Debe permitir registrar:

- fecha;
- hora;
- duración estimada;
- tipo de Cita;
- responsable;
- Organización;
- Ubicación;
- Caso relacionado.

La integración con Google Calendar deberá incorporarse de forma que Ocre OS conserve el contexto de negocio y Google Calendar funcione como agenda sincronizada.

### MVP inicial

Es aceptable comenzar con sincronización unidireccional o manualmente asistida si eso acelera la primera versión utilizable.

La agenda automática para clientes quedará en una iteración posterior del mismo MVP ampliado.

---

## 5.11 Visitas

Una Visita debe funcionar como espacio de captura de trabajo en campo.

Debe permitir registrar:

- hora de inicio y término;
- técnicos;
- Ubicación;
- Servicios trabajados;
- descripción de actividades;
- fotografías y archivos;
- mediciones;
- Síntomas;
- Hallazgos;
- Pruebas;
- diagnóstico;
- Intervenciones;
- refacciones utilizadas;
- recomendaciones;
- Pendientes;
- resultado de la Visita.

### Criterio de aceptación

Al terminar la Visita debe existir suficiente información para producir el Reporte sin reconstruir de memoria lo realizado.

---

## 5.12 Evidencias

Debe ser posible adjuntar Evidencias desde teléfono.

Tipos iniciales:

- fotografía;
- video o enlace a video;
- documento;
- captura de pantalla;
- medición;
- archivo técnico.

Cada Evidencia debe conservar contexto suficiente para saber a qué corresponde.

### Criterio de aceptación

Una fotografía no debe quedar como archivo huérfano cuyo significado sea imposible identificar meses después.

---

## 5.13 Diagnóstico

La primera versión no necesita implementar todavía el motor inteligente completo.

Sí debe separar conceptualmente:

- Síntoma;
- Hallazgo;
- Hipótesis;
- Prueba;
- Evidencia;
- diagnóstico o conclusión;
- Causa y Causa raíz cuando se conozcan;
- Intervención.

### Estrategia inicial

Algunas secciones pueden comenzar con estructuras simples y texto enriquecido mientras se recopila evidencia real sobre qué campos necesitan convertirse en catálogos o estructuras más rígidas.

### Criterio de aceptación

El técnico debe poder expresar incertidumbre sin ser obligado a marcar una hipótesis como causa confirmada.

---

## 5.14 Reportes

Este es uno de los componentes de mayor prioridad del MVP.

Debe generar un Reporte profesional a partir de la información ya capturada.

### Contenido inicial

- identidad visual de Ocre;
- folio;
- fecha;
- Organización;
- Contacto;
- Ubicación;
- Equipo o Equipos;
- Solicitud original;
- objetivo del Servicio;
- actividades realizadas;
- diagnóstico;
- Evidencias seleccionadas;
- mediciones;
- Intervenciones;
- refacciones;
- estado final;
- Pendientes;
- recomendaciones;
- próximos pasos;
- responsable técnico.

### Funciones

- vista previa;
- generación PDF;
- descarga;
- registro de fecha de emisión;
- conservación de la versión emitida.

### Criterio de aceptación crítico

Un Servicio real debe poder terminar con un PDF profesional sin que el técnico tenga que volver a redactar manualmente todo el reporte.

---

## 5.15 Pendientes

Debe existir una bandeja central de Pendientes.

Cada Pendiente debe permitir:

- responsable;
- descripción;
- contexto de origen;
- prioridad;
- estado;
- fecha objetivo;
- condición de reactivación;
- notas.

Ejemplos:

- pedir refacción;
- esperar respuesta del fabricante;
- llamar al cliente;
- volver a medir después de una semana;
- emitir cotización;
- generar factura;
- confirmar llegada de pieza.

### Criterio de aceptación crítico

Un Pendiente creado durante una Visita debe aparecer posteriormente sin depender de que el técnico recuerde revisarlo.

---

## 5.16 Control económico mínimo

El MVP no necesita contabilidad completa.

Sí necesita mostrar por Caso o Servicio:

- importe acordado cuando exista;
- anticipo requerido;
- anticipo recibido;
- saldo conocido;
- estado de cobro;
- Pagos registrados;
- si requiere factura;
- estado de Solicitud de facturación.

### Estados económicos preliminares

- sin cotizar;
- cotización pendiente;
- pendiente de anticipo;
- anticipo recibido;
- pendiente de cobro;
- parcialmente pagado;
- pagado;
- no cobrable / cortesía, con motivo.

Estos estados deben validarse antes de convertirse en catálogo definitivo.

### Criterio de aceptación crítico

Debe ser posible responder rápidamente: **¿qué trabajos ya realicé y todavía no he cobrado?**

---

## 5.17 Solicitud de facturación

Debe permitir reunir:

- Organización o persona fiscal;
- Perfil fiscal;
- documentos requeridos;
- correo receptor;
- concepto;
- monto;
- Pago relacionado;
- responsable de emitir externamente;
- estado;
- fecha de solicitud;
- factura recibida cuando corresponda.

### Criterio de aceptación

Una factura pendiente no debe depender de una conversación de WhatsApp o de que alguien recuerde solicitarla.

---

# 6. Funcionalidades deliberadamente fuera de la primera entrega

No se consideran necesarias para que la primera versión interna genere valor:

- motor completo de diagnóstico con IA;
- aplicación móvil nativa;
- inventario avanzado con compras y proveedores completamente automatizados;
- portal de terceros/talleres completo;
- facturación fiscal directa;
- analítica avanzada;
- automatización completa de WhatsApp;
- marketplace de técnicos;
- optimización automática de rutas;
- base de conocimiento totalmente estructurada;
- mantenimiento predictivo avanzado.

Estas funciones no se descartan. Se posponen para evitar retrasar el ciclo operativo que actualmente genera dinero.

---

# 7. Entidades necesarias para la primera implementación

La primera implementación probablemente necesitará, como mínimo, persistencia para los siguientes conceptos:

- Usuario;
- Contacto;
- Organización;
- relación Contacto–Organización;
- Perfil fiscal;
- Ubicación;
- Equipo;
- Interacción;
- Solicitud;
- Caso;
- relación entre Casos;
- Servicio;
- Cita;
- Visita;
- Pendiente;
- Evidencia;
- registros de diagnóstico;
- Reporte y versión de Reporte;
- Cotización, si se incorpora desde la primera iteración;
- Pago;
- Solicitud de facturación.

Contacto 0 no requiere inicialmente persistencia como Entidad independiente; puede representarse mediante estado de clasificación de la Interacción.

---

# 8. Corte vertical de primera utilidad

Para evitar construir muchos módulos incompletos, la primera implementación debe priorizar un corte vertical completo.

## Corte V0

**Organización → Contacto → Equipo → Caso → Servicio → Visita → Reporte → Pendiente de cobro**

Debe incluir lo mínimo necesario de Interacción y Solicitud para conservar el origen del trabajo.

### Demostración de terminación

El corte V0 se considera funcional cuando se pueda realizar este ejercicio con datos reales:

1. registrar un cliente;
2. registrar una máquina;
3. abrir un Caso real;
4. comenzar una Visita desde el teléfono;
5. tomar fotografías;
6. capturar actividades y diagnóstico;
7. finalizar la Visita;
8. generar el PDF;
9. marcar el trabajo pendiente de cobro;
10. ver ese pendiente desde el tablero.

Hasta que este recorrido funcione de principio a fin, no deberá priorizarse el desarrollo de características avanzadas no necesarias para completarlo.

---

# 9. Segundo corte funcional

Una vez estable el corte V0, el siguiente incremento debe incorporar:

- Interacciones y Contacto 0 completos;
- clasificación y reincidencias;
- DGI estructurado;
- Cotizaciones;
- Pagos;
- Solicitud de facturación;
- sincronización con Google Calendar;
- primera versión del portal del cliente.

---

# 10. Tercer corte funcional

Posteriormente:

- inventario y refacciones;
- trazabilidad de unidades físicas reutilizables;
- relaciones de proceso entre Equipos;
- base de conocimiento;
- asistencia diagnóstica;
- incorporación de técnicos externos;
- automatizaciones avanzadas.

---

# 11. Requisitos no funcionales iniciales

Aunque el MVP sea pequeño, debe respetar desde el comienzo ciertos requisitos mínimos.

## 11.1 Seguridad

- autenticación;
- control de permisos;
- protección de documentos de clientes;
- separación entre organizaciones en el portal;
- uso de HTTPS en producción;
- secretos fuera del código fuente.

## 11.2 Trazabilidad

Los cambios críticos deben conservar autor y fecha.

## 11.3 Respaldo

La base de datos y archivos importantes deben tener estrategia de respaldo antes de que el sistema almacene información operacional única.

## 11.4 Portabilidad

La implementación debe poder migrarse razonablemente entre servidores y ambientes.

## 11.5 Diseño responsivo

Las funciones de campo deben funcionar correctamente en pantalla móvil.

## 11.6 Integridad documental

Los Reportes emitidos deben conservarse como versiones identificables.

---

# 12. Definición de éxito del MVP

El MVP será exitoso cuando Ocre pueda utilizarlo en operación real y observar, como mínimo, estos efectos:

- disminución de Servicios sin Reporte;
- reducción del tiempo entre Servicio y entrega de Reporte;
- visibilidad de trabajos pendientes de cobro;
- visibilidad de Pendientes técnicos y administrativos;
- crecimiento automático del historial de cada Equipo;
- capacidad de retomar un Caso sin depender exclusivamente de memoria;
- datos suficientes para empezar a construir posteriormente automatización e inteligencia.

---

# 13. Próxima decisión técnica

Con el Modelo de Dominio y el MVP definidos, el siguiente paso técnico es diseñar el **modelo de datos V0 exclusivamente para el corte vertical de primera utilidad**.

No se diseñará todavía toda la base de datos futura.

Se modelarán primero las estructuras necesarias para:

**Organización → Contacto → Equipo → Caso → Servicio → Visita → Reporte → Pendiente de cobro**

más la información mínima requerida para preservar Solicitud e Interacción.
