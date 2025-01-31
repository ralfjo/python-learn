Section 62: 62일차 – 고급 – 플라스크, WTForms, 부트스트랩 및 CSV – 커피와 와이파이 프로젝트

시작 프로젝트 다운로드
1. 아래의 시작 프로젝트를 다운로드하고 압축을 풉니다.

(Starting Files - coffee-and-wifi.zip)



2. 파이참(PyCharm)에서 프로젝트를 열고 필요한 모든 패키지가 설치되었는지 확인합니다.

(Repl.it에서 다운로드하는 경우 모든 패키지가 사전에 설치되어 있어야 합니다. 단, 프로젝트 기본 설정은 언제든지 확인할 수 있습니다.)


Resources for this lecture



바람직한 최종 결과물 확인하기



요구 사항 확인하기
이제 코드를 작성할 차례입니다. 본 프로젝트에 대한 아래의 요구 사항 목록을 확인하세요. 실제 클라이언트 프로젝트와 마찬가지로 프런트 엔드는 이미 구축되어 있습니다(시간이 넉넉하거나 HTML/부트스트랩 관련 연습을 더 많이 해보고 싶은 경우 간단히 빈 파이참 프로젝트를 새로 생성하여 처음부터 전체 프로젝트를 구축할 수도 있습니다). 그러나 오늘의 주요 목표는 플라스크 WTF, 플라스크 부트스트랩, 부트스트랩 클래스에 숙달하고, csv 조작을 약간 수정하는 것입니다.



요구사항
홈페이지는 css/styles.css 파일을 사용해야 하며, 다음과 같이 표시되어야 한다.

힌트: 부트스트랩 블록과 슈퍼 블록을 떠올려 보세요.





/cafes 경로는 cafes.html 파일을 렌더링해야 하며, 이 파일에는 cafe-data.csv의 모든 데이터를 표시하는 부트스트랩 표가 포함되어야 합니다.



힌트: cafes라는 객체는 /cafes 경로에서 cafes.html로 전달됩니다. 카페의 데이터가 어떻게 표시되는지 보려면 <p>에 해당 데이터를 넣어보세요.




· 위치 URL은 표 안에서 전체 링크 대신 앵커 태그 <a>로 렌더링 되어야 합니다. 'Maps Link'라는 링크 텍스트가 있어야 하고 href가 실제 링크여야 합니다.

힌트: 모든 위치 링크의 처음 네 글자는 'http'로 표시됩니다.




홈페이지의 '보기(Show Me!)" 버튼을 클릭하면 cafes.html 페이지로 이동해야 합니다.




버튼은 없지만 아는 사람은 접근할 수 있는 '/add' 비밀 경로가 있어야 하며, 이를 클릭할 경우 add.html 파일로 이동해야 합니다.




WTForms에 대해 배운 내용을 활용하여 add.html 페이지에 아래 데모에서 볼 수 있는 모든 필드가 포함된 quick_form을 만듭니다.

힌트: https://flask-wtf.readthedocs.io/en/stable/quickstart.html

https://pythonhosted.org/Flask-Bootstrap/forms.html




입력한 데이터가 유효한 URL인지 확인하는 유효성 검증 규칙이 위치 URL 필드에 포함되어야 합니다.

힌트: https://wtforms.readthedocs.io/en/2.3.x/validators/

quick_forms를 이용한 클라이언트측(브라우저) 유효성 검사 해제 방법: https://stackoverflow.com/a/61166621/10557313




사용자가 성공적으로 add.html에 양식을 제출할 경우 데이터가 cafe-data.csv에 추가될 수 있도록 합니다. csv 파일의 끝에 추가되어야 하며, 각 필드의 데이터는 cafe-data.csv의 다른 모든 데이터 라인과 마찬가지로 쉼표로 구분되어야 합니다.

힌트: https://www.w3schools.com/python/python_file_write.asp




웹 사이트의 모든 탐색 링크가 제대로 작동할 수 있도록 합니다.




항상 기억할 점은 문제에 봉착하고 이를 해결하는 과정을 통해 배우게 된다는 겁니다. 진정한 학습은 강의가 아니라 문제와 씨름하며 이를 극복할 때 이루어집니다. 나를 괴롭히는 문제들에게 누가 승자인지 보여주세요!

본 프로젝트의 코드 작성 및 디버깅에 최소한 1시간 이상을 투자할 것을 권합니다. 처음 30분 동안은 1단계를 벗어나지 못해 답답할 수도 있고, 이러한 과정이 비생산적으로 느껴져서 자기 능력에 의문을 품게 될 수도 있습니다. 하지만 걱정하지 마세요. 다들 그러니까요. 그냥 잠시 쉬면서 산책하고 간식도 먹은 다음에 다시 코드로 돌아와서 계속해 나가다 보면 내가 얼마나 많은 해결책을 발견했는지 놀라게 될 거예요.

프로젝트에 충분한 시간을 할애했거나 내가 만든 해결책과 답안을 비교하고 싶은 경우에만 정답을 확인하세요(참고로 동일한 작업일지라도 여러 방법으로 수행할 수 있으므로 샘플 답안이 본 프로젝트를 해결하는 유일한 방법은 아닙니다).



이 강의의 학습자료에서 완성된 해답 코드를 다운로드하실 수 있습니다.

Resources for this lecture