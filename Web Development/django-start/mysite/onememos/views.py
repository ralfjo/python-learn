from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Memo

# Create your views here.
def main(request):
    # return HttpResponse("Onememos~ Hello, World~")
    # return render(request, "main.html")
    lists = Memo.objects.all()
    data = {'lists':lists}  # 반드시 딕셔너리 타입으로 만들어서 data 변수를 --> 템플릿 파일로 전달 --> 안그러면 에러 발생.

    return render(request, 'main.html', data)

@csrf_exempt
def createMemo(request):
    # memoContent = request.GET['memoContent']
    memoContent = request.POST['memoContent']

    # DB 입력
    # article = Memo(memo_text = memoContent)
    # article.save()
    
    # return HttpResponse("create Memo = " + memoContent)
    return HttpResponseRedirect( reverse('main') )

@csrf_exempt
def writeMemo(request):
    # return HttpResponse('Write Page 요청')
    # Get vs POST 처리
    if request.method == "GET":
        return HttpResponse('GET 방식')
        # return render(request, 'my_template.html', {'Method': 'GET 방식'})
    if request.method == "POST":
        return HttpResponse('POST 방식')
        # return render(request, 'my_template.html', {'Method': 'POST 방식'})

@csrf_exempt
def editPage(request, idx):
    # return HttpResponse('수정 페이지 = ' + idx)
    article = Memo.objects.get(id=idx)
    data = {'article':article}

    return render(request, 'edit.html', data)

@csrf_exempt
def updateMemo(request):
    idx = request.POST['idx']
    memoContent = request.POST['memoContent']

    # return HttpResponse(idx + memoContent)
    # 실질적인 DB에서의 수정 처리
    db_article = Memo.objects.get(id = idx)
    db_article.memo_text = memoContent
    db_article.save()

    return HttpResponseRedirect(reverse('main'))

@csrf_exempt
def deleteMemo(request, idx):
    # return HttpResponse(idx)

    # DB삭제 처리
    db_article = Memo.objects.get(id = idx)
    db_article.delete()

    return HttpResponseRedirect(reverse('main'))
