# Generated by Django 5.0.3 on 2024-03-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_alter_themes_options_themes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themes',
            name='image',
            field=models.ImageField(default='themes_img/theme.jpg', upload_to='themes_img', verbose_name='ThemeImage'),
        ),
    ]