from django.shortcuts import render
from .import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Sub_CategoryInterface(request):
    try:
        admin=request.session['ADMIN']
        return render(request,"subCategoryInterface.html")
    except:
     return render(request,"AdminLogIn.html")
@xframe_options_exempt
def Submit_SubCategory(request):
 try:
    DB,CMD=pool.ConnectionPooling()
    categoryid=request.POST['categoryid']
    subcategoryname=request.POST['subcategoryname']
    subcategoryicon=request.FILES['subcategoryicon']
    Q = "insert into subcategories(subcategoryname,categoryid,subcategoryicon) values('{0}','{1}','{2}')".format(subcategoryname,categoryid,subcategoryicon.name)
    F = open("d:/medassistt_ecom/assets/" + subcategoryicon.name, 'wb')
    for chunk in subcategoryicon.chunks():
        F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return render(request, 'subCategoryInterface.html', {'message': 'Record Submitted successfully'})
 except  Exception as d:
    print("error:", d)
    return render(request, 'subCategoryInterface.html', {'message': 'Record Failed'})
@xframe_options_exempt
def Display_All_SubCategoriy(request):
    try:
        admin=request.session['ADMIN']
    except:
     return render(request,"AdminLogIn.html")
    try:
        DB,CMD=pool.ConnectionPooling()
        Q= "select S.*,(select C.categoryname from categories C where C.categoryid=S.categoryid)as cname from subcategories S"
        print(Q)
        CMD.execute(Q)
        records=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllSubCategories.html',{'records':records})
    except Exception as d:
        return render(request, 'DisplayAllSubCategories.html',{'records':None})
@xframe_options_exempt
def Edit_Subcategory(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        subcategoryname=request.GET['subcategoryname']
        subcategoryid=request.GET['subcategoryid']
        Q="update subcategories set subcategoryname='{0}' where subcategoryid={1}".format(subcategoryname,subcategoryid)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as d:
        print("Error:",d)
        return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Delet_Subcategory(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        subcategoryid=request.GET['subcategoryid']
        Q="delete from subcategories where subcategoryid={0}".format(subcategoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as d:
        print("Error:",d)
        return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Edit_SubcategoryIcon(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    subcategoryid = request.POST['subcategoryid']
    subcategoryicon = request.FILES['subcategoryicon']
    Q = "update subcategories set subcategoryicon='{0}' where subcategoryid={1}".format(subcategoryicon.name, subcategoryid)
    F=open("d:/medassistt_ecom/assets/"+subcategoryicon.name,'wb')
    for chunk in subcategoryicon.chunks():
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
def Fetch_All_Subcategory_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      categoryid=request.GET["categoryid"]
      Q = "select * from subcategories where categoryid={0}".format(categoryid)
      CMD.execute(Q)
      records = CMD.fetchall()
      # print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as d:
      print('Error:', d)
      return render(request, 'DisplayAllBrand.html', {{'data':None}})
