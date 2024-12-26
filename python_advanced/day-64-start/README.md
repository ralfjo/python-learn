64일차 목표: 우리가 구축할 것
역대 최고의 인기 영화 목록을 집계하는 웹 사이트를 본 적이 있나요?

예)

영국영화협회(British Film Institute): https://www2.bfi.org.uk/greatest-films-all-time

엠파이어매거진: https://www.empireonline.com/movies/features/best-movies-2/

뉴욕타임스: https://www.imdb.com/list/ls058705802/

실로 사람들이 좋아하는 것을 목록으로 만들 수 있도록 돕는 비즈니스를 전문적으로 하는 회사들이 있습니다.

예)

https://www.listchallenges.com/

오늘 수업에서는 플라스크/WTForms/SQ 라이트/SQL 알케미 등을 사용하여 그런 웹 사이트를 만들어 보려고 합니다. 이러한 애플리케이션을 통해 역대 최고의 영화 10편을 꼽는 웹 사이트를 만들고, 앞으로 보는 영화를 목록에 업데이트하고 사람들에게 추천할 영화를 관리할 수 있도록 해보겠습니다.

예)


요구 사항 1 - 영화 목록 항목을 볼 수 있을 것
홈페이지를 방문했을 때 아래와 같은 화면이 보이는 것을 목표로 합니다.





이러한 목표를 달성하려면 다음과 같은 작업을 해야 합니다.

1. SQL 알케미를 사용하여 SQ 라이트 데이터베이스를 만듭니다. 데이터베이스에는 'Movie'라는 이름의 표가 있어야 하며, 이 표에는 다음의 필드가 포함되어야 합니다.

id 
title 
year 
description 
rating 
ranking
review
img_url


2. 코드/DB Viewer를 사용하여 다음 값으로 데이터베이스에 새 항목을 추가합니다.

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
힌트: 코드를 한 번 실행한 후 2단계에서 추가 입력된 코드를 제거해야 합니다. 그렇지 않으면 다음과 같은 메시지가 뜰 수 있습니다.






3. 데이터베이스의 각 항목이 홈페이지에 올바르게 표시되도록 코드를 작성합니다.

각각의 데이터가 어떻게 표시되는지 확인하세요.

앞면:


뒷면:




해답
https://gist.github.com/angelabauer/66fdff2a3aaf38c75a6c18c50499f32d



요구 사항 2 - 영화 등급 및 리뷰를 수정할 수 있을 것
영화 카드 뒷면에는 수정 버튼이 있고, 이 버튼을 클릭하여 평점과 리뷰를 변경할 수 있어야 합니다.

예)




1. WTForms에 대해 배운 내용을 활용해서 RateMovieForm을 만들고 이를 사용하여 edit.html에서 렌더링할 Quick Form을 생성합니다.

참고: edit.html의 코드는 변경할 필요 없습니다. 학생들이 단순 HTML 양식을 작성하지 않도록 하기 위해, Quick Form을 렌더링하는 데 필요한 모든 것을 사전에 마련해 두었습니다.

WTForms 사용법을 잊어버린 경우 이전 수업으로 돌아가서 복습하거나 다음 링크의 문서를 참고하시기 바랍니다.

https://pythonhosted.org/Flask-Bootstrap/forms.html

https://wtforms.readthedocs.io/en/2.3.x/

https://flask-wtf.readthedocs.io/en/stable/



2. 폼을 제출하고 유효성을 검사한 다음에는 데이터베이스의 해당 영화 항목에 업데이트 사항을 추가합니다. SQL 알케미에 관한 보다 자세한 내용은 다음의 링크에서 확인할 수 있습니다.

https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application



해답
https://gist.github.com/angelabauer/8534bff2eceda9870d489a6719805aa2



요구 사항 3 - ​​데이터베이스에서 영화를 삭제할 수 있을 것
각 영화 카드의 뒷면에는 삭제 버튼도 있어야 하며, 이 버튼을 클릭하면 데이터베이스에서 영화 항목을 삭제할 수 있어야 합니다.

예)

해답
https://gist.github.com/angelabauer/206a8e2ab705157426385f86d8a7d5d0


요구 사항 4 - 페이지 추가를 통해 새 영화를 추가할 수 있을 것
앞에서는 하드코딩된 코드 조각이나 DB 뷰어를 사용하여 데이터베이스에 새 항목을 추가했으나, 이번에는 이러한 작업을 수행할 수 없는 사용자를 위해 추가 페이지가 작동시킴으로써 영화를 추가하고 API를 사용하여 포스터 이미지, 출시 연도, 영화 설명을 가져올 수 있도록 해야 합니다.

1. 홈페이지에서 ‘영화 추가(Add Movie)’ 버튼을 클릭하면 추가 페이지가 렌더링되도록 합니다. 추가 페이지에는 영화 제목이라는 1개의 필드만 포함된 WTF quick form이 표시되어야 합니다.

예)


해답
https://gist.github.com/angelabauer/ae6154dffa3f502c2a480bd9cce9705f


2. 사용자가 영화 제목을 입력하고 '영화 추가'를 클릭하면 플라스크 서버가 해당 영화 제목을 수신해야 합니다. 그런 다음 요청 라이브러리를 사용하여 해당 제목과 일치하는 모든 영화에 대해 The Movie Database API를 요청 및 검색해야 합니다.

영화 데이터베이스(Movie Database)에 무료 계정을 등록합니다.

그런 다음 설정 -> API로 가서 API 키를 받고, 해당 API 키를 프로젝트에 복사합니다.




검색 쿼리를 만들어 영화 데이터를 요청하는 방법은 영화 데이터베이스에 있는 문서를 참고하세요.

https://developers.themoviedb.org/3/search/search-movies

힌트 1: API 문서의 '테스트해보기(Try it out)' 탭은 요청의 구조와 예상 반환 데이터를 확인하는 데 특히 유용합니다.

힌트 2: API 요청 방법은 지난 33일차 수업에서 다루었습니다. 이 부분에서 막혔다면 해당 수업을 복습해보세요.



API에서 얻은 데이터를 사용하여 select.html 페이지를 렌더링하고 모든 영화 제목과 개봉 연도를 페이지에 추가해야 합니다. 이런 방법으로 사용자는 추가할 영화를 선택할 수 있는데, 보통 비슷한 제목의 영화가 여러 편 있습니다.

예)




해답
https://gist.github.com/angelabauer/d6bec8eec3420ac9632a96d1ac5857b6


3. 사용자가 select.html 페이지에서 특정 영화를 선택하면 해당 영화 ID를 사용하여 영화 데이터베이스 API의 다른 경로가 요청되어 해당 영화에 대한 모든 데이터(예: 포스터 이미지 URL)를 가져올 수 있어야 합니다.

get-movie-details 경로를 요청하기 위해 사용자가 선택한 영화의 id를 사용합니다.

https://developers.themoviedb.org/3/movies/get-movie-details

API에서 얻은 데이터는 데이터베이스를 새 항목으로 채우는 데 사용되어야 하며, 채워야 하는 속성은 다음과 같습니다.

제목 (title)

이미지 URL (img_url)

개봉연도 (year)

설명 (description)

항목이 추가되면 홈페이지로 리디렉션되며 새 영화가 카드로 표시되어야 합니다. 일부 누락된 데이터가 있을 텐데 괜찮습니다.

예)




해답
https://gist.github.com/angelabauer/daf0f55d7ed2034ab07be56e345a8471


4. 올바른 영화를 찾은 다음에는 영화 항목에서 평점과 리뷰가 누락되었으므로 홈페이지로 리디렉션하는 대신 edit.html 페이지로 리디렉션합니다. 수정 페이지 폼에는 이 두 필드가 포함되도록 하고, 새로운 데이터로 데이터베이스의 영화 항목을 업데이트합니다.

예)




요구 사항 5 - 영화를 등급별로 정렬하고 순위를 매길 수 있을 것
현재 영화 카드의 앞면에는 ‘없음’이라고 큰 글씨로 쓰여 있습니다.

아래의 예시와 같이 이 부분에 '없음'이 아닌 평점에 따른 영화의 순위를 표시하고자 합니다.

현재까지 추가한 영화가 '매트릭스(The Matrix)'와 '센과 치히로의 행방불명(Spirited Away)' 뿐이고 해당 영화에 각각 평점 9.2와 9.5를 부여했다면 다음과 같이 표시되어야 합니다.




이후 추가한 다른 영화가 가장 높은 평점을 받은 경우 해당 평점에 따라 순위가 매겨져야 합니다.

예를 들면, 매트릭스(9.3), 센과 치히로의 행방불명(9.5), 기생충(9.9)이었으나,


평점을 수정하여 매트릭스(9.3), 센과 치히로의 행방불명(9.5), 기생충(8.9)가 된 경우,

다음과 같이 되어야 합니다.




힌트 1: https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.order_by

힌트 2: index.html의 코드는 변경할 필요 없습니다.

힌트 3: home()함수의 코드만 변경하면 됩니다.



해답
https://gist.github.com/TheMuellenator/5dc0b3a6147e93d82147869990bca02a


이 강의의 학습자료에서 완성된 프로젝트를 다운로드하실 수 있습니다.