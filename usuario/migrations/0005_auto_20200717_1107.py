# Generated by Django 2.2.9 on 2020-07-17 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20200717_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='pasta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.Pasta'),
        ),
    ]
