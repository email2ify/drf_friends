# Generated by Django 3.2.19 on 2023-07-16 11:38

import cloudinary.models
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, unique=True)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('countries', multiselectfield.db.fields.MultiSelectField(choices=[('Algeria', 'Algeria'), ('Angola', 'Angola'), ('Benin', 'Benin'), ('Botswana', 'Botswana'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cabo Verde', 'Cabo Verde'), ('Cameroon', 'Cameroon'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Comoros', 'Comoros'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Republic of the Congo', 'Republic of the Congo'), ("Cote d'Ivoire", "Cote d'Ivoire"), ('Djibouti', 'Djibouti'), ('Egypt', 'Egypt'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Ghana', 'Ghana'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Kenya', 'Kenya'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Mali', 'Mali'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Sudan', 'Sudan'), ('Tanzania', 'Tanzania'), ('Togo', 'Togo'), ('Tunisia', 'Tunisia'), ('Uganda', 'Uganda'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]