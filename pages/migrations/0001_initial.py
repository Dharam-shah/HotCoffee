# Generated by Django 4.0.3 on 2022-04-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banner_title', models.CharField(max_length=200)),
                ('Banner_subtitle', models.CharField(max_length=200)),
                ('Banner_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
