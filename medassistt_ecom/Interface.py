from django.shortcuts import render
from .import pool
from django.http import JsonResponse
import json
from urllib.parse import unquote
def AddToCart(request):
    try:
        product=request.GET['product']
        qty=request.GET['qty']
        product=product.replace("'","\"")
        product=json.loads(product)
        product['qty']=qty
        print("Updated Products:",product)
        #Create Cart using SESSION
        try:
            CART_CONTAINER=request.session['CART_CONTAINER']
            CART_CONTAINER[str(product['productid'])]=product
            request.session['CART_CONTAINER'] = CART_CONTAINER
            # print("Cart_Container:",CART_CONTAINER)
        except:

            CART_CONTAINER={str(product['productid']):product}
            request.session['CART_CONTAINER']=CART_CONTAINER
            print("Error:")
        print("\nCart_Containerrrrrrrrrrrrrrrrrrrrrrrrrr:\n",CART_CONTAINER)
        CART_CONTAINER=str(CART_CONTAINER).replace("'","\"")
        return JsonResponse({'data': CART_CONTAINER },safe="False")
    except Exception as err :
        print("Errorrrrrrrooooooooooooo:",err)
        return JsonResponse({'data': [] }, safe=False)
def FetchCart(request):
    try:
        try:
            CART_CONTAINER=request.session['CART_CONTAINER']
        except:
            CART_CONTAINER={}
        print("\nCart_Containerssssssssssssssssssssss:\n",CART_CONTAINER)
        CART_CONTAINER=str(CART_CONTAINER).replace("'","\"")
        return JsonResponse({'data': CART_CONTAINER },safe="False")
    except Exception as err :
        print("Errorrrrrrrooooooooooooo:",err)
        return JsonResponse({'data': [] }, safe=False)

def RemoveFromCart(request):
    try:
        productid=request.GET['productid']
        CART_CONTAINER=request.session['CART_CONTAINER']
        del CART_CONTAINER[productid]
        request.session['CART_CONTAINER'] = CART_CONTAINER
        print("After Product Remove    ***********************:\n",CART_CONTAINER)
        CART_CONTAINER=str(CART_CONTAINER).replace("'","\"")
        return JsonResponse({'data': CART_CONTAINER },safe="False")
    except Exception as err :
        print("Errorrrrrrrooooooooooooooooooooooooooooo*****:",err)
        return JsonResponse({'data': [] }, safe=False)
def MyShoppingCart(request):
    try:
        try:
            total=0
            actualtotal=0
            discount=0
            CART_CONTAINER=request.session['CART_CONTAINER']
            for key in CART_CONTAINER.keys():
                amt=(CART_CONTAINER[key]['price'] - CART_CONTAINER[key]['offerprice'])
                CART_CONTAINER[key]['save']=amt
                total+=CART_CONTAINER[key]['offerprice']*int(CART_CONTAINER[key]['qty'])
                CART_CONTAINER[key]['totalprice']=(CART_CONTAINER[key]['offerprice'])*int(CART_CONTAINER[key]['qty'])
                actualtotal+=CART_CONTAINER[key]['price']*int(CART_CONTAINER[key]['qty'])
                discount+=amt*int(CART_CONTAINER[key]['qty'])
        except Exception as er:
            CART_CONTAINER={}
            print("Error______________________________________________________________:",er)
        print("\nMy Shooping Cart_Container###########:\n",CART_CONTAINER.values())
        # CART_CONTAINER=str(CART_CONTAINER).replace("'","\"")
        return render(request,"Articals.html",{'data': CART_CONTAINER.values(),'totalamount':total,'totalproducts':len(CART_CONTAINER.keys()),'actualprice':actualtotal,'dis':discount})
    except Exception as err :
        print("Errorrrrrrrooooooooooooo:",err)
        return render(request,"Articals.html",{'data': {}})

def Index(request):
    return render(request,"index.html")
def Buy_Product(request):
    product=unquote(request.GET['product'])
    product=json.loads(product)
    print("zzzzzzzzzzzzzzzz",product,type(product))
    return render(request,"BuyProduct.html",{'product':product})
def Fetch_All_Products_JSON(request):
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
         return JsonResponse({'data': records}, safe=False)
         print("FetchSuccessfully")
    except Exception as d:
          return JsonResponse({'data': "Error"}, safe=False)
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
      return JsonResponse({'data': []}, safe=False)
def Fetch_All_SubCategory_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from subcategories"
      CMD.execute(Q)
      records = CMD.fetchall()
      print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)
def CheckUserMobileno(request):
    mobileno=request.GET['mobileno']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from users where mobileno='{0}'".format(mobileno)
      CMD.execute(Q)
      record = CMD.fetchone()
      print('RECORD:', record)
      if(record):
          return JsonResponse({'data':record, 'status' : True},safe=False)
      else:
          return JsonResponse({'data':[], 'status' : False},safe=False)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)
def InsertUser(request):
    emailid=request.GET['emailid']
    mobileno=request.GET['mobileno']
    firstname=request.GET['firstname']
    lastname=request.GET['lastname']
    password=request.GET['password']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "insert into users values('{0}','{1}','{2}','{3}','{4}')".format(emailid,mobileno,firstname,lastname,password)
      print(Q)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      return JsonResponse({'status' : True},safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'status': False }, safe=False)

def CheckUserMobilenoForAddress(request):
    mobileno=request.GET['mobileno']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select UA.*,(select U.firstname from users U where U.mobileno=UA.mobileno) as firstname,(select U.lastname from users U where U.mobileno=UA.mobileno) as lastname from users_address UA where UA.mobileno='{0}'".format(mobileno)
      CMD.execute(Q)
      record = CMD.fetchone()
      print('RECORD:', record)
      if(record):
          return JsonResponse({'data':record, 'status' : True},safe=False)
      else:
          return JsonResponse({'data':[], 'status' : False},safe=False)
      DB.close()
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)

def InsertUserAddress(request):
    mobileno=request.GET['mobileno']
    emailid=request.GET['emailid']
    address1=request.GET['address1']
    address2=request.GET['address2']
    landmark=request.GET['landmark']
    city=request.GET['city']
    state=request.GET['state']
    zipcode=request.GET['zipcode']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "insert into users_address(mobileno, emailid, address1, address2, landmark, city, state, zipcode) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(mobileno,emailid,address1,address2,landmark,city,state,zipcode)
      print(Q)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      return JsonResponse({'status' : True},safe=False)
    except Exception as e:
      print("Varun Kate")
      print('Error:', e)
      return JsonResponse({'status': False }, safe=False)



    # Categories Paths
def Allopaty_Path(request):
    return render(request,"allopathy.html")
def Ayurveda_Path(request):
    return render(request,"Ayurveda.html")
def Cosmatics_Path(request):
    return render(request,"cosmatics.html")
def MedicalTools_Path(request):
    return render(request,"medicaltools.html")
def LabTest_Path(request):
    return  render(request,"LabTest.html")
