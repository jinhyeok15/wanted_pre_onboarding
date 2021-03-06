# Logs

## 4.18

+ 환경세팅 및 MarkDown 정리
+ RDS 설정
+ S3 conf.ini 업로드
+ 세팅 확인
+ swagger 문서 연결하기
+ profile UserModel test case 작성
+ app 올리기 +profile +user && model 작성하기 => User

## 4.19

+ model 구조 설계
+ 상품 등록 test case 작성
+ 서비스 분석 부분 추가 && md 파일 구조 수정
+ Pocket model 생성 && User 등록시 Pocket 자동 생성

## 4.20

+ signup API
+ POST shop/post/

## 4.21

+ authentification mixin 설계
+ abstract -> core로 변경
+ core/models 모듈 구분 abstract/interface/dummy
+ serializer validation mixin 설계 -> django ValidationError로 validate 할 수 있도록
+ views class 명 뒤에 View 붙이기

## 4.22

+ Response 관련 core view 설계 && ShopPostItemView 리팩토링
+ PostItemView -> ShopPostItemView 변경

## 4.23

+ docs 정리 및 주석 구체화 && 4xx, 5xx errors response 반영
+ date validation
+ POST shop/post/ response 부분 변경 && swagger_auto_schema 부분 모듈화 작업

## 4.25

+ ShopPost item, poster populate하기

## 4.27

+ models refactoring && test case 수정 (test_create_item_post case 추가)
+ exceptions에 DateValidationError 추가

## 4.28

+ POST shop/v1/post v1.0.0 update
+ user pocket validation 추가

## 4.30

+ GET shop/v1/:post_id/want_participate/ update

## 5.1

+ POST shop/v1/:post_id/participate/ 개발
+ mixins refactoring

## 5.2

+ GET shop/v1/post/:post_id

## 5.3

+ PATCH shop/v1/post/:post_id
+ DELETE shop/v1/post/:post_id

## 5.7

+ GET shop/v1/posts/

## 5.10

+ item price 조회시 구분쉼표로 표시 -> components.money 자료형 추가
+ price 관련 serializer method 수정
+ 0 division error validation

## 5.16

+ date type에서 sorting관련 함수 임시로 만들고 unittest 통과시키기

## 5.17

+ all_funding_amount로 정렬할 때, compare메소드를 통해 sorting할 것
  + component의 base를 만들고, base는 abcmethod로 implement 규격화 시키기

## 5.24

+ 정렬시 status 우선 순위 고려, FUNDING->SUCCESS->CLOSE

## 5.25

+ cashing할 때, search 쿼리가 작동하지 않는 버그 수정하기
- 배치 프로그래밍 by https://cholol.tistory.com/531

- settings에 pagination 설정 지정하기
- login
- PostFigure 모델 설계
- post 생성, 조회 부분 수정
- admin 페이지 개발
- django-jenkins by https://django-jenkins.readthedocs.io/en/latest/
- social login - kakao, google, apple
- post comment 기능 추가
