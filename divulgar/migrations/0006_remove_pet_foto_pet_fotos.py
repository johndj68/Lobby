# Generated by Django 4.1.5 on 2023-01-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0005_rename_tag_pet_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='foto',
        ),
        migrations.AddField(
            model_name='pet',
            name='fotos',
            field=models.ImageField(default=1, upload_to='fotos_pet'),
            preserve_default=False,
        ),
    ]