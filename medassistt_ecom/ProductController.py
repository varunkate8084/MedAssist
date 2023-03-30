from django.shortcuts import render
from .import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Product_Interface(request):
    try:
        admin=request.session['ADMIN']
        return render(request,"ProductInterface.html")
    except:
     return render(request,"AdminLogIn.html")
@xframe_options_exempt
def Submit_Product(request):
 try:
    DB,CMD=pool.ConnectionPooling()
    categoryid=request.POST['categoryid']
    subcategoryid=request.POST['subcategoryid']
    brandid=request.POST['brandid']
    offerprice=request.POST['offerprice']
    price=request.POST['price']
    quantity=request.POST['quantity']
    salestatus=request.POST['salestatus']
    status=request.POST['status']
    rating=request.POST['rating']
    productimg=request.FILES['productimg']
    productname=request.POST['productname']
    packingtype=request.POST['packingtype']
    Q = "insert into products(categoryid,subcategoryid,brandid,offerprice,price,quantity,salestatus,status,rating,productname,packingtype,productimg) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(categoryid,subcategoryid,brandid,offerprice,price,quantity,salestatus,status,rating,productname,packingtype,productimg.name)
    print(Q)
    F = open("d:/medassistt_ecom/assets/" + productimg.name, 'wb')
    for chunk in productimg.chunks():
        F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return render(request, 'ProductInterface.html', {'message': 'Record Submitted successfully'})
 except  Exception as d:
    print("error:", d)
    return render(request, 'ProductInterface.html', {'message': 'Record Failed'})
@xframe_options_exempt
def DisplayAllProducts(request):
    try:
        admin=request.session['ADMIN']
    except:
     return render(request,"AdminLogIn.html")
    try:
         DB, CMD = pool.ConnectionPooling()
         Q = "select b.*,(select C.categoryname from categories C where C.categoryid=b.categoryid)as cname,(select s.subcategoryname from subcategories s where s.subcategoryid=b.subcategoryid)as scname,(select br.brandname from brands br where b.brandid=br.brandid) as bname from products b "
         print(Q)
         CMD.execute(Q)
         records = CMD.fetchall()
         DB.close()
         return render(request, 'DisplayProducts.html', {'records': records})
    except Exception as d:
         print("Varun Kate")
         return render(request, 'DisplayallBrands.html', {'records': None})
@xframe_options_exempt
def Edit_Product(request):
    try:
        DB,CMD=pool.ConnectionPooling()
        productname=request.GET['productname']
        productid=request.GET['productid']
        Q="update products set productname='{0}' where productid={1}".format(productname,productid)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as d:
        print("Error:",d)
        return JsonResponse({'result':False},safe=False)
