
from  rest_framework.test import APITestCase
from apps.account.models import Account



class UserCreateTestCase(APITestCase):

    def test_create_account(self):

        initial_count = Account.objects.count()
        product_attributes = {
            'email' : "test@rabble.com",
            'mobile': "1234567891",
            'password' : '1234'
        }
        response = self.client.post('/api/user/',product_attributes) 

        if response.status_code != 201:
            print(response.data)

        

        self.assertEqual(
            Account.objects.count(),
            initial_count + 1
        )

        for attr,excepted_value in product_attributes.items():
              if attr == 'password': continue
              self.assertEqual(response.data[attr],excepted_value)

        self.assertEqual(
             response.data['email'],
               "test@rabble.com", 
        )



class UserListTest(APITestCase):
    
    def test_list_account(self):
        user_count = Account.objects.count()
        response = self.client.get('/api/user/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'],user_count)
        self.assertEqual(len(response.data['results']),user_count)


