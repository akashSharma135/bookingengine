# Generated by Django 3.2 on 2021-11-19 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_reservation_booking_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='booking_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_info', to='listings.bookinginfo'),
        ),
    ]