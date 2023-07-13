# from django.db import models

# # Create your models here.
# class CounselPost(models.Model):
#     title = models.CharField(max_length=512)
#     content = models.TextField()
#     hashtag_choices = [('취업고민', '취업고민'), ('진로고민', '진로고민'), ('연애고민', '연애고민'), ('인간관계', '인간관계'), ('번아웃', '번아웃'),('다이어트', '다이어트')]
#     hashtag = models.CharField(max_length=128, choices = hashtag_choices)
#     date = models.DateField(auto_now_add=True)
#     post_like = models.IntegerField(default=0)
#     image = models.ImageField(blank=True, null=True, upload_to='post_image')


# class CounselComment(models.Model):
#     comment = models.TextField()
#     post = models.ForeignKey('post.CounselPost', null=True, blank=True, on_delete=models.CASCADE, related_name='post_comment')
#     comment_like = models.IntegerField(default=0)
#     date = models.DateField(auto_now_add=True)

# class CounselRecomment(models.Model):
#     recomment = models.TextField()
#     comment = models.ForeignKey('post.CounselComment', null=True, blank=True, on_delete=models.CASCADE, related_name='recomment')
#     recomment_like = models.IntegerField(default=0)
#     date = models.DateField(auto_now_add=True)

# class JarPost(models.Model):
#     content = models.TextField()
#     jar_like = models.IntegerField(default=0)
#     date = models.DateField(auto_now_add=True)
#     image = models.ImageField(blank=True, null=True, upload_to='post_image')