 ![Logo](https://i.pinimg.com/1200x/7f/45/95/7f4595bfe7e80086c681bc22ddd08a94.jpg)
 
 **Capítulo II: Estructura Organizacional**


## 📌 Introducción
Breve resumen sobre la implementación de Salesforce en ConstruFurgo. 

### **Artículo 3. Información Legal de la Empresa**

1️⃣ **Razón Social:** ConstruFurgo S.A.S. 

2️⃣ **Número de Identificación Tributaria (NIT):** 901456789-2 

3️⃣ **Domicilio Principal:** Av. Boyacá #12-33, Bogotá, Colombia. 

4️⃣ **Capital Social:** $5,000,000 USD 

5️⃣ **Tipo de Empresa:** Sociedad por Acciones Simplificada (S.A.S.) 

6️⃣ **Objeto Social:** Diseño, fabricación, comercialización y mantenimiento de furgones industriales. 

7️⃣ **Representante Legal:** Juan Pérez López 

8️⃣ **Registro Mercantil:** Matrícula 456789 en la Cámara de Comercio de Bogotá. 

9️⃣ **Correo Oficial:** [contacto@construfurgo.com](mailto:contacto@construfurgo.com)

### **Configuración del objeto Account según los requerimientos**

- La **Razón Social** se registra en el campo requerido **Account Name**.
- Se crea un campo personalizado para el **Número de Identificación Tributaria (NIT)**.
- El **Domicilio Principal** (Av. Boyacá #12-33, Bogotá, Colombia) se registra en **Billing Address**, utilizando los campos **Billing Street, City, State y Country**.
- Se añade un campo personalizado para registrar el **Capital Social**.
- En **Type values**, se agrega la opción **"S.A.S"**, permitiendo su selección en el desplegable de **Type**.
- Para mejorar la organización, se crea un campo personalizado **Objeto Social**, de tipo **Text Area (Long)**.
- Se agrega un campo personalizado **Representante Legal** para registrar el nombre del representante de la empresa.
- Se crea un campo personalizado para el **Registro Mercantil**, donde se almacena la matrícula mercantil.
- El **Correo Oficial** se registra en el campo predeterminado **Email**.


## 📌 Configuración General
- Información de la empresa registrada en Salesforce.
- Jerarquía de roles y permisos.
​
### **Artículo 5. Organigrama empresarial establecido **

- CEO
- **Gerente de Ventas** → Administrador de Ventas, Ejecutivo de Ventas
- **Gerente de Soporte** → Coordinador de Soporte, Técnico de Ensamblaje
- **Gerente de Compras** → Ejecutivo de Compras, Coordinador de Logística


### **Artículo 5. Organigrama empresarial establecido **

![Logo](https://i.pinimg.com/1200x/35/1b/61/351b611ceca843e61e904f7ef9a9b08c.jpg)

# Asignación de Permisos por Usuario

## Permisos por Perfil

| **Usuario**             | **Perfil**                 | **Funciones Principales**                    | **Objetos**                                                                                      | **Permisos Adicionales**                                                     |
|-------------------------|----------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Rojas, David**         | Custom: Sales Profile      | Gestión de leads, oportunidades y ventas.    | **Leads:** Lectura, Escritura, Creación, Eliminación. <br> **Opportunities:** Lectura, Escritura, Creación, Eliminación. <br> **Accounts:** Lectura, Escritura. <br> **Contacts:** Lectura, Escritura. <br> **Producto__c:** Lectura. | Acceso a Dashboards de Ventas. <br> Permiso para convertir leads en oportunidades. <br> Permiso para crear y enviar propuestas comerciales. |
| **Montalvo, Sam**        | Procurement Specialist     | Gestión de compras y proveedores.            | **Accounts:** Lectura, Escritura (solo para proveedores). <br> **Producto__c:** Lectura, Escritura. <br> **Stage_Venta__c:** Lectura. | Acceso a Panel de Compras y Proveedores. <br> Permiso para crear órdenes de compra. |
| **Furgo, Constru**       | System Administrator       | Supervisión general de la empresa.           | **Todos los objetos:** Lectura, Escritura, Creación, Eliminación.                               | Acceso a todos los Dashboards y Reportes. <br> Permiso para realizar auditorías y cambios de configuración. <br> Permiso para restaurar datos (solo en casos críticos). |
| **Schifrin, James**      | Technical_Support          | Soporte técnico y resolución de casos.       | **Cases:** Lectura, Escritura, Creación. <br> **Accounts:** Lectura. <br> **Contacts:** Lectura. | Acceso a Reporte de Casos de Soporte. <br> Permiso para cerrar casos resueltos. |

---

## Permission Sets

| **Permission Set**             | **Asignado a**          | **Permisos**                                                                                         |
|---------------------------------|-------------------------|------------------------------------------------------------------------------------------------------|
| **Sales_Permission_Set**        | Rojas, David            | Convertir Leads. <br> Enviar propuestas comerciales. <br> Acceso a Dashboards de Ventas.              |
| **Procurement_Permission_Set**  | Montalvo, Sam           | Crear órdenes de compra. <br> Acceso a Panel de Compras y Proveedores.                              |
| **Support_Permission_Set**      | Schifrin, James         | Acceso a Reporte de Casos de Soporte.                                                                |


**Activar múltiples monedas en Salesforce y configurar USD**

para Lograr que el Capital Social sea $5,000,000 USD, se establece la taza de cambio con un valor de 4.000 ,  Las tasas de conversión se definen en relación con la moneda corporativa. Todas las tasas de conversión de monedas ya definidas en salesforce.com se modificarán adecuadamente para reflejar el cambio. selecciona USD.

## Usuarios creados con sus respectivos roles y perfiles 

| Action  | Full Name          | Alias  | Username                                        | Role                        | Active  | Profile                           |
|---------|-------------------|--------|------------------------------------------------|-----------------------------|---------|-----------------------------------|
| Edit    | Rojas, David      | droja  | admvenconstrufurgo@gmail.com                   | Administrador de Ventas      | Checked | Custom: Sales Profile            |
| Edit    | Montalvo, Sam     | smont  | ejecutivocomprasconstrufurgo@gmail.com        | Ejecutivo de Compras         | Checked | Procurement Specialist            |
| Edit    | Furgo, Constru    | CFurg  | construfurgo9@gmail.com                        | CEO                         | Checked | System Administrator              |
| Edit    | Schifrin, James   | jschi  | tecnicoensamblajeconstrufurgo@gmail.com        | Técnico de Ensamblaje       | Checked | Technical_Support                 |


## Asignación de permisos por perfil y creación de Permission Sets para usuarios


| ![img](https://contrufurgo-dev-ed.develop.my.salesforce.com/img/s.gif)Active Currencies |      |      |
| ------------------------------------------------------------ | ---- | ---- |
|                                                              |      |      |

| Action                                                       | Currency Code | Currency Name  |                          Corporate                           | Conversion Rate | Decimal Places | Last Modified By                                             |
| :----------------------------------------------------------- | :------------ | :------------- | :----------------------------------------------------------: | --------------: | -------------: | :----------------------------------------------------------- |
| [Edit](javascript:srcUp('%2F01Lbm000002ZsSb%2Fe%3FretURL%3D%2Fsetup%2Fcur%2Fcurrencylist.jsp%3FretURL%3D%252Fsetup%252Fhome%26appLayout%3Dsetup%26tour%3D%26sfdcIFrameOrigin%3Dhttps%253A%252F%252Fcontrufurgo-dev-ed.develop.lightning.force.com%26sfdcIFrameHost%3Dweb%26nonce%3D039c5c20240184235d551e42632532e5f13f6370641df4b174dc0dbd5dcf2198%26ltn_app_id%3D%26clc%3D1%26isdtp%3Dp1%26isdtp%3Dp1');) \| [Deactivate](javascript:srcUp('%2F01Lbm000002ZsSb%2Fe%3FIsoCode%3DCOP%26active%3D0%26retURL%3D%2Fsetup%2Fcur%2Fcurrencylist.jsp%3FretURL%3D%252Fsetup%252Fhome%26appLayout%3Dsetup%26tour%3D%26sfdcIFrameOrigin%3Dhttps%253A%252F%252Fcontrufurgo-dev-ed.develop.lightning.force.com%26sfdcIFrameHost%3Dweb%26nonce%3D039c5c20240184235d551e42632532e5f13f6370641df4b174dc0dbd5dcf2198%26ltn_app_id%3D%26clc%3D1%26isdtp%3Dp1%26isdtp%3Dp1');) | COP           | Colombian Peso | ![Not Checked](https://contrufurgo-dev-ed.develop.my.salesforce.com/img/checkbox_unchecked.gif) |    4,000.000000 |              2 | [Constru Furgo](javascript:srcUp('%2F005bm00000CTSfd%3Fisdtp%3Dp1%26isUserEntityOverride%3D1%26noredirect%3D1');), 3/15/2025, 12:40 AM |
| [Edit](javascript:srcUp('%2F01Lbm000002ZsZ3%2Fe%3FretURL%3D%2Fsetup%2Fcur%2Fcurrencylist.jsp%3FretURL%3D%252Fsetup%252Fhome%26appLayout%3Dsetup%26tour%3D%26sfdcIFrameOrigin%3Dhttps%253A%252F%252Fcontrufurgo-dev-ed.develop.lightning.force.com%26sfdcIFrameHost%3Dweb%26nonce%3D039c5c20240184235d551e42632532e5f13f6370641df4b174dc0dbd5dcf2198%26ltn_app_id%3D%26clc%3D1%26isdtp%3Dp1%26isdtp%3Dp1');) \| Deactivate | USD           | U.S. Dollar    | ![Checked](https://contrufurgo-dev-ed.develop.my.salesforce.com/img/checkbox_checked.gif) |        1.000000 |              2 | [Constru Furgo](javascript:srcUp('%2F005bm00000CTSfd%3Fisdtp%3Dp1%26isUserEntityOverride%3D1%26noredirect%3D1');), 3/15/2025, 12:30 AM |

Ahora, todas las conversiones de moneda toman el USD como referencia, 1 USD = 4,000 COP.

# Configuración de impuestos
1. Establece un campo en productos "Tax Rate" que almacena la tasa de impuestos, con un valor predeterminado del 19%.
2. Se crea un campo de tipo fórmula que calcula automáticamente el precio del producto con impuestos incluidos.

`Price__c + (Price__c * Tax_Rate__c / 100)`

 El campo "Precio Con Impuestos" refleja el precio con impuestos calculado en base al 19%.


# Definición de Objetos en Salesforce

## 1. Users.csv
**Objeto:** User (Objeto estándar de Salesforce)  

| Campo      | Tipo                           | Descripción                      |
|------------|--------------------------------|----------------------------------|
| User_ID    | Texto (ID externo, único)     | Identificador único del usuario. |
| Name       | Texto                          | Nombre completo del usuario.     |
| Email      | Email                          | Correo electrónico.              |
| Role       | Texto                          | Rol del usuario.                 |
| Profile    | Texto                          | Perfil del usuario.              |
| Department | Texto                          | Departamento.                     |
| Active     | Casilla de verificación        | Indica si el usuario está activo.|

---

## 2. Roles_Profiles.csv
**Objeto:** Role_Profile__c (Objeto personalizado)  

| Campo | Tipo  | Descripción           |
|-------|-------|-----------------------|
| Role  | Texto | Rol del usuario.      |
| Profile | Texto | Perfil del usuario. |

---

## 3. Accounts.csv
**Objeto:** Account (Objeto estándar de Salesforce)  

| Campo       | Tipo                        | Descripción                     |
|-------------|-----------------------------|---------------------------------|
| Account_ID  | Texto (ID externo, único)   | Identificador único de la empresa. |
| Company     | Texto                        | Nombre de la empresa.          |
| Email       | Email                        | Correo electrónico de la empresa. |

---

## 4. Contacts.csv
**Objeto:** Contact (Objeto estándar de Salesforce)  

| Campo       | Tipo                        | Descripción                     |
|-------------|-----------------------------|---------------------------------|
| Contact_ID  | Texto (ID externo, único)   | Identificador único del contacto. |
| Name        | Texto                        | Nombre completo del contacto.  |
| Account_ID  | Relación (Lookup con Account) | Relación con la empresa.       |
| Email       | Email                        | Correo electrónico del contacto. |

---

## 5. Productos.csv
**Objeto:** Producto__c (Objeto personalizado)  

| Campo      | Tipo                        | Descripción                      |
|------------|-----------------------------|----------------------------------|
| Product_ID | Texto (ID externo, único)   | Identificador único del producto. |
| Name       | Texto                        | Nombre del producto.            |
| Category   | Texto                        | Categoría del producto.         |
| Price      | Moneda                       | Precio del producto.            |
| Stock      | Número                       | Cantidad en stock.              |

---

## 6. leads.csv
**Objeto:** Lead (Objeto estándar de Salesforce)  

| Campo      | Tipo                        | Descripción                     |
|------------|-----------------------------|---------------------------------|
| Lead_ID    | Texto (ID externo, único)   | Identificador único del lead.   |
| Name       | Texto                        | Nombre completo del lead.       |
| Email      | Email                        | Correo electrónico del lead.    |
| Industry   | Texto                        | Industria del lead.             |
| Phone      | Teléfono                     | Número de teléfono del lead.    |

---

## 7. Opportunities_clean.csv
**Objeto:** Opportunity (Objeto estándar de Salesforce)  

| Campo         | Tipo                        | Descripción                     |
|--------------|-----------------------------|---------------------------------|
| Opportunity_ID | Texto (ID externo, único) | Identificador único de la oportunidad. |
| Account_ID   | Relación (Lookup con Account) | Relación con la empresa.       |
| Name         | Texto                        | Nombre de la oportunidad.      |
| Stage        | Texto                        | Etapa de la oportunidad.       |
| Amount       | Moneda                       | Monto de la oportunidad.       |

---

## 8. Cases.csv
**Objeto:** Case (Objeto estándar de Salesforce)  

| Campo      | Tipo                        | Descripción                     |
|------------|-----------------------------|---------------------------------|
| Case_ID    | Texto (ID externo, único)   | Identificador único del caso.   |
| Account_ID | Relación (Lookup con Account) | Relación con la empresa.       |
| Subject    | Texto                        | Asunto del caso.               |
| Priority   | Texto                        | Prioridad del caso.            |
| Status     | Texto                        | Estado del caso.               |

---

## 9. stage_ventas.csv
**Objeto:** Stage_Venta__c (Objeto personalizado)  

| Campo        | Tipo                        | Descripción                      |
|-------------|-----------------------------|----------------------------------|
| Stage_ID    | Texto (ID externo, único)   | Identificador único de la etapa. |
| Stage_Name  | Texto                        | Nombre de la etapa.              |
| Probability | Número                       | Probabilidad de cierre.         |
| Description | Texto largo                  | Descripción de la etapa.        |

#  Términos de pago dentro del CRM

Para optimizar la gestión de facturación en Salesforce, se implementaron automatizaciones que facilitan el control de términos de pago y vencimientos. Estas soluciones incluyen la aprobación de facturas con crédito a 60 días, notificaciones para crédito a 30 días y alertas automáticas para facturas próximas a vencer. Con estas mejoras, se agiliza la comunicación con el equipo de ventas y se garantiza un mejor seguimiento de los plazos de pago.

 **Crédito a 60 Días**
Se creó un proceso de aprobación en Salesforce para gestionar las facturas con crédito a 60 días. Se definieron los criterios de entrada para que solo las facturas con esta condición sean enviadas a aprobación. Para los rechazos, se creó una tarea para notificar al equipo de ventas sobre el rechazo, facilitando la comunicación con el cliente.

![Logo](https://i.pinimg.com/1200x/82/3b/91/823b919b356a9430a50b1f95c64009fd.jpg)

**Crédito a 30 Días**
el flujo enviará un correo al propietario de la factura cada vez que esta sea creada o actualizada con los términos de pago "Crédito a 30 días" y el estado "Pending"

![Logo](https://i.pinimg.com/1200x/50/c3/eb/50c3eb04ad3ccac2f093dbc1057021a0.jpg)

**Alerta de Factura Próxima a Vencer**
En este proceso, se configura un Flow para automatizar el envío de alertas cuando una factura está próxima a vencer. Definimos una condición:
Se configuró una fórmula para calcular si el Due Date de la factura está a 5 días o menos.

`  DATETIMEVALUE(TEXT(TODAY() + 5) & " 00:00:00") `


![Logo](https://i.pinimg.com/1200x/c1/a9/97/c1a997ed111e116bf3f2abdfc567637b.jpg)


## 📌 Seguridad y Accesos
- Configuración de auditoría de accesos con alertas automáticas.
- Restricciones por perfil y rol detalladas con permisos específicos.
- Manejo de sesiones con reglas estrictas de expiración y control de actividad.


**Registros de accesos fallidos con detalles de IP y usuario**

Para acceder a la información de "Login Histories" se crea un custom report type, este permite realizar un reporte con los registros de accesos fallidos, detalles de ip y usuarios

![Logo](https://i.pinimg.com/1200x/e7/2c/fb/e72cfbc2a802061e6adf71bf63e7f237.jpg)


El reporte generado  recopila todos los intentos de inicio de sesión fallidos registrados en el historial de accesos, sin restricciones de fecha, ya que el filtro de "Created Date" se ha establecido en "All Time". Se han excluido los accesos exitosos mediante el filtro "Status ≠ Success", permitiendo así visualizar únicamente los intentos fallidos. Esto facilita la detección de posibles intentos de acceso no autorizado, errores de autenticación recurrentes y patrones de intentos fallidos por usuario o dirección IP. El reporte es útil para auditorías de seguridad y monitoreo de accesos, proporcionando información clave como la dirección IP de origen, la cuenta de usuario involucrada, la fecha y hora del intento, y la razón del fallo, como contraseñas incorrectas o dispositivos no activados.

![Logo](https://i.pinimg.com/1200x/60/b0/24/60b024fd29ae06be83819df32d506706.jpg)

Se ha configurado una suscripción mensual al reporte de accesos fallidos en Salesforce, asegurando que el Director Ejecutivo reciba automáticamente un informe actualizado con los intentos de inicio de sesión no exitosos.

![Logo](https://i.pinimg.com/1200x/1e/7c/19/1e7c191b5027f26da4d4365ac13efafb.jpg)


**Cambios en la configuración de seguridad que afecten roles y permisos**

El reporte de "Permission Set Assignments" permite auditar los permisos asignados a los usuarios en Salesforce, mostrando quién tiene acceso a qué funciones, cuándo se otorgaron o modificaron los permisos y qué tipo de acceso se les concedió. Al igual que el reporte de accesos fallidos, el Director Ejecutivo está suscrito a este informe y lo recibirá mensualmente, lo que garantiza una supervisión continua sobre la configuración de seguridad y los cambios en los permisos de usuario.

![Logo](https://i.pinimg.com/1200x/c3/80/62/c38062d74b8048f61a2cadb920b548d2.jpg)

 **Implementación de procesos de validación de datos en Salesforce:**

  **Correos electrónicos deben cumplir con un formato estandarizado:**

La validación implementada garantiza que los correos electrónicos ingresados sigan un formato estándar, evitando errores y asegurando la calidad de los datos. Mediante una Regla de Validación, el sistema detecta correos con formatos incorrectos y bloquea su ingreso, mostrando un mensaje de error  Esto mejora la integridad de la base de datos y optimiza los procesos, al garantizar que solo se almacenen direcciones de correo válidas.

![Logo]( https://i.pinimg.com/1200x/66/29/12/662912de90a8d40915c4316cfc8b635c.jpg)

**Teléfonos deben contener el código de país y estar estructurados en un formato válido:**

Esta validación en garantiza que los números de teléfono ingresados deben contener el código de país y un formato específico (+1-XXX-XXXX).De lo contrario se muestra un mensaje de error, evitando que se guarde un dato incorrecto.

![Logo](https://i.pinimg.com/1200x/b4/26/ec/b426ecad454c1c2f7d7fe6f8d1e8bf1b.jpg)


**Los registros duplicados serán bloqueados automáticamente con un proceso de de duplicación:**

Configuración de una Matching Rule para evitar la creación de Leads duplicados por email, utilizando una coincidencia exacta en el campo Email.  implementación de una Duplicate Rule vinculada a esta regla, estableciendo la opción de bloquear la creación de registros duplicados o mostrar una alerta en caso de coincidencia. Activación de ambas reglas para garantizar la integridad de los datos en el objeto de Leads

![Logo](https://i.pinimg.com/1200x/62/18/d0/6218d0162f12a9d577b0aeb5b1b92b55.jpg)


9️⃣ **Creación de un mecanismo de respaldo y recuperación de datos:**

**Se deben realizar respaldos automáticos cada 24 horas.**

En DataLoader.io, el proceso permite configurar un respaldo automático de datos desde Salesforce. Para ello, se crea una tarea de exportación seleccionando el objeto que se desea respaldar, en este caso "Login_Histories", y eligiendo los campos específicos que se van a exportar. Luego, se configura la programación del respaldo, eligiendo que se ejecute de manera diaria a una hora específica. Finalmente, la tarea se guarda y se ejecuta, asegurando que los respaldos se realicen automáticamente de acuerdo con el horario establecido.

![Logo](https://i.pinimg.com/1200x/22/08/e2/2208e2b98999e047a9ec803ae189a827.jpg)

En la configuración de respaldo, se debe ingresar una dirección de correo electrónico donde se enviarán los datos exportados. A esta dirección llegará una notificación con un enlace que permitirá descargar los datos de "Login_Histories" en formato CSV.
![Logo](https://i.pinimg.com/1200x/4b/d7/ea/4bd7ead6eeec251833aa84a26fff1b5b.jpg)






