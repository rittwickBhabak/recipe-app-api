from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse 

class AdminSiteTests(TestCase):

    def setUp(self):  # This function will run before every test that we run
        self.client = Client() 
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@indiaappdev.com",
            password="test212"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='testF@indiaappdev.com',
            password='pass123',
            name="Test user full name"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # What 'self.client.get' does?
        # Answer: This performs a HTTP get on the 'url'

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        # What 'self.assertContains' does?
        # Answer: This 'assertContains' checks,
        # if the 'res' has cerain items and it 
        # also checks if the HTTP response is 
        # HTTP200


    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/<int:id>
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        

    # default django user model has a field called 'username'
    # so, by default django admin expects a 'username' filed
    # in the User model. But in our case, we don't have a 
    # 'username' field. So, we've to customize the default 
    # django admin behaviour

    