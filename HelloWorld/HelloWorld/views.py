from django.shortcuts import render


def index(request):
    context = {"name": "工程師小安"}

    # 列表
    views_list = ["Django課程", "python課程", "C++課程"]
    context["views_list"] = views_list

    # 字典
    views_dic = {"name": "工程師小安", "age": 23}
    context["views_dic"] = views_dic

    # if/else
    score = 89
    context["score"] = score

    # empty list
    empty_list = []
    context["empty_list"] = empty_list

    return render(request, "index.html", context)


def index1(request):
    context = {"name": "工程師小安"}
    return render(request, "index.html", context)
