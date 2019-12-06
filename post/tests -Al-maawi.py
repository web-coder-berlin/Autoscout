# Books/tests.py
from datetime import  datetime

import post as post
from django.contrib.auth.models import User
from django.test import TestCase
from .models import post

class SpamTests(TestCase):
    def setUp(self):

        post.objects.create(
            title = 'Test Title',
            text = 'Test text',
            author = 'Test Author',

            date_published = datetime(2019,10,16,11,12,30),
            type = 'fake news',


            user = User.objects.create_user(
                username='test_spamer'
            ),
        )
        post.objects.create(
             title='Test Title',
             text='Test text',
             author='Test Author',

             date_published=datetime(2019, 10, 16, 11, 12, 32),
             type='fake news',

             user=User.objects.get(
               username='test_spamer'
             ),
        )




        post.objects.create(
            title = 'Test Title',
            text = 'Test text',
            author = 'Test Author',

            date_published = datetime(2019,10,16,11,12,30),
            type = 'fake news',


            user = User.objects.create_user(
                username='test_normal'
            ),
        )
        post.objects.create(
             title='Test Title',
             text='Test text',
             author='Test Author',

             date_published=datetime(2019, 10, 16, 11, 15, 40),
             type='fake news',

             user=User.objects.get(
               username='test_normal'
             ),
        )

    def test1(self):

        self.assertTrue(post.spamercheck('test_spamer'))

    def test2(self):

        self.assertFalse(post.spamercheck('test_normal'))