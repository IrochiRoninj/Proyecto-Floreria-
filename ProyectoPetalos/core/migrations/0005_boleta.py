# Generated by Django 2.2.6 on 2019-12-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191210_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]
