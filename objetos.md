Orden de Inserción de los Datos
Users.csv

Roles_Profiles.csv

Accounts.csv

Contacts.csv

Productos.csv

leads.csv

Opportunities_clean.csv

Cases.csv

stage_ventas.csv

Configuración de Objetos, Campos y Relaciones
1. Users.csv
Objeto: User (Objeto estándar de Salesforce).

Campos:

User_ID: Texto (ID externo, único).

Name: Texto (Nombre completo del usuario).

Email: Email (Correo electrónico).

Role: Texto (Rol del usuario).

Profile: Texto (Perfil del usuario).

Department: Texto (Departamento).

Active: Casilla de verificación (Activo o inactivo).

Relaciones:

No se requieren relaciones adicionales, ya que User es un objeto estándar.

2. Roles_Profiles.csv
Objeto: Crear un objeto personalizado llamado Role_Profile__c.

Campos:

Role: Texto (Rol del usuario).

Profile: Texto (Perfil del usuario).

Relaciones:

No se requieren relaciones adicionales, ya que este objeto es de referencia.

3. Accounts.csv
Objeto: Account (Objeto estándar de Salesforce).

Campos:

Account_ID: Texto (ID externo, único).

Company: Texto (Nombre de la empresa).

Email: Email (Correo electrónico de la empresa).

Relaciones:

No se requieren relaciones adicionales, ya que Account es un objeto estándar.

4. Contacts.csv
Objeto: Contact (Objeto estándar de Salesforce).

Campos:

Contact_ID: Texto (ID externo, único).

Name: Texto (Nombre completo del contacto).

Account_ID: Relación (Lookup) con Account.

Email: Email (Correo electrónico del contacto).

Relaciones:

Account_ID: Relación de Lookup con el objeto Account.

5. Productos.csv
Objeto: Crear un objeto personalizado llamado Producto__c.

Campos:

Product_ID: Texto (ID externo, único).

Name: Texto (Nombre del producto).

Category: Texto (Categoría del producto).

Price: Moneda (Precio del producto).

Stock: Número (Cantidad en stock).

Relaciones:

No se requieren relaciones adicionales, ya que este objeto es independiente.

6. leads.csv
Objeto: Lead (Objeto estándar de Salesforce).

Campos:

Lead_ID: Texto (ID externo, único).

Name: Texto (Nombre completo del lead).

Email: Email (Correo electrónico del lead).

Industry: Texto (Industria del lead).

Phone: Teléfono (Número de teléfono del lead).

Relaciones:

No se requieren relaciones adicionales, ya que Lead es un objeto estándar.

7. Opportunities_clean.csv
Objeto: Opportunity (Objeto estándar de Salesforce).

Campos:

Opportunity_ID: Texto (ID externo, único).

Account_ID: Relación (Lookup) con Account.

Name: Texto (Nombre de la oportunidad).

Stage: Texto (Etapa de la oportunidad).

Amount: Moneda (Monto de la oportunidad).

Relaciones:

Account_ID: Relación de Lookup con el objeto Account.

8. Cases.csv
Objeto: Case (Objeto estándar de Salesforce).

Campos:

Case_ID: Texto (ID externo, único).

Account_ID: Relación (Lookup) con Account.

Subject: Texto (Asunto del caso).

Priority: Texto (Prioridad del caso).

Status: Texto (Estado del caso).

Relaciones:

Account_ID: Relación de Lookup con el objeto Account.

9. stage_ventas.csv
Objeto: Crear un objeto personalizado llamado Stage_Venta__c.

Campos:

Stage_ID: Texto (ID externo, único).

Stage_Name: Texto (Nombre de la etapa).

Probability: Número (Probabilidad de cierre).

Description: Texto largo (Descripción de la etapa).

Relaciones:

No se requieren relaciones adicionales, ya que este objeto es de referencia.

Resumen de Relaciones entre Objetos
Objeto	Relación	Objeto Relacionado
Contact	Account_ID (Lookup)	Account
Opportunity	Account_ID (Lookup)	Account
Case	Account_ID (Lookup)	Account
Herramientas para Insertar Datos
Data Loader:

Ideal para cargar grandes volúmenes de datos desde archivos CSV.

Permite mapear campos y definir relaciones.

Import Wizard:

Útil para importar datos directamente en la interfaz de Salesforce.

Soporta objetos estándar como Account, Contact, Lead, Opportunity y Case.

Registros Manuales:

Para crear algunos registros manualmente y probar la estructura.

Consejos Finales
Valida los Datos Antes de Insertar:

Asegúrate de que los archivos CSV estén limpios y no contengan errores (por ejemplo, correos mal formateados o campos vacíos).

Usa IDs Externos:

Define campos como User_ID, Account_ID, Contact_ID, etc., como IDs externos para facilitar la creación de relaciones.

Prueba las Relaciones:

Después de insertar los datos, verifica que las relaciones (Lookups) funcionen correctamente.

Backup de Datos:

Realiza un respaldo de los datos antes de comenzar la inserción masiva.