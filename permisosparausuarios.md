3. Asignación de Permisos por Usuario
A. Rojas, David (Administrador de Ventas)
Perfil: Custom: Sales Profile

Funciones Principales: Gestión de leads, oportunidades y ventas.

Permisos Necesarios:

Objetos:

Leads: Lectura, Escritura, Creación, Eliminación.

Opportunities: Lectura, Escritura, Creación, Eliminación.

Accounts: Lectura, Escritura.

Contacts: Lectura, Escritura.

Producto__c: Lectura.

Permisos Adicionales:

Acceso a Dashboards de Ventas.

Permiso para convertir leads en oportunidades.

Permiso para crear y enviar propuestas comerciales.

B. Montalvo, Sam (Ejecutivo de Compras)
Perfil: Procurement Specialist

Funciones Principales: Gestión de compras y proveedores.

Permisos Necesarios:

Objetos:

Accounts: Lectura, Escritura (solo para proveedores).

Producto__c: Lectura, Escritura.

Stage_Venta__c: Lectura.

Permisos Adicionales:

Acceso a Panel de Compras y Proveedores.

Permiso para crear órdenes de compra.

C. Furgo, Constru (CEO)
Perfil: System Administrator

Funciones Principales: Supervisión general de la empresa.

Permisos Necesarios:

Todos los objetos: Lectura, Escritura, Creación, Eliminación.

Permisos Adicionales:

Acceso a todos los Dashboards y Reportes.

Permiso para realizar auditorías y cambios de configuración.

Permiso para restaurar datos (solo en casos críticos).

D. Schifrin, James (Técnico de Ensamblaje)
Perfil: Technical_Support

Funciones Principales: Soporte técnico y resolución de casos.

Permisos Necesarios:

Objetos:

Cases: Lectura, Escritura, Creación.

Accounts: Lectura.

Contacts: Lectura.

Permisos Adicionales:

Acceso a Reporte de Casos de Soporte.

Permiso para cerrar casos resueltos.

4. Creación de Permission Sets
Para asignar permisos adicionales que no están cubiertos por los perfiles, se recomienda crear Permission Sets. Estos son algunos ejemplos:

A. Permission Set para Ventas (Sales_Permission_Set)
Asignado a: Rojas, David.

Permisos:

Convertir Leads.

Enviar propuestas comerciales.

Acceso a Dashboards de Ventas.

B. Permission Set para Compras (Procurement_Permission_Set)
Asignado a: Montalvo, Sam.

Permisos:

Crear órdenes de compra.

Acceso a Panel de Compras y Proveedores.

C. Permission Set para Soporte (Support_Permission_Set)
Asignado a: Schifrin, James.

Permisos:


Acceso a Reporte de Casos de Soporte.

