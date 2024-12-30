# 63일차 목표: 가상 책장 만들기

내가 읽은 책을 기록하고 각각의 책에 평점을 매기고 싶었던 적이 있나요?
사실 이는 새로운 발상은 아닙니다. 이미 이런 목적으로 무언가를 구축한 많은 회사가 있죠.
그중 한 예가 https://www.librarything.com/입니다.
하지만 그러기 위해서는 데이터베이스를 사용하는 방법을 배워야 하죠. 오늘 수업에서는 SQ 라이트 데이터베이스를 생성하는 방법과 데이터베이스에서 데이터를 생성, 읽기, 업데이트, 삭제하는 방법을 배워보겠습니다.
아울러 필요할 때마다 데이터를 제공할 수 있도록 데이터베이스를 Flask 애플리케이션과 연결해보도록 하겠습니다.
그럼 안전벨트를 매고 다음 수업으로 출발하세요!

시작 프로젝트 다운로드
1. 아래의 Starting+Files+-+library-start.zip 파일을 다운로드하세요.
2. 파일의 압축을 풀고 파이참에서 여세요.
3. 필요한 패키지가 모두 오류 없이 설치되었는지 확인하세요.

웹사이트 작동시키기
다음 요구 사항이 충족될 수 있도록 main.py index.html 및 add.html을 코딩하세요.

도전 과제 1
http://locahost:5000(또는 main.py를 실행할 때 URL로 표시되는 모든 항목)로 이동하면 '내 라이브러리(My Library)'라고 표시된 <h1>이 있어야 하며, '새 책 추가(Add New Book)'를 위한 링크 <a>가 있어야 합니다.

해답 1 - https://gist.github.com/angelabauer/4e303378383f2b847361740ce6e59997


도전 과제 2
/add 경로(예: http: // locahost:5000/add)로 이동하면, 아래와 같은 폼이 표시되어야 합니다.

해답 2 - https://gist.github.com/angelabauer/3def76077443db8d184fb741fa6141e3


도전 과제 3
'책 추가'를 클릭하면 main.py에서 all_books라는 목록에 책 세부 정보가 사전으로 추가될 수 있도록 /add 경로의 폼을 만듭니다.
all_books의 데이터 구조는 다음 예시와 같은 사전 목록 객체여야 합니다.

all_books = [
     {
        "title": "Harry Potter",
        "author": "J. K. Rowling",
        "rating": 9,
    }
]
해답 3
https://gist.github.com/angelabauer/a61522818d3688730ddd8170f42e0635


도전 과제 4
홈페이지상에서  all_books의 각각의 도서가 순서가 없는 목록 <ul> 내에 항목 <li>로 홈페이지에 표시되도록 합니다.

예시.

해답 4 - https://gist.github.com/angelabauer/03d622f7ad854602a019ac117ad4b83d


도전 과제 5
책이 없는 경우 홈페이지에 <p>Library is empty.</p>라고 표시되도록 합니다. 또한 '새 책 추가' 링크가 제대로 작동하여 사용자를 /add 페이지로 이동시킬 수 있도록 합니다.

힌트: 책이 없는 경우 all_books = []

해답 5 - https://gist.github.com/angelabauer/de2f3faa28586ca970032f9249f2b310




# 서버를 갱신하면 어떻게 될까?
웹 사이트에 책 몇 권을 추가하세요. 추가된 책이 홈페이지상의 목록에 표시되어야 합니다.
이제 파이참에서 정지 버튼을 눌러 서버를 정지시키세요.
그런 다음 서버를 다시 실행하세요.
웹 사이트로 이동하여 홈페이지를 새로고침하세요. 무엇을 볼 수 있으며, 여러분의 책은 어떻게 되었나요?
이는 책이 현재 List all_books에 저장되어 있는 관계로 main.py를 재실행하면 이 변수가 다시 초기화되고 내부에 있는 모든 데이터가 손실되기 때문입니다.
만약 사용자 데이터에 이런 일이 발생했다면 사용자들이 웹 사이트를 신뢰할 수 없게 됩니다.
이러한 문제를 해결하려면 데이터 영속성과 플라스크 애플리케이션에서 데이터베이스를 사용하는 방법을 배워야 합니다.

# SQLite 데이터베이스
먼저 데이터베이스를 만들어 보겠습니다. 전 세계에서 가장 많이 사용되는 데이터베이스는 SQ 라이트이며, 모든 파이썬 설치에 기본적으로 포함되어 있을 정도로 인기가 높으므로 파이썬 프로젝트를 생성할 경우에는 이미 설치된 상태라고 보시면 됩니다. 그럼 책 데이터를 저장할 SQ 라이트 데이터베이스를 만들어 봅시다.
1. 새 프로젝트를 만들고 main.py 파일 내에서 sqlite3 모듈을 가져옵니다.
import sqlite3
2. 이제 새 데이터베이스에 대한 연결을 생성합니다(데이터베이스가 존재하지 않는 경우 생성됨).
db = sqlite3.connect("books-collection.db")
3. main.py를 실행하면 books-collection.db라는 새 파일이 파이참에 표시되어야 합니다.
참고: .db 파일은 파이참에서는 작동하지 않으니 열지 마세요. 해당 파일을 열 수 있는 소프트웨어를 다운로드하는 방법은 잠시 후에 알려 드리겠습니다.
4. 다음에는 데이터베이스를 제어하는 커서를 만들어야 합니다.
cursor = db.cursor()
커서는 마우스 또는 포인터라고도 합니다. 엑셀이나 구글 시트에서 작업하는 경우 커서를 사용하여 데이터 행을 추가하거나 데이터를 편집/삭제하며, SQ 라이트 데이터베이스를 수정할 때도 커서가 필요합니다.
데이터베이스에 표 만들기
엑셀에 대한 이야기로 돌아가 보면, 단일 엑셀 파일에는 여러 개의 표가(시트)이 포함될 수 있으며 각 탭은 별도의 표가 됩니다.
이와 마찬가지로 데이터베이스에도 많은 표가 포함될 수 있습니다.
5. 표를 하나 만들어 봅시다. 앞서 작성한 모든 줄 아래에 다음과 같은 코드를 추가합니다.

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
하나씩 살펴보겠습니다.
cursor - 4단계에서 생성한 커서는 데이터베이스의 마우스 포인터로서 모든 작업을 수행하게 됩니다.
.execute() - 이 메소드는 커서가 작업을 실행하도록 명령합니다. SQ 라이트 데이터베이스의 모든 작업은 구조화 질의어(SQL, Structured Query Language)라는 명령어로 표현되는데, 이는 키워드가 모두 대문자로 쓰인 영어 문장과 비슷합니다. SQL 명령어는 상당히 많지만 외울 필요는 없으니 걱정 마세요.
CREATE TABLE -  - 데이터베이스에 새 표를 생성하는 키워드로 이 뒤에 표 이름이 오게 됩니다.
관련 문서: https://www.w3schools.com/sql/sql_ref_create_table.asp
books -  생성 중인 새 표에 우리가 부여한 이름입니다.
() -  CREATE TABLE books ( ) 다음의 괄호 안에 들어가는 부분은 이 표의 필드입니다. 또는 엑셀 시트의 열 제목이라고 생각하면 됩니다.
id INTEGER PRIMARY KEY - 'id'라고 불리는 첫 번째 필드로서 데이터 유형이 INTEGER이고 이 표의 PRIMARY KEY가 됩니다. 기본키(primary key)는 표에서 이 레코드를 고유하게 식별하는 데이터 중 일부입니다. 예를 들어 한 국가 내에서 동일한 여권 번호를 가진 사람은 없기 때문에 사람의 기본 키는 여권 번호가 될 수 있습니다.
title varchar(250) NOT NULL UNIQUE - 두 번째 필드로 '제목(title)'이라고 합니다. 문자로 구성된 가변 길이 문자열이 허용되며, 괄호 안의 250은 최대 텍스트 길이입니다. NOT NULL은 값이 있어야 하며 비워 둘 수 없음을 의미합니다. 또한, UNIQUE는 이 표의 두 레코드가 동일한 제목을 가질 수 없음을 의미합니다.
author varchar(250) NOT NULL - author라고 불리는 필드로 최대 250자의 작성자 가변 길이 문자열이 허용되며 비워 둘 수 없습니다.
rating FLOAT NOT NULL - rating이라는 필드로 실수형(FLOAT) 데이터 유형 숫자가 허용되며 비워 둘 수 없습니다.

6. 5단계에서 작성한 코드를 실행해도 눈에 띄는 변화는 없을 것입니다. 데이터베이스를 보려면 몇 가지 특수한 소프트웨어를 다운로드해야 합니다.
아래 링크로 이동하여 운영 체제에 맞는 DB 브라우저를 다운로드하세요(Windows의 경우 표준 설치 프로그램 사용).
https://sqlitebrowser.org/dl/

7. DB Browser를 다운로드 및 설치했으면 해당 브라우저를 열고 '데이터베이스열기(Open Database)'를 클릭합니다.
8. 프로젝트 위치(PyCharm Projects라는 폴더에 있어야 함)로 이동하여 books-collection.db를 엽니다.
이때 4개의 필드가 포함된 books라는 표가 표시되어야 합니다.
이게 우리가 만든 데이터베이스입니다.

9. 데이터를 표에 추가하려면 main.py로 돌아가서 다음의 코드를 작성하면 됩니다.
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
그러면 books 표에 '해리 포터'라는 새 항목이 생성되고 변경 사항이 데이터베이스에 적용됩니다.

10. 이제 books라는 표가 생성된 이전 코드 라인을 주석 처리합니다. 그렇지 않으면 sqlite3.OperationalError: table books already exists라는 오류 메시지가 뜨게 됩니다.

11. 그런 다음 '데이터베이스 닫기(Close Database)'를 클릭하여 DB Browser에서 데이터베이스를 닫습니다. 그렇지 않을 경우 파이참에서 데이터베이스로 작업할 때 database locked 이라는 경고가 표시됩니다.

12. 이제 main.py에서 코드를 실행하고, DB Browser에서 데이터베이스를 다시 열어서 업데이트된 books 표를 확인합니다. 다음과 같이 표시되어야 합니다.
SQL 쿼리는 오타에 매우 민감합니다. 만약 다음과 같이 작성하지 않고,
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
아래와 같이 작성한다면,
cursor.execute("INSERT INTO books VALUE(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
코드가 실행되지 않습니다(코드에서 차이점을 발견하셨나요?)

하지만 다행히 파이썬 프로젝트에서 SQ 라이트로 작업할 때 오류가 발생하기 쉬운 이러한 SQL 명령어 대신 사용할 수 있는 훨씬 좋은 방법이 있습니다. 바로 SQL 알케미(SQLAlchemy)라는 도구를 사용하여 파이썬 코드를 작성하는 거죠. 그럼 다음 수업에서 함께 작성해보겠습니다!




# SQLAlchemy
보셨듯이 SQL 명령어 작성은 복잡하며 오류가 발생하기 쉽습니다. 이럴 때 파이썬 코드를 작성하고 컴파일러가 코드상의 오타와 오류를 찾아낼 수 있도록 도와주는 무언가가 있으면 훨씬 편리하겠죠. 그래서 만들어진 것이 바로 SQLAlchemy입니다.
SQL 알케미는 객체 관계형 매핑(ORM, Object Relational Mapping) 라이브러리라고 정의되는데, 이는 데이터베이스의 관계를 객체에 매핑할 수 있다는 뜻입니다. 이때 필드는 객체 속성이 되고, 표는 별도의 클래스, 데이터의 각 행은 새 개체로 정의될 수 있습니다. 이러한 내용은 코드를 작성하고 SQL 알케미를 사용하여 데이터베이스/표/데이터 행을 만드는 방법을 배우고 나면 더 잘 이해될 것입니다.

1. SQ 라이트3 모듈을 사용하여 SQ 라이트 데이터베이스를 직접 생성한 기존 코드를 모두 주석 처리합니다.

2. 필요한 패키지인 flask 및 flask_sqlalchemy를 설치하고 각각에서 Flask와 SQLAlchemy 클래스를 임포트합니다.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


도전 과제: 주석 처리된 코드에서 수행한 모든 작업을 SQL 알케미로 수행하는 방법을 SQL알케미 문서를 활용하여 찾아보세요.

요구사항:
- new-books-collection.db라는 SQ 라이트 데이터베이스를 생성합니다
- 해당 데이터베이스 내에 books라는 표를 만듭니다.
- books 표에는 아이디(id), 제목(title), 저자(author), 평점(rating)이라는 4개의 필드가 있어야 하며, 해당 필드에는 INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL 등과 같은 이전과 동일한 제약이 있어야 합니다.
- books 표에 다음 데이터로 구성된 새 항목을 만듭니다.

아이디: 1
제목: "해리 포터"
저자: "J. K. 롤링 "
평점: 9.3

힌트 1: 데이터베이스의 URL은 "sqlite:///new-books-collection.db"여야합니다.

힌트 2: 콘솔에서 SQL_ALCHEMY_TRACK_MODIFICATIONS 과 관련된 사용 중지 경고가 표시되는 경우에는 그대로 사용하지 말고,

다음과 같은 구문으로 경고가 뜨지 않도록 할 수 있습니다.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

힌트 3: DB Browser를 사용하면 언제든지 데이터베이스를 확인할 수 있습니다.

해답 - https://gist.github.com/angelabauer/d7af893cdd72311d674d709421fa389d



# SQLAlchemy를 사용한 CRUD 작업
지난 수업에서 문제 해결 방법을 알아내셨기를 바라며, 복습하는 의미로 지난 시간에 했던 작업을 아래와 같이 요약 정리해드리니 참고하세요.

새 데이터베이스 만들기
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
db = SQLAlchemy(app)


새 표 만들기
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False
 
db.create_all()


이러한 것들 외에도 새로운 데이터베이스 기술로 작업할 때 알아야 할 가장 중요한 것은 데이터 기록에 대한 CRUD 작업을 수행하는 방법입니다.

Create(생성)

Read(읽기)

Update(갱신)

Delete(삭제)



그럼 SQ 라이트와 SQL 알케미를 사용하여 각각의 작업에 대해 살펴보겠습니다.



새 레코드 만들기
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
참고: 새 레코드를 만들 때 기본키 필드는 선택 사항이며, 다음과 같이 작성할 수도 있습니다.

new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)

id 필드는 자동 생성됩니다.



모든 레코드 읽기
all_books = session.query(Book).all()


쿼리별 특정 레코드 읽기
book = Book.query.filter_by(title="Harry Potter").first()


쿼리별 레코드 업데이트하기
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()  


기본키로 레코드 업데이트하기
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()  


기본키로 특정 레코드 삭제하기
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
제목 또는 다른 속성별 특정 값을 조회하여 삭제할 수도 있습니다.

플라스크 웹 사이트에 SQLite 데이터베이스 구축하기
지난 수업에서 코드로 여러 작업을 해 봤으니 SQL 알케미를 사용하여 이제 CRUD 작업뿐만 아니라 표와 데이터베이스를 생성할 수 있기를 바랍니다.

왜냐하면 이제 최종 과제를 풀어볼 시간이거든요.

오늘 수업 초반에 구축한 플라스크 웹 사이트에 SQ 라이트 데이터베이스를 구축해 보도록 하겠습니다. 추가한 모든 책이 데이터베이스에 저장될 수 있도록 하고, 데이터베이스의 전체 CRUD 기능을 활용하기 위한 몇 가지 추가 기능을 만들어보세요.



웹 사이트 요구사항
/add 경로를 통해 새 책을 추가하고, 책이 데이터베이스에 성공적으로 추가되면 홈페이지로 리디렉션되어야 합니다.


해답
https://gist.github.com/angelabauer/08f3b88d8f50ddaa37fa4be79501cf13


홈페이지에 데이터베이스의 모든 책이 표시되어야 합니다:


해답
https://gist.github.com/angelabauer/8a65dc448d58859d3cafa26546a9e6bf


각각의 도서 <li>에 평점 수정(Edit Rating) 앵커 태그를 추가합니다. 버튼을 누르면 사용자가 해당 책에 대한 새로운 평점을 입력할 수 있는 평점 수정 페이지로 이동할 수 있어야 합니다. 그런 다음 '평점 변경'을 클릭하면 홈페이지로 돌아가고 책 옆에 새로운 평점이 표시되어야 합니다. 예)



힌트: 평점 수정 페이지를 표시하기 위한 GET 요청 시 책 ID를 매개변수로 전달하는 방법을 생각해보세요. 여러 방법으로 수행 가능합니다. 다음은 도움이 될 만한 몇 가지 내용입니다.

https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building

https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask



해답
https://gist.github.com/angelabauer/e2e5840de409681ef94ca95db0a4853c



각 도서 목록 <li>에 삭제(Delete) 앵커 태그를 추가하여, 클릭 시 데이터베이스에서 책을 삭제하고 홈페이지로 다시 리디렉션되도록 합니다.


해답
https://gist.github.com/TheMuellenator/eee79b73b711617f470321a9c8191e4e


이 강의의 학습자료에서 완성된 프로젝트를 다운로드하실 수 있습니다.

Resources for this lecture
