# Generated by Django 3.2.5 on 2021-07-19 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0009_alter_advertisement_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=11)),
            ],
        ),
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_advertisements.advertisementstatus'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_advertisements.author'),
        ),
    ]
