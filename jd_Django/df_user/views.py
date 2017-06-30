# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from hashlib import sha1
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from decorator import user_login
# Create your views here.

def login(request):
    return render(request, 'df_user/login.html')


def login_handler(request):
    #获取用户输入的用户名,密码,验证吗,保存登陆状态
    post = request.POST
    username = post.get('username')
    upassword = post.get('password')
    uyzm = post.get('checkcode')

    yzm = request.session.get('verifycode','').lower()

    saveuser = post.get('saveUser')
    # 查询数据库中的对应用户
    dbuser = python41_user.objects.filter(user_name=username)

    # 判断用户是否存在
    # 存在
    if len(dbuser)>0:
        db_user_object = dbuser[0]

        # 加密用户输入的密码,取出数据库中的密码进行比较
        s1 = sha1()
        s1.update(upassword)
        sha1_passwd = s1.hexdigest()
        db_passwd = db_user_object.user_pwd
        # 判断验证码是否相等
        # 密码相等
        if sha1_passwd == db_passwd:
            # 验证码相等
            if uyzm == yzm:
                # 判断是否记住登陆账户
                response = render(request, 'df_user/login.html')
                if saveuser == '1':
                    # 记住
                    # 写入cookies
                    response.set_cookie('username',username)
                # 否则
                else:
                    #删除cookies,max_age 为负数,立即过期
                    response.set_cookie('username','',max_age=-1)
                # 写入session id usename
                print '==============='
                request.session['user_id'] = db_user_object.id
                request.session['user_name'] = db_user_object.user_name
                #a = request.session.get('user_name', 'oooo')
                a=request.session.has_key('user_name')
                print a
                print '============='


                return response
            # 验证码不相等
            else:

                return render(request,'df_user/login.html',{'z':1})
                # 返回验证码错误

        # 密码不相等
        else:
            # 返回用户名或密码错误
            return render(request, 'df_user/login.html', {'p': 1,'user_name':username})
    # 不存在
    else:

        #返回用户名或错误

        return render(request,'df_user/login.html',{'u':1})


def exit_login(request):
    # 删除session
    request.session.flush()

    return redirect('/user/login')


def regist(request):
    # context = {"u": 0, "p": 0, "y": 0, "t": 0}
    return render(request,'df_user/regist.html')


# 验证码
def regist_yz(request):
    request.session.set_expiry(6000)
    # 生成验证吗
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 150
    height = 36
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    yz = buf.getvalue()
    return HttpResponse(yz,'image/png')

def regist_handler(request):
    # 获取账号,密码,确认密码,验证码
    post = request.POST
    username = post.get('username','')
    password = post.getlist('password')
    uyzm = post.get('checkcode').lower()
    yzm = request.session['verifycode'].lower()
    t = post.get('t',0)
    print username
    print uyzm
    print yzm
    print t


        # 查询t数据库中的用户名
    user_name = python41_user.objects.filter(user_name=username)
    print len(user_name)

    if len(password)==2:
        if password[0] == password[1] and password[0] != '' and password[1] != '':
            # 加密密码,将用户信息写入数据库并删除session验证码信息
            s1 = sha1()
            s1.update(password[0])
            upasswd_sha1 = s1.hexdigest()
        else:
            context =  {"u": 0, "p": 1, "y": 0, "t": 0,'username':username}
            return render(request, 'df_user/regist.html', context)


    if len(user_name) == 0 and uyzm == yzm and t == '1':
            print '888888'
            user_info = python41_user()
            user_info.user_name = username
            user_info.user_pwd = upasswd_sha1
            now = datetime.now()
            user_info.add_time = now.strftime('%Y-%m-%d %H:%M:%S')
            user_info.save()
            request.session.flush()
            #del request.session['verifycode']
            print '========'
            context = {"u": 0, "p": 0, "y": 0, "t": 0,'username':username}

    else:
        print '[[[['
        print uyzm
        if len(user_name) != 0:
            u = 1
        else:
            u = 0
        if password[0] != '' and password[1] != '':
            p = 1
        else:
            p = 0
        if  uyzm != yzm and uyzm != '':
            y = 1
        else:
            y = 0
        if t == 0:
            t = 1
        else:
            t = 1
            print '3====='
        context = {"u":u,"p":p,"y":y,"t":t,'username':username}



        #context = {"u":2,"p":1,"y":1,"t":1,'username':username}
    print context
    return render(request,'df_user/regist.html',context)

@user_login
def user(request):
    # 获取用户名
    dbuser_object = python41_user.objects.get(id=request.session['user_id'])
    dbuser = dbuser_object.user_name
    dbemail = dbuser_object.user_email
    dbphone = dbuser_object.user_tel
    context = {'top':1,'dbuser':dbuser,'dbemail':dbemail,'dbphone':dbphone}
    return render(request,'df_user/user.html',context)



@user_login
def address(request):
    # 获取用户的收货信息对象,返回一个列表
    addr_object_list = UserAddress.objects.filter(uid=request.session['user_id'])
    context = {'top':1,'addr_list':addr_object_list}
    return render(request, 'df_user/address.html',context)



@user_login
def address_add(request):
    # 获取用户输入的收货信息
    post = request.POST
    consignee = post.get('consignee')
    city = post.get('city')
    area1 = post.get('area1')
    area2 = post.get('area2')
    detailAddr = post.get('detailAddr')
    iphone = post.get('iphone')
    default = post.get('default','')

    # 创建地址对象,添加字段
    addr_object = UserAddress()
    addr_object.consignee = consignee
    addr_object.address = city + area1 + area2 + detailAddr
    addr_object.iphone = iphone
    if default == '1':
        print '1====='
        addr_object.default_addr = True


    addr_object.uid = python41_user.objects.get(id=request.session['user_id'])
    addr_object.save()
    addr_objects_list = UserAddress.objects.exclude(id=addr_object.id)
    for addr in addr_objects_list:
        addr.default_addr = 0
        addr.save()
        print addr.consignee
        print addr.default_addr

    return redirect('/user/address/')

@user_login
def address_update(request):
    addr_id = request.GET.get('addr_id')
    addr_status = request.GET.get('status') # 状态码 '1' 删除 '2' 修改 '3' 设置
    try:
        addr_object = UserAddress.objects.get(id=int(addr_id))
        if addr_status == '1':
            addr_object.delete()

        elif addr_status == '2':
            pass
        elif addr_status == '3':
            print '3======='
            addr_object.default_addr = 1
            addr_object.save()
            addr_objects_list = UserAddress.objects.exclude(id=int(addr_id))
            for addr in addr_objects_list:
                addr.default_addr = 0
                addr.save()
        result = 'ok'
    except:
        print '没有接收到收货地址id'
        result = 'No'
    return JsonResponse({'result':result})



