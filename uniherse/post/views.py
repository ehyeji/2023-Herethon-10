# from django.shortcuts import render, redirect
# from .models import CounselRecomment, CounselComment, CounselPost
# from .forms import CounselCommentForm, CounselPostForm, CounselRecommentForm, JarPostForm
# # Create your views here.
# def home(request):
#     post = CounselPost.objects.filter().order_by('-like')
#     return render(request, '#html파일이름', {'post':post})

# def write_post(request):
#     if request.method == 'POST':
#         form = CounselPost(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('고민상담으로 이동')
#     else:
#         form = CounselPostForm()
#         return render(request, '포스트작성칸html', {'form':form})

# def counsel_post_list(request):
#     posts = CounselPost.objects.all().order_by('-date')
#     return render(request, '리스트보여주는 html', {'posts':posts})

# def post_detail(request, id):
#     post = CounselPost.objects.get(id=id)
#     return render(request, '디테일페이지', {'post':post})

# def post_update(request, id):
#     post = CounselPost.objects.get(id=id)
#     if request.method == 'POST':
#         form = CounselPostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('리스트')
#     else: 
#         form = CounselPostForm(instance=post)
#         return render(request, '작성하는 html', {'form':form,'id':id})
    
# def post_delete(request, id):
#     post = CounselPost.objects.get(pk=id)
#     post.delete()
#     return redirect('리스트')