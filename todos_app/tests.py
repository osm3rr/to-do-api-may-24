from django.test import TestCase

# Create your tests here.
from .models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            
            #completed=False
        )
    
    def test_model_content(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(str(self.task), 'Test Task')