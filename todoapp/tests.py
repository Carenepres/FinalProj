from django.test import TestCase, Client
from django.urls import reverse
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title="Test Task")

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create(self):
        response = self.client.post(reverse('task-list'), {'title': 'New Task'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update(self):
        response = self.client.post(reverse('task-update', args=[self.task.id]), {'title': 'Updated Task'})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_delete(self):
        response = self.client.post(reverse('task-delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())