# Generated by Django 3.2.5 on 2021-07-20 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news',
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
