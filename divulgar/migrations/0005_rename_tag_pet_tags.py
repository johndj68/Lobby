# Generated by Django 4.1.5 on 2023-01-15 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0004_alter_pet_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='tag',
            new_name='tags',
        ),
    ]
