from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm, ProductForm  # ProductForm은 상품 등록 폼입니다

# 메인 페이지
def main_page(request):
    return render(request, 'main/main.html')


# 상품 상세 페이지
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 조회수 증가
    product.view_count += 1
    product.save()

    # 댓글을 작성일 순으로 정렬
    comments = product.comments.order_by('created_at')

    # POST 요청시 댓글 저장
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 폼에서 작성자 이름과 댓글 내용 받아서 저장
            comment = form.save(commit=False)
            comment.product = product  # 해당 상품에 댓글 연결
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'form': form,
    }
    return render(request, 'main/product_detail.html', context)


# 상품 등록 페이지
def product_register(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'main/product_register.html', context)


# 전체 상품 페이지
def all_products(request):
    # 기본적으로 모든 상품을 가져옵니다.
    products = Product.objects.all()

    # 검색어와 필터링 값 받기
    search_query = request.GET.get('search_query', '')
    school = request.GET.get('school', '')
    grade = request.GET.get('grade', '')
    subject = request.GET.get('subject', '')

    # 제목에서 검색어가 포함된 상품 필터링
    if search_query:
        products = products.filter(title__icontains=search_query)

    # 학교 필터링
    if school:
        products = products.filter(school=school)

    # 학년 필터링
    if grade:
        products = products.filter(grade=grade)

    # 과목 필터링
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


def popular_products(request):
    # 조회수가 많은 상위 10개 상품
    popular_products = Product.objects.order_by('-view_count')[:10]

    context = {
        'products': popular_products,
    }
    return render(request, 'main/popular_products.html', context)
