# Generated by Django 2.0.5 on 2018-06-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180629_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='code',
            field=models.CharField(default='000', max_length=100),
        ),
        migrations.AddField(
            model_name='entry',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]