# Custom Partner Search in Sales

Este módulo de Odoo 17 restringe la búsqueda de contactos en la vista de cotizaciones (`sale.order`)
para que solo se busquen por el campo `company_registry`.

## 📌 Características

- Modifica la vista de `sale.order` para establecer un dominio en `partner_id`.
- Sobrescribe el método `name_search` en `res.partner` para filtrar por `company_registry`.
- Evita que los usuarios busquen por nombre, correo u otros campos.
