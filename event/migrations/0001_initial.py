# Generated by Django 2.0.3 on 2018-03-17 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_goals', models.IntegerField()),
                ('first_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Matchs_first_team', to='team.Club')),
                ('second_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Matchs_second_team', to='team.Club')),
            ],
        ),
        migrations.CreateModel(
            name='MatchDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('goal', 'GOAL'), ('assist', 'ASSIT'), ('red_card', 'RED CARD'), ('yellow_card', 'YELLOW CARD'), ('penalty_success', 'PENALTY SUCCESS'), ('penalty_failed', 'PENALTY FAILED')], max_length=50)),
                ('team', models.IntegerField(choices=[(1, 'Team 1'), (2, 'Team 2')])),
                ('time', models.CharField(max_length=10)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Player')),
            ],
        ),
    ]
