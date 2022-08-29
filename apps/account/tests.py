# Create your tests here.
from  rest_framework.test import APITestCase

from apps.userprofile.models import Profile

class AccountTest(APITestCase):
    def test_list_account(self):
        user_count = Profile.objects.count()
        response = self.client.get('/api/profile/')
        print(11111111111111111111111,response.data)
        print('count  :',user_count)

        

        # self.assertIsNone(response.data['next'])
        # self.assertIsNone(response.data['previous'])
        # self.assertListEqual(response.data['count'],user_count)
        self.assertIs(0,user_count)

