# Generated by Django 3.1.5 on 2021-01-17 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('unique_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('time', models.FloatField()),
                ('username', models.CharField(max_length=100)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='htn_backend.show')),
            ],
        ),
    ]
