 **Capítulo II: Estructura Organizacional**



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

### **Artículo 5. Organigrama empresarial establecido **

- CEO
- **Gerente de Ventas** → Administrador de Ventas, Ejecutivo de Ventas
- **Gerente de Soporte** → Coordinador de Soporte, Técnico de Ensamblaje
- **Gerente de Compras** → Ejecutivo de Compras, Coordinador de Logística


**Activar múltiples monedas en Salesforce y configurar USD**

para Lograr que el Capital Social sea $5,000,000 USD, se establece la taza de cambio con un valor de 4.000 ,  Las tasas de conversión se definen en relación con la moneda corporativa. Todas las tasas de conversión de monedas ya definidas en salesforce.com se modificarán adecuadamente para reflejar el cambio. selecciona USD.

| ![img](https://contrufurgo-dev-ed.develop.my.salesforce.com/img/s.gif)Active Currencies |      |      |
| ------------------------------------------------------------ | ---- | ---- |
|                                                              |      |      |

| Action                                                       | Currency Code | Currency Name  |                          Corporate                           | Conversion Rate | Decimal Places | Last Modified By                                             |
| :----------------------------------------------------------- | :------------ | :------------- | :----------------------------------------------------------: | --------------: | -------------: | :----------------------------------------------------------- |
| [Edit](javascript:srcUp('%2F01Lbm000002ZsSb%2Fe%3FretURL%3D%2Fsetup%2Fcur%2Fcurrencylist.jsp%3FretURL%3D%252Fsetup%252Fhome%26appLayout%3Dsetup%26tour%3D%26sfdcIFrameOrigin%3Dhttps%253A%252F%252Fcontrufurgo-dev-ed.develop.lightning.force.com%26sfdcIFrameHost%3Dweb%26nonce%3D039c5c20240184235d551e42632532e5f13f6370641df4b174dc0dbd5dcf2198%26ltn_app_id%3D%26clc%3D1%26isdtp%3Dp1%26isdtp%3Dp1');) \| [Deactivate](javascript:srcUp('%2F01Lbm000002ZsSb%2Fe%3FIsoCode%3DCOP%26active%3D0%26retURL%3D%2Fsetup%2Fcur%2Fcurrencylist.jsp%3FretURL%3D%252Fsetup%252Fhome%26appLayout%3Dsetup%26tour%3D%26sfdcIFrameOrigin%3Dhttps%253A%252F%252Fcontrufurgo-dev-ed.develop.lightning.force.com%26sfdcIFrameHost%3Dweb%26nonce%3D039c5c20240184235d551e42632532e5f13f6370641df4b174dc0dbd5dcf2198%26ltn_app_id%3D%26clc%3D1%26isdtp%3Dp1%26isdtp%3Dp1');) | COP           | Colombian Peso | ![Not Checked](https://contrufurgo-dev-ed.develop.my.salesforce.com/img/checkbox_unchecked.gif) |    4,000.000000 |              2 | [Constru Furgo](javascript:srcUp('%2F005bm00000CTSfd%3Fisdtp%3Dp1%26isUserEntityOverride%3D1%26noredirect%3D1');), 3/15/2025, 12:40 AM |
| [Edit](javascript:srcUp('%2F01Lbm000002ZsZ3%2Fe%3FretURL%3D%2Fsetup%2Fcur%2Fcurrencylist.jsp%3FretURL%3D%252Fsetup%252Fhome%26appLayout%3Dsetup%26tour%3D%26sfdcIFrameOrigin%3Dhttps%253A%252F%252Fcontrufurgo-dev-ed.develop.lightning.force.com%26sfdcIFrameHost%3Dweb%26nonce%3D039c5c20240184235d551e42632532e5f13f6370641df4b174dc0dbd5dcf2198%26ltn_app_id%3D%26clc%3D1%26isdtp%3Dp1%26isdtp%3Dp1');) \| Deactivate | USD           | U.S. Dollar    | ![Checked](https://contrufurgo-dev-ed.develop.my.salesforce.com/img/checkbox_checked.gif) |        1.000000 |              2 | [Constru Furgo](javascript:srcUp('%2F005bm00000CTSfd%3Fisdtp%3Dp1%26isUserEntityOverride%3D1%26noredirect%3D1');), 3/15/2025, 12:30 AM |

Ahora, todas las conversiones de moneda toman el USD como referencia, 1 USD = 4,000 COP.

