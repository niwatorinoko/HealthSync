from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 投稿モデルの表示に使用されるフィールド
    list_display = ('author', 'title', 'body', 'created_at')
    fieldsets = (
        ('Post', {
            'fields': (
                'author', 'title', 'body', 'image',
            )
        }),
    )
    # 1つのフィールドでユーザーを絞り込む
    list_filter = ('author', 'created_at',)

    # 検索される時に使われるフィールド
    search_fields = ('author__username', 'title', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_at')
    fieldsets = (
        ('Comment', {
            'fields': (
                'post',
                'author',
                'body',
            )
        }),
    )
    list_filter = ('author', 'created_at', )
    search_fields = ('author','body')