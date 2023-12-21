from django.urls import path

# Explicit imports

urlpatterns = [
    # Currently only takes GET requests
    path("", All_moves.as_view(), name="all_moves"),
    
]
