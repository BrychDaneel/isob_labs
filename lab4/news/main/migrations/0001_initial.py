# Generated by Django 2.1.4 on 2018-12-15 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Коментарий')),
                ('pubtime', models.DateTimeField(auto_now_add=True, verbose_name='Дата коментирования')),
            ],
            options={
                'verbose_name': 'коментарий',
                'verbose_name_plural': 'коментарии',
                'db_table': 'comments',
                'ordering': ['pubtime'],
            },
        ),
        migrations.CreateModel(
            name='EmailConfirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=uuid.uuid4, max_length=36)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='temp', verbose_name='Изображение')),
                ('short_text', models.TextField(verbose_name='Краткое описание')),
                ('text', models.TextField(verbose_name='Тескт')),
                ('pubtime', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
                'ordering': ['-pubtime'],
            },
        ),
        migrations.AddField(
            model_name='coments',
            name='new',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='main.News'),
        ),
        migrations.AddField(
            model_name='coments',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
