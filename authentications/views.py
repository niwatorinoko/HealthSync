from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import FormView, View, DetailView, TemplateView
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .videos import VIDEO_LIBRARY
from .nutrition_guide import personalized_nutrition_guide

from .forms import UserCreationForm, UserLoginForm


User = get_user_model()

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class UnauthenticatedOnly(UserPassesTestMixin):
    """
    ログイン済みのユーザーのアクセスを制限する
    """
    def test_func(self):
        # ログイン状態じゃないかチェック
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        # ログイン状態なら投稿一覧へリダイレクト
        return redirect('authentications:index')
    
class AuthenticationsSignupView(UnauthenticatedOnly, FormView):
    """ 
    ユーザーの登録フォームをHTMLに渡す
    """
    template_name = 'authentications/authentications_signup.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        """ 
        Postリクエスト時の処理
        Userモデルのフォームを検証し、データを保存する
        検証成功すれば投稿一覧ページにリダイレクトし、自動でログインした状態にする
        検証失敗すれば登録ページを返す
        """
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()

            # 保存後に認証を実行してログイン
            user = authenticate(email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('authentications:index')
            else:
                print("Authentication failed")  # 認証失敗時
                # 認証が失敗した場合はエラーメッセージを表示
                return redirect('authentications:signup')
        else:
            print("Form is not valid:", user_form.errors)  # 検証エラーの詳細を表示
            return render(request, self.template_name, {'form': user_form})

        
class AuthenticationsLoginView(UnauthenticatedOnly ,FormView):
    """ 
    ログインフォームを渡す
    """
    template_name = 'authentications/authentications_login.html'
    form_class = UserLoginForm

    def post(self, request, *args, **kwargs):
        """ 
        Postリクエスト時の処理
        送信されたメールアドレスとパスワードでユーザーを検索し見つかったらログインする
        見つからなかったらログインページを返す
        """
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentications:index')
        return redirect('authentications:login')

class AuthenticationsLogoutView(View):
    """
    ログアウト機能 HTMLファイルはなし
    """
    def get(self, request):
        logout(request)
        return redirect('authentications:login')

class UserProfileView(DetailView):
    """
    特定のユーザーの投稿一覧を取得しHTMLを返す
    """
    model = User
    template_name = 'authentications/user_profile.html'

    def get(self, request, pk):
        """ 
        ユーザーとそのユーザーの全ての投稿を返す
        """
        user = User.objects.get(id=pk)
        user_posts = user.post_set.all()
        context = {
            'user': user,
            'posts': user_posts
        }
        return render(request, self.template_name, context)
    

class SportPlanView(LoginRequiredMixin, TemplateView):
    template_name = 'authentications/sports_plan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        sport = user.preferred_sports
        level = user.fitness_level

        beginner_title = VIDEO_LIBRARY[sport][0]['title']
        beginner_benefits = VIDEO_LIBRARY[sport][0]['benefits']
        beginner_url = VIDEO_LIBRARY[sport][0]['url']
        intermediate_title = VIDEO_LIBRARY[sport][1]['title']
        intermediate_benefits = VIDEO_LIBRARY[sport][1]['benefits']
        intermediate_url = VIDEO_LIBRARY[sport][1]['url']
        advanced_title = VIDEO_LIBRARY[sport][2]['title']
        advanced_benefits = VIDEO_LIBRARY[sport][2]['benefits']
        advanced_url = VIDEO_LIBRARY[sport][2]['url']

        
        context.update({
            'sport': sport,
            'level': level,
            'beginner_title': beginner_title,
            'beginner_benefits': beginner_benefits,
            'beginner_url': beginner_url,
            'intermediate_title': intermediate_title,
            'intermediate_benefits': intermediate_benefits,
            'intermediate_url': intermediate_url,
            'advanced_title': advanced_title,
            'advanced_benefits': advanced_benefits,
            'advanced_url': advanced_url,
        })
        return context
    

class NutritionPlanView(LoginRequiredMixin, TemplateView):
    template_name = 'authentications/nutrition_plan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # ユーザー情報を取得
        sport = user.preferred_sports
        age_group = user.age_range
        health_condition = "Yes" if user.health_condition.lower() == "yes" else "No"
        food_allergies = "Yes" if user.food_allergies.lower() == "yes" else "No"
        dietary_preference = user.dietary_preferences

        # パーソナライズされた栄養ガイドを生成
        nutrition_guide = personalized_nutrition_guide(
            sport=sport,
            age_group=age_group,
            health_condition=health_condition,
            food_allergies=food_allergies,
            dietary_preference=dietary_preference
        )

        # Sample_Menuが辞書かどうかを確認
        sample_menu_is_dict = isinstance(nutrition_guide.get("Sample Menu"), dict)

        # コンテキストに栄養ガイド情報を追加
        context.update({
            'sport': sport,
            'age_group': age_group,
            'health_condition': health_condition,
            'food_allergies': food_allergies,
            'dietary_preference': dietary_preference,
            'nutrition_guide': nutrition_guide,
            'sample_menu_is_dict': sample_menu_is_dict,  # 追加
        })
        return context
