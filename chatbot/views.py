from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv

# Create your views here.
def main(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_reponse = generate_response(user_message)
        return JsonResponse(
            {
                'response':bot_reponse
            }
        )
    
    return render(
        request,
        'chatbot/main.html',
    )

def generate_response(message):
    f = open('hyeonseo.csv','r',encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    # 질문리스트, 답변리스트
    ques = []; ans = []; order = []

    for row in data:
        # 순서
        order.append(row[0])
        # 질문
        q = row[1].split('/')
        ques.append(q)
        # 답변
        ans.append(row[2])

    f.close()

    # 조건 설정
    for i in range(len(order)+1):
        if i == len(order):
            return ans[19]
        elif message in ques[i]:
            return ans[i]
        elif message == ques[i]:
            return ans[i]
        
