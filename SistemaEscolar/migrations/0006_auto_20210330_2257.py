# Generated by Django 3.1.7 on 2021-03-31 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaEscolar', '0005_auto_20210330_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
