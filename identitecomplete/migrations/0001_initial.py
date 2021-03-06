# Generated by Django 2.2.6 on 2020-04-20 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CNI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_CNI', models.CharField(max_length=20)),
                ('last_name_CNI', models.CharField(max_length=20)),
                ('father_fullname_CNI', models.CharField(max_length=20)),
                ('mother_fullname_CNI', models.CharField(max_length=20)),
                ('province_CNI', models.CharField(max_length=20)),
                ('commune_CNI', models.CharField(max_length=20)),
                ('birth_zone_CNI', models.CharField(max_length=20)),
                ('birthday_CNI', models.DateTimeField(max_length=20)),
                ('marital_status_CNI', models.CharField(max_length=20)),
                ('kind_of_work_CNI', models.CharField(max_length=20)),
                ('CNI_number', models.CharField(max_length=20)),
                ('delivered_date', models.CharField(max_length=20)),
                ('delivered_zone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CommuneLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('commune_leaded', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('province_leaded', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identitecomplete.Commune')),
            ],
            options={
                'unique_together': {('name', 'commune')},
            },
        ),
        migrations.CreateModel(
            name='ZoneLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('zone_leaded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identitecomplete.Zone')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompleteIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('first_name_beneficiary', models.CharField(max_length=20)),
                ('last_name_beneficairy', models.CharField(max_length=20)),
                ('beneficiary_father_first_name', models.CharField(max_length=50)),
                ('benefiaciary_mother_first_name', models.CharField(max_length=50)),
                ('birth_zone', models.CharField(max_length=20)),
                ('birth_year', models.CharField(max_length=20)),
                ('birth_commune', models.CharField(max_length=20)),
                ('birth_province', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('marital_status', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=20)),
                ('residence_zone', models.CharField(max_length=20)),
                ('residence_quarter', models.CharField(max_length=20)),
                ('CNI_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='commune',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identitecomplete.Province'),
        ),
        migrations.AlterUniqueTogether(
            name='commune',
            unique_together={('name', 'province')},
        ),
    ]
