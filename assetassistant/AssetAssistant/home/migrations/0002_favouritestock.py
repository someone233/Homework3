# Generated by Django 2.0.5 on 2018-05-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailaddress', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=30)),
                ('rate', models.FloatField()),
            ],
        ),
    ]
