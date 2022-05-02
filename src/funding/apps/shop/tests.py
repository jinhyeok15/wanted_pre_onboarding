from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import *
from funding.apps.user.models import User, Pocket
from funding.apps.core.exceptions import (
    DoesNotIncludeStatusError,
    UserAlreadyParticipateError
)
from funding.apps.core.components.date import DateComponent


class ShopModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.item = Item.objects.create(
            tag="cheeze",
            price=4500,
            target_amount=600000
        )
        self.item=Item.objects.create(tag="item2", price=20000, target_amount=1000000)
        self.purchase = Purchase.objects.create(
            user_id=self.user,
            production=self.item
        )
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_item(self):
        self.assertEqual(self.item.tag, "item2")
    
    def test_Purchase_get(self):
        self.assertRaises(DoesNotIncludeStatusError, Purchase.objects.get, pk=self.purchase.id)


class ShopAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.headers = {"HTTP_AUTHORIZATION": 'Token '+self.token.key}

        self.item = Item.objects.create(
            tag="cheeze",
            price=4500,
            target_amount=600000
        )

        self.fin_date = DateComponent('2022-07-10')
        
        self.post = Post.objects.create(
            poster=self.user,
            title="hi hi hi",
            content="nice to meet you",
            item=self.item,
            poster_name="jj",
            final_date=str(self.fin_date)
        )

    def test_ShopPostItemView_post(self):
        uri = '/shop/v1/post/'
        request_data = {
            'title': '안녕하세요',
            'poster_name': '이진혁',
            'content': '어쩔티비 저쩔티비 우짤래미 저쩔래미 ^&^',
            'target_amount': 1000000,
            'final_date': '2023-04-26',  # component에서 DateCpnt로 date 유효성 검사
            'price': 15000
        }

        # DOES_NOT_EXIST_USER_POCKET test
        response = self.client.post(uri, request_data, format='json', **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'DOES_NOT_EXIST_USER_POCKET')

        Pocket.objects.get(user_id=self.user.id, is_active=False).update(bank_account_type="NH", is_active=True)
        response = self.client.post(uri, request_data, format='json', **self.headers)
        self.assertEqual(response.status_code, 201, "201 fail")

        # serializer validation error
        request_data['poster_name'] = ''
        response = self.client.post(uri, request_data, format='json', **self.headers)
        self.assertEqual(response.status_code, 400, "400 serializer error fail")

        # date관련 에러
        request_data["final_date"] = "2022-04-25"
        response = self.client.post(uri, request_data, format='json', **self.headers)
        self.assertEqual(response.status_code, 400, "400 date형 관련 에러 fail")
    
    def test_ShopWantParticipateView_get(self):
        uri = f'/shop/v1/{self.post.id}/want_participate/'
        partner = User.objects.create_user('partner1', 'partner1@partner.com', 'partner123')
        ptoken = Token.objects.create(user=partner)

        headers = {
            "HTTP_AUTHORIZATION": 'Token '+ptoken.key
        }

        # POSTER_CANNOT_PARTICIPATE test
        response = self.client.get(uri, **self.headers)
        self.assertEqual(response.data['status'], 'POSTER_CANNOT_PARTICIPATE')

        # DOES_NOT_EXIST_USER_POCKET test
        response = self.client.get(uri, **headers)
        self.assertEqual(response.data['status'], 'DOES_NOT_EXIST_USER_POCKET')

        # 200 test
        Pocket.objects.get(user_id=partner.id, is_active=False).update(bank_account_type="NH", is_active=True)
        response = self.client.get(uri, **headers)
        self.assertEqual(response.status_code, 200)

        # USER_ALREADY_PARTICIPATE test
        purchase=Purchase.objects.create(
            user_id=partner,
            production=self.item
        )
        Participant.objects.create(
            user=partner,
            post_id=self.post,
            purchase=purchase
        )
        response = self.client.get(uri, **headers)
        self.assertEqual(response.data['status'], 'USER_ALREADY_PARTICIPATE')

    def test_ShopParticipateView_post(self):
        uri = f'/shop/v1/{self.post.id}/participate/'
        partner = User.objects.create_user('partner1', 'partner1@partner.com', 'partner123')
        ptoken = Token.objects.create(user=partner)

        headers = {
            "HTTP_AUTHORIZATION": 'Token '+ptoken.key
        }

        purchase = Purchase.objects.create(
            user_id=partner,
            production=self.item
        )

        # POST_CANNOT_PARTICIPATE test
        self.post.status = 'CLOSE'
        self.post.save()
        response = self.client.post(uri, format='json', **headers)
        self.assertEqual(response.data['status'], "POST_CANNOT_PARTICIPATE")
        self.post.status = 'FUNDING'
        self.post.save()

        # POSTER_CANNOT_PARTICIPATE test
        response = self.client.post(uri, format='json', **self.headers)
        self.assertEqual(response.data['status'], 'POSTER_CANNOT_PARTICIPATE')

        # USER_ALREADY_PARTICIPATE test
        participant = Participant.objects.create(
            user=partner,
            post_id=self.post,
            purchase=purchase
        )
        response = self.client.post(uri, format='json', **headers)
        self.assertEqual(response.data['status'], 'USER_ALREADY_PARTICIPATE')

        # 200 OK
        participant.delete()

        response = self.client.post(uri, format='json', **headers)
        self.assertEqual(response.data['status'], 'HTTP_200_OK')

    def test_ShopPostDetailView_get(self):
        uri = f'/shop/v1/post/{self.post.id}/'
        num = 3
        for i in range(num):
            info = (f'user{i}', f'user{i}.user.com', 'user1234')
            user = User.objects.create_user(*info)
            Token.objects.create(user=user)

            Pocket.objects.get(user_id=user.id, is_active=False).update(bank_account_type="NH", is_active=True)
            purchase = Purchase.objects.create(user_id=user, production=self.item)
            Participant.objects.create(user=user, post_id=self.post, purchase=purchase)

        # 200 OK test
        response = self.client.get(uri)
        self.assertEqual(response.data['data']['participant_count'], 3)
        self.assertEqual(response.data['data']['all_funding_amount'], 13500)
        self.assertEqual(response.data['data']['d_day'], self.fin_date.get_d_day())
        self.assertEqual(response.status_code, 200)

        # POST_DOES_NOT_EXIST test
        self.post.status='CANCEL'
        self.post.save()
        response = self.client.get(uri)
        self.assertEqual(response.data['status'], 'POST_DOES_NOT_EXIST')
        self.post.status='FUNDING'
        self.post.save()
