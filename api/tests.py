from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create a suer
        testuser1 = User.objects.create(username = 'testuser1', password = 'testuser123')
        testuser1.save()

        #Create a blog post

        test_post = Post.objects.create(title = 'code', body = 'code image', image = 'code.jpg')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        body = f'{post.body}'
        image = f'{post.image}'

        self.assertEqual(title, 'code')
        self.assertEqual(body, 'code image')
        self.assertEqual(image, 'code.jpg')