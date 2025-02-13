from django.db import migrations
from tasks.models import Task  # Import your Task model

def create_default_tasks(apps, schema_editor):
    """Creates initial default tasks if they don't already exist."""
    default_tasks = [
        {
            'title': 'Adicione suas tarefas, edite e as excluas, como quiser!',
            'completed': False,
        },
        {
            'title': 'Quando completar a tarefa, marque a caixa ao lado',
            'completed': True,
        },
    ]

    for task_data in default_tasks:
        if not Task.objects.filter(title=task_data['title']).exists(): # Check if task with this title already exists
            Task.objects.create(**task_data) # Create task if it doesn't exist

def delete_default_tasks(apps, schema_editor):
    """Deletes the default tasks (reverse migration - not strictly necessary for initial setup, but good practice)."""
    default_task_titles = [
        'Adicione suas tarefas, edite e as excluas, como quiser!',
        'Quando completar a tarefa, marque a caixa ao lado',
    ]
    Task.objects.filter(title__in=default_task_titles).delete() # Delete tasks with these titles

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_tasks, delete_default_tasks), # Add RunPython operation
    ]