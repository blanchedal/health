from django.shortcuts import render
from django.http import HttpResponse
import json
import pymysql

# def index(request):
#     contx_dic = {
#         'main_line_lbl' : ['apple','melon','orange','banana'],
#         'main_line_val' : [100000,60000,120000,18000],
#     }
#     result = json.dumps(contx_dic,ensure_ascii=False)
#     print(result)
#     context = {'result' : result}
#     return render(request, 'graph/index.html',context)

def index(request):
    # MySQL 데이터베이스 연결
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='smartfarm', charset='utf8')
    cur = conn.cursor()

    # 쿼리 실행
    query =  "SELECT * FROM environment ORDER BY DAT DESC LIMIT 5;"
    cur.execute(query)
    rows = cur.fetchall()

    # 결과 처리
    main_line_lbl = []
    main_line_val = []
    for row in rows:
        main_line_lbl.append(row[2])
        main_line_val.append(row[1])

    # 연결 및 커서 닫기
    cur.close()
    conn.close()

    # 결과를 JSON 형식으로 변환
    contx_dic = {
        'main_line_lbl': main_line_lbl,
        'main_line_val': main_line_val,
    }
    result = json.dumps(contx_dic, ensure_ascii=False)
    print(result)
    context = {'result': result}
    return render(request, 'graph/index.html', context)
