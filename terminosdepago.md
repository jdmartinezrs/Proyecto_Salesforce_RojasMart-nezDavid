🚀 Cómo Crear los Términos de Pago en Salesforce SIN CPQ
Puedes manejar los términos de pago en las entidades estándar de Cuentas (Accounts) o Facturas (Invoices), dependiendo de cómo manejen los pagos en ConstruFurgo.

1️⃣ Agregar un Campo de Términos de Pago en Cuentas
Si los términos de pago dependen del cliente, puedes almacenarlos en Cuentas (Accounts).

🔹 Pasos:
1️⃣ Ve a Setup (Configuración) > Object Manager (Administrador de Objetos).
2️⃣ Busca Account (Cuenta) y haz clic en él.
3️⃣ Ve a la pestaña Fields & Relationships (Campos y Relaciones).
4️⃣ Haz clic en New (Nuevo) y selecciona Picklist.
5️⃣ Nombra el campo "Términos de Pago" y agrega valores como:

Pago Inmediato
Net 30 (Pago a 30 días)
Net 60 (Pago a 60 días)
50% Anticipo – 50% Entrega
6️⃣ Guarda los cambios y agrégalo a la vista de la página de la cuenta.
Ahora, al editar cualquier cuenta, podrás asignarle su término de pago correspondiente.

2️⃣ Agregar los Términos de Pago en Facturas
Si los términos deben aplicarse por factura y no por cliente, puedes agregarlos en el objeto Facturas (Invoices).

🔹 Pasos:
1️⃣ Ve a Setup > Object Manager > busca Factura (Invoice) o el objeto que estés usando para registrar pagos.
2️⃣ Agrega un campo de tipo Picklist con los mismos valores de términos de pago.
3️⃣ Asigna el término de pago correcto en cada factura emitida.

Esto permitirá un mejor control de pagos en cada transacción.

3️⃣ Automatizar Recordatorios de Pago
Si quieres que Salesforce envíe notificaciones de pago automático a los clientes, puedes hacer lo siguiente:

🔹 Opción 1: Flujo de Trabajo (Workflow Rule)

Crea una regla que envíe un correo cuando la fecha límite de pago esté cerca.
🔹 Opción 2: Flow en Salesforce

Genera un Flow para alertar al equipo financiero cuando una factura esté por vencer.
📊 4️⃣ Crear Reportes y Dashboards
Para monitorear los pagos, puedes crear un Reporte de Facturación que muestre:
✅ Términos de pago de cada cliente.
✅ Facturas pendientes y vencidas.
✅ Alertas de pago automático.

🎯 Conclusión
Aunque Salesforce CPQ no esté habilitado, puedes manejar términos de pago usando objetos estándar. Lo clave es:
✅ Agregar un campo de Términos de Pago en Cuentas o Facturas.
✅ Automatizar recordatorios con Flows o Workflows.
✅ Crear reportes para monitorear pagos.

🚀 ¿Quieres ayuda creando el Flow para recordatorios de pago?







