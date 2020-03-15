# Generated by Django 2.2.5 on 2019-12-17 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20191201_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='last_read_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='message.Message', verbose_name='последнее прочитанное сообщение'),
        ),
    ]
