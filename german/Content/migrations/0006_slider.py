# Generated by Django 3.0.2 on 2020-01-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0005_auto_20200115_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]