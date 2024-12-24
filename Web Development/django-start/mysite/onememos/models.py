from django.db import models

# Create your models here.
# idx (정수형) -> pk (굳이 만들어줄 필요 없음, 알아서 자동으로 생성) x
# memo_text (문자형)
# published_date (날짜형)

class Memo(models.Model):
    memo_text = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memo_text