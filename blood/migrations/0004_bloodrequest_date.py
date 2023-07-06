
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_auto_20210213_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
