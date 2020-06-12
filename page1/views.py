from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import customer,product,cart,client,contact
from math import ceil
# Create your views here.
# for home page
def home(request,m=9):
    allprods=[]
    catprods=product.objects.values('category')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslides=(n//4+ceil(n/4-n//4))
        allprods.append([prod,range(1,nslides),nslides])
    param={'allprods':allprods,'msg':m}
    return render(request,'page1/homeb.html',param)
def matching(prod,value):
    pro=[]
    for i in prod:
        if i.product_name.lower().find(value.lower())!=-1 or i.desc.lower().find(value.lower())!=-1:
            pro.append(i)
            print(pro)
    return pro
def search(request):
    allprods=[]
    catprods=product.objects.values('category')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        prod=matching(prod,request.GET['txt'])
        print(prod)
        n=len(prod)
        nslides=(n//4+ceil(n/4-n//4))
        if prod:
            allprods.append([prod,range(1,nslides),nslides])
    if allprods:
        param={'allprods':allprods}
    else:
        param={'msg':"NO result found"}
    return render(request,'page1/search.html',param)
def about(request):
    return render(request,'page1/about.html')
def contact1(request):
    if request.method=="POST":
        x=contact(email=request.POST['txtemail'],user_name=request.POST['txtname'],mobile=request.POST['txtmob'],desc=request.POST['txtdesc'])
        x.save()
        return redirect('/')
    return render(request,'page1/contact.html')
# after login if user want to go to userdash
def gotouserdash(request):
    if request.session.has_key('skey'):
        return redirect('userdash')
    elif request.session.has_key('ske'):
        return redirect('userdashc')
    return home(request,8)
def productview(request):
    s=product.objects.get(pk=request.GET['q'])
    return render(request,'page1/productview.html',{'r':s})
# for cart
def addcart(request):
    if request.method=="POST":
        e=cart.objects.get(product_id=request.GET['q'])
        qua=e.quantity
        qua=qua+int(request.POST['txtquantity'])
        e.quantity=qua
        e.save()
        return redirect('/')
    if request.session.has_key('skey'):
        procart=request.GET['c']
        print(procart)
        pro=product.objects.get(pk=procart)
        cus=customer.objects.get(mobile=request.session['skey'])
        b=cart.objects.filter(product_id=procart)
        if b:
            pass
        else:
            s=cart(product_id=procart,customer_name=cus.user_name)
            s.save()
        return render(request,'page1/quantity.html',{'r':procart,'s':pro})
    return redirect('/')
def checkout(request):
    if request.session.has_key('skey'):
        return redirect('userdash')
    return home(request,8)
def emovequantity(request):
    ca=cart.objects.get(pk=request.GET['q'])
    qua=ca.quantity
    if qua==0 or qua==1:
        ca.delete()
    else:
        qua-=1
        ca.quantity=qua
        ca.save()
    return redirect('userdash')
def ddquantity(request):
    ca=cart.objects.get(pk=request.GET['q'])
    qua=ca.quantity
    if qua==0 or qua==1:
        ca.delete()
    else:
        qua+=1
        ca.quantity=qua
        ca.save()
    return redirect('userdash')
# for customer
def signup(request):
    if request.method=="POST":
        s=customer(user_name=request.POST['txtname'],password=request.POST['txtpass'],mobile=request.POST['txtmob'],email=request.POST['txtemail'])
        s.save()
        return redirect('/')
    return render(request,'page1/signup.html')
def login(request):
    if request.method=="POST":
        s=customer.objects.filter(mobile=request.POST['txtmob'],password=request.POST['txtpass'])
        if s:
            request.session['skey']=request.POST['txtmob']
            return redirect('userdash')
        else:
            return render(request,'page1/login.html',{'msg':8})
    return render(request,'page1/login.html')
def userdash(request):
    if request.session.has_key('skey'):
        s=customer.objects.get(mobile=request.session['skey'])
        ca=cart.objects.filter(customer_name=s.user_name)
        pri=0
        prolist=[]
        for i in ca:
            pro=product.objects.get(pk=i.product_id)
            qua=i.quantity
            pricequan=qua*pro.price
            prolist.append([qua,pricequan,pro,i])
            pri=pri+pricequan
        return render(request,'page1/userdash.html',{'r':s,'prolis':prolist,'pric':pri})
    return redirect('/')
def logout(request):
    del request.session['skey']
    return redirect('/')
def find(request):
    s=customer.objects.get(pk=request.GET['q'])
    return render(request,'page1/update.html',{'msg':s})
def update(request):
    s=customer.objects.get(pk=request.GET['q'])
    s.user_name=request.POST['txtname']
    s.password=request.POST['txtpass']
    s.mobile=request.POST['txtmob']
    s.email=request.POST['txtemail']
    s.save()
    return redirect('userdash')
def delete(request):
    s=customer.objects.get(pk=request.GET['q'])
    s.delete()
    return redirect('userdash')
# end customer
# for client
def signupc(request):
    if request.method=="POST":
        s=client(user_name=request.POST['txtname'],password=request.POST['txtpass'],mobile=request.POST['txtmob'],email=request.POST['txtemail'])
        s.save()
        return redirect('/')
    return render(request,'page1/signupc.html')
def loginc(request):
    if request.method=="POST":
        s=client.objects.filter(mobile=request.POST['txtmob'],password=request.POST['txtpass'])
        if s:
            request.session['ske']=request.POST['txtmob']
            return redirect('userdashc')
        else:
            return render(request,'page1/loginc.html',{'msg':8})
    return render(request,'page1/loginc.html')
def userdashc(request):
    if request.session.has_key('ske'):
        s=client.objects.get(mobile=request.session['ske'])
        p=product.objects.filter(client_name=s.user_name)
        return render(request,'page1/userdashc.html',{'r':s,'q':p})
    return redirect('/')
# for adding product
def add(request):
    if request.method=="POST":
        s=product(client_name=request.POST['txtuser'],product_name=request.POST['txtname'],category=request.POST['txtcat'],subcategoru=request.POST['txtsub'],desc=request.POST['txtdesc'],price=request.POST['txtprice'],pub_date=request.POST['txtpub'],image=request.FILES['txtimage'])
        s.save()
        return redirect('userdashc')
    else:
        cl=client.objects.get(pk=request.GET['q'])
        user=cl.user_name
        return render(request,'page1/add.html',{'name':user})
# for removing product
def remove(request):
    s=product.objects.get(pk=request.GET['q'])
    s.delete()
    return redirect('userdashc')
# edit product
def editproduct(request):
    if request.method=="POST":
        s=product.objects.get(pk=request.GET['q'])
        s.client_name=request.POST['txtuser']
        s.product_name=request.POST['txtname']
        s.category=request.POST['txtcat']
        s.subcategoru=request.POST['txtsub']
        s.desc=request.POST['txtdesc']
        s.price=request.POST['txtprice']
        s.pub_date=request.POST['txtpub']
        s.image=request.FILES['txtimage']
        s.save()
        return redirect('userdashc')
    s=product.objects.get(pk=request.GET.get('q'))
    return render(request,'page1/editproduct.html',{'msg':s})
def logoutc(request):
    del request.session['ske']
    return redirect('/')
def findc(request):
    s=client.objects.get(pk=request.GET.get('q'))
    return render(request,'page1/updatec.html',{'msg':s})
def updatec(request):
    s=client.objects.get(pk=request.GET['q'])
    s.user_name=request.POST['txtname']
    s.password=request.POST['txtpass']
    s.mobile=request.POST['txtmob']
    s.email=request.POST['txtemail']
    s.save()
    return redirect('userdashc')
def deletec(request):
    s=client.objects.get(pk=request.GET['q'])
    s.delete()
    return redirect('userdashc')
# end client