# Generated by Django 4.2.3 on 2023-07-28 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_categorie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='slider_images')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('date_text', models.CharField(max_length=50)),
                ('button_text', models.CharField(max_length=50)),
                ('button_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('zip_code', models.CharField(max_length=10, verbose_name='ZIP Code')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact Phone')),
                ('email_address', models.EmailField(max_length=100, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_Speakers', models.CharField(max_length=25)),
                ('N_Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, to='events.myclubuser')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.categories')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('speakers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.speakers')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]