# Generated by Django 4.2.4 on 2023-12-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emilio_salinas_Final_app', '0003_alter_inscrito_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
    ]
