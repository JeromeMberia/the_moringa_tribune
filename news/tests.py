from django.test import TestCase
from .models import Editor,Article,tags

# class EditorTestClass(TestCase):
    
#     # Set up method
#     def setUp(self):
#         self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    
#     def test_instance(self):
#         self.assertTrue(isinstance(self.james,Editor))

#     def test_save_method(self):
#         self.james.save_editor()
#         editors = Editor.objects.all()
#         self.assertTrue(len(editors) > 0)

#     def test_delete(self):
#         self.James.delete_editor()
#         editor = Editor.object.all()
#         self.assertTrue(len(editor) == 0)
#         self.assertEqual(len(editor), 0 )
