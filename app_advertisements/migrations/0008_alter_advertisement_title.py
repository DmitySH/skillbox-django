# Generated by Django 3.2.5 on 2021-07-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0007_alter_advertisement_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
