# Modelo Operativo de Ocre OS

**Estado:** Borrador  
**Versión:** 0.2

## 1. Propósito del documento

Este documento define cómo opera Ocre desde el punto de vista del negocio.

Su propósito es establecer una referencia común para diseñar Ocre OS sin depender de interpretaciones individuales, conversaciones aisladas o decisiones técnicas prematuras.

Este documento describe:

- qué busca resolver Ocre para sus clientes;
- cómo nace y evoluciona una solicitud;
- qué información debe conservarse;
- cómo se relacionan clientes, personas, ubicaciones, equipos y servicios;
- cómo se ejecuta y documenta el trabajo técnico;
- y qué principios deben respetarse al desarrollar Ocre OS.

Este documento no define todavía tablas de base de datos, tecnologías, APIs ni interfaces específicas.

---

# 2. Filosofía operativa

## 2.1 El objetivo no es reparar máquinas

Ocre no tiene como objetivo final reparar una máquina.

El objetivo es **resolver o atender la necesidad productiva del cliente**.

Una máquina es un medio dentro de un proceso productivo. Una máquina funcionando correctamente pero incapaz de producir lo que el cliente necesita no necesariamente representa una necesidad resuelta.

Por lo tanto, una intervención puede requerir acciones sobre:

- la propia máquina;
- su instalación eléctrica;
- sistemas neumáticos, hidráulicos o de extracción;
- computadoras y software;
- archivos y configuraciones;
- operadores;
- materiales y consumibles;
- equipos anteriores o posteriores dentro del proceso;
- infraestructura de la empresa;
- proveedores o fabricantes;
- o incluso alternativas externas de producción.

El criterio de éxito debe relacionarse con la necesidad real del cliente.

---

## 2.2 Necesidad expresada y necesidad real

La solicitud expresada por el cliente y su necesidad real pueden ser diferentes.

Ejemplo:

> "Mi máquina no funciona."

puede significar realmente:

> "No puedo producir lo que necesito."

Si el diagnóstico demuestra que la máquina funciona correctamente pero existe una falla en la instalación eléctrica, el problema técnico cambió, pero la necesidad del cliente continúa siendo la misma: recuperar su capacidad de producción.

Ocre OS debe conservar ambas cosas:

1. lo que el cliente solicitó originalmente;
2. la necesidad real identificada durante el proceso.

La solicitud original nunca debe sobrescribirse o perderse debido a descubrimientos posteriores.

---

## 2.3 Alcance adaptable

No todos los clientes desean el mismo nivel de intervención.

Ocre puede operar, al menos, bajo dos enfoques:

### Ejecución específica

El cliente ya determinó qué necesita y desea que Ocre ejecute una actividad concreta.

En este contexto, Ocre debe respetar el alcance solicitado y evitar introducir innecesariamente consultoría adicional.

### Acompañamiento integral

Ocre analiza la necesidad productiva y puede proponer soluciones más allá de la reparación puntual del equipo.

Esto puede incluir:

- modificaciones;
- mejoras;
- optimización de procesos;
- capacitación;
- cambios de operación;
- integración entre equipos;
- producción mediante terceros;
- apoyo mediante otros equipos disponibles;
- mejoras de calidad;
- reducción de tiempos;
- maximización de consumibles;
- o estrategias para mantener la producción mientras se resuelve una falla.

Este nivel de acompañamiento debe poder activarse o desactivarse según las necesidades y preferencias del cliente.

---

# 3. Principio de continuidad de información

Ocre OS debe funcionar como una memoria operativa acumulativa.

La información obtenida durante una interacción no debe desaparecer al terminar el servicio.

Cada interacción debe enriquecer progresivamente la información existente sobre:

- personas;
- empresas;
- ubicaciones;
- equipos;
- configuraciones;
- procesos productivos;
- proveedores;
- fabricantes;
- refacciones;
- fallas;
- diagnósticos;
- soluciones;
- documentación técnica;
- y conocimiento adquirido.

El sistema debe evitar solicitar repetidamente información que ya conoce, pero debe permitir verificarla y actualizarla cuando sea necesario.

---

# 4. Inicio de una atención: Interacción y Contacto 0

Toda atención comienza con una **Interacción**, es decir, con un evento de comunicación que Ocre recibe o registra.

La Interacción puede producirse mediante:

- llamada telefónica;
- WhatsApp;
- correo electrónico;
- formulario;
- mensaje desde el portal;
- recomendación;
- referencia de otra persona;
- contacto presencial;
- u otro canal.

La Interacción debe conservarse incluso cuando posteriormente se determine que corresponde a información ya existente.

En el momento de recibirla puede desconocerse:

- quién es exactamente la persona;
- a qué Organización pertenece;
- si ya existe como Contacto;
- si existe una Solicitud relacionada;
- si existe un Caso relacionado;
- qué Equipo está involucrado;
- cuál es la necesidad concreta;
- o qué acción debe realizarse.

Ocre OS debe permitir registrar esta realidad sin obligar a inventar información inexistente.

Cuando no exista información suficiente para clasificar la Interacción con certeza, podrá utilizarse provisionalmente la clasificación:

**Contacto 0 (C0)**

Contacto 0 no representa una persona, una Organización ni una Interacción adicional. Representa únicamente que la Interacción todavía requiere clasificación.

Al resolverse C0, la Interacción puede:

- relacionarse con un Contacto existente;
- relacionarse con una Organización existente;
- relacionarse con una Solicitud existente;
- relacionarse con un Caso existente;
- generar una nueva Solicitud;
- actualizar información existente;
- generar un Pendiente;
- o cerrarse sin acción posterior.

Resolver o cerrar Contacto 0 nunca elimina la Interacción que lo originó.

---

# 5. Solicitud

Cuando existe una necesidad identificable que requiere atención o seguimiento, se genera una solicitud.

Una solicitud debe conservar:

- quién la realizó;
- qué expresó;
- qué necesita o espera;
- a qué empresa corresponde;
- a qué ubicación corresponde, cuando se conozca;
- qué equipo está relacionado, cuando aplique;
- nivel de urgencia;
- información obtenida durante el contacto;
- evidencia disponible;
- acuerdos realizados;
- y siguiente acción requerida.

Una solicitud puede existir aun cuando todavía no se conozca el equipo involucrado.

La solicitud debe crecer conforme se obtiene información.

---

# 6. Cliente, empresa y personas

Debe evitarse utilizar la palabra "cliente" para representar indistintamente a una empresa y a una persona.

Una organización puede tener múltiples personas relacionadas con Ocre, por ejemplo:

- propietario;
- encargado de compras;
- operador;
- supervisor;
- gerente;
- administración;
- mantenimiento;
- contabilidad;
- responsable de pagos;
- responsable de facturación.

Una misma persona puede desempeñar más de una función.

El sistema deberá permitir relacionar personas con organizaciones sin duplicar innecesariamente información.

Los datos fiscales forman parte de la información de la organización o entidad correspondiente y deben estar disponibles dentro de su expediente.

La generación de la factura fiscal permanecerá inicialmente fuera de Ocre OS.

Ocre OS deberá, sin embargo, ser capaz de generar una **solicitud de facturación** con la información y documentación necesarias para que una persona externa realice el proceso fiscal.

---

# 7. Ubicaciones

Una organización puede operar en una o múltiples ubicaciones.

Los equipos deben poder relacionarse con su ubicación física actual.

Una ubicación puede contener información relevante para el servicio, incluyendo:

- dirección;
- contactos;
- condiciones de acceso;
- horarios;
- características de la instalación;
- alimentación eléctrica;
- infraestructura;
- condiciones ambientales;
- restricciones;
- y observaciones técnicas.

Debe conservarse la posibilidad de registrar movimientos históricos de equipos entre ubicaciones.

---

# 8. Equipo y expediente técnico

Todo equipo atendido por Ocre debe desarrollar progresivamente un expediente técnico.

El expediente no debe limitarse a marca, modelo y número de serie.

Puede contener:

- identificación única dentro de Ocre OS;
- fabricante;
- marca;
- modelo;
- número de serie;
- fotografías;
- placas y etiquetas;
- características técnicas;
- alimentación eléctrica;
- componentes;
- accesorios;
- configuraciones;
- software;
- firmware;
- parámetros;
- respaldos;
- modificaciones;
- reparaciones;
- mantenimientos;
- diagnósticos;
- pruebas;
- refacciones utilizadas;
- documentos;
- manuales;
- proveedores;
- fabricante;
- distribuidor original;
- historial de servicios;
- y conocimiento acumulado.

El expediente debe crecer durante toda la relación de Ocre con el equipo.

---

# 9. Diagnóstico General Inicial

El primer servicio realizado por Ocre sobre un equipo debe incluir un **Diagnóstico General Inicial**, incluso cuando el cliente haya solicitado originalmente una reparación específica.

El propósito es establecer una línea base confiable del estado del equipo.

El diagnóstico debe permitir conocer y documentar, según corresponda:

- identificación del equipo;
- estado general;
- condiciones de instalación;
- alimentación eléctrica;
- condiciones mecánicas;
- sistemas eléctricos y electrónicos;
- software y configuraciones;
- condiciones de seguridad;
- estado de componentes relevantes;
- pruebas funcionales;
- pruebas dimensionales o de calidad;
- fotografías;
- operador actual;
- perfil recomendado de operador;
- necesidades productivas;
- expectativas del propietario;
- y problemas conocidos.

Una reparación menor puede realizarse durante el mismo diagnóstico cuando:

- puede resolverse inmediatamente;
- no requiere una inversión relevante;
- no requiere una refacción significativa;
- y no altera materialmente el alcance o tiempo del servicio.

Estas acciones deben documentarse aunque no generen un cargo adicional.

---

# 10. Operador

El operador forma parte del contexto técnico del equipo.

Ocre OS debe permitir registrar:

- quién opera el equipo;
- experiencia;
- capacitación;
- conocimiento relevante;
- observaciones de operación;
- y adecuación respecto del perfil recomendado.

El perfil ideal puede variar según el equipo.

Entre otros factores pueden ser relevantes:

- atención al detalle;
- delicadeza;
- fuerza física;
- conocimiento de herramientas;
- comprensión de materiales;
- capacidad de ajuste;
- criterio de calidad;
- disciplina de operación;
- y conocimientos técnicos.

El objetivo no es calificar personalmente al operador, sino determinar si existe una diferencia relevante entre las necesidades del equipo y las capacidades requeridas para operarlo correctamente.

---

# 11. El equipo dentro del proceso productivo

Un equipo no debe analizarse necesariamente de forma aislada.

Debe documentarse su función dentro del proceso productivo.

Ocre OS debe permitir representar, de forma sencilla:

**Entrada → Equipo → Salida**

Cuando sea posible, los equipos relacionados deben identificarse mediante sus códigos únicos dentro de Ocre OS.

Un equipo puede recibir información, material o trabajo de otro equipo y alimentar posteriormente a uno o varios equipos adicionales.

Las relaciones pueden existir incluso entre equipos pertenecientes a organizaciones diferentes.

Esto permitirá identificar incompatibilidades entre procesos.

Ejemplo:

Una impresora puede producir una salida dimensionalmente incorrecta y la discrepancia hacerse visible únicamente cuando el producto llega posteriormente al proceso de corte láser.

El sistema debe ayudar a analizar la cadena productiva y no únicamente cada máquina de manera aislada.

---

# 12. Proveedores, distribuidores y fabricantes

El expediente técnico debe permitir identificar:

- quién fabricó el equipo;
- quién lo vendió;
- cómo fue adquirido;
- distribuidores;
- proveedores de refacciones;
- contactos técnicos;
- disponibilidad de soporte;
- documentación disponible;
- y nivel de apoyo obtenido.

Ocre debe procurar obtener oportunamente:

- manuales;
- manuales de servicio;
- documentación técnica;
- listas de refacciones;
- piezas de falla frecuente;
- actualizaciones;
- modificaciones;
- upgrades;
- software;
- herramientas especializadas;
- procedimientos;
- boletines;
- y capacitación.

Esta información debe conservarse aunque no exista una necesidad inmediata.

La disponibilidad futura de información sobre maquinaria industrial no está garantizada; por ello, el conocimiento obtenido durante la vida comercial del equipo constituye un activo técnico.

---

# 13. Refacciones y componentes

Las refacciones no deben clasificarse mediante una única categoría rígida.

Una misma pieza puede tener múltiples características, clasificaciones y usos posibles.

Por ejemplo, un contactor de 20 A adquirido para una máquina específica podría ser compatible con otros equipos o utilizarse posteriormente para resolver una emergencia.

Por ello, las características de una refacción deben conservarse como información reutilizable y consultable.

El sistema debe permitir distinguir, entre otros conceptos:

- pieza nueva;
- pieza usada;
- pieza reparada;
- pieza recuperada;
- pieza para uso permanente;
- pieza apta únicamente para uso temporal;
- pieza de emergencia;
- pieza pendiente de reparación;
- pieza no utilizable.

Una pieza retirada no necesariamente se convierte en desperdicio.

Después de mantenimiento o reparación puede conservarse como refacción temporal cuando sea técnicamente seguro hacerlo.

Ejemplo:

Un contactor retirado puede ser reacondicionado y mantenerse disponible para restaurar temporalmente la producción durante una emergencia. Una vez recibida la pieza nueva, ésta sustituye a la temporal y el contactor recuperado puede regresar al inventario de emergencia.

El sistema deberá conservar las restricciones de uso de este tipo de componentes para evitar que una solución temporal sea interpretada posteriormente como una reparación permanente.

---

# 14. Filosofía de diagnóstico

El diagnóstico de Ocre debe basarse en la lógica de funcionamiento del sistema y no exclusivamente en experiencia estadística.

La experiencia sirve para generar hipótesis, pero no debe convertirse en una conclusión automática.

Siempre pueden existir fallas fuera de los patrones habituales.

## Principios observados hasta ahora

### 14.1 Validar antes de asumir

No debe asumirse que existe una falla interna del equipo antes de comprobar las condiciones externas y básicas necesarias para su funcionamiento.

### 14.2 Analizar cambios recientes

Ante una falla que anteriormente no existía, debe investigarse qué cambió:

- operador;
- procedimiento;
- energía;
- material;
- archivo;
- software;
- configuración;
- instalación;
- ambiente;
- componentes;
- o condiciones de producción.

### 14.3 Fenómeno antes que componente

Primero se intenta comprender qué fenómeno puede producir el síntoma.

Después se identifican los componentes capaces de producir ese fenómeno.

### 14.4 Priorizar por lógica física

La prioridad diagnóstica debe considerar:

- cómo funciona físicamente el sistema;
- qué elementos sufren desgaste;
- qué componentes están sometidos a carga;
- qué recursos son compartidos;
- y qué hipótesis pueden comprobarse de manera sencilla.

### 14.5 De lo simple a lo complejo

Cuando varias causas pueden producir el mismo síntoma, deben descartarse primero aquellas que sean lógicas y sencillas de comprobar antes de asumir una falla compleja o costosa.

### 14.6 Recursos compartidos

Cuando aparecen múltiples fallas aparentemente independientes, debe investigarse si existe un recurso común.

Ejemplos:

- alimentación eléctrica;
- fuente de poder;
- tierra;
- comunicación;
- controladora;
- cableado común.

### 14.7 Comportamiento bajo carga

Una prueba estática correcta no descarta necesariamente una falla dinámica.

Componentes mecánicos, transmisiones, conexiones y actuadores pueden comportarse correctamente sin carga y fallar únicamente durante el trabajo real.

### 14.8 Patrones temporales

Una falla que aparece después de determinado tiempo puede indicar fenómenos acumulativos, especialmente temperatura.

Debe considerarse observación térmica y análisis del comportamiento antes, durante y después de la falla.

### 14.9 Separar percepción de evidencia

Los testimonios de operadores y supervisores son información valiosa, pero no constituyen por sí mismos una medición.

Las afirmaciones deben convertirse, cuando sea posible, en condiciones comprobables.

### 14.10 Separar subsistemas

Si una parte del sistema deja de funcionar mientras el resto continúa operando, debe analizarse primero el subsistema afectado.

Ejemplo:

Si un monitor se apaga pero la máquina continúa trabajando, debe distinguirse entre una falla de visualización y una falla general de operación.

### 14.11 Conservar hipótesis alternativas

Encontrar una causa posible no significa haber encontrado la causa raíz.

Una hipótesis debe comprobarse antes de considerarse conclusión cuando existan otras explicaciones razonables capaces de producir el mismo síntoma.

---

# 15. Configuraciones y respaldos

Cuando durante un servicio se identifica o establece una configuración correcta, ésta debe poder conservarse.

Esto incluye, según el equipo:

- parámetros;
- archivos de configuración;
- preferencias;
- firmware;
- software;
- compensaciones;
- calibraciones;
- archivos de máquina;
- perfiles;
- y procedimientos de restauración.

El objetivo es que una futura pérdida o corrupción de configuración pueda restaurarse sin repetir innecesariamente todo el proceso de calibración.

La prevención y el respaldo forman parte del valor del servicio, no únicamente la reparación inmediata.

---

# 16. Visita y ejecución del servicio

La visita debe partir de la solicitud existente y mostrar al técnico la información ya conocida.

Durante la visita debe ser posible:

- completar información faltante;
- registrar diagnóstico;
- documentar pruebas;
- tomar fotografías;
- registrar mediciones;
- agregar componentes;
- registrar actividades;
- documentar soluciones;
- identificar pendientes;
- registrar recomendaciones;
- registrar materiales o refacciones;
- y establecer el resultado.

El sistema debe reducir la necesidad de reconstruir posteriormente el servicio de memoria.

La documentación debe generarse durante la ejecución del trabajo siempre que sea posible.

---

# 17. Criterio de cierre

La prioridad número uno de un servicio es atender la solicitud y necesidad acordada con el cliente.

El cierre no significa simplemente que el técnico terminó de trabajar.

Debe quedar documentado:

- qué solicitó el cliente;
- qué se encontró;
- qué se hizo;
- qué pudo comprobarse;
- qué no pudo comprobarse;
- estado final;
- pendientes;
- recomendaciones;
- y siguientes acciones.

La validación debe adaptarse al tipo de problema.

Algunas reparaciones pueden comprobarse directamente mediante una prueba.

Otras, especialmente fallas intermitentes, pueden únicamente permitir comprobar que se eliminó una causa identificada y requerir seguimiento posterior.

El reporte debe reflejar esta diferencia y no presentar como certeza aquello que no pudo comprobarse.

---

# 18. Reporte de servicio

El reporte es una salida natural de la información capturada durante el servicio.

No debe requerir que el técnico vuelva a escribir desde cero todo lo ocurrido.

Debe poder generarse un documento profesional que permita al cliente comprender:

- motivo del servicio;
- equipo atendido;
- condiciones encontradas;
- diagnóstico;
- actividades realizadas;
- evidencias;
- mediciones;
- refacciones;
- resultado;
- recomendaciones;
- pendientes;
- y próximos pasos.

El reporte constituye además evidencia del trabajo realizado y soporte para seguimiento y cobro.

---

# 19. Cobro y agenda

Ocre OS debe conectar el ciclo técnico con el ciclo administrativo.

Para clientes nuevos, el primer servicio normalmente corresponderá a un Diagnóstico General Inicial.

Cuando corresponda, debe poder solicitarse un anticipo, inicialmente contemplado como 50 % del servicio.

El flujo futuro debe permitir que:

1. el cliente reciba la información del servicio;
2. pueda realizar el pago correspondiente;
3. el pago sea identificado por el sistema;
4. se muestren horarios disponibles;
5. el cliente pueda seleccionar una cita;
6. la cita quede vinculada con el calendario operativo;
7. y el técnico reciba la solicitud y su información asociada.

La integración con Google Calendar deberá evitar duplicidad entre la agenda de Ocre OS y la agenda operativa real.

---

# 20. Portal del cliente

Ocre OS debe contemplar un acceso para clientes.

Una cuenta deberá permitir, según permisos:

- consultar solicitudes;
- consultar servicios;
- consultar equipos;
- revisar reportes;
- consultar pendientes;
- realizar o consultar pagos;
- solicitar facturación;
- aportar documentación;
- y dar seguimiento a trabajos en curso.

Una empresa podrá requerir múltiples usuarios con diferentes funciones y niveles de acceso.

---

# 21. Solicitud de facturación

La facturación fiscal no será generada inicialmente dentro de Ocre OS.

El sistema sí debe preparar y controlar la solicitud.

Debe poder reunir:

- identidad fiscal;
- datos fiscales requeridos;
- documentación proporcionada por el cliente;
- correo para recepción;
- operación o pago relacionado;
- concepto;
- información necesaria para elaboración;
- estatus de solicitud;
- fecha de solicitud;
- responsable externo;
- y posteriormente la factura resultante cuando corresponda.

El objetivo es que ninguna factura pendiente dependa exclusivamente de memoria, mensajes aislados o seguimiento manual.

---

# 22. Base de conocimiento

Cada servicio debe tener el potencial de incrementar el conocimiento de Ocre.

La base de conocimiento debe poder relacionar información con:

- fabricantes;
- familias de máquinas;
- modelos;
- componentes;
- síntomas;
- fenómenos;
- causas;
- procedimientos;
- mediciones;
- configuraciones;
- refacciones;
- documentación;
- y soluciones comprobadas.

El objetivo futuro es que Ocre OS no sea únicamente un sistema de registro, sino un asistente técnico capaz de utilizar conocimiento histórico para apoyar el diagnóstico.

La base de conocimiento deberá conservar, cuando sea posible, no solamente **qué se hizo**, sino también **por qué se tomó una decisión**.

---

# 23. Principios de diseño de Ocre OS

## 23.1 Valor operativo primero

La primera versión debe resolver problemas que actualmente afectan directamente la operación y los ingresos:

- servicios sin documentar;
- reportes no entregados;
- trabajos sin seguimiento;
- trabajos realizados que no se cobran oportunamente;
- información dispersa;
- y pérdida de conocimiento.

La inteligencia avanzada se incorporará progresivamente sobre una operación que ya funciona.

## 23.2 Capturar una vez, reutilizar muchas veces

La información ingresada durante el proceso debe alimentar automáticamente expedientes, reportes, seguimiento y conocimiento siempre que sea posible.

## 23.3 No inventar información para satisfacer el sistema

El sistema debe admitir información incompleta y permitir completarla posteriormente.

## 23.4 Trazabilidad

Los cambios relevantes deben poder relacionarse con:

- quién los realizó;
- cuándo;
- por qué;
- y dentro de qué servicio o contexto.

## 23.5 Información estructurada

Siempre que una información pueda ser útil posteriormente para búsqueda, análisis, automatización o diagnóstico, debe evitarse esconderla exclusivamente dentro de texto libre.

El texto libre seguirá existiendo, pero no debe sustituir innecesariamente información estructurada.

## 23.6 Flexibilidad sin perder consistencia

Los formularios y procesos deben permitir excepciones reales sin convertir cada servicio en un procedimiento completamente diferente.

## 23.7 El sistema debe asistir

Ocre OS no debe ser solamente un lugar donde almacenar información.

Debe ayudar activamente a:

- recordar pendientes;
- identificar información faltante;
- sugerir siguientes acciones;
- evitar olvidos;
- generar documentación;
- mantener seguimiento;
- y progresivamente apoyar decisiones técnicas.

## 23.8 La fuente oficial no es el chat

Las conversaciones, herramientas de IA y sesiones de diseño sirven para analizar y desarrollar ideas.

Las decisiones aceptadas deben trasladarse a la documentación y posteriormente al sistema.

El repositorio de Ocre OS debe convertirse en la referencia formal del proyecto.

---

# 24. Estado de este documento

Este documento es deliberadamente evolutivo.

Describe el modelo operativo conocido hasta este momento y deberá modificarse cuando el análisis del negocio revele una representación mejor.

Una decisión documentada puede corregirse.

El objetivo no es proteger decisiones anteriores, sino construir una representación cada vez más precisa del funcionamiento real de Ocre.

Toda modificación importante deberá conservar claridad sobre el motivo del cambio.
