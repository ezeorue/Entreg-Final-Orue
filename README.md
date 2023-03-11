Proyecto Python CoderHouse La idea del proyecto es registrar Clientes y sus Autos los cuales asisten al Taller para hacer reparaciones y presupuestos de sus vehiculos. Luego tendremos 2 tipos de usuarios. El administrador (digamos el propio taller) quien podrá dar de alta clientes, autos, presupuestos e historiales y luego el propio cliente quien solo podra ver sus datos, los de su auto y ver el historial del mismo. también realizar el pago de los presupuestos.

En esta primer entrega tenemos cargado 4 Modelos
Clientes
Autos
Historiales
Presupuestos.

Cada Modelo tiene su action Index (Listar) y Add (Agregar registro).
El modelo Clientes es el único que por ahora tiene el Formulario para buscar por DNI. (En el ejemplo vimos que el filtro se aplicaba con Include, digamos que el dato que se buscaba tendria que estar dentro de... pero yo corregi eso para que sea la busqueda por el valor identico digamos "cliente.dni=dniBuscado")
