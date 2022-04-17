# Generated by Django 4.0.4 on 2022-04-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('blog_image', models.ImageField(upload_to='images/')),
                ('blog_desc', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Homepage_banner',
            new_name='HomepageBanner',
        ),
        migrations.RenameField(
            model_name='homepagebanner',
            old_name='Banner_image',
            new_name='banner_image',
        ),
        migrations.RenameField(
            model_name='homepagebanner',
            old_name='Banner_subtitle',
            new_name='banner_subtitle',
        ),
        migrations.RenameField(
            model_name='homepagebanner',
            old_name='Banner_title',
            new_name='banner_title',
        ),
    ]
