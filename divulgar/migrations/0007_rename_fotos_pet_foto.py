# Generated by Django 4.1.5 on 2023-01-15 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0006_remove_pet_foto_pet_fotos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='fotos',
            new_name='foto',
        ),
    ]
