# -*- coding: utf-8 -*-

from django.http import HttpResponse

# from testWebtest.testWeb01.HelloWorld.TestModel.models import Test
#
#
# # 数据库操作
# def testdb(request):
#
#     #================================================
#     # response = ""
#     # response1 = ""
#     #
#     # #获取所有数据，相当于slelct * from
#     # list = Test.objects.all()
#     #
#     # # filter相当于SQL中的WHERE，可设置条件过滤结果
#     # response2 = Test.objects.fliter(id=1)
#     #
#     # # 获取单个对象
#     # response3 = Test.objects.get(id=1)
#     #
#     # # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#     # Test.objects.order_by('name')[0:2]
#     #
#     # #数据排序
#     # Test.objects.order_by("id")
#     #
#     # # 上面的方法可以连锁使用
#     # Test.objects.filter(name="runoob").order_by("id")
#     # # 输出所有数据
#     # for var in list:
#     #     response1 += var.name + " "
#     # response = response1
#     # return HttpResponse("<p>" + response + "</p>")
#
#
#     #================================================
#     # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
#     test1 = Test.objects.get(id=1)
#     test1.name = 'Google'
#     test1.save()
#     return HttpResponse("<p>修改成功</p>")