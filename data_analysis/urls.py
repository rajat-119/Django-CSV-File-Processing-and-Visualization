from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('show-records/', views.show_first_five_records, name='show_first_five_records'),
    path('summary/', views.show_summary_statistics, name='show_summary_statistics'),
    path('handle-missing-values/', views.handle_missing_values, name='handle_missing_values'),
    path('generate-histograms/', views.generate_histograms, name='generate_histograms'),
    path('generate-scatter-plots/', views.generate_scatter_plots, name='generate_scatter_plots'),
    path('generate-heatmaps/', views.generate_heatmaps, name='generate_heatmaps'),
    path('generate-box-plots/', views.generate_box_plots, name='generate_box_plots'),

]