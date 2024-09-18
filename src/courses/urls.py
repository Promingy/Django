from django.urls import include, path

from .views import (
    CourseView,
    CourseListView,
    my_fbv
)

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="courses-list"),
    # path("", my_fbv, name="courses-list")

    path("<int:id>/", CourseView.as_view(), name="course-detail")
]