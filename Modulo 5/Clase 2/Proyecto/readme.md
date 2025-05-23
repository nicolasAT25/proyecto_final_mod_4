# Sistema de Gestión de Inventario y Despacho de Medicamentos (SIGID-MED)

---

## Descripción General

**SIGID-MED** es una aplicación de terminal diseñada para una gestión integral del inventario y despacho de medicamentos. Su característica principal es la capacidad de manejar **inventarios diferenciados para múltiples ubicaciones**: tanto bodegas (almacenes centrales con mayor volumen) como locales (puntos de venta con stock más reducido).

El sistema prioriza el despacho de medicamentos directamente desde el inventario del local donde se realiza la solicitud. Si el medicamento no está disponible o el stock es insuficiente en el local, se generará automáticamente un ticket de despacho desde bodega. Este ticket incluirá los detalles necesarios para el envío a domicilio del cliente, **solicitando la dirección de envío solo en este caso específico**.

---

## Requerimientos Clave

1.  **Gestión de Inventario Multinivel y Diferenciado:**
    * **Inventario por Bodega:** Controla el stock a gran escala, ideal para redistribución o envíos a domicilio.
    * **Inventario por Local:** Gestiona el stock disponible para venta directa en cada punto de venta.
    * **Un mismo medicamento puede tener una cantidad de stock diferente en cada bodega y en cada local.**

2.  **Despacho Inteligente y Prioritario:**
    * **Prioridad de Despacho:** Siempre se intenta despachar desde el inventario del **local** donde se está realizando la operación.
    * **Generación de Ticket por Falta de Stock Local:** Si el stock en el local es insuficiente, se **genera automáticamente un ticket** para solicitar el despacho desde una bodega central.

3.  **Gestión de Tickets de Despacho desde Bodega:**
    * Registro completo de la solicitud de despacho (medicamento, cantidad, cliente).
    * **Solicitud Condicional de Dirección:** La **dirección de envío solo se pedirá y almacenará cuando se genere un ticket de despacho desde bodega**, ya que es indispensable para el envío a domicilio.
    * Manejo de **estados del ticket** (ej., "pendiente", "en proceso", "despachado", "cancelado") para su seguimiento.

4.  **Informes Básicos:**
    * Consulta del stock actual de medicamentos por ubicación (bodega o local).
    * Listado y filtrado de tickets de despacho (pendientes, despachados, etc.).

5.  **Interfaz de Terminal:**
    * Navegación sencilla mediante un **menú interactivo** basado en texto.
    * Interacción con el usuario a través de la **entrada y salida estándar** de la consola.

6.  **Persistencia de Datos:**
    * Uso de **SQLAlchemy ORM** para una gestión robusta y flexible de la base de datos relacional.
    * Se recomienda **SQLite** para el desarrollo inicial por su facilidad de uso.

---

## Estructura de la Base de Datos (Esquema con SQLAlchemy ORM)

Los siguientes modelos de datos serán mapeados a tablas en la base de datos:

* ### `Medicamento`
    * `id` (Integer, Primary Key)
    * `nombre` (String, Non-nullable)
    * `descripcion` (String, Nullable)
    * `codigo_barras` (String, Unique, Nullable)

* ### `Ubicacion`
    * `id` (Integer, Primary Key)
    * `nombre` (String, Unique, Non-nullable)
    * `tipo` (String, Non-nullable): "bodega" o "local".

* ### `Inventario`
    * `id` (Integer, Primary Key)
    * `medicamento_id` (Integer, Foreign Key a `Medicamento.id`, Non-nullable)
    * `ubicacion_id` (Integer, Foreign Key a `Ubicacion.id`, Non-nullable)
    * `cantidad` (Integer, Non-nullable, Default=0): **Stock actual del medicamento en esa ubicación específica.**

* ### `Cliente`
    * `id` (Integer, Primary Key)
    * `nombre` (String, Non-nullable)
    * `apellido` (String, Non-nullable)
    * `telefono` (String, Nullable)
    * `direccion` (String, **Nullable**): **Solo se llenará si el cliente requiere despacho a domicilio.**
    * `ciudad` (String, **Nullable**)
    * `codigo_postal` (String, Nullable)

* ### `TicketDespachoBodega`
    * `id` (Integer, Primary Key)
    * `medicamento_id` (Integer, Foreign Key a `Medicamento.id`, Non-nullable)
    * `cantidad` (Integer, Non-nullable)
    * `cliente_id` (Integer, Foreign Key a `Cliente.id`, Non-nullable)
    * `fecha_solicitud` (DateTime, Non-nullable, Default=Now)
    * `estado` (String, Non-nullable): "pendiente", "en proceso", "despachado", "cancelado".

---

## Funcionalidades del Menú en Terminal

El sistema se operará a través de un menú interactivo en la terminal:

1.  ### Gestión de Inventario
    * **Medicamentos:** Agregar, editar, eliminar.
    * **Ubicaciones:** Crear, editar, eliminar (bodegas/locales).
    * **Gestión de Stock:**
        * Actualizar stock de un medicamento en una **ubicación específica**.
        * Consultar inventario por ubicación.
        * Consultar inventario global por medicamento (total en todas las ubicaciones).

2.  ### Despacho de Medicamentos
    * Seleccionar el **local** desde el cual se intenta despachar.
    * Buscar medicamento por nombre o código.
    * Ingresar cantidad a despachar.
    * **Lógica de Despacho:**
        * Verifica el **stock del medicamento en el local seleccionado**.
        * **Si hay stock suficiente en el local:**
            * Reduce la cantidad en `Inventario` para ese medicamento y ubicación.
            * Mensaje: "Despacho exitoso desde el Local."
            * **No se solicita información de dirección.**
        * **Si el stock es insuficiente en el local:**
            * Mensaje: "Stock insuficiente en local. Generando ticket para despacho desde Bodega."
            * Solicita datos del Cliente (nombre, apellido, teléfono).
            * **¡Aquí se solicita la dirección!** Se pedirá explícitamente la **dirección completa** (calle, número, ciudad, etc.) para el envío a domicilio.
            * Crea un nuevo `TicketDespachoBodega` con estado "pendiente".

3.  ### Gestión de Tickets de Despacho desde Bodega
    * Listar tickets pendientes.
    * Listar todos los tickets (con filtro por estado).
    * **Actualizar Estado de un Ticket:** Permite cambiar el estado (ej., a "despachado").
        * **Importante:** Al marcar un ticket como "despachado", se debe **reducir el stock de la bodega** correspondiente (ej., bodega principal) en la cantidad del medicamento.
    * Ver detalles de un ticket específico (incluyendo cliente y dirección de envío).

4.  ### Informes y Consultas
    * Reporte de Inventario Actual (desglosado por ubicación).
    * Reporte de Tickets por Estado.

5.  ### Salir
    * Termina la aplicación.

---

## Tecnologías a Utilizar

* **Python 3.x:** El lenguaje de programación.
* **SQLAlchemy:** ORM para la interacción con la base de datos.
* **SQLite3:** Base de datos ligera y local para el desarrollo.
* **Módulos estándar de Python:** Para entrada/salida (`input()`, `print()`) y fechas.
* **(Opcional) `Rich`:** Para mejorar la presentación visual en la terminal (colores, tablas).

---

## Pasos para el Desarrollo

1.  **Configuración del Entorno:**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    pip install SQLAlchemy
    # pip install rich (opcional)
    ```

2.  **Definición de Modelos SQLAlchemy:**
    * Crea un archivo `models.py` para definir las clases de los modelos con sus atributos y relaciones.

3.  **Inicialización de la Base de Datos:**
    * Configura el `Engine` de SQLAlchemy (ej., `sqlite:///sigid_med.db`).
    * Usa `Base.metadata.create_all(engine)` para crear las tablas.

4.  **Implementación de Operaciones CRUD Básicas:**
    * Desarrolla funciones para agregar, obtener, actualizar y eliminar registros de cada modelo.

5.  **Desarrollo de la Lógica Principal:**
    * Implementa el bucle del menú y las funciones para cada opción, integrando la lógica de negocio y la **solicitud condicional de dirección**.

6.  **Validaciones y Manejo de Errores:**
    * Asegura la validación de entradas de usuario y maneja excepciones (ej., stock insuficiente).

7.  **Pruebas exhaustivas:**
    * Realiza pruebas de todas las funcionalidades y casos límite.

---

## Consideraciones Futuras (Potenciales mejoras)

* **Roles de Usuario y Autenticación:** Para un sistema multiusuario.
* **Historial de Transacciones:** Registro detallado de todos los movimientos de stock.
* **Alertas de Stock Mínimo:** Notificaciones cuando el stock de un medicamento esté bajo.
* **Generación de Reportes Avanzados:** Reportes de rotación de inventario, etc.

---

