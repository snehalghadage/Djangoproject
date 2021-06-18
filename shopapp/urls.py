from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),

    url(r'^dealerform/', views.dealerform, name="dealerform"),
    url(r'^dealerforminsert/', views.dealerforminsert, name="dealerforminsert"),
    url(r'^dealerformview/', views.dealerformview, name="dealerformview"),
    url(r'^dealerupdate/', views.dealerupdate, name="dealerupdate"),
    url(r'^UpdateRecord/', views.UpdateRecord, name="UpdateRecord"),
    url(r'^dealerdelete/', views.dealerdelete, name="dealerdelete"),

    # customer urls
    
    url(r'^customerform/', views.customerform, name="customerform"),
    url(r'^customerinsert/', views.customerinsert, name="customerinsert"),
    url(r'^customerformview/', views.customerformview, name="customerformview"),
    url(r'^deletecustomer/', views.deletecustomer, name="deletecustomer"),
    url(r'^Updatecustomer/',views.Updatecustomer,name="Updatecustomer"),
    url(r'^UpdateCustomerRecord/',views.UpdateCustomerRecord,name="UpdateCustomerRecord"),


    # employee urls 

    url(r'^empform/',views.empform,name="empform"),
    url(r'^empforminsert/',views.empforminsert,name="empforminsert"),
    url(r'^empformview/',views.empformview,name="empformview"),
    url(r'^empdelete/',views.empdelete,name="empdelete"),
    url(r'^empupdate/',views.empupdate,name="empudate"),
    url(r'^UpdateEmpRecord/',views.UpdateEmpRecord,name="UpdateEmpRecord"),

    # medicine urls

    url(r'^medicineform/',views.medicineform,name="medicineform"),
    url(r'^medicineinsert/',views.medicineinsert,name="medicineinsert"),
    url(r'^medicineformview/',views.medicineformview,name="medicineformview"),
    url(r'^deletemedicine/',views.deletemedicine,name="deletemedicine"),
    url(r'^Updatemedicineinfo/',views.Updatemedicineinfo,name="Updatemedicineinfo"),
    url(r'^updatemedicinerecord/',views.updatemedicinerecord,name="updatemedicinerecord"),
    url(r'^search_product/',views.search_product,name="search_product"),

    # dealer purchase urls 
    url(r'^Dealerpurchaseform/',views.Dealerpurchaseform,name="Dealerpurchaseform"),
    url(r'^dealerpurchaseinsert/',views.dealerpurchaseinsert,name="dealerpurchaseinsert"),
    url(r'^dealerpurchaseformview/',views.dealerpurchaseformview,name="dealerpurchaseformview"),
    url(r'^Updatedealerpurchase/',views.Updatedealerpurchase,name="Updatedealerpurchase"),
    url(r'^Updtpurdealerrecord/',views.Updtpurdealerrecord,name="Updtpurdealerrecord"),
    url(r'^dealerpurchasedelete/',views.dealerpurchasedelete,name="dealerpurchasedelete"),
    

    # customer purchase urls

    url(r'^Customerpurchaseform/',views.Customerpurchaseform,name="Customerpurchaseform"),
    url(r'^custpurchinsert/',views.custpurchinsert,name="custpurchinsert"),
    url(r'^custpurchaseformview/',views.custpurchaseformview,name="custpurchaseformview"),
    url(r'^custpurchdelete/',views.custpurchdelete,name="custpurchdelete"),
    url(r'^Updatecustpur/',views.Updatecustpur,name="Updatecustpur"),
    url(r'^Updatecustpurrecord/',views.Updatecustpurrecord,name="Updatecustpurrecord"),
    
    



]
