# Generated by Django 4.1.5 on 2023-01-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField(default='', editable=False, max_length=1000)),
                ('address', models.CharField(max_length=100)),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]