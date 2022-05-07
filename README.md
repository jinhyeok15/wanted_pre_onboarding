# 원티드러닝 프리온보딩 백엔드 2차 코스 지원 과제

## Docs

### [Work Logs](docs/work.md)

### [서비스 분석 및 구현](docs/services.md)

## 활용 기술

### Language

* python 3.7

### Framework

* django
* django_restframework(DRF)

### Library

* PyJWT
* drf-yasg

### DB

* postgresql(RDS)

### Server

* (web) Nginx
* Docker
* (cache) redis

## 주요 개발 부분

* 모델 구조 재사용성을 위한 AbstractModel 활용

* 유저 토큰 기반 인증 구현

* 주석, 설명 상세화, swagger 기반 문서 Schema 작성 (Customizing)

* unittest 기반 API 개발. 선 test 후 view 작성

* JWT로 settings.py 보안 부분 token화 하여 ini파일로 관리.

* redis로 게시물 조회 부분 캐싱 -> 조회 속도 개선

* 데이터베이스 트랜잭션 처리

## 제출 필수 사항

* Github Repository 주소를 원티드 이력서 최하단 링크 섹션에 작성해 주세요.

* Repository 명은 “wanted_pre_onboarding” 으로 생성 합니다.

## wanted_pre_onboarding 과제안내

### * 과제설명

아래 서비스 개요 및 요구사항을 만족하는 Backend 시스템을 구현합니다.
Django 또는 Flask 를 사용하여 구현합니다.

### * 서비스 개요

본 서비스는 크라우드 펀딩 기능을 제공합니다. 게시자는 크라우드 펀딩을 받기위한 상품(=게시물)을 등록합니다.
유저는 해당 게시물의 펀딩하기 버튼을 클릭하여 해당 상품 ‘1회펀딩금액’ 만큼 펀딩합니다.

### * 요구사항

상품을 등록합니다.
제목, 게시자명, 상품설명, 목표금액, 펀딩종료일, 1회펀딩금액로 구성.

상품을 수정합니다.
단, 모든 내용이 수정 가능하나 '목표금액'은 수정이 불가능합니다.

상품을 삭제합니다.
DB에서 삭제됩니다.

상품 목록을 가져옵니다.
제목, 게시자명, 총펀딩금액, 달성률 및 D-day(펀딩 종료일까지) 가 포함되어야 합니다.
상품 검색 기능 구현
(상품 리스트 API 에 ?search=취미 조회 시 ,제목에  ‘내 취미 만들..’  ‘취미를 위한 ..’ 등 검색한 문자 포함된 상품 리스트만 조회)
상품 정렬 기능 구현
생성일기준, 총펀딩금액 두 가지 정렬이 가능해야합니다.
?order_by=생성일 / ?order_by=총펀딩금액
(달성률: 1,000,000원 목표금액 일때,  총 펀딩금액이 5,000,000원 이면 500%, 소수점 무시)

상품 상세 페이지를 가져옵니다.
제목, 게시자명, 총펀딩금액, 달성률, D-day(펀딩 종료일까지), 상품설명, 목표금액  및 참여자 수 가 포함되어야 합니다.

### * 필수 기술요건

Django ORM or SQLAlchemy 등 ORM을 사용하여 구현.
REST API 로 구현(Json response).
RDBMS 사용 (SQLite, PostgreSQL 등).
Backend 이외의 요소 개발 하지 않음(html, css, js 등)
개발 범위에 제외된다는 의미이며, 구현시에 불이익은 없습니다. 다만, 평가에 이점 또한 없습니다.

### * 평가 요소

코드 효율성
모델링
요구사항 구현정도
REST API 설계 적합성
코드 가독성 및 코드 컨벤션

### * 가산점 요소

Unit Test 구현
README 에 요구사항 분석 및 구현 과정을 작성
Git commit 메시지 컨벤션

### ※ 추가설명

요구사항 및 필수기술을 모두 구현하지 않더라도, 구현 정도에 따라 점수가 부여됩니다.
요구사항 이외 요소는 평가에 포함되지 않습니다. (인증, 권한 등)
