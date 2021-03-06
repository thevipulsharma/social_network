# Generated by Django 2.0.3 on 2018-05-30 04:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_liked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'newsfeed',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='ProfilePictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'profile_pictures',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='profilepictures',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.UserInfo'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.UserInfo'),
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.UserInfo'),
        ),
        migrations.AddField(
            model_name='messages',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_receiver', to='newsfeed.UserInfo'),
        ),
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_sender', to='newsfeed.UserInfo'),
        ),
        migrations.AddField(
            model_name='likes',
            name='newsfeed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.NewsFeed'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.UserInfo'),
        ),
        migrations.AddField(
            model_name='comments',
            name='newsfeed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.NewsFeed'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.UserInfo'),
        ),
    ]
