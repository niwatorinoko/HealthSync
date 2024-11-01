from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Post
from .form import PostForm


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
    

class PostsListView(ListView):
    model = Post
    template_name = 'community/posts_list.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class PostsDetailView(DetailView):
    model = Post
    template_name = 'community/posts_detail.html' 


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