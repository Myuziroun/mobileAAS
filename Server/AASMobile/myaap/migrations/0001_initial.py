# Generated by Django 5.0.4 on 2024-07-03 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail_user',
            fields=[
                ('id_detail_user', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'detail_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id_game', models.AutoField(primary_key=True, serialize=False)),
                ('nama_game', models.CharField(max_length=100)),
                ('genre_game', models.CharField(max_length=100)),
                ('gambar_game', models.BinaryField()),
                ('description_game', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'games',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
