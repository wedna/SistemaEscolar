# Generated by Django 3.1.7 on 2021-03-31 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaEscolar', '0006_auto_20210330_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='matricula',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
