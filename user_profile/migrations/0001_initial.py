from django.db import migrations, models

def add_initial_profiles(apps):
    Profile = apps.get_model('user_profile', 'Profile')
    Profile.objects.create(name="John Doe", checked=False, age=30, comments="Sample comment", gender="Male", items=5, place="New York")

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # 他のアプリケーションの依存関係がある場合はここに記述
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=64)),
                ("checked", models.BooleanField(default=False)),
                ("age", models.IntegerField(default=0)),
                ("comments", models.TextField(blank=True, max_length=1000, null=True)),
                ("gender", models.CharField(blank=True, max_length=64, null=True)),
                ("items", models.IntegerField(default=0)),
                ("place", models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RunPython(add_initial_profiles),
    ]
