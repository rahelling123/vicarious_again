# Generated by Django 2.1.3 on 2019-01-05 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='datatest',
        ),
        migrations.AddField(
            model_name='directmessage',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.DirectMessage'),
        ),
    ]
