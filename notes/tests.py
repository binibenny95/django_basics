from django.template.defaultfilters import title
from django.test import TestCase
from django.urls import reverse
from .models import Note, Category
from django.utils import timezone
# Create your tests here.

class NoteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category')

        self.note = Note.objects.create(
            title='Test Note',
            text='This is a test note',
            reminder='This is a test note',
            category=self.category,
        )
    def test_note_create(self):

        response = self.client.post(reverse('list_notes'), {
            'title': 'Test Note',
            'text': 'This is a test note.',
            'reminder': 'This is a test note.',
            'category': self.category.id
        })

        # Check that the response is a redirect (after successful creation)
        self.assertEqual(response.status_code, 302)

        # Check that a new note is created
        note = Note.objects.get(title='Test Note')
        self.assertIsNotNone(note)
        self.assertEqual(note.text, 'This is a test note.')


    def test_edit_note(self):
        """Test editing an existing note"""
        # Prepare new data for editing
        response = self.client.post(reverse('edit_note', args=[self.note.id]), {
            'title': 'Updated Title',
            'text': 'This is updated text.',
            'reminder':'test',
            'category': self.category.id
        })

        # Check that the response is a redirect (after successful edit)
        self.assertEqual(response.status_code, 302)


        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
        self.assertEqual(self.note.text, 'This is updated text.')
