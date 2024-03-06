from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# from django.contrib.auth.tokens import default_token_generator 
from django.contrib.auth.models import *
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate
from django.http import JsonResponse,HttpResponse
import random
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import re


 

def index(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        cnt=c.count()
        wcnt=w.count()
        return render(r,'index.html',{'cnt':cnt,'wcnt':wcnt})
    else:
        return  render(r,'index.html')
def furni(r1): 
    if 'id' in r1.session:
        se=r1.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        cnt=c.count()
        wcnt=w.count()
        return render(r1,'furnitures.html',{'cnt':cnt,'wcnt':wcnt})
    else:
        return render(r1,'furnitures.html')
    
def company(r2):
    if 'id' in r2.session:
        se=r2.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        cnt=c.count()
        wcnt=w.count()
        return render(r2,'company.html',{'cnt':cnt,'wcnt':wcnt})
    else:
        return render(r2,'company.html')
    
def contact(r3):
    if 'id' in r3.session:
        se=r3.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        u=registration.objects.filter(id=val).first()
        cnt=c.count()
        wcnt=w.count()
        if r3.method=='POST':
            name=r3.POST.get('name')
            phone=r3.POST.get('phone')
            email=r3.POST.get('email')
            complaint=r3.POST.get('complaint')
            obj=complaints.objects.create(name=name,phone=phone,email=email,complaint=complaint)
            obj.save()
            return redirect(contact)
        return render(r3,'contact.html',{'cnt':cnt,'wcnt':wcnt,'u':u})
    else:
        return redirect(login)
    



    
def about(r4):
    if 'id' in r4.session:
        se=r4.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        cnt=c.count()
        wcnt=w.count()
        return render(r4,'about.html',{'cnt':cnt,'wcnt':wcnt})
    else:
        return render(r4,'about.html')
    


#******************Search Buttton ****************
    
def search(s):
    if 'id' in s.session:
        se=s.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        u=registration.objects.filter(id=val).first()
        cnt=c.count()
        wcnt=w.count() 
        cnt=c.count()
        if s.method=='POST':
            search_term=s.POST.get('search')
            obj=product.objects.filter(name__icontains=search_term)
        return render(s,'search.html',{'obj':obj,'u':u,'cnt':cnt,'wcnt':wcnt})
    else:
        if s.method=='POST':
            search_term=s.POST.get('search')
            obj=product.objects.filter(name__icontains=search_term)
            return render(s,'search.html',{'obj':obj})
        return redirect(index)


# ****************** login and signup page and logout *************************#

def signup(r5):
    if r5.method=='POST':
        Name=r5.POST.get('name')
        Number=r5.POST.get('number')
        Email=r5.POST.get('email')
        Username=r5.POST.get('username')
        Password=r5.POST.get('password')
        Confirm=r5.POST.get('confirm')
        if Password==Confirm:
            if registration.objects.filter(Username=Username).exists():
                messages.info(r5,"Username already exists",extra_tags='myusr')
                return redirect(signup)
            elif registration.objects.filter(Email=Email).exists():
                messages.info(r5,"Email already exists",extra_tags='mymail')
                return redirect(signup)
            else:
                val1=User.objects.create_user(first_name=Name,last_name=Number,email=Email,username=Username,password=Password)
                val1.save()
                obj=registration.objects.create(Name=Name,Number=Number,Email=Email,Username=Username,Password=Password)
                obj.save()
                usr=registration.objects.filter(Username=Username).first()
                r5.session['id']=[usr.id]
                return redirect(signup)
        else:
            messages.info(r5,"Password doesn't exists",extra_tags='mypass')
            return redirect(signup)
    return render(r5,'login.html')
    

def login(r6):
    if r6.method=='POST':
        Username=r6.POST.get('username')
        Password=r6.POST.get('password')
        if Username=='admin':
            if Password=='1234':
                return render(r6,'admin/adminindex.html')
            
            else:
                messages.info(r6,"Incorrect Password",extra_tags='mynotpass')
                return redirect(login)

        elif registration.objects.filter(Username=Username).exists():
            usr=registration.objects.filter(Username=Username).first()
            user=authenticate(username=Username,password=Password)
            if user is not None:
                r6.session['id']=[usr.id]
                return redirect(index)
            else:
                messages.info(r6,"Incorrect Password",extra_tags='mynotpass')
                return redirect(login)
        else:
            messages.info(r6,"User Not Found",extra_tags='mynotfnd')
            return redirect(login)
    return render(r6,'login.html')


def logout(r13):
    if 'id' in r13.session:
        r13.session.pop('id')
        messages.info(r13,'logout succesfully')
        return redirect(index)
    return render(r13,'index.html')

#************************************************************************#
    
def cartt(r7):
    if 'id' in r7.session:
        se=r7.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        wcnt=w.count()
        cnt=c.count()
        c1 = {}
        t=0
        for i in c:
            c1[i.products]=[i.quantity,i.id,i.products.price*i.quantity]
            t=t+(i.products.price*i.quantity)
        usr = registration.objects.filter(id=val).first()
        return render(r7,'cart.html',{"usr":usr,"c1":c1,'cnt':cnt,'t':t,'wcnt':wcnt})
    return redirect(login)

def addtocart(a1,wal=0):
    if 'id' in a1.session:
        se=a1.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        if a1.method=='POST':
            p=product.objects.filter(id=wal).first()
            user=registration.objects.get(id=val)
            if c:
                f=0
                for i in c:
                    if i.products==p:
                        f=1
                        i.quantity=i.quantity+1
                        i.save()
                        return redirect(cartt)
                if f==0:
                    val=mycart.objects.create(user=user,products=p,quantity=1,delivered=False)
                    val.save()
                    return redirect(cartt)
            else:
                val=mycart.objects.create(user=user,products=p,quantity=1,delivered=False)
                val.save()
                return redirect(cartt)
    return redirect(login)


def wishlist(wi):
    if 'id' in wi.session:
        se=wi.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        user=registration.objects.filter(id=val).first()
        cnt=c.count()
        wcnt=w.count()
        c1={}
        c=mycart.objects.filter(user=val).all()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        for i in w:
            c1[i.products]=[i.id]
        user=registration.objects.filter(Username=val).first()
        return render(wi,'whishlist.html',{"user":user,"wcnt":wcnt,"c1":c1,'cnt':cnt,'w':w})
    return redirect(login)


def addwish(aw,wal=0):
    if 'id' in aw.session:
        se=aw.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        if aw.method=='POST':
            p=product.objects.filter(id=wal).first()
            user=registration.objects.filter(id=val).first()
            if w:
                val=wish.objects.create(user=user,products=p)
                val.save()
                return redirect(wishlist)
            else:
                val=wish.objects.create(user=user,products=p)
                val.save()
                return redirect(wishlist)
    return redirect(login)


def delwish(dele,de):
    if 'id' in dele.session:
        se=dele.session.get('id')
        val=se[0]
        w=wish.objects.get(id=de)
        w.delete()
        return redirect(wishlist)

def seemore(r8):
    if 'id' in r8.session:
        se=r8.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        wcnt=w.count()
        cnt=c.count()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        obj=product.objects.all()
        return render(r8,'seemore.html',{'obj':obj,'cnt':cnt,'wcnt':wcnt,'ca':ca})
    else:
        obj=product.objects.all()
        return render(r8,'seemore.html',{'obj':obj})

# single product views 
def product_list(p,wal):
    if 'id' in p.session:
        se=p.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        cnt=c.count()
        wcnt=w.count()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        l=product.objects.filter(id=wal).first()
        return  render(p,'product_list.html',{'l':l,'cnt':cnt,'wcnt':wcnt,'ca':ca})
    else:
        l=product.objects.filter(id=wal).first()
        return  render(p,'product_list.html',{'l':l})


# ***************** user pages ********************** #

# def userprofile(r9):
#     return render(r9,'userprofile.html')

def userr(us):
    if 'id' in us.session:
        se=us.session.get('id')
        val=se[0]
        user=registration.objects.filter(id=val).first()
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        wcnt=w.count()
        cnt=c.count()
        return render(us,'user.html',{'user':user,'cnt':cnt,'wcnt':wcnt})  
    return render(us,'user.html')

def uedit(ed):
    se=ed.session.get('id')
    val=se[0]
    u=registration.objects.filter(id=val).first()
    w=wish.objects.filter(user=val).all()
    c=mycart.objects.filter(user=val).all()
    wcnt=w.count()
    cnt=c.count()
    return render(ed,'uedit.html',{'u':u,'cnt':cnt,'wcnt':wcnt})

def uedit1(ed1):
    se=ed1.session.get('id')
    val=se[0]
    w=wish.objects.filter(user=val).all()
    c=mycart.objects.filter(user=val).all()
    u=registration.objects.get(id=val)
    b=User.objects.get(username=u.Username)
    cnt=c.count()
    wcnt=w.count()
    if ed1.method=='POST':
        u.Name=ed1.POST.get('name')
        u.Email=ed1.POST.get('email')
        u.Number=ed1.POST.get('number')

        b.first_name=ed1.POST.get('name')
        b.email=ed1.POST.get('email')
        b.last_name=ed1.POST.get('number')
        u.save()
        b.save()
        return redirect(userr)
    return render(ed1,'uedit.html',{'u':u,'cnt':cnt,'wcnt':wcnt})


def ureset(ur):
    se=ur.session.get('id')
    val=se[0]
    w=wish.objects.filter(user=val).all()
    c=mycart.objects.filter(user=val).all()
    usr=registration.objects.filter(id=val).first()
    cnt=c.count()
    wcnt=w.count()
    return render(ur,'ureset.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt})

def ureset1(ur1):
    se=ur1.session.get('id')
    val=se[0]
    w=wish.objects.filter(user=val).all()
    c=mycart.objects.filter(user=val).all()
    usr=registration.objects.filter(id=val).first()
    cnt=c.count()
    wcnt=w.count()
    if ur1.method=='POST':
        np=ur1.POST.get('newpass')
        cp=ur1.POST.get('confirmpass')
        user=authenticate(username=usr.Username,password=ur1.POST.get('oldpass'))         
        if user is not None:
            if np==cp:
                user.set_password(np)
                user.save()
                usr.Password=np
                usr.save()
                return redirect(userr)
            else:
                messages.info(ur1,"password doesn't exist")
                return redirect(userr)
        else:
            messages.info(ur1,'password wrong')
            return redirect(userr)
    return render(ur1,'user.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt})

    
#********************************************************************#

def checkout(r12):
    if 'id' in r12.session:
        se=r12.session.get('id')
        val=se[0]
        w=wish.objects.filter(user=val).all()
        c=mycart.objects.filter(user=val).all()
        cnt=c.count()
        wcnt=w.count()
        c1 = {}
        t=0
        for i in c:
            c1[i.products]=[i.quantity,i.id,i.products.price*i.quantity]
            t=t+(i.products.price*i.quantity)
        usr = registration.objects.filter(id=val).first()
        return render(r12,'checkout.html',{"usr":usr,"c1":c1,'cnt':cnt,'t':t,'wcnt':wcnt})
    else:
        return render(r12,'checkout.html')








# quantity increase
def pluscart(p,de):
    if 'id' in p.session:
        c=mycart.objects.get(id=de)
        c.quantity = c.quantity + 1
        c.save()
        return redirect(cartt)

#quantity decrease
def minuscart(m,de):
    if 'id' in m.session:
        c=mycart.objects.get(id=de)
        if c.quantity>1:
            c.quantity = c.quantity - 1
            c.save()
        else:
            c.delete()
        return redirect(cartt)
        
#delete order
def deletecart(d,de):
    if 'id' in d.session:
        c=mycart.objects.get(id=de)
        c.delete()
        return redirect(cartt)








# ************************ admin pages ********************** #

def adminindex(ad):
    return render(ad,'admin/adminindex.html')

def userdetails(ud):
    obj=registration.objects.all()
    return render(ud,'admin/userdetails.html',{'obj':obj})

def products(pd):
    obj1=product.objects.all()
    return render(pd,'admin/products.html',{'obj1':obj1})

def addproduct(add):
    if add.method=='POST':
        name=add.POST.get('name')
        price=add.POST.get('number')
        wood=add.POST.get('wood')
        colour=add.POST.get('colour')
        desc=add.POST.get('desc')
        img=add.FILES.get('img')
        obj=product.objects.create(name=name,price=price,wood=wood,colour=colour,description=desc,image=img)
        obj.save()
        return redirect(products)
    return render(add,'admin/addproducts.html')

def edit(ed,wal):
    l=product.objects.filter(id=wal).first()
    return render(ed,'admin/edit.html',{'l':l})

def edit1(ed1,wal1):
    l=product.objects.get(id=wal1)
    if ed1.method=='POST':
        if ed1.POST.get("save")=='save':
            l.name=ed1.POST.get('name')
            l.price=ed1.POST.get('price')
            l.wood=ed1.POST.get('wood')
            l.colour=ed1.POST.get('colour')
            l.description=ed1.POST.get('desc')
            img=ed1.FILES.get('img')
            if img==None:
                l.save()
            else:
                l.image=ed1.FILES.get('img')
                l.save()
            return redirect(products)
    return render(ed1,'admin/products.html')

def admindelete(de,id):
    c=product.objects.get(pk=id)
    c.delete()
    return redirect(products)

def comp(com):
    com1=complaints.objects.all()
    return render(com,'admin/complaints.html',{'com1':com1})

def reply(r,em):
    l=complaints.objects.filter(id=em).first()
    return render(r,"admin/replymail.html",{'l':l})

def replymail(r,em):
    if r.method=='POST':
        l=complaints.objects.filter(id=em).first()
        n=r.POST.get('message')
        send_mail('Reset Your Password', f'{n}','settings.EMAIL_HOST_USER', [l.email],fail_silently=False)
        return redirect(comp)
    return render(r, 'admin/replymail.html')

def comdelete(de,wal):
    c=complaints.objects.get(id=wal)
    c.delete()
    return redirect(comp)


def userbooking(r):
    l= order.objects.all()
    return render(r,'admin/userbooking.html',{'l':l})


def statusup(r,wal):
    if r.method == "POST":
        st = order.objects.get(id=wal)
        st.status = r.POST.get('status')
        st.save()
        return redirect(userbooking)





# payment methods
#************************


def placeorder(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = registration.objects.get(id = val)
        c = mycart.objects.filter(user=val).all()
        t=0
        for i in c:
            t=t+(i.products.price*i.quantity)
        if r.method == 'POST':
            if profile.objects.filter(user=usr) == None:
                userprofile = profile()
                userprofile.user = usr
                userprofile.fname = r.POST.get('fname')
                userprofile.lname = r.POST.get('lname')
                userprofile.email = r.POST.get('email')
                userprofile.district = r.POST.get('district')
                userprofile.phone = r.POST.get('phone')
                userprofile.address = r.POST.get('address')
                userprofile.state = r.POST.get('state')
                userprofile.save()

            neworder = order()
            neworder.user = usr
            neworder.fname = r.POST.get('fname')
            neworder.lname = r.POST.get('lname')
            neworder.email = r.POST.get('email')
            neworder.district = r.POST.get('district')
            neworder.phone = r.POST.get('phone')
            neworder.address = r.POST.get('address')  
            neworder.state = r.POST.get('state')
            

            neworder.total_price = t

            neworder.payment_mode = r.POST.get('payment_mode')
            neworder.payment_id = r.POST.get('payment_id')

            trackno = 'woodo'+str(random.randint(1111111,9999999))
            while order.objects.filter(tracking_no=trackno) is None:
                trackno = 'woodo'+str(random.randint(1111111,9999999))
            neworder.tracking_no = trackno
            neworder.save()

            for item in c:
                orderitem.objects.create(
                    orderdet = neworder,
                    product = item.products,
                    price = item.products.price,
                    quantity = item.quantity
                )

            mycart.objects.filter(user=val).delete()

            messages.success(r, 'Your order has been placed successfully')

            payMode = r.POST.get('payment_mode')
            if payMode == "Razorpay":
                return JsonResponse({'status':'Your order has been placed successfully'})

        return redirect(index)
    

def razorpaycheck(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        c = mycart.objects.filter(user=val).all()
        t=0
        for i in c:
            t=t+(i.products.price*i.quantity)

    return JsonResponse({
        'total_price':t
    })

def orderss(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = registration.objects.get(id=val)
        o = order.objects.all()
        l=[]
        for i in o:
            if i.user==usr:
                l.append(i)
        return render(r,'myorders.html',{'l':l})
    return render(r,'myorders.html')












# Create your views here.
