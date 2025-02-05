from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread,Message

# Create your tests here.

class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1',None,'test123')
        self.user2 = User.objects.create_user('user2',None,'test123')
        self.user3 = User.objects.create_user('user3',None,'test123')
        
        self.thread = Thread.objects.create()
    
    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1,self.user2)
        self.assertEqual(len(self.thread.users.all()),2)
        
    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1,self.user2)
        threads = Thread.objects.filter(users = self.user1).filter(users = self.user2)
        self.assertEqual(self.thread,threads[0])
    
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users = self.user1).filter(users = self.user2)
        self.assertEqual(len(threads),0) 
        
    def test_add_messages_to_threads(self):
        self.thread.users.add(self.user1,self.user2)
        mensaje1 = Message.objects.create(user = self.user1,content ="muy buenas creaturitas del senior")
        mensaje2 = Message.objects.create(user = self.user2,content ="hola")
        self.thread.messages.add(mensaje1,mensaje2)
        self.assertEqual(len(self.thread.messages.all()),2)
        
        for mensajes in self.thread.messages.all():
            print("({}): {}".format(mensajes.user,mensajes.content))
   
    def test_add_message_from_user_not_in_thread(self):
        
        self.thread.users.add(self.user1,self.user2)
        mensaje1 = Message.objects.create(user = self.user1,content ="muy buenas creaturitas del senior")
        mensaje2 = Message.objects.create(user = self.user2,content ="hola")
        mensaje3 = Message.objects.create(user = self.user3,content ="Soy un espiaaa jajajajajajaj!")
        self.thread.messages.add(mensaje1,mensaje2,mensaje3)
        self.assertEqual(len(self.thread.messages.all()),2)
        
    def test_find_threads_with_custom_manager(self):
        self.thread.users.add(self.user1,self.user2)
        threads = Thread.objects.find(self.user1,self.user2)
        self.assertEqual(self.thread,threads)
    
    def test_find_or_create_threads_with_custom_manager(self):
        self.thread.users.add(self.user1,self.user2)
        threads = Thread.objects.find_or_create(self.user1,self.user2)
        self.assertEqual(self.thread,threads)
        threads = Thread.objects.find_or_create(self.user1,self.user3)
        self.assertIsNotNone(threads)