# Generated by Django 3.0.5 on 2020-06-16 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200609_0559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('order',)},
        ),
    ]