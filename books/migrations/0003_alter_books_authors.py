# Generated by Django 5.0.3 on 2024-03-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_category_publisher_books_price_books_authors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='authors',
            field=models.ManyToManyField(to='books.author'),
        ),
    ]
