from django.db import migrations

def add_initial_data(apps,schema_editor):
    MyModel = apps.get_model('user_profile', 'Profile')
    MyModel.objects.create(name="John Doe", checked=False, age=30, comments="Sample comment", gender="Male", items=5, place="New York", image="profile_images/dfl.png/",)



class Migration(migrations.Migration):

    dependencies = [
        ('user_profile','0001_initial'),
          # 依存するマイグレーションを指定
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
