from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import UserInfo
# Create your views here.

def demo01(request):
	#返回一个HttpsResponse对象
	# html = '<h1>i am demo01</h1>'
	# print(html)
	# 此处不能直接return html, 必须返回一个HttpResponse对象
	#request,html模板,传递到html页面的信息 ->字典格式
	return render(request, "../templates/app1/demo.html")



def demo02_form(request):
		# print(request.GET)
		username = request.GET.get("email")
		# username = request.GET["email"]——在输入地址时需要username的参数
		password = request.GET.get("passwd")

	# password = request.GET["passwd"]——在输入url时需要passwd的参数
		return render(request, "app1/demo02_form.html", {"user":username})


def demo02_form2(request):
	userlist = {"a@a.com":"123123", 'b@b.cim':"abcabc"}
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("passwd")
		if username in userlist.keys() and password == userlist[username]:
				return HttpResponse(f"<h2>欢迎您,{username}</h2>")
		# else:
	# username = request.GET["email"]——在输入地址时需要username的参数
	# 			return HttpResponse(f"<h1>您没有权限</h1>")
	# 			return HttpResponse(f"<h1>您没有权限</h1>")
	# password = request.GET["passwd"]——在输入url时需要passwd的参数
	return render(request,'app1/demo02_form2.html')

def demo_form_db(request):
	msg = ""
	user_lsit = UserInfo.objects.all()
	print(user_lsit)
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("passwd")
		try :
			result = UserInfo.objects.get(email=username)
			if result and result.password == password:
					return HttpResponse(f"<h2>欢迎您,{username}</h2>")
			else:
					msg = "用户名密码错误"
		except Exception as ex:
	# password = request.GET["passwd"]——在输入url时需要passwd的参数
					msg = "用户不存在"
	kwgs = {
		"msg":msg,
	}
	return render(request,'app1/demo_form_db.html',kwgs)

def getinformation(request):
	user_list ={}
	print(request.method)
		# username = UserInfo.objects.get(email=username)
		# 添加数据到库
		# UserInfo.objects.create(username=username, password=password)
		# 查询数据
	user_list = UserInfo.objects.all()
	print(user_list)
	return render(request, 'app1/index.html', {'user_list': user_list})

def adduser(request):
	msg = ""
	user_list = UserInfo.objects.all()
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("passwd")
		result = UserInfo.objects.filter(username=username)
		print(result)
		if result and username == result.username :
			return HttpResponse(f"<h2>欢迎您,{username}</h2>")
		else:
			UserInfo.objects.create(username=username, password=password)
			msg = "用户不存在"
			# password = request.GET["passwd"]——在输入url时需要passwd的参数
	kwgs = {"msg": msg}
	return render(request, 'app1/reg.html', kwgs)

def demo(request):
    """最简单的html页面"""
    # 返回一个HttpResponse对象
    # return HttpResponse('HelloWorld')
    # request, html模板, 传递到html页面的信息
    return render(request, 'app1/demo.html')
