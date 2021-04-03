# Generated by Django 3.1.7 on 2021-03-30 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaEscolar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(blank=True, null=True)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SistemaEscolar.aluno')),
            ],
        ),
    ]
