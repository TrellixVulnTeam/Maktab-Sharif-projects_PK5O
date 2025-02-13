# Generated by Django 3.2.9 on 2021-11-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedPerson',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testproxy.person',),
        ),
    ]
