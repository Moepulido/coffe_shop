#!/bin/bash

# Script para copiar archivos de media en AWS Elastic Beanstalk
# Este script se ejecuta después de cada despliegue

echo "🔄 [MEDIA] Iniciando copia de archivos de media..."

# Cambiar al directorio de la aplicación
cd /var/app/current

# Crear directorio de media si no existe
mkdir -p /var/app/current/media
mkdir -p /var/app/current/media/logos

# Copiar archivos de media existentes
echo "🔄 [MEDIA] Copiando archivos de media..."
if [ -d "media" ]; then
    cp -r media/* /var/app/current/media/ 2>/dev/null || true
    echo "✅ [MEDIA] Archivos de media copiados"
else
    echo "⚠️ [MEDIA] No se encontró directorio media"
fi

# Verificar que los archivos se copiaron
echo "🔍 [MEDIA] Verificando archivos de media..."
if [ -d "/var/app/current/media/logos" ]; then
    echo "📁 [MEDIA] Contenido de /var/app/current/media/logos:"
    ls -la /var/app/current/media/logos/
else
    echo "❌ [MEDIA] No se encontró directorio logos"
fi

# Configurar permisos
echo "🔧 [MEDIA] Configurando permisos..."
chown -R webapp:webapp /var/app/current/media/
chmod -R 755 /var/app/current/media/

echo "✅ [MEDIA] Proceso completado" 