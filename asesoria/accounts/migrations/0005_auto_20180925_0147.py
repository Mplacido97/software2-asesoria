# Generated by Django 2.0.2 on 2018-09-25 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180925_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesoria',
            name='codCurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Curso'),
        ),
    ]