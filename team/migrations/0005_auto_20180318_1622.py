# Generated by Django 2.0.3 on 2018-03-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20180318_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='dribling',
            new_name='dribbling',
        ),
        migrations.AlterField(
            model_name='club',
            name='founded_year',
            field=models.IntegerField(),
        ),
    ]
