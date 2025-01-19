# Django 기본

project 추가
```
django-admin startproject myproject
```

디렉토리
```
- mysite
  - manage.py       (가장 자주 사용하는 파일 중 하나, 서버 구동 등...)
  - mysite
    - settings.py   (프로젝트 내 환경 구성 등 여러 설정 정보를 담고 있음)
    - urls.py       (URL 패턴 등 패스 관련 여러 정보를 담고 있음)
                    (일단 위 2개가 중요한 파일 --> 자주 사용되는 파일)
```

django start
```
python manage.py runserver (기본 8000번 포트 서버 구동)
python manage.py runserver 8080 (포트변경)
```

기본 테이블 생성
```
python manage.py migrate
```

super user  생성
```
python manage.py createsuperuser
```

# 개념
Framework (모델-뷰-컨트롤러)
VirtualEnvironment
Project vs App
Model
- 모델은 곧 데이터(데이터베이스)
- 모델을 이용하여 데이터 및 데이터베이스 연동 작업을 처리
- DB를 건드리지 않고 코딩만으로 DB 작업을 처리
- 장고의 모델을 사용하면 기존의 SQL 쿼리문과 같은 것 없이 데이터 처리 및 DB 연동 작업을 할 수 있다.
MVC
MVT
```
HTTP 요청 -> 요청 받음 -> URL conf -> 뷰를 결정 (url.py) -> 메소드 실행 (views.py) -> templates (render) -> html 리턴
```

# App 생성하기
app 추가
```
python manage.py startapp onememos
```

app 폴더 생성 및 파일들
```
- migrations (폴더)
- admin.py
- views.py
- models.py
- urls.py   (별도로 수동 생성해줘야 하는 파일. 최상위 URLconf 와의 연결을 위하여 필요. 최상위 urls.py 파일에 있음)
            (사용자가 브라우저에 어떤 내용을 입력하고 들어올 요청에 대해서 어떤 뷰를 연결해서 보여줄 것인지 그런 내용을 작성해줘야함)
```

최상 urls.py --> urlpatterns --> 앱패스 추가
```
- path('onmemos/', 어떤걸(View) 호출??),  --> include('onememos.urls')  ## include 임포트 했는지 확인. 안하면 서버 구동 시 에러
- path('onmemos/', include('onememos.urls')),
- path('admin/', admin.site.urls),
```

include() 함수
- 다른 URLconf 패스들을 참조할 수 있도록 해주는 함수. 앱 구동 및 연결 시 중요한 역할을 하는 함수.


# 테이블 생성하기
장고 프로젝트에서 어플리케이션(App)을 생성하고, 여러 데이터 값들을 저장하기 위해서 --> 모델(models)
이 모델을 사용하여 테이블을 생성하고, 데이터를 어떻게 처리하는지에 대해서 학습

python manage.py migrate --> 실행 --> 프로젝트 생성 시 필요한 기본적인 테이블, 앱들이 설치.
이렇게 설치된 앱들은 어디? --> 환경설정폴더(myproject or config)/setting.py 파일에서 확인

어떤 프로그램(APP)을 만들 때 데이터가 저장되고 관리되는 것이 필요한데 이러한걸 처리하기 위한 모델(표본)이 필요하다.
이러한 모델 --> 데이터 모델 or 데이터베이스 모델
한 줄 메모장
- 한줄 메모장에 필요한 데이터 모델이 필요
- 어떤 필드(컬럼)들이 필요하고, 또 각각의 필드 타입은 어떻게 정할까?
- 이렇게해서 만들어진 데이터 모델 --> 테이블

최소한의 필요한 것 위주로 데이터 모델을 만든다면?
idx (정수형)
memo_text (문자형)
published_date (날짜형)

작성 후 --> 반영을 위해서 --> 어디에? --> Admin 사이트에 반영 --> admin.py 열고 추가 작성.
마지막으로 migrate 하기 전에 2가지 작업을 해야 함
- 최상위 폴더 settings.py에 app을 등록 INSTALLED_APPS
- makemigration 진행 --> migrations 폴더와 관련, 이행할 소스등을 만들어놔라

# urlpatterns 정리
- 슬래시(/)는 기본적으로 장고가 알아서 하기는 하지만 특별한 경우가 아니라면 붙여주도록 하자.
- 마지막단의 , 도 생략해도 되고 붙여도 된다.
- 초기화면 view.index 또는 views.main 등으로 해도 된다.

# render 함수와 template 파일의 관계
- render 함수 - 웹사이트 개발 시 파이썬 코드와 데이터를 템플릿 파일로 만들어주는 함수. (쉽게말해 HTML로 변환해서 적용해주는 함수)
- 결국 리턴은 HTML 파일로 리턴
- 이렇게 HTML 파일로 리턴한 것을 --> 템플릿 또는 템플릿 파일
- 그러나 템플릿 파일이 HTML 파일은 아니다.
- 이러한 템플릿 파일은 대부분의 프레임워크에서도 마찬가지인데 프레임워크 전용 파일의 개념.
- 즉, 장고에서만 사용할 수 있는 문법 (템플릿 문법 태그) 등을 이러한 템플릿에 적용 --> 일반 HTML 파일 X
- 당연히 템플릿도 규칙과 최소한의 문법(템플릿 태그라 불리우는 것들)이 존재
- 조건 처리, 반복 처리 등이 가능 --> 얼핏 프로그래밍 언어처럼도 보이나 --> 언어라기 보다는 템플릿 전용 표현 언어쯤

템플릿 폴더 만들기
- 첫번째, 프로젝트 루트 폴더에 templates 폴더를 만들어서 사용 ---> settings.py --> 템플릿 경로 추가하여 사용
- 두번째, 생성한 앱(App)쪽 바로 하위에다가 --> templates 폴더를 만들어서 사용 --> App별로 템플릿 사용이 가능 (환경설정 필요 없음)
- 정리하면, 장고는 템플릿 폴더를 인식하는 방식이 여러가지이다.

앞으로
- 뷰페이지 템플릿 꾸미기(Form) --> 입력과 출력
- 템플릿 파일의 목적 (용도)
    - 뷰페이지 처리 --> 템플릿 파일
    - 개발과 디자인의 분리
    - 개발자 코드 vs 디자인 코드 (HTML, CSS)
    - 다른 프레임워크들에서도 보통 template(s) 이라는 폴더명을 만들어서 템플릿 폴더로 인식시켜서 사용.
    - 아무튼 디자이너(뷰페이지 담당자) 입장에서는 템플릿 언어의 고유문법이나 태그들을 배워야함
- 관리자 모드에서의 DB 조작 vs CMD 명령 프롬프트에서의 DB 조작(dbshell)
    - 이 과정에서 오류가 발생하곤 한다 --> 이때 --> 어떻게 처리해줘야 하는지에 대해서 체크.
    - sqlite tool 설치가 안되서 나는 오류.
    python manage.py dbshell
- 꾸민 폼 페이지에서 한줄 메모 작성 --> DB에 입력 및 출력

CSRF (cross site request forgeries)
- 특정 사용자가 마치 접속하여 요청값을 보낸 것처럼 글 작성.
- 즉, 위조된(가짜의) 요청 액션을 보내 악의적으로 요청을 이용하는 행위
- 예를들면, iframe 등을 몰래 삽입하여 로그인한 사용자가 본인도 모르게 글 작성을 요청 넣는 것처럼 하는 행위
장고 대비책:
- 방법은 여러가지 --> token 이용
- csrf_token 발급은 값이 매번 변경 -> 전송된 토큰을 통해 -> 뷰가 호출되기 전 유효성 검증
- POST 방식을 사용하는 템플릿 form 태그쪽에 {% csrf_token %} -> 템플릿 태그 사용


# 리다이렉트
- 임포트 필요 - HttpResponseRedirect, reverse
- redirect() 함수란?
    - view 페이지 등에서 특정 로직 수행 후 다시 특정 url로 이동시키고자 할 때 사용
- reverse() 함수란?
    - URL을 역으로 계산 --> path 가 변경되어도 --> url을 외울 필요 X
    - urls.py에서 만든 urlpatterns 들의 name을 사용
    - name을 통해서 해당 name의 url을 반환
    - name 정보가 틀리면 페이지 에러 발생

# 리스트뷰(출력) 처리를 위해서
- 제일 먼저 생각? --> main(=index) 함수를 수정 --> 출력
- 기존 --> 그냥 메인 페이지용 템플릿 파일을 요청 시 --> 보여주기만 하면 되었지만, 지금은 DB에서 전체 글 목록을 가져와서 뿌려줘야 한다.
- main 함수 내에서 DB로 부터 전체 글 목록을 가져와서 --> 템플릿 파일로 --> 전달 (변수)
    반드시 딕셔너리 타입으로 만들어서 data 변수를 --> 템플릿 파일로 전달 --> 안그러면 에러 발생.
    이때 all() 메서드를 사용 --> 글 목록 전체를 가져올 수 있다.
    아티클 하나하나를 객체(obejct)라고 생각.
    Memo.objects.all()
- 템플릿 문법 (태그)
    - {% %} - 반복처리, 조건처리 등등 - 이러한 템플릿 테그를 이용하여 안쪽에 파이썬 문법을 사용
        - main 함수에서 전달 -> data 변수 (딕셔너리) -> 딕셔너리 변수 이름인 data로 전달했다해서 -> 사용하나?
        - 직접적인 딕셔너리 이름(data)를 사용하지 않고 -> 키(key)를 사용 -> lists
        - 즉, key(=lists) 이름을 통해서 value 값에 접근
    - {{ }} - 객체를 출력할 때 사용
        - 1번의 템플릿 태그가 반복 처리나 조건 처리 등을 위해서 사용한다면,
        - 2번의 템플릿 태그는 데이터 값을 화면에 출력할 때 사용
        - 반복 처리 시 하나하나의 item (=article, object) 항목에 들어있는 속성 값을 꺼내서 화면에 출력시키고자 할 때 사용

