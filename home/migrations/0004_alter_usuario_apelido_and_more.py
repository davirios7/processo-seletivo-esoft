# Generated by Django 4.1.4 on 2022-12-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_usuario_apelido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apelido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_de_nascimento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='observacao',
            field=models.CharField(max_length=50),
        ),
    ]
