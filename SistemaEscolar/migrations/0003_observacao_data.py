# Generated by Django 3.1.7 on 2021-03-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaEscolar', '0002_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
