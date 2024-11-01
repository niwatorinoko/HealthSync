from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from .form import PostForm, CommentForm


class AuthorOnly(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        """
        投稿の作者とログインしてるユーザーが同じかどうか判定する
        """
        post = self.get_object()
        return post.author == self.request.user
    
    def handle_no_permission(self):
        """
        test_funcでFalseだった場合特定のページにリダイレクトする
        """
        return redirect('posts:detail', pk=self.kwargs['pk'])
    

class PostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'community/posts_list.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class PostsDetailView(DetailView):
    model = Post
    template_name = 'community/posts_detail.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # コメントフォームをテンプレートに渡す
        context['form'] = CommentForm()
        # 該当の投稿に関連するコメントを取得
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return redirect('community:detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)
    

class PostsCreateView(FormView):
    template_name = 'community/posts_create.html'
    form_class = PostForm
    success_url = reverse_lazy('community:list')

    def form_valid(self, form):
        post_instance = form.save(commit=False)
        post_instance.author = self.request.user
        post_instance.save()
        return super().form_valid(form)
    

class PostsDeleteView(AuthorOnly, DeleteView):
    """
    投稿削除するHTMLを渡す
    削除成功後投稿一覧ページにリダイレクト
    """
    template_name = 'community/posts_delete.html'
    model = Post
    success_url = reverse_lazy('community:list')