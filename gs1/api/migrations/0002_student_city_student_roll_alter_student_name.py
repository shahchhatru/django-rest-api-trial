# Generated by Django 4.1.3 on 2022-12-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
