from django.db import models
from decimal import Decimal

# 과목 선택지
SUBJECT_CHOICES = [
    ('korean', '국어'),
    ('english', '영어'),
    ('math', '수학'),
    ('history', '한국사'),
    ('social', '사회 탐구'),
    ('science', '과학 탐구'),
]

# 학년 선택지
GRADE_CHOICES = [
    ('1', '1학년'),
    ('2', '2학년'),
    ('3', '3학년'),
]

# 학교 선택지
SCHOOL_CHOICES = [
    ('middle', '중학교'),
    ('high', '고등학교'),
]

# 상품 모델
class Product(models.Model):
    title = models.CharField(max_length=200)  # 상품 제목
    description = models.TextField()  # 상품 설명
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 가격
    school = models.CharField(max_length=10, choices=SCHOOL_CHOICES)  # 학교 선택
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)  # 과목 선택
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES)  # 학년 선택
    is_free = models.BooleanField(default=False)  # 무료 여부
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)  # 사진 업로드
    view_count = models.PositiveIntegerField(default=0)  # 조회수 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)  # 등록일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def formatted_price(self):
        """소수점 없는 가격을 반환"""
        return int(self.price.quantize(Decimal('1')))

    def __str__(self):
        return self.title

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)  # 연결된 상품
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글 작성일
    name = models.CharField(max_length=100, default='익명')  # 댓글 작성자 이름 필드 추가 #기본값=익명

    def __str__(self):
        return f"Comment on {self.product.title} by {self.name} at {self.created_at}"