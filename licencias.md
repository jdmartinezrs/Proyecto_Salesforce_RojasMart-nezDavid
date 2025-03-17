Asignación de Licencias y Perfiles por Rol
1. CEO (Gerente General)
Licencia: Salesforce (permite acceso completo a todas las funcionalidades de Salesforce)
Perfil a Clonar: System Administrator (perfil con permisos completos de administración)
2. Gerente de Ventas
Licencia: Salesforce (licencia completa)
Perfil a Clonar: Standard User (perfil estándar para usuarios de ventas, permite acceso a oportunidades, cuentas y contactos)
3. Administrador de Ventas
Licencia: Salesforce (permite gestionar la configuración y el acceso de la plataforma)
Perfil a Clonar: Standard User o Custom: Sales Profile (perfil personalizado para ventas con más permisos según necesidades específicas)
4. Ejecutivo de Ventas
Licencia: Salesforce (acceso completo a objetos de ventas)
Perfil a Clonar: Standard User (perfil estándar, suficiente para gestión de cuentas, oportunidades y contactos)
5. Gerente de Soporte Técnico
Licencia: Salesforce (acceso completo a gestión de casos y cuentas)
Perfil a Clonar: Custom: Support Profile (perfil personalizado para usuarios de soporte técnico, con permisos para gestionar casos)
6. Coordinador de Soporte
Licencia: Salesforce o Salesforce Platform (si solo necesita gestión de casos y no acceso completo a la plataforma)
Perfil a Clonar: Custom: Support Profile (perfil personalizado para soporte con permisos más específicos para tareas operativas)
7. Técnico de Ensamblaje
Licencia: Customer Portal Manager Standard o Customer Community User (estos perfiles son adecuados para usuarios con acceso limitado, como técnicos que sólo gestionan casos y actividades relacionadas con su área)
Perfil a Clonar: Customer Portal Manager Standard o Customer Community User (perfil estándar para usuarios de portal, con permisos limitados a la visualización de datos y actualización de ciertos objetos)
8. Gerente de Compras y Logística
Licencia: Salesforce (licencia completa, ya que este rol podría necesitar acceso a información financiera, de compras y proveedores)
Perfil a Clonar: Standard User (perfil estándar, con acceso adecuado a cuentas, oportunidades y objetos relacionados con compras)
9. Ejecutivo de Compras
Licencia: Salesforce o Salesforce Platform (dependiendo de las necesidades de acceso)
Perfil a Clonar: Standard User (perfil estándar para gestión de proveedores y órdenes de compra)
10. Coordinador de Logística
Licencia: Salesforce o Salesforce Platform (según el tipo de funciones que deban realizar, pueden usar la licencia de Salesforce Platform si solo gestionan procesos)
Perfil a Clonar: Standard User (perfil estándar para gestión de registros de compras y logística)
Consideraciones de Asignación de Licencias y Perfiles
Licencias: Dependerá del acceso que cada rol necesite a los objetos dentro de Salesforce. Por ejemplo, Salesforce es una licencia completa, mientras que Salesforce Platform es más limitada en cuanto a funcionalidades.
Perfiles: Los perfiles son el mecanismo para personalizar los permisos de cada rol. Si un rol necesita más acceso a funcionalidades avanzadas, como la administración de la plataforma o la configuración de la seguridad, es mejor optar por un perfil de System Administrator.
Permisos Adicionales: Dependiendo de la licencia y el perfil, puedes añadir permisos adicionales a los usuarios para tareas específicas, como la gestión de reportes, visualización de dashboards, etc.
Ejemplo de Flujo para Crear un Rol y Asignar su Perfil:
Acceder a Salesforce como Administrador.
Ir a Configuración y luego seleccionar Usuarios.
Crear un Nuevo Usuario.
Seleccionar la Licencia adecuada:
Por ejemplo, para un Gerente de Ventas, seleccionas Salesforce como licencia.
En Perfil, selecciona el perfil correspondiente: en este caso, sería Standard User.
Completa la información de usuario (nombre, correo, etc.) y asigna los permisos específicos adicionales si es necesario.
Guardar y el usuario estará listo para acceder a Salesforce con los permisos y accesos establecidos.
Resumen:
Usuarios con Licencia Salesforce: Tendrán acceso completo a las funcionalidades estándar de Salesforce, como cuentas, oportunidades, reportes, etc.
Usuarios con Licencia Salesforce Platform: Solo tendrán acceso a los objetos de la plataforma (más limitada, útil para roles operativos).
Perfiles deben ser asignados en función de las tareas que cada usuario realiza (por ejemplo, ventas, soporte, compras, etc.).
Licencias y Perfiles Personalizados se utilizan cuando un rol tiene necesidades muy específicas de acceso o funcionalidades.
Si necesitas más ayuda con el proceso o configuraciones avanzadas, no dudes en preguntar. ¡Espero que esta información te sea útil!



