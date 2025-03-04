.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

connector_beezup
================

Crea un controlador para generar ficheros CSV para Beezup con información de
los productos para diferentes idiomas desde una URL para que sea automatizado por el importador de Beezup. 

Los ficheros que puede automatizar para que Beezup los descarge periodicamente son:
- Catálogo de producto desde  https://DOMAIN/beezup/csv/last/standard
- Actualización de stock desde https://DOMAIN/beezup/csv/last/update_stock

Configuración
-------------

En cada compañía, rellenar los campos:
- "Tarifa Beezup".
- "Impuestos producto".

Por defecto el sistema usará para conectarse a Beezup el valor del parámetro
de configuración 'beezup.url' o, en caso de estar vacío, el valor del parámetro
de configuración 'web.base.url'.

### Entorno con multiples base de datos.

En el caso de que tenga múltiples base de datos las llamadas a las descarga de los ficheros CSV es necesario que indique con el parametro `db=BASE_DE_DATOS` en la URL. Además en la configuración de Odoo tendrá que añadir el módulo como `server_wide_modules` en el fichero de configuración:
```
server_wide_modules=web,connector_beezup
```

Otras funcionalidades
---------------------

Además añade un asistente para permitir importar pedidos de venta de Beezup
desde un fichero. Se accede desde el menú Ajustes/Técnico/Importar fichero.

Autor
=====
.. image:: https://trey.es/logo.png
   :alt: License: Trey Kilobytes de Soluciones SL
`Trey Kilobytes de Soluciones SL <https://www.trey.es>`_
