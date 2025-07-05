#!/bin/bash

# Script para ejecutar collectstatic en AWS Elastic Beanstalk
# Este script se ejecuta después de cada despliegue

echo "🔄 [COLLECTSTATIC] Iniciando recolección de archivos estáticos..."

# Cambiar al directorio de la aplicación
cd /var/app/current

# Activar el entorno virtual
source /var/app/venv/staging-LQM1lest/bin/activate

# Configurar variables de entorno necesarias
export DJANGO_SETTINGS_MODULE=coffe_shop.settings
export IS_AWS_ENV=true

# Ejecutar collectstatic sin interacción
echo "🔄 [COLLECTSTATIC] Ejecutando python manage.py collectstatic --noinput..."
python manage.py collectstatic --noinput --clear --verbosity=2

# Verificar que los archivos del admin se copiaron
echo "🔍 [COLLECTSTATIC] Verificando archivos del admin..."
if [ -f "/var/app/current/staticfiles/admin/css/base.css" ]; then
    echo "✅ [COLLECTSTATIC] Archivos del admin encontrados correctamente"
else
    echo "❌ [COLLECTSTATIC] ERROR: No se encontraron archivos del admin"
    echo "📁 [COLLECTSTATIC] Listando contenido de staticfiles:"
    ls -la /var/app/current/staticfiles/
    echo "📁 [COLLECTSTATIC] Listando contenido de staticfiles/admin (si existe):"
    ls -la /var/app/current/staticfiles/admin/ 2>/dev/null || echo "Directorio admin no existe"
fi

# Verificar permisos
echo "🔧 [COLLECTSTATIC] Configurando permisos..."
chown -R webapp:webapp /var/app/current/staticfiles/
chmod -R 755 /var/app/current/staticfiles/

echo "✅ [COLLECTSTATIC] Proceso completado" 