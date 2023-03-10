# Generated by Django 4.1.4 on 2022-12-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0006_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('data_de_nascimento', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('apelido', models.CharField(max_length=50, null=True)),
                ('observacao', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
