# Generated by Django 5.0.1 on 2024-01-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ai_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_version', models.CharField(max_length=100)),
                ('prompt', models.CharField(max_length=100)),
                ('input_audio', models.FileField(upload_to='')),
            ],
        ),
    ]