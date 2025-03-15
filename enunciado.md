Documentación oficial para la implementación de ConstruFurgo en Salesforce 🚛🏗️

📌 Capítulo I: Disposiciones Generales
Artículo 1. Introducción
ConstruFurgo es una empresa dedicada a la fabricación y comercialización de furgones industriales diseñados para diversas aplicaciones, tales como logística, alimentos, construcción y manufactura. A causa de su expansión en diferentes partes del país, la empresa ha tenido mayor captación de clientes potenciales, causando que necesiten plantear su manejo de ellos a una plataforma robusta y concisa. 



Artículo 2. Requerimiento
Para ello, se decide utilizar los recursos proveídos de Salesforce, los cuales si son utilizados de manera correcta permitirán que la empresa mejore su gestionamiento y relación con el cliente final. Con el fin de asegurar su buena implementación se construye el siguiente documento , el cual establece los lineamientos básicos esperados al momento de realizar la implementación y gestión del sistema Salesforce en ConstruFurgo.





📌 Capítulo II: Estructura Organizacional

Artículo 3. Información Legal de la Empresa
1️⃣ Razón Social: ConstruFurgo S.A.S. 

2️⃣ Número de Identificación Tributaria (NIT): 901456789-2 

3️⃣ Domicilio Principal: Av. Boyacá #12-33, Bogotá, Colombia. 

4️⃣ Capital Social: $5,000,000 USD 

5️⃣ Tipo de Empresa: Sociedad por Acciones Simplificada (S.A.S.) 

6️⃣ Objeto Social: Diseño, fabricación, comercialización y mantenimiento de furgones industriales. 

7️⃣ Representante Legal: Juan Pérez López 

8️⃣ Registro Mercantil: Matrícula 456789 en la Cámara de Comercio de Bogotá. 

9️⃣ Correo Oficial: contacto@construfurgo.com


Artículo 4. Organización Jerárquica
ConstruFurgo se encuentra estructurada de la siguiente manera:





1️⃣ Gerencia General (CEO): Responsable de la estrategia global de la empresa.   

2️⃣ Gerencia de Ventas: Administración de clientes, oportunidades de negocio y crecimiento del mercado. 

3️⃣ Gerencia de Soporte Técnico: Atención a clientes post-venta y resolución de problemas. Nota: Para este caso de estudio, tomaremos en consideracion el usuario creado por predeterminado, el cual sería el de Salesforce Administrator

4️⃣ Gerencia de Compras y Logística: Manejo de proveedores y optimización de entregas.


Artículo 5. Organigrama Empresarial
 El organigrama de ConstruFurgo debe reflejarse en Salesforce con permisos y accesos adecuados.

CEO
Gerente de Ventas → Administrador de Ventas, Ejecutivo de Ventas
Gerente de Soporte → Coordinador de Soporte, Técnico de Ensamblaje
Gerente de Compras → Ejecutivo de Compras, Coordinador de Logística




📌 Capítulo III: Configuración de la Empresa en Salesforce

Artículo 6. Configuración General
Para un buen control y legalización de documentos, los  siguientes elementos deben estar bien planteados en la organización de Salesforce:

1️⃣ Registro de ConstruFurgo en Salesforce con su información fiscal y legal. 

2️⃣ Definir estructura de seguridad de la organización.

3️⃣ Configuración de accesos, permisos y restricciones según jerarquía.

4️⃣ Creación de cuentas empresariales y configuración de roles en Salesforce. 

5️⃣ Definición de reglas de flujo de trabajo y automatización de procesos internos. 

6️⃣ Configuración de moneda, impuestos y términos de pago dentro del CRM. 

7️⃣ Implementación de un sistema de auditoría de registros y transacciones:

Las auditorías deben ser enviadas al Director Ejecutivo cada mes y deben incluir:

Registros de accesos fallidos con detalles de IP y usuario.
Cambios en la configuración de seguridad que afecten roles y permisos.
Modificaciones en datos críticos como cuentas, oportunidades y reportes financieros.
Actividades inusuales en los flujos de aprobación que requieran revisión manual.
Intentos de acceso fuera del horario laboral establecido.
Listado de usuarios con permisos administrativos y cambios realizados. 
8️⃣ Implementación de procesos de validación de datos en Salesforce:

Correos electrónicos deben cumplir con un formato estandarizado.
Teléfonos deben contener el código de país y estar estructurados en un formato válido.
Los registros duplicados serán bloqueados automáticamente con un proceso de de duplicación. 
9️⃣ Creación de un mecanismo de respaldo y recuperación de datos:

Se deben realizar respaldos automáticos cada 24 horas.
La restauración de datos solo podrá ser ejecutada por el Administrador de Salesforce.
Todo intento de restauración deberá ser registrado en un log de auditoría.




📌 Capítulo III: Configuración de la Empresa en Salesforce
Artículo 6. Configuración General
Para un buen control y legalización de documentos, los  siguientes elementos deben estar bien planteados en la organización de Salesforce:

1️⃣ Registro de ConstruFurgo en Salesforce con su información fiscal y legal. 

2️⃣ Definir estructura de seguridad de la organización.

3️⃣ Configuración de accesos, permisos y restricciones según jerarquía.

4️⃣ Creación de cuentas empresariales y configuración de roles en Salesforce. 

5️⃣ Definición de reglas de flujo de trabajo y automatización de procesos internos. 

6️⃣ Configuración de moneda, impuestos y términos de pago dentro del CRM. 

7️⃣ Implementación de un sistema de auditoría de registros y transacciones:

Las auditorías deben ser enviadas al Director Ejecutivo cada mes y deben incluir:

Registros de accesos fallidos con detalles de IP y usuario.
Cambios en la configuración de seguridad que afecten roles y permisos.
Modificaciones en datos críticos como cuentas, oportunidades y reportes financieros.
Actividades inusuales en los flujos de aprobación que requieran revisión manual.
Intentos de acceso fuera del horario laboral establecido.
Listado de usuarios con permisos administrativos y cambios realizados. 
8️⃣ Implementación de procesos de validación de datos en Salesforce:

Correos electrónicos deben cumplir con un formato estandarizado.
Teléfonos deben contener el código de país y estar estructurados en un formato válido.
Los registros duplicados serán bloqueados automáticamente con un proceso de de duplicación. 
9️⃣ Creación de un mecanismo de respaldo y recuperación de datos:

Se deben realizar respaldos automáticos cada 24 horas.
La restauración de datos solo podrá ser ejecutada por el Administrador de Salesforce.
Todo intento de restauración deberá ser registrado en un log de auditoría.




📌 Capítulo IV: Procesos Automatizados y Reportes en Salesforce

Artículo 12. Procesos Automatizados en la Plataforma
ConstruFurgo requiere la automatización de los siguientes procesos en Salesforce:

1️⃣ Asignación Automática de Leads:

Se enviará una notificación automática al Gerente de Ventas.
2️⃣ Conversión de Lead a Oportunidad:

Una vez que un lead haya interactuado tres veces con el equipo comercial, debe ser convertido automáticamente en una oportunidad de venta.
Se generará una propuesta comercial automática basada en el interés del cliente.
3️⃣ Seguimiento de Casos de Soporte:

Los casos críticos recibirán alertas a la Gerencia de Soporte para intervención inmediata.
4️⃣ Proceso de Facturación Automática:

Una vez que una oportunidad de venta haya sido cerrada con éxito, debe generarse una factura en Salesforce automáticamente.
La factura será enviada al cliente y registrada en la base de datos de cuentas por cobrar.
Artículo 13. Dashboards y Reportes en Salesforce
Se deben crear los siguientes paneles y reportes con accesos según rol:

1️⃣ Dashboard de Ventas (Acceso: CEO, Gerente de Ventas):

Gráficos de oportunidades ganadas y perdidas.
Reporte de ingresos proyectados y alcanzados.
2️⃣ Reporte de Casos de Soporte (Acceso: CEO, Gerente de Soporte):

Casos abiertos vs. casos cerrados.
Sesgo de canales utilizados vs los casos abiertos y cerrados.
3️⃣ Panel de Compras y Proveedores (Acceso: CEO, Gerente de Compras):

Historial de órdenes de compra.
Compras completadas vs Compras no culminadas.

Artículo 14. Aplicaciones Lightning para Roles Específicos
Se requiere la creación de aplicaciones personalizadas en Salesforce Lightning para cada perfil organizacional:

1️⃣ Aplicación de Ventas (Usuarios: CEO, Gerente de Ventas,Gerente de Compras):

Gestión centralizada de oportunidades y leads.
Gestión de compradores y órdenes de compra.
Dashboard interactivo con cotizaciones enviadas y pendientes.
Registro de actividad comercial y reuniones con clientes.
2️⃣Aplicación de Soporte (Usuarios: CEO, Gerente de Soporte):

Registro automático de tickets de servicio al cliente.
Base de conocimientos con soluciones a problemas frecuentes.
Panel de métricas sobre cantidad de casos abiertos y la resolución del mismo.

📌 Capítulo V: Entregables del Proyecto
Para la entrega de la organización hacia la empresa se debe realizar los siguientes entregables en los formatos correspondientes:


Artículo 15. Presentación para el Cliente
📌 La presentación deberá contener: 

1️⃣ Resumen ejecutivo del proyecto Salesforce en ConstruFurgo. 

2️⃣ Impacto de la implementación en ventas, producción y soporte técnico. 

3️⃣ Explicación de la estructura organizacional reflejada en Salesforce.

 4️⃣ Mapa de procesos automatizados y su relevancia para la empresa. 

5️⃣ Flujos de aprobación y validación de datos con ejemplos reales. 

6️⃣ Seguridad y acceso: configuración de sesiones, auditoría de accesos y restricciones. 

7️⃣ Capturas de reportes y dashboards, incluyendo segmentaciones por departamento. 

8️⃣ Demostración de Salesforce App en dispositivos móviles y su funcionalidad clave. 

9️⃣ Casos de éxito basados en la optimización de procesos dentro de Salesforce. 

🔟 Conclusiones, desafíos superados y próximos pasos.


Artículo 16. Documentación en Markdown (Notion o .md)
📌 Se deberá entregar un documento técnico en formato Markdown (Notion) que contenga los siguientes ítems (Por favor cumplir con los mínimos requerimientos y expandir cuando se vea requerido):

# 📘 Documentación Técnica de Salesforce - ConstruFurgo
​
## 📌 Introducción
Breve resumen sobre la implementación de Salesforce en ConstruFurgo.
​
## 📌 Configuración General
- Información de la empresa registrada en Salesforce.
- Jerarquía de roles y permisos.
​
## 📌 Procesos de Negocio
- Gestión de Leads y automatización de conversión.
- Flujos de aprobación en ventas y seguimiento de oportunidades.
- Gestión de órdenes de compra y facturación automatizada.
​
## 📌 Seguridad y Accesos
- Configuración de auditoría de accesos con alertas automáticas.
- Restricciones por perfil y rol detalladas con permisos específicos.
- Manejo de sesiones con reglas estrictas de expiración y control de actividad.
​
## 📌 Dashboards y Reportes
- Reportes clave de desempeño según roles y objetivos empresariales.
- Configuración de dashboards estratégicos personalizados por usuario.
​
## 📌 Implementación de Salesforce App
- Personalización de interfaz móvil con accesos según perfil.
- Funcionalidades habilitadas: actualización de leads, reporte de actividad y notificaciones.
​
## 📌 Conclusiones

Artículo 17. Entregables Adicionales
Además de los entregables solicitados, anexar en la misma entrega los siguientes elementos:

1️⃣ CSV con los usuarios creados, roles y perfiles con permisos detallados. 

2️⃣ CSV con los productos, precios y stages de venta configurados. 

3️⃣ Capturas de configuración de roles, permisos y restricciones aplicadas. 

4️⃣ Capturas de reportes y dashboards en Salesforce segmentados por departamento. 

5️⃣ Capturas de procesos automatizados en Salesforce con flujo detallado. 

6️⃣ Capturas de la aplicación Lightning desarrollada con personalización. 

7️⃣ Capturas del uso de Salesforce App en iOS y su integración con la plataforma. 

8️⃣ Plan de mantenimiento y escalabilidad en Salesforce con plan de mejoras futuras.



Cabe destacar que dichos elementos adicionales también deberán estar bien documentados para tener trazabilidad del asunto.



Recursos a utilizar: Enlace.

