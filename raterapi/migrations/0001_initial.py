# Generated by Django 4.0.5 on 2022-06-17 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('maker', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('game_image', models.ImageField(default=None, upload_to='uploads/')),
                ('game_url', models.URLField(default=None, max_length=500)),
                ('categories', models.ManyToManyField(to='raterapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='RateGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.gametype'),
        ),
        migrations.AddField(
            model_name='game',
            name='registrant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player'),
        ),
    ]
