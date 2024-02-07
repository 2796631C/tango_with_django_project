from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name = 'about'),
path('category/<slug:category_name_slug>/',
    views.show_category, name='show_category'),
]

#<h2>Most Liked Categories</h2>

#        <h2>Most Viewed Pages</h2>
#        <div>
#        {% if pages %}
#            <ul>
#                {% for page in pages %}
#                <li>
#                    <a href="/rango/category/category">
#
#        </div>