# Generated by Django 4.1.7 on 2023-10-31 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelfile',
            name='reservoir',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.reservoirs'),
        ),
        migrations.AddField(
            model_name='reservoirs',
            name='category',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='textfile',
            name='reservoir',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.reservoirs'),
        ),
    ]
