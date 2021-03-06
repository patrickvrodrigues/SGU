# Generated by Django 2.2.9 on 2020-07-17 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200702_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pasta',
                'verbose_name_plural': 'Pastas',
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='setor',
            name='nome',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='setor',
            name='polo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Polo'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='setor',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='usuario.Setor'),
        ),
        migrations.AddField(
            model_name='setor',
            name='pasta',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuario.Pasta'),
        ),
    ]
