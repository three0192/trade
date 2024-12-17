from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Comment, Profile
from .forms import CommentForm, ProductForm

# 메인 페이지
def main_page(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'main/main.html', {'username': username})

# 상품 상세 페이지
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 조회수 증가
    product.view_count += 1
    product.save()

    # 댓글 정렬
    comments = product.comments.order_by('created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    context = {'product': product, 'comments': comments, 'form': form}
    return render(request, 'main/product_detail.html', context)

# 상품 등록 페이지
@login_required
def product_register(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'main/product_register.html', context)

# 전체 상품 페이지
def all_products(request):
    products = Product.objects.all()
    search_query = request.GET.get('search_query', '')
    school = request.GET.get('school', '')
    grade = request.GET.get('grade', '')
    subject = request.GET.get('subject', '')

    if search_query:
        products = products.filter(title__icontains=search_query)
    if school:
        products = products.filter(school=school)
    if grade:
        products = products.filter(grade=grade)
    if subject:
        products = products.filter(subject=subject)

    context = {
        'products': products,
        'search_query': search_query,
        'school': school,
        'grade': grade,
        'subject': subject,
    }
    return render(request, 'main/all_products.html', context)

# 인기 상품 페이지
def popular_products(request):
    popular_products = Product.objects.order_by('-view_count')[:10]
    context = {'products': popular_products}
    return render(request, 'main/popular_products.html', context)

# 로그인 페이지
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
    return render(request, 'main/login.html')

# 회원가입 페이지
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        school = request.POST['school']
        grade = request.POST['grade']
        name = request.POST['name']

        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 사용 중인 아이디입니다.')  # 실패 메시지
        else:
            try:
                # 유저 생성 및 프로필 저장
                user = User.objects.create_user(username=username, password=password, first_name=name)
                profile = Profile(user=user, school=school, grade=grade)
                profile.save()
                messages.success(request, '회원가입이 완료되었습니다.')  # 성공 메시지
                return redirect('main_page')  # 메인 페이지로 리다이렉트
            except Exception as e:
                messages.error(request, f'회원가입에 실패했습니다: {e}')  # 예외 처리로 실패 메시지
    return render(request, 'main/signup.html')

# 로그아웃 처리
def logout_view(request):
    logout(request)
    messages.success(request, '로그아웃되었습니다.')
    return redirect('main_page')
