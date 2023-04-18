from django.urls import path
from .views import (
    post_list_and_create,
    load_post_data_view,
    hello_world_view,
    like_unlike_post,
    post_detail_data_view,
    post_detail,
    delete_post,
    update_post,

    
)

app_name = 'posts'

urlpatterns = [

    path('', post_list_and_create, name = 'main-board'),
    path('like-unlike/', like_unlike_post, name = 'like-unlike'),
    
    path('data/<int:num_posts>/', load_post_data_view, name = 'posts-data'),

    path('<pk>/', post_detail, name= 'post-detail'),

    path('<pk>/data/', post_detail_data_view, name = 'post-detail-data'),
    path('hello-world/', hello_world_view, name='hello-world'),

    path('<pk>/update/', update_post, name= 'post-update'),
    path('<pk>/delete/', delete_post, name= 'post-delete'),

]