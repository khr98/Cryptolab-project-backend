import json
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Qrcode

# 설정한 엔드포인트 경로를 통해 함수를 호출. request나 http와 비슷한 일


# 테스트 케이스를 만들 때는 항상 TestCase() 객체를 상속받아 새로운 테스트 클래스를 생성한다.
class TestQRcodeViews(TestCase): 
    client = APIClient()
    
    def setUp(self):
        Qrcode.objects.create(latitude=111.1, longitude=222.2)
	# 테스트 함수는 test_ 를 붙여주어야 테스트 함수로 인식한다.
    def test_location_post_success(self): 
	# 테스트를 위해 User Model의 Field값에 임의의 데이터를 저장한다.
        url = '/locations/'
        data = {"latitude":111.1,"longitude":222.2}
        response = self.client.post(url, data ,format='json')
        self.assertEqual(response.status_code, 201)
        content = json.loads(response.content)
        print(content)
        self.assertEquals(response.data, data)
