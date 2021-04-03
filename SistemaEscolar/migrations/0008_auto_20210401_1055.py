# Generated by Django 3.1.7 on 2021-04-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaEscolar', '0007_auto_20210330_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacao',
            name='status',
            field=models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('CONCLUÍDA', 'CONCLUÍDA')], default='PENDENTE', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='status',
            field=models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('CONCLUÍDA', 'CONCLUÍDA'), ('CANCELADA', 'CANCELADA'), ('RECUSADA', 'RECUSADA')], default='PENDENTE', max_length=20, null=True),
        ),
    ]
