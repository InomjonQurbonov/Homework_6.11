# Generated by Django 5.0.3 on 2024-03-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='themes',
            options={'ordering': ('id',), 'verbose_name': 'Theme'},
        ),
        migrations.AddField(
            model_name='themes',
            name='image',
            field=models.ImageField(default='theme.jpg', upload_to='themes_img', verbose_name='ThemeImage'),
        ),
    ]