from drf_yasg import openapi
from drf_yasg.openapi import *
from drf_yasg.openapi import Parameter
from funding.apps.core.views import get_status_by_code
from funding.apps.shop.serializers import ShopPostSerializer


SHOP_POST_ITEM_CREATE_LOGIC = {
    "request_body": Schema(
        type=TYPE_OBJECT,
        properties={
            "title": Schema(title="제목", type=TYPE_STRING),
            "poster_name": Schema(
                title="게시자 이름",
                description="게시자 이름과 유저의 이름은 다를 수 있음",
                type=TYPE_STRING
            ),
            "content": Schema(
                title="펀딩 아이템 소개 컨텐츠",
                type=TYPE_STRING
            ),
            "target_amount": Schema(
                title="목표 금액",
                type=TYPE_INTEGER
            ),
            "final_date": Schema(
                title="종료일",
                type=TYPE_STRING
            ),
            "price": Schema(
                title="아이템 가격",
                type=TYPE_INTEGER
            )
        }
    ),
    "manual_parameters": [
        Parameter('Authorization', openapi.IN_HEADER, description="유저 토큰 -> Token {your token}", type=openapi.TYPE_STRING)
    ],
    "responses": {
        201: ShopPostSerializer,
        400: get_status_by_code(400)
    }
}