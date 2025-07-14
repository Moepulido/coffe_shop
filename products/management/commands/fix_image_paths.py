import os
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Fixes the paths for product photos, removing the "logos/" prefix and correcting extensions.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('--- Iniciando corrección de rutas de imágenes de productos ---'))
        
        updated_count = 0
        products_to_check = Product.objects.exclude(photo__isnull=True).exclude(photo__exact='')

        for product in products_to_check:
            original_path = product.photo
            
            # Quita el prefijo 'logos/' si existe
            new_path = os.path.basename(original_path)
            
            # Corrección especial para 'Latte.jpg.jpeg' -> 'Latte.jpeg'
            if new_path == 'Latte.jpg.jpeg':
                new_path = 'Latte.jpeg'
            
            # Si el nombre ha cambiado, actualízalo
            if new_path != original_path:
                product.photo = new_path
                product.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f'OK: Producto ID {product.id} actualizado de "{original_path}" a "{new_path}"'))
            else:
                self.stdout.write(self.style.WARNING(f'-- Producto ID {product.id} ya parece correcto ("{original_path}"), no se necesita cambio.'))

        if updated_count > 0:
            self.stdout.write(self.style.SUCCESS(f'\n¡Listo! Se actualizaron {updated_count} productos.'))
        else:
            self.stdout.write(self.style.WARNING('\nNo se encontraron productos que necesitaran ser actualizados.')) 