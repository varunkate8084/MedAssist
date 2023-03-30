from django.shortcuts import render
from .import pool
from django.http import JsonResponse
def AdminLogIn(request):
    return render(request,"AdminLogIn.html")
def AdminLogOut(request):
    # SECURITY PURPOSE
    del request.session['ADMIN']
    return render(request,"AdminLogIn.html")
def Check_LogIn(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        emailid = request.POST['emailid']
        password = request.POST['password']
        Q = "select * from adminlogin where emailid='{0}'and password='{1}'".format(emailid,password)
        print(Q)
        CMD.execute(Q)
        row=CMD.fetchone()
        if(row):
            request.session['ADMIN']=row
            return render(request, 'DashBoard.html',{'AdminData':row})
        else:
            return render(request, 'AdminLogIn.html', {'message': 'Invalid User Id/Password'})
        DB.close()
    except  Exception as d:
        print("error:", d)
        return render(request, 'AdminLogIn.html', {'message': 'Something went wrong'})

