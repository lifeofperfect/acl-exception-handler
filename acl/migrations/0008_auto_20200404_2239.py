# Generated by Django 2.2 on 2020-04-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acl', '0007_auto_20200404_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='camtDecision',
            field=models.CharField(blank=True, choices=[('TruePositive', 'TruePositive'), ('FalsePositive', 'FalsePositive')], default='', max_length=20, null=True),
        ),
    ]
