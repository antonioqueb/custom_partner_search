# Custom Partner Search in Sales

## Descripción
Este módulo modifica la búsqueda de contactos en los pedidos de venta para que se filtren por el campo `company_registry` cuando el contexto `from_sale_order` está presente. Esto evita que se seleccionen contactos sin registro de empresa en cotizaciones.

## Características
- Modifica `name_search` en `res.partner` para aplicar el filtro solo en órdenes de venta.
- Hereda la vista de `sale.order` y ajusta el campo `partner_id` para incluir el contexto `from_sale_order`.
- Aplica un dominio que excluye contactos sin `company_registry` definido.

## Archivos y estructura

- **models/res_partner.py**: Extiende `res.partner` para modificar la búsqueda de nombres.
- **views/sale_order_view.xml**: Hereda la vista de `sale.order` y ajusta el dominio y contexto del campo `partner_id`.
- **__manifest__.py**: Define la configuración del módulo y sus dependencias.

## Instalación
1. Copiar el módulo en la carpeta `addons` de Odoo.
2. Actualizar la lista de módulos con:
   ```bash
   odoo -u custom_partner_search
   ```
3. Instalar el módulo desde la interfaz de Odoo.

## Uso
1. Ir a **Ventas** > **Cotizaciones**.
2. Al seleccionar un contacto en `partner_id`, solo aparecerán aquellos con un `company_registry` definido.

## Licencia
Este módulo está disponible bajo la licencia LGPL-3.

## Autor
**Alphaqueb Consulting**
[https://alphaqueb.com](https://alphaqueb.com)

