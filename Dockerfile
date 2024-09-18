# Utilizar la imagen base de Odoo 16
FROM odoo:16

# Copiar archivos de configuración personalizados, si los tienes
# COPY ./custom_config.conf /etc/odoo/odoo.conf

# Copiar módulos personalizados, si los tienes
# COPY ./addons /mnt/extra-addons

# Establecer el directorio de trabajo
WORKDIR /mnt/extra-addons

# Exponer el puerto 8069 para acceder a Odoo
EXPOSE 8069