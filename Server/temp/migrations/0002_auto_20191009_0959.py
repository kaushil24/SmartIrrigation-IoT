# Generated by Django 2.2.5 on 2019-10-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('parent', models.CharField(default='Adruino UNO', max_length=100)),
                ('data', models.FloatField(default=-1.0)),
                ('unit', models.CharField(default="'C", max_length=10)),
                ('anamoly', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]