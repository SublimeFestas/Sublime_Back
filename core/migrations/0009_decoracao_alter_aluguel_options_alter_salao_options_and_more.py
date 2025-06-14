# Generated by Django 5.1.7 on 2025-04-15 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_telefonesalao_salao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decoracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True, verbose_name='Nome da decoração')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço da decoração')),
                ('descricao', models.TextField(verbose_name='Descrição da decoração')),
            ],
            options={
                'verbose_name_plural': 'Decorações',
            },
        ),
        migrations.AlterModelOptions(
            name='aluguel',
            options={'verbose_name_plural': 'Alugueis'},
        ),
        migrations.AlterModelOptions(
            name='salao',
            options={'verbose_name_plural': 'Saloes'},
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='salao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.salao', verbose_name='Salão'),
        ),
    ]
