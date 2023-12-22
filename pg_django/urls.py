from django.contrib import admin
from django.urls import path, include
# import pgdb_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pgdb_test.urls'))
]
