# Generated by Django 3.2.13 on 2022-06-26 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0003_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
