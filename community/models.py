from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Common(models.Model):
    """
    抽象モデル
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    # オブジェクトが最初に作成されたときに、フィールドを now に自動的に設定
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        abstract = True


class Post(Common):
    """ 
    投稿に関するモデル
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    title = models.CharField(max_length=50, verbose_name='Title')
    body = models.CharField(max_length=300, verbose_name='Content')
    image = models.ImageField(upload_to="", verbose_name='Image')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    #保存した時に表示される文字列
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        各インスタンスに対応するURLを返す 
        """
        return reverse('posts:detail', kwargs={'pk': self.pk})
    

class Comment(Common):
    """ 
    投稿のコメントに関するモデル
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=150, verbose_name='comment')

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return self.body[:50]