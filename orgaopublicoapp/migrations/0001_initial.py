# Generated by Django 3.1.5 on 2021-01-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orgaopublico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_orgaopublico', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('tipo_orgaopublico', models.CharField(max_length=200)),
                ('conceito_orgaopublico', models.CharField(max_length=200)),
            ],
        ),
    ]
