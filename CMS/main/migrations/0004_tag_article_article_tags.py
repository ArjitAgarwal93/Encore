# Generated by Django 4.2.8 on 2023-12-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_article_article_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=15)),
                ('tag_slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(to='main.tag'),
        ),
    ]
