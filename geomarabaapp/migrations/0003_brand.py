# Generated by Django 2.2.2 on 2019-06-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomarabaapp', '0002_auto_20190617_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('teste', models.CharField(max_length=200)),
            ],
        ),
    ]
