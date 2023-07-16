# Generated by Django 3.0.10 on 2022-05-17 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number_of_pages', models.IntegerField()),
                ('description', models.TextField()),
                ('published', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(choices=[(1, 'Read'), (2, 'Not Read'), (3, 'Ongoing')])),
                ('author', models.ManyToManyField(to='book_app.Author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_app.Genre')),
            ],
        ),
    ]
