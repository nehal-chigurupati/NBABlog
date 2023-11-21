# Generated by Django 4.2.7 on 2023-11-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.TextField()),
                ('player_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.TextField()),
                ('team_city', models.TextField()),
                ('team_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.TextField()),
                ('tag_description', models.TextField()),
                ('tag_id', models.IntegerField()),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_title', models.TextField()),
                ('stat_description', models.TextField()),
                ('stat_id', models.IntegerField()),
                ('stat_value', models.TextField()),
                ('stat_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.player')),
                ('stat_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.team')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.team'),
        ),
        migrations.AddField(
            model_name='article',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.player'),
        ),
        migrations.AddField(
            model_name='article',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.team'),
        ),
    ]