# Generated by Django 2.2.1 on 2019-06-21 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0003_auto_20190617_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sublocation',
            field=models.CharField(default='Njoro', max_length=100),
        ),
        migrations.CreateModel(
            name='Growing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(choices=[('Baringo', 'BARINGO'), ('Bomet', 'BOMET'), ('Bungoma', 'BUNGOMA'), ('Busia', 'BUSIA'), ('Elegeyo Marakwet', 'ELGEYO MARAKWET'), ('Embu', 'EMBU'), ('Garissa', 'GARISSA'), ('Isiolo', 'ISIOLO'), ('Homa Bay', 'HOMA BAY'), ('Kajiado', 'KAJIADO'), ('Kakamega', 'KAKAMEGA'), ('Kericho', 'KERICHO'), ('Kiambu', 'KIAMBU'), ('Kilifi', 'KILIFI'), ('Kirinyaga', 'KIRINYAGA'), ('Kisii', 'KISII'), ('Kisumu', 'KISUMU'), ('Kitui', 'KITUI'), ('Kwale', 'KWALE'), ('Laikipia', 'LAIKIPIA'), ('Bungoma', 'BUNGOMA'), ('Lamu', 'LAMU'), ('Machakos', 'MACHAKOS'), ('Makueni', 'MAKUENI'), ('mandera', 'MANDERA'), ('meru', 'MERU'), ('migori', 'MIGORI'), ('marsabit', 'MARSABIT'), ('mombasa', 'MOMBASA'), ('muranga', 'MURANGA'), ('nairobi', 'NAIROBI'), ('nakuru', 'NAKURU'), ('nandi', 'NANDI'), ('narok', 'NAROK'), ('nyamira', 'NYAMIRA'), ('nyandarua', 'NYANDARUA'), ('nyeri', 'NYERI'), ('samburu', 'SAMBURU'), ('siaya', 'SIAYA'), ('taita taveta', 'TAITA TAVETA'), ('tana river', 'TANA RIVER'), ('tharaka nithi', 'THARAKA NITHI'), ('trans nzoia', 'TRANS NZOIA'), ('turkana', 'TURKANA'), ('uasin gishu', 'UASIN GISHU'), ('vihiga', 'VIHIGA'), ('wajir', 'WAJIR'), ('west pokot', 'WEST POKOT')], default='Nairobi', max_length=300)),
                ('category', models.CharField(choices=[('equipment', 'FARM EQUIPMENT'), ('cereals', 'CEREALS'), ('vegetables', 'VEGETABLES'), ('livestock', 'LIVESTOCK'), ('other', 'OTHER'), ('cash crops', 'CASH CROPS'), ('agrochemicals', 'AGROCHEMICALS'), ('fruits', 'FRUITS'), (' fertilizers', 'FERTILIZERS'), ('fishery', 'FISHERY')], default='other', max_length=10)),
                ('image', models.FileField(blank=True, upload_to='products_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('unitofsale', models.CharField(choices=[('whole', 'whole unit'), ('item', 'per single item')], max_length=10)),
                ('sublocation', models.CharField(default='Njoro', max_length=100)),
                ('MaturityDate', models.DateTimeField()),
                ('DescribeFarming', models.TextField(max_length=450)),
                ('slug', models.SlugField(max_length=200)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]