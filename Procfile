# Este archivo le dice a Elastic Beanstalk qué comando ejecutar para iniciar la aplicación web.
# Gunicorn es el servidor de aplicaciones WSGI recomendado para producción con Django.

web: gunicorn --bind :8000 --workers 3 --threads 3 coffe_shop.wsgi:application 