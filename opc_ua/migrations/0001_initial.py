# Generated by Django 2.2.7 on 2019-11-27 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('enable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=20)),
                ('enable', models.BooleanField(default=False)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opc_ua.Server')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(default='[]')),
                ('date', models.DateField()),
                ('status', models.TextField(default='[]')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opc_ua.Tag')),
            ],
        ),
    ]
