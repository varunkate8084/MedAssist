"""medassistt_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import CategoryController
from .import SubCategoryController
from .import BrandController
from .import ProductController
from .import AdminLogInController
from .import Interface
urlpatterns = [

    # Urls of Categories
    path('admin/', admin.site.urls),
    path('categoryinterface/',CategoryController.Action_CategoryInterface),
    path('submitcategory',CategoryController.Submit_Category),
    path('showallcategories/',CategoryController.Display_All_Categoriy),
    path('editcategory/',CategoryController.Edit_category),
    path('deletecategory/',CategoryController.Delet_category),
    path('editcategoryicon',CategoryController.Edit_categoryIcon),
    path('fetch_all_category_json',CategoryController.Fetch_All_Category_JSON),

    # Urls of SubCategories
    path('subcategoryinterface/',SubCategoryController.Sub_CategoryInterface),
    path('submitsubcategory',SubCategoryController.Submit_SubCategory),
    path('showallsubcategories/',SubCategoryController.Display_All_SubCategoriy),
    path('editsubcategory/',SubCategoryController.Edit_Subcategory),
    path('deletesubcategory/',SubCategoryController.Delet_Subcategory),
    path('editsubcategoryicon',SubCategoryController.Edit_SubcategoryIcon),
    path('fetch_all_subcategory_json',SubCategoryController.Fetch_All_Subcategory_JSON),

    # Urls of Brand
    path('brandinterface/',BrandController.Brand_Interface),
    path('submitbrand',BrandController.Submit_Brand),
    path('showallbrands/',BrandController.DisplayAllBrands),
    path('editbrand/',BrandController.Edit_Brand),
    path('deletebrand/',BrandController.Delete_Brand),
    path('editbrandlogo',BrandController.Edit_BrandIcon),
    path('fetch_all_brand_json',BrandController.Fetch_All_Brands_JSON),

     # urls for Products
    path('productinterface/',ProductController.Product_Interface),
    path('submitproduct',ProductController.Submit_Product),
    path('showallproduct/',ProductController.DisplayAllProducts),
    path('editproduct/',ProductController.Edit_Product),


    #urls of AdminLogIn
    path('adminlogin/',AdminLogInController.AdminLogIn),
    path('adminlogout/',AdminLogInController.AdminLogOut),
    path('checkadminlogin',AdminLogInController.Check_LogIn),



    #urls of Interface
    path('home/',Interface.Index),
    path('fetch_all_user_categories/',Interface.Fetch_All_Category_JSON),
    path('fetch_all_products/',Interface.Fetch_All_Products_JSON),
    path('fetch_all_user_subcategories_json/',Interface.Fetch_All_SubCategory_JSON),
    path('buyproduct/',Interface.Buy_Product),
    path('add_to_cart/',Interface.AddToCart),
    path('fetch_cart/',Interface.FetchCart),
    path('remove_from_cart/',Interface.RemoveFromCart),
    path('my_shopping_cart/',Interface.MyShoppingCart),
    path('check_user_mobileno/',Interface.CheckUserMobileno),
    path('inster_user_registration',Interface.InsertUser),
    path('check_user_mobileno_for_address/',Interface.CheckUserMobilenoForAddress),
    path('inster_user_address/',Interface.InsertUserAddress),
#     urls FOR CATEGORIES
    path('Allopathycategory/',Interface.Allopaty_Path),
    path('Ayurvedacategory/',Interface.Ayurveda_Path),
    path('Cosmaticscategory/',Interface.Cosmatics_Path),
    path('Medical Toolscategory/',Interface.MedicalTools_Path),
    path('labtest/',Interface.LabTest_Path),
]