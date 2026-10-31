
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_alter_categoria_options_remove_categoria_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(
                max_length=50,
                null=True,
                blank=True
            ),
        ),
    ]
