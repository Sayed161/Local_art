# Generated by Django 4.2.7 on 2024-04-12 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', models.TextField()),
                ('Created_date', models.DateTimeField(auto_now_add=True)),
                ('Image_url', models.URLField()),
                ('Artworker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='Artists.artists')),
            ],
        ),
    ]
