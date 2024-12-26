문의 양식

어제는 부트스트랩으로 스타일링하여 업그레이드 버전의 블로그 웹사이트를 만들었습니다. 이 웹사이트에서 CONTACT 페이지의 문의 양식만 아직 동작이 되지 않죠. 문의 양식을 완성하려면, HTML 입력양식을 제출하고, 제출한 데이터를 플라스크 서버에서 받는 방법에 대해 배워야 합니다.

플라스크에서 HTML 입력양식
오늘의 목표는 HTML 입력양식을 제출하고, 사용자가 입력한 데이터를 이메일로 받는 방법을 이해하는 것입니다.

예)


결과:

HTML 입력양식 변경 - 입력양식 직접 만들기
1. 새 파이참 프로젝트 html-forms를 생성하세요. 프로젝트 안에 main.py와 index.html이 있어야 합니다.

2. 새 플라스크 애플리케이션을 만들고 index.html 페이지를 렌더링 하여 브라우저에 표시합니다. index.html 파일에 <h1>을 추가하여 제대로 동작하는지 확인하세요.

3. 과제: index.html에 HTML 입력양식을 만들어 웹페이지로 렌더링 했을 때 다음과 같이 나오게 하세요.

해답:

https://gist.github.com/angelabauer/81c9f4512a14c3cb04ba03540888875d



플라스크 서버로 POST 요청 처리하기
입력양식을 만들었으니, 이제 동작을 시켜야 합니다. 사용자가 입력한 데이터를 받을 수 있도록 플라스크 서버가 필요합니다


지금은 양식을 채우고 ‘Ok’ 버튼을 눌러도 아무 반응이 없죠.

입력된 데이터를 전송하려면 HTML 입력양식을 변경해야 합니다. action과 method가 있어야 해요.



1. 과제: 아래 문서를 참고하여, HTML 입력양식에 입력된 데이터를 "POST" 요청 방식으로 "/login" 경로에 전달하는 방법을 알아보세요.

https://www.w3schools.com/tags/att_form_method.asp

https://www.w3schools.com/tags/att_form_action.asp



해답: https://gist.github.com/angelabauer/889ac7cfdfed5cfeb79559f41c9c6a07



2. 입력양식을 제출했으면, 서버에서 이 POST 요청을 받아야 합니다. 그러려면 먼저 입력양식의 각 입력 값에 name 속성이 있어야 해요.




3. 이제 POST 요청을 받았을 때, 이 요청을 처리하도록 데코레이터를 main.py 안에 만들면 됩니다.


methods 매개변수는 딕셔너리 형으로 쓸 수 있으므로 하나의 제출 경로에 메소드 방식은 여러 개 있을 수 있습니다. 예)

@app.route("/contact", methods=["GET", "POST"]

더 많은 정보는 아래 문서를 참고하세요.https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods



4. 플라스크에는 서버로 전송된 요청 매개변수를 활용할 수 있는 request 메소드(요청 모듈과 혼동하지 마세요)가 있습니다.

💪 어려운 과제: 아래 플라스크 문서를 참고하여, 양식에 입력된 이름과 비밀번호를 다시 클라이언트로 보내어 <h1>으로 출력하세요. 예)


문서:

https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object

힌트:

https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask

해답은 다음 강의에 있습니다.


플라스크 서버로 POST 요청 처리 솔루션
플라스크 요청(Request) 객체
과제를 수행하려면 request 객체를 사용해야 합니다. 플라스크 문서를 적극 활용하여 과제를 해결하세요.



해답 코드:

https://gist.github.com/angelabauer/045264ca6ad168b986f6687ee1368078



해답 풀이:




주의: 입력양식의 action 속성은 "/login"으로 설정할 수 있습니다. 예)

<form action="/login" method="post">
혹은 url_for를 사용하여 동적으로 생성할 수도 있습니다. 예)

<form action="{‌{ url_for('receive_data') }}" method="post">
서버가 호스트 되는 장치에 따라 "/login" 경로가 바뀔 수 있습니다. 그러므로 여러분의 플라스크 서버에서 특정 기능을 위한 URL을 url_for을 사용하여 동적으로 생성하는 것이 좋습니다.



문의 양식이 작동하도록 하기
양식에 입력된 데이터를 플라스크 서버에서 받는 방법을 봤습니다. 이제 블로그 웹사이트에 배운 내용을 적용해 봅시다.

1. 이 강의의 자료에서 starting  코드를 다운로드하세요. 59일의 ending  코드와 동일하지만 약간의 차이가 있습니다. html 양식을 main.py에 더 쉽게 연결할 수 있도록 contact.html이 단순화되었습니다.

2. 양식에 입력된 데이터를 받기 위해 main.py에서 "/form-entry" 경로를 추가하세요.


3. 과제: contact.html과 main.py의 코드를 업데이트하여, 사용자가 입력한 정보를 콘솔에 출력하고, 사용자에게 ‘메시지를 성공적으로 보냈습니다’라는 <h1>을 표시하세요. 예)


해답:

https://gist.github.com/angelabauer/97e23a7e6a044413ec3ed76456fd1c2e



4. 과제: ‘/form-entry’를 ‘/contact’ 경로로 통합하여, 같은 ‘/contact’ 경로에서 메소드 방식(GET/POST)에 따라 올바르게 요청을 처리하세요.

힌트: request.method를 사용하여 어떤 메소드 방식으로 해당 경로에 데이터가 전달되었는지 확인할 수 있습니다.

https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods

다음과 같이 동작해야 합니다.


해답:

https://gist.github.com/angelabauer/bcb90f5060fe7204814da3249b069b7b



5. 과제: ‘메시지를 성공적으로 보냈습니다’를 contact.html 파일의 <h1>으로 출력하도록 변경하세요.

힌트: https://jinja.palletsprojects.com/en/2.11.x/templates/#if

다음과 같이 동작해야 합니다.


해답: https://gist.github.com/angelabauer/4db9f611e8b11a86021dc2eb6cdc61e7

Resources for this lecture



smtplib로 이메일 전송하기
32일차에서 smtplib를 이용한 이메일 전송 방법에 대해 배웠습니다. 이 지식을 활용하여 사용자가 문의하기를 원할 때, 실제로 여러분(웹사이트 관리자)에게 이메일을 보내어 문의 기능을 완성해 보세요.

필요하다면 32일차의 smtplib 관련 강의를 복습하세요.

다음과 같이 동작해야 합니다.


해답:

https://gist.github.com/angelabauer/6e9dec2b75b3d6b4b5f2feed011a0d13


