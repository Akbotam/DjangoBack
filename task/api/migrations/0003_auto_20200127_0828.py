# Generated by Django 3.0.2 on 2020-01-27 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200126_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]
