#!/bin/bash
# Este script se ejecuta en el servidor de AWS después de cada despliegue.
# Su propósito es aplicar las migraciones de la base de datos automáticamente.
# Ubicación: .platform/hooks/postdeploy/01_migrate.sh

# La variable de entorno 'EB_IS_COMMAND_LEADER' es 'true' solo en una instancia
# por cada despliegue. Esta es la forma recomendada y más segura por AWS 
# para ejecutar comandos que solo deben correr una vez.

if [ "$EB_IS_COMMAND_LEADER" = "true" ]; then
  echo "Soy la instancia líder. Ejecutando migraciones de Django..."
  
  # El entorno virtual de Python ya está activado en este punto.
  # Ejecutamos las migraciones sin pedir confirmación.
  python manage.py migrate --noinput
  
  echo "Migraciones completadas exitosamente."
else
  echo "No soy la instancia líder. Saltando migraciones."
fi 