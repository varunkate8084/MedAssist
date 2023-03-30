from django.shortcuts import render
from .import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Brand_Interface(request):
    try:
        admin=request.session['ADMIN']
        return render(request,"BrandInterface.html")
    except:
     return render(request,"AdminLogIn.html")
@xframe_options_exempt
def Submit_Brand(request):
 try:
    DB,CMD=pool.ConnectionPooling()
    categoryid=request.POST['categoryid']
    subcategoryid=request.POST['subcategoryid']
    brandname=request.POST['brandname']
    contactperson=request.POST['contactperson']
    mobileno=request.POST['mobileno']
    status=request.POST['status']
    logo=request.FILES['logo']
    Q = "insert into brands(categoryid,subcategoryid,brandname,contactperson,mobileno,status,logo) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,subcategoryid,brandname,contactperson,mobileno,status,logo.name)
    print(Q)
    F = open("d:/medassistt_ecom/assets/" + logo.name, 'wb')
    for chunk in logo.chunks():
        F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return render(request, 'BrandInterface.html', {'message': 'Record Submitted successfully'})
 except  Exception as d:
    print("error:", d)
    return render(request, 'BrandInterface.html', {'message': 'Record Failed'})
@xframe_options_exempt
def DisplayAllBrands(request):
    try:
        admin=request.session['ADMIN']
    except:
     return render(request,"AdminLogIn.html")
    try:
         DB, CMD = pool.ConnectionPooling()
         Q = "select b.*,(select C.categoryname from categories C where C.categoryid=b.categoryid)as cname,(select s.subcategoryname from subcategories s where s.subcategoryid=b.subcategoryid) as scname from brands b "
         # print(Q)
         CMD.execute(Q)
         records = CMD.fetchall()
         DB.close()
         return render(request, 'DisplayAllBrands.html', {'records': records})
    except Exception as d:
         return render(request, 'DisplayAllBrands.html', {'records': None})
@xframe_options_exempt
def Edit_Brand(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        brandname=request.GET['brandname']
        brandid=request.GET['brandid']
        contactperson=request.GET['contactperson']
        mobileno=request.GET['mobileno']
        Q = "update brands set brandname='{0}',categoryid={1},subcategoryid={2},contactperson='{3}',mobileno='{4}' where brandid={5}".format(brandname,categoryid,subcategoryid,contactperson,mobileno,brandid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as d:
        print("Varun Kate")
        print("Error:",d)
        return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Delete_Brand(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    brandid = request.GET['brandid']
    Q="delete from brands where  brandid={0}".format(brandid)
    print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as d:
    print("Error:",d)
    return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Edit_BrandIcon(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    brandid = request.POST['brandid']
    logo = request.FILES['logo']
    Q = "update brands set logo='{0}' where brandid={1}".format(logo.name, brandid)
    F=open("d:/medassistt_ecom/assets/"+logo.name,'wb')
    for chunk in logo.chunks():
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
def Fetch_All_Brands_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      subcategoryid=request.GET["subcategoryid"]
      Q = "select * from brands where subcategoryid='{0}'".format(subcategoryid)
      print(Q)
      CMD.execute(Q)
      records = CMD.fetchall()
      # print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as d:
      print('Error:', d)
      print("Riyaaaaaaaaaa")
      return render(request, 'DisplayAllBrand.html', {{'data':None}})

