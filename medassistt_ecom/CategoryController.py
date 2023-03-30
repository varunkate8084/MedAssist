from django.shortcuts import render
from .import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Action_CategoryInterface(request):
    try:
        admin=request.session['ADMIN']
        return render(request,"categoryInterface.html")
    except:
     return render(request,"AdminLogIn.html")
@xframe_options_exempt
def Submit_Category(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    categoryname=request.POST['categoryname']
    categoryicon = request.FILES['categoryicon']
    Q="insert into categories(categoryname,categoryicon) values('{0}','{1}')".format(categoryname,categoryicon.name)
    F=open("d:/medassistt_ecom/assets/"+categoryicon.name,'wb')
    for chunk in categoryicon.chunks():
        F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return render(request,'categoryInterface.html',{'message': 'Record Submitted successfully'})
  except  Exception as d:
      # print("Varun kate")
      print("error:",d)
      return render(request, 'categoryInterface.html', {'message':'Record Failed'})
@xframe_options_exempt
def Display_All_Categoriy(request):
    try:
        admin=request.session['ADMIN']
    except:
     return render(request,"AdminLogIn.html")
    try:
        DB,CMD=pool.ConnectionPooling()
        Q= "select * from categories"
        CMD.execute(Q)
        records=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllCategories.html',{'records':records})
    except Exception as d:
        return render(request, 'DisplayAllCategories.html',{'records':None})
@xframe_options_exempt
def Edit_category(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryname=request.GET['categoryname']
        categoryid=request.GET['categoryid']
        Q="update categories set categoryname='{0}' where categoryid={1}".format(categoryname,categoryid)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as d:
        print("Error:",d)
        return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Delet_category(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        Q="delete from categories where categoryid={0}".format(categoryid)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as d:
        print("Error:",d)
        return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Edit_categoryIcon(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    categoryid = request.POST['categoryid']
    categoryicon = request.FILES['categoryicon']
    Q = "update categories set categoryicon='{0}' where categoryid={1}".format(categoryicon.name, categoryid)
    F=open("d:/medassistt_ecom/assets/"+categoryicon.name,'wb')
    for chunk in categoryicon.chunks():
        F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result': True}, safe=False)
  except Exception as d:
   print("Error:", d)
   return JsonResponse({'result': False}, safe=False)
@xframe_options_exempt
def Fetch_All_Category_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from categories"
      CMD.execute(Q)
      records = CMD.fetchall()
      print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return render(request, 'DisplayAllCategories.html', {{'data':None}})

