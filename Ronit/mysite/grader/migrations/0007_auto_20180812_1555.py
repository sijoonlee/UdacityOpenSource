# Generated by Django 2.1 on 2018-08-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0006_essay_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
