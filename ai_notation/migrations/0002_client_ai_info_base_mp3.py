# Generated by Django 5.0.1 on 2024-02-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_notation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_ai_info',
            name='base_mp3',
            field=models.FileField(null=True, upload_to='D:\\DEV\\Crescendo_python\\ai_download'),
        ),
    ]
