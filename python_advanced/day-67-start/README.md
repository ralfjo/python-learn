# 67일차 목표: 편집으로 RESTful한 블로그 구축하기!

우리가 얻은 지식을 활용해서 블로그를 더 발전시켜 보겠습니다. 더 많은 HTTP 경로를 추가해서 새로운 블로그 게시물을 만들고, 수정하고, 삭제할 수 있도록 해 볼 거예요. 그 모든 기능을 여러분의 블로그 웹 사이트 안에 넣는 거죠.
오늘 수업이 끝나고 나면 여러분의 블로그는 이러한 작업을 할 수 있게 될 겁니다.

# 시작 프로젝트 다운로드
1. Starting Files - RESTful-blog-start.zip 파일을 다운로드하세요.
2. 파일의 압축을 풀고 파이참에서 여세요.
3. 필요한 패키지를 모두 설치하고(임포트) 빨간색 밑줄이 없는지 확인하세요.
시작 파일은 posts.db라는 SQLite 데이터베이스로 이루어져 있으며, 이전에 데이터베이스를 만들었던 것과 같은 방식으로 만들어졌습니다. 또한 앞서 npoint JSON bucket에 저장된 모든 게시물을 추가해두었습니다.
4. DB 뷰어를 사용하여 데이터베이스를 살펴보고 데이터베이스의 필드를 숙지하시기 바랍니다.

# 요구 사항 1 - 블로그 게시물 항목을 가져올 수 있을 것
npoint JSON bin에서 블로그 게시물을 가져오는 대신에 시작 프로젝트에 포함된 posts.db SQLite 데이터베이스에서 게시물을 가져오세요.
참고: 시작 파일에서 requests.get() 메소드 호출은 주석 처리되어 있습니다. 즉, 앱을 실행할 때 홈 페이지(index.html)가 로드되지 않으며, posts가 없기 때문에 충돌하게 됩니다.
posts.db에서 블로그 게시물을 읽을 때 다음과 같이 표시되어야 합니다.
각 게시물 중 하나를 클릭하면 다음과 같이 표시됩니다.

해답
https://gist.github.com/angelabauer/eff89874dfbda23ac3ac1c51c618b6e1



# 요구 사항 2 - 신규 블로그 게시물을 게시할 수 있을 것
플라스크 서버에 /new-post라는 새 POST 경로를 만드세요.
1. '새 게시물 작성(Create New Post)' 버튼을 클릭하면 make-post.html 페이지가 표시되어야 합니다.
플라스크 CKEditor 패키지를 사용하여 WTForm의 블로그 콘텐츠(body)를 전체 CKEditor로 입력하는 방법을 알아야 합니다.

유용한 문서:
https://flask-ckeditor.readthedocs.io/en/latest/basic.html
https://pythonhosted.org/Flask-Bootstrap/forms.html
https://flask-wtf.readthedocs.io/en/stable/

예)
힌트 1: HTML 파일의 Jinja2 템플레이팅을 변경할 때마다 서버를 중지했다가 다시 실행해야 변경 사항이 적용됩니다.
해답
https://gist.github.com/angelabauer/e06ac346ed921142a5497bcfbe0e0e17

참고: 게시물 제출(Submit Post )' 버튼을 흰색 대신 파란색으로 하려면 button_map 매개변수를 wtf quickform에 추가하고 제출 필드를 부트스트랩 '기본' 버튼으로 만들면 됩니다.
문서: https://pythonhosted.org/Flask-Bootstrap/forms.html#form-macro-reference

부트스트랩 기본 버튼: https://getbootstrap.com/docs/4.0/components/buttons/
코드
https://gist.github.com/angelabauer/e7d8cc58a384da47a0f13e3bc5d6b5b1


2. 사용자가 모든 필드를 입력하면 폼의 데이터를 posts.db에 BlogPost 객체로 저장해야 합니다.
게시물이 저장되면 사용자는 홈페이지로 리디렉션되어야 하며, 저장 프로세스가 성공적으로 이루어진 경우 새 게시물이 표시되어야 합니다.
참고: 날짜는 서버의 datetime 모듈을 사용하여 자동으로 계산되어야 하기 때문에 WTForm에는 날짜 필드가 없습니다. 날짜는 다음과 같은 형식이어야 합니다.
August 31, 2019
<월(완전한 명칭)> <일>, <년>
문서:https://www.w3schools.com/python/python_datetime.asp
예)

해답
https://gist.github.com/angelabauer/3c582ce4bf1c667972641c7a49911614


참고: CKEditorField의 데이터는 HTML로 저장되며, 여기에는 블로그 게시물의 모든 구조와 스타일이 포함됩니다. 블로그 게시물의 post.html 페이지로 이동했을 때 이러한 구조가 반영되도록 하려면 Jinja safe() filter를 추가해야 합니다.
이렇게 하면 진자(Jinja)가 post.html 템플릿을 렌더링할 때 HTML을 텍스트로 처리하지 않게 됩니다.
진자 필터를 적용하려면 파이프 기호 '|'가 필요하며, 이 기호는 진자 표현식과 진자 필터 사이에 들어갑니다.
예) {‌{ Jinja 표현식 | Jinja 필터 }}

코드
https://gist.github.com/angelabauer/7dbf4554ebba5fcccc5197bc1b857b7e



# 요구 사항 3 - ​​기존 블로그 게시물을 편집할 수 있을 것
홈페이지에서 각 블로그 게시물을 클릭하면 해당 블로그 게시물의 post.html 페이지로 이동해야 합니다. 또한 게시물 끝에는 게시물 수정 버튼이 표시되며, 이 버튼을 클릭하면 make-post.html 페이지로 이동해야 합니다.
1. 새로운 경로 /edit-post/<post_id>를 생성합니다.
사용자가 블로그 게시물(post.html 페이지) 하단에 있는 '게시물 수정(Edit Post)' 버튼을 클릭하면 이 경로로 GET 요청이 이루어져야 합니다. 여기서 post_id는 읽고 있던 게시물의 id입니다.
사용자가 '새 게시물 작성(Create New Post)'에서 온 경우, <h1>은 '새 게시물(New Post)'을 읽어 들여야 하지만 사용자가 특정 블로그 게시물을 수정하려고 온 경우에는 '게시물 수정(Edit Post)'을 읽어 들여야 합니다.
예)
해답
https://gist.github.com/angelabauer/20715bb39cb3b2f824e0a3a282b5b9e5

2. make-post.html로 이동하면 블로그 게시물의 데이터로 WTForm의 필드가 자동으로 채워져야 합니다. 이렇게 하면 사용자가 블로그 게시물을 다시 입력할 필요가 없습니다.
이러한 작업은 폼 생성 시 post 객체의 속성을 전달함으로써 수행할 수 있습니다.

edit_form = CreatePostForm(
    title=post.title,
    subtitle=post.subtitle,
    img_url=post.img_url,
    author=post.author,
    body=post.body
)
코드
https://gist.github.com/angelabauer/f951a0c84f3197ad758a25a538801569

3. 사용자가 WTForm에서 수정을 마치고 '게시물 제출(Submit Post)'을 클릭하면 데이터베이스에서 게시물이 업데이트되어야 하며, 사용자는 해당 블로그 게시물의 post.html 페이지로 리디렉션되어야 합니다.
참고: HTML 폼(WTForms 포함)은 PUT, PATCH 또는 DELETE 메소드를 허용하지 않습니다. 따라서 이는 일반적으로 PUT 요청(기존 데이터 교체)이지만, HTML 폼에서 오는 요청이므로 수정된 게시물을 POST 요청으로 받아들여야 합니다.
또한 date 필드는 변경되어서는 안 되며, 수정된 날짜가 아닌 게시물이 최초 작성된 날짜가 표시되어야 합니다.
예시.
해답
https://gist.github.com/angelabauer/8e886bb17bc5e652a76aee2927d42d3d



# 요구 사항 4- 블로그 게시물을 삭제할 수 있을 것
1. index.html에서 각 게시물 옆에 ✘ 표시만 보여지는 앵커 태그를 만듭니다. (이 문서에 있는 ✘ 표시를 복사하여 넣어도 됩니다).
해당 표시를 클릭하면 데이터베이스에서 게시물이 삭제되고, 사용자가 홈페이지로 리디렉션되어야 합니다.
/delete/<post_id> 경로에 DELETE 경로를 생성해야 합니다.
예)
해답
https://gist.github.com/TheMuellenator/1877ebbb5fa0714e42405333c093d1eb
