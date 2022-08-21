from django.shortcuts import render,redirect
from store.models import Category,Product,Cart,Order,OrderItem
from django.contrib.auth.models import User
from store import forms
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def get_current_user(request):
    try:
        user = User.objects.get(id=request.user.id)
    except ObjectDoesNotExist:
        return None
    return user.id

def store_home(request):   
    if request.method=="POST":
        search = request.POST["search"]
        products = Product.objects.filter(name__icontains=search)
        categories = Category.objects.all()
    else:
        products = Product.objects.all()
        categories = Category.objects.all()
    try:
        customer = Order.objects.get(customer__id=get_current_user(request))
    except ObjectDoesNotExist:
        customer = None

    paginatior = Paginator(products, 9)
    page_number = request.GET.get('page')
    try:
        products = paginatior.page(page_number)
    except PageNotAnInteger:
        products = paginatior.page(1)
    except EmptyPage:
        products = paginatior.page(paginator.num_pages)
    return render(request, "store/store.html", {"products": products, "categories": categories,'customer':customer})


def store_product_category_view(request,id=None):
    categories = Category.objects.all()
    products = Product.objects.filter(category__id=id)
    return render(request, "store/store.html", {"products": products, "categories": categories})

def store_product_details(request,id=None):
    product = Product.objects.get(id=id)
    request.session["product_id"] = id
    categories = Category.objects.all()
    return render(request, "store/product_details.html", {"product": product, "categories": categories})

def store_cart_view(request):
    if request.method =="POST":
        cart_id = request.POST["cart_id"]
        cart = Cart.objects.get(id=cart_id).delete()
    user = User.objects.get(id=request.user.id)
    carts = Cart.objects.filter(customer__id=user.id)
    total_price = 0
    for cart in carts:
        total_price += cart.total
    if carts:
        sent = True
    else:
        sent = False
    return render(request, "store/cart.html",{"carts":carts,"total_price":total_price,"sent":sent})

def store_cart_create_view(request):
    product_id = request.session["product_id"]
    user = User.objects.get(id=request.user.id)
    product = Product.objects.get(id=product_id)

    if Cart.objects.filter(product__id=product.id,customer__id=user.id).exists():
        messages.info(request, "Item already exists in cart..!")
        return redirect("/cart")
    del request.session["product_id"]
    #cart creation
    cart = Cart(customer=user,product=product,total=product.price)
    cart.save()
    carts = Cart.objects.all()
    return redirect("/cart")

def store_order_create_view(request):
    form=None
    order=None
    product=None
    quantity = None
    product_id=None
    if request.method =="POST":
        quantity = request.POST["quantity"]
        size = request.POST["size"]
        product_id = request.POST["product_id"]

        request.session['quantity'] = quantity
        request.session['size'] = size
        request.session['product_id'] = product_id
    
    quantity = request.session['quantity']
    product_id = request.session['product_id']
    size = request.session['size']
    try:
        product = Product.objects.get(id=product_id)
        total_price = product.price*int(quantity)+1
        request.session['total_price'] = total_price
    except ObjectDoesNotExist:
        pass
    user = User.objects.get(id=request.user.id)
    if Order.objects.filter(customer__id=user.id).exists():
        sent = True
        order = Order.objects.get(customer__id=user.id)
    else:
        sent = False
        form = forms.CheckoutUserForm()
    context = {
        'form': form, "order": order, "sent": sent, "product": product, 
        "quantity": quantity, "total_price": total_price,"size":size
    }
    return render(request, "store/order.html", context)

def store_order_save_view(request):
    if request.method =="POST":
        user = User.objects.get(id=request.user.id)
        if Order.objects.filter(customer__id=user.id).exists():
            messages.info(request, "Address already exists to the Customer.!")
            return redirect("/order_create")
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        postal_code = request.POST["zip_code"]
        city = request.POST["city"]

        user.first_name = first_name
        user.last_name  = last_name
        user.email = email
        user.save()
        order = Order(customer=user,mobile=mobile,address=address,postal_code=postal_code,city=city)
        order.save()
        return redirect("/order_create")

    
def store_order_item_view(request):
    quantity = request.session['quantity']
    product_id = request.session['product_id']
    size = request.session['size']
    total_price =  request.session['total_price']

    if request.method =="POST":
        payment = request.POST["payment"]
        print(payment)
        product = Product.objects.get(id=product_id)
        user = User.objects.get(id=request.user.id)
        try:
            address = Order.objects.get(customer__id=user.id)
        except ObjectDoesNotExist:
            address =None
        
        # Creating Order Items   
        ordered_item = OrderItem(order=address,product=product,price=product.price,quantity=quantity,total=total_price,size=size,payment=payment)
        ordered_item.save()

        del request.session['quantity']
        del request.session['product_id']
        del request.session['size']
        del request.session['total_price']
        return redirect("/ordered_track")


def store_ordered_items_track(request):
    user = get_current_user(request)
    ordered_items = OrderItem.objects.filter(order__customer__id=user)
    if ordered_items:
        sent = True
    else:
        sent = False
    return render(request, "store/order_track.html", {"ordered_items":ordered_items,"sent":sent})


def store_cart_checkout_view(request):
    if Order.objects.filter(customer__id=get_current_user(request)).exists():
        carts = Cart.objects.filter(customer__id=get_current_user(request))
        order = Order.objects.get(customer__id=get_current_user(request))
        for cart in carts:
            item = Cart.objects.get(id=cart.id)
            product = Product.objects.get(id=item.product.id)
            ordered_items = OrderItem(order=order,product=product,price=product.price,quantity=item.quantity,total=item.total,size=cart.size)
            ordered_items.save()           

    else:
        messages.info(request, "Update Your Address first,Kindly....!")
        return redirect("/address_update")
    return redirect("/ordered_track")

def store_cart_items_update(request):
    categories = Category.objects.all()
    carts = Cart.objects.filter(customer__id=get_current_user(request))
    if request.method =="POST":
        cart_id = request.POST["cart_id"]
        quantity = request.POST["quantity"]
        size = request.POST["size"]
        
        cart = Cart.objects.get(id = cart_id)
        price = cart.product.price
        total_price = int(price) * int(quantity)
        cart.quantity = quantity
        cart.size = size
        cart.total = total_price
        cart.save()
        return redirect("/cart")
    return render(request, "store/cart_update.html",{"carts":carts,"categories":categories})


#user account
def store_user_profile(request):
    try:
        user = Order.objects.get(customer__id=get_current_user(request))
    except ObjectDoesNotExist:
        return HttpResponse("Kindly,Re-login again...!")
    return render(request, "registration/account.html",{'user':user})

def store_user_profile_orders(request):
    orders = OrderItem.objects.filter(
        order__customer__id=get_current_user(request), status='Delivered')
    if orders:
        sent = True
    else:
        sent = False
    return render(request, "registration/orders.html",{'orders':orders,'sent':sent})

def store_user_profile_address(request):
    try:
        address = Order.objects.get(customer__id=get_current_user(request))
    except ObjectDoesNotExist:
        address = False
    return render(request, "registration/address.html",{'address':address})

def store_user_profile_update(request):
    if request.method=="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        city = request.POST["city"]
        postal_code = request.POST["postal_code"]

        user = User.objects.get(id=get_current_user(request))
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        order = Order.objects.get(customer__id=user.id)
        order.mobile = mobile
        order.address = address
        order.city = city
        order.postal_code = postal_code
        order.save()
        return redirect("/address")
    return render(request, "registration/address_update.html")

def Order_user_profile_update(request):
    form = forms.ProfileForm()
    if request.method =="POST":
        form = forms.ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            order = Order.objects.get(customer__id=get_current_user(request))
            image = form.cleaned_data["image"]
            order.image = image
            order.save()
            return redirect("/profile")
    return render(request, "registration/pic_update.html",{'form':form})

def customer_password_change(request):
    if request.method=="POST":
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 and password2 and password1 != password2:
            messages.info(request, "both Passwords should be same..!")
        user = User.objects.get(id=get_current_user(request))
        user.set_password(password1)
        user.save()
        messages.info(request, "Password Changed Successfully..!")
    return redirect("/address_update")




#authentication
def customer_login_view(request):
    form = forms.LoginPageForm()
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.get(username=username)
        #user = authenticate(username,password)
        if user.check_password(password):
            login(request, user)
            return redirect("/store")
        messages.error(request,"invalid password and user.!")
    return render(request, "authenticate/login.html",{'form':form})

def customer_logout_view(request):
    logout(request)
    return redirect("/store")

def customer_register_view(request):
    form = forms.RegsiterForm()
    if request.method =="POST":
        form = forms.RegsiterForm(request.POST)
        if form.is_valid():
           username = request.POST['username']
           first_name = request.POST['first_name']
           last_name = request.POST['last_name']
           email = request.POST['email']
           password1 = request.POST['password1']
           password2 = request.POST['password2']
           
           if password1 and password2 and password1 != password2:
               messages.warning(request, "Both Passwords must be Same.!")
               return redirect("/register")
           user = User(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
           user.set_password(user.password)
           user.save()
           order = Order(customer=user)
           order.save()
           return redirect("/login")
    return render(request, "authenticate/signup.html",{'form':form})
