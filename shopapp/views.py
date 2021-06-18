from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.db import IntegrityError, reset_queries
from .models import Dealer, Purchase
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Custpurchase
#from .models import Purchase
# Create your views here.
def hello(request):
    return HttpResponse("hello world")
def home(request):
    return render(request,'index.html')

def dealerform(request):
    dict = {'add': True, }
    return render(request,'dealer.html',dict)


def dealerforminsert(request):
 
    try:
        dname = request.POST['dname']
        address = request.POST['address']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        Dealer(dname=dname,address=address,phone_no=phone_no,email=email).save()
        
    except IntegrityError:
        return render(request, "new.html")
    return redirect(dealerformview)

def dealerformview(request):
    data = Dealer.objects.all()
    return render(request,'showdata.html',{'data':data})

# def dealerupdate(request,ph):
def dealerupdate(request):
    phone_no = request.GET['phone_no']
    for data in Dealer.objects.filter(phone_no=phone_no):
        dname = data.dname
        address = data.address
        email = data.email
        dict = {'data':data}
    # return render(request,'update.html',{'dname':dname,'address':address,'phone_no':phone_no,'email':email})
    return render(request,'update.html',dict)

# def UpdateRecord(request,ph):
def UpdateRecord(request):
    try:
        ph= request.GET['phone_no']
        dname = request.POST['dname']
        address = request.POST['address']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        if ph == phone_no:
            Dealer.objects.filter(phone_no=ph).update(dname=dname,address=address,email=email)
            return redirect(dealerformview)
        else:
            Dealer.objects.filter(phone_no=ph).update(dname=dname,address=address,email=email,phone_no=phone_no)
            return  redirect(dealerformview)
    except Exception as e:
        return render(request, 'error.html')

def dealerdelete(request):
    pno = request.GET['phone_no']
    Dealer.objects.filter(phone_no=pno).delete()
    return redirect(dealerformview)
    
# employee operataions ---

def empform(request):
    return render(request,'emp.html')    

def empforminsert(request):
    try:
        emp_id = request.POST['emp_id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        email = request.POST['email']
        salary = request.POST['salary']
        phone_no = request.POST['phone_no']
        Employee(emp_id=emp_id,fname=fname,lname=lname,address=address,email=email,salary=salary,phone_no=phone_no).save()
    except IntegrityError:
        return render(request, "new.html")
    return redirect(empformview)

def empformview(request):
    empdata = Employee.objects.all()
    return render(request,'showempdata.html',{'empdata':empdata})

def empdelete(request):
    ID = request.GET['emp_id']
    Employee.objects.filter(emp_id=ID).delete()
    return redirect(empformview)

def empupdate(request):
    ID = request.GET['emp_id']
    for empdata in Employee.objects.filter(emp_id=ID):
        emp_id= empdata.emp_id
        fname = empdata.fname
        lname = empdata.lname
        address = empdata.address
        email = empdata.email
        salary = empdata.salary
        phone_no = empdata.phone_no
        dict = {'empdata':empdata}
    return render(request,'empupdate.html',dict)

def UpdateEmpRecord(request):
    id = request.GET['emp_id']
    emp_id = request.POST['emp_id']
    fname = request.POST['fname']
    lname = request.POST['lname']
    address = request.POST['address']
    email = request.POST['email']
    salary = request.POST['salary']
    phone_no = request.POST['phone_no']
    if id == emp_id:
        Employee.objects.filter(emp_id=id).update(fname=fname,lname=lname,address=address,email=email,salary=salary,phone_no=phone_no)
        return redirect(empformview)
    else:
        return render(request,'emperror.html')

def customerform(request):
    return render(request,'customer.html')

def customerinsert(request):
    try:
        cid = request.POST['cid']
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        Customer(cid=cid,fname=fname,lname=lname,address=address,email=email,phone_no=phone_no).save()
    except IntegrityError:
        return render(request, "new.html")
    return redirect(customerformview)


def customerformview(request):
    custdata = Customer.objects.all()
    dict = {'custdata':custdata}
    return render(request,'showcustomer.html',dict)

def deletecustomer(request):
    ID = request.GET['cid']
    Customer.objects.filter(cid=ID).delete()
    return redirect(customerformview)

def Updatecustomer(request):
    ID = request.GET['cid']
    for custdata in Customer.objects.filter(cid=ID):
        cid = custdata.cid
        fname = custdata.fname
        lname = custdata.lname
        address = custdata.address
        email = custdata.email
        phone_no = custdata.phone_no
        dict = {'custdata':custdata}
    return render(request,'updatecustomer.html',dict)

def UpdateCustomerRecord(request):
    ID = request.GET['cid']
    cid = request.POST['cid']
    fname = request.POST['fname']
    lname = request.POST['lname']
    address = request.POST['address']
    email = request.POST['email']
    phone_no = request.POST['phone_no']
    if ID == cid :
        Customer.objects.filter(cid=ID).update(fname=fname,lname=lname,address=address,email=email,phone_no=phone_no)
        return redirect(customerformview)
    else:
        return render(request,'custerror.html')

def medicineform(request):
    return render(request,'medicine.html')

def medicineinsert(request):
    try:
        m_id = request.POST['m_id']
        mname = request.POST['mname']
        dname = request.POST['dname']
        desc = request.POST['desc']
        price = request.POST['price']
        stock = request.POST['stock']
        expiry_date = request.POST['expiry_date']
        Medicine(m_id=m_id,mname=mname,dname=dname,desc=desc,price=price,stock=stock,expiry_date=expiry_date).save()
    except IntegrityError:
        return render(request, "new.html")
    return redirect(medicineformview)

def medicineformview(request):
    mdata = Medicine.objects.all()
    dict = {'mdata':mdata}
    return render(request,'showmedicine.html',dict)
    
def deletemedicine(request):
    ID = request.GET['m_id']
    Medicine.objects.filter(m_id=ID).delete()
    return redirect(medicineformview)

def Updatemedicineinfo(request):
    Id = request.GET['m_id']
    for mdata in Medicine.objects.filter(m_id=Id):
        m_id = mdata.m_id
        mname = mdata.mname
        dname = mdata.dname
        desc = mdata.desc
        price = mdata.price
        stock = mdata.stock
        expiry_date = mdata.expiry_date
        dict = {'mdata':mdata}
    return render(request,'updatemedicine.html',dict)

def updatemedicinerecord(request):
    ID = request.GET['m_id']
    m_id = request.POST['m_id']
    mname = request.POST['mname']
    dname = request.POST['dname']
    desc = request.POST['desc']
    price = request.POST['price']
    stock = request.POST['stock']
    expiry_date = request.POST['expiry_date']
    if m_id == ID:
        Medicine.objects.filter(m_id=ID).update(mname=mname,dname=dname,desc=desc,price=price,
        stock=stock,expiry_date=expiry_date)
        return redirect(medicineformview)
    else:
        return render(request,'custerror.html')

def Dealerpurchaseform(request):
    return render(request,'purchase.html')

def dealerpurchaseinsert(request):
    try:
        p_id = request.POST['p_id']
        mname = request.POST['mname']
        dname = request.POST['dname']
        desc = request.POST['desc']
        phone_no = request.POST['phone_no']
        price = request.POST['price']
        stock = request.POST['stock']
        total = (int(price)) * (int(stock))
        Purchase(p_id=p_id,mname=mname,dname=dname,desc=desc,
        phone_no=phone_no,price=price,stock=stock,total=total).save()
    except IntegrityError:
        return render(request, "new.html")
    return redirect(dealerpurchaseformview)

def dealerpurchaseformview(request):
    dpurdata = Purchase.objects.all()
    dict = {'dpurdata':dpurdata}
    return render(request,'showdealerpur.html',dict)

def dealerpurchasedelete(request):
    Id = request.GET['p_id']
    Purchase.objects.filter(p_id=Id).delete()
    return redirect(dealerpurchaseformview)

def Updatedealerpurchase(request):
    Id = request.GET['p_id']
    for dpurdata in Purchase.objects.filter(p_id=Id):
        p_id = dpurdata.p_id
        mname = dpurdata.mname
        dname = dpurdata.dname
        desc = dpurdata.desc
        phone_no = dpurdata.phone_no
        price = dpurdata.price
        stock = dpurdata.stock
        total = dpurdata.total
        dict = {'dpurdata':dpurdata}
    return render(request,'updatedealerpurchase.html',dict)

def Updtpurdealerrecord(request):
    Id = request.GET['p_id']
    p_id = request.POST['p_id']
    mname = request.POST['mname']
    dname = request.POST['dname']
    desc = request.POST['desc']
    phone_no = request.POST['phone_no']
    price = request.POST['price']
    stock = request.POST['stock']
    total = (int(price)) * (int(stock))
    if p_id == Id:
        Purchase.objects.filter(p_id=Id).update(mname=mname,dname=dname,desc=desc,phone_no=phone_no,
        price=price,stock=stock,total=total)
        return redirect(dealerpurchaseformview)
    else:
        return render(request,'custerror.html')

def Customerpurchaseform(requst):
    return render(requst,'custpurchase.html')

def custpurchinsert(request):
    try:
        p_id = request.POST['p_id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mname = request.POST['mname']
        desc = request.POST['desc']
        phone_no = request.POST['phone_no']
        price = request.POST['price']
        quantity = request.POST['quantity']
        total = (int(price)) * (int(quantity))
        Custpurchase(p_id=p_id,fname=fname,lname=lname,mname=mname,desc=desc,
        phone_no=phone_no,price=price,quantity=quantity,total=total).save()
    except IntegrityError:
        return render(request, "new.html")
    return redirect(custpurchaseformview)

def custpurchaseformview(request):
    cdata = Custpurchase.objects.all()
    dict = {'cdata':cdata}
    return render(request,'showcustpur.html',dict)

def custpurchdelete(request):
    Id = request.GET['p_id']
    Custpurchase.objects.filter(p_id=Id).delete()
    return redirect(custpurchaseformview)

def Updatecustpur(request):
    Id = request.GET['p_id']
    for cdata in Custpurchase.objects.filter(p_id=Id):
        p_id = cdata.p_id
        fname = cdata.fname
        lname = cdata.lname
        mname = cdata.mname
        desc = cdata.desc
        phone_no = cdata.phone_no
        price = cdata.price
        quantity = cdata.quantity
        total = cdata.total
        dict = {'cdata':cdata}
    return render(request,'updatecustpur.html',dict)

def Updatecustpurrecord(request):
    Id = request.GET['p_id']
    p_id = request.POST['p_id']
    fname = request.POST['fname']
    lname = request.POST['lname']
    mname = request.POST['mname']
    desc = request.POST['desc']
    phone_no = request.POST['phone_no']
    price = request.POST['price']
    quantity = request.POST['quantity']
    total = (int(price)) * (int(quantity))
    if p_id == Id:
        Custpurchase.objects.filter(p_id=Id).update(fname=fname,lname=lname,mname=mname,desc=desc,phone_no=phone_no,
        price=price,quantity=quantity,total=total)
        return redirect(custpurchaseformview)
    else:
        return render(request,'custerror.html')

def search_product(request):
    if request.method == "POST":
        query_name = request.POST.get('mname', None)
        if query_name:
            results = Medicine.objects.all().filter(mname__contains=query_name)
            return render(request, 'product-search.html', {"results":results})

    return render(request, 'product-search.html')
