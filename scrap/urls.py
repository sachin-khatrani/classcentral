from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings


from scrap import views
app_name = "scrap"
urlpatterns = [
    path('classcentral/', views.home_page),
    path('report/free-certificates/', views.report_cer),
    path('report/most-popular-courses-2022/', views.report_2022),
    path('report/most-popular-online-courses/', views.report_pop_cource),
    path('report/best-free-online-courses-2022/', views.report_free_2022),
    path('report/best-free-online-courses-2021/', views.report_free_2021),


    path('report/harvard-cs50-guide/', views.harvard_cs50_guide),
    path('report/report/', views.report),
    path('report/emoocs-2023-cfp/', views.emoocs_2023_cfp),
    path('report/coursera-google-new-deal/', views.coursera_google_new_deal),
    path('report/best-digital-art-courses/', views.best_digital_art_courses),
    path('report/year-in-review/', views.year_in_review),
    path('report/online-learning-deals/', views.online_learning_deals),
    path('report/best-free-online-courses-2021/', views.best_free_online_courses_2021),
    path('report/review-china-economic-transformation/', views.review_china_economic_transformation),
    path('report/free-certificates/', views.free_certificates),
    path('report/best-elm-courses/', views.best_elm_courses),
    path('report/chinese-mooc-platforms/', views.chinese_mooc_platforms),
    path('report/free-google-certifications/', views.free_google_certifications),
    path('report/most-cited-mooc-research/', views.most_cited_mooc_research),
    path('report/coursera-free-online-courses/', views.coursera_free_online_courses),
    path('report/udemy-layoffs/', views.udemy_layoffs),

    path('report/futurelearn-expands-paywall/', views.futurelearn_expands_paywall),
    path('report/best-davinci-resolve-courses/', views.best_davinci_resolve_courses),
    path('report/google-free-certificates/', views.google_free_certificates),
    path('report/udemy-top-courses/', views.udemy_top_courses),
    path('report/most-popular-courses-2023/', views.most_popular_courses_2023),
    path('report/india-online-degrees/', views.india_online_degrees),
    path('report/open-university-insiders-perspective/', views.open_university_insiders_perspective),
    path('report/writing-free-online-courses/', views.writing_free_online_courses),
    path('report/cs50-free-certificate/', views.cs50_free_certificate),
    path('report/edx-top-courses/', views.edx_top_courses),
    path('report/class-central-ddos-attack/', views.class_central_ddos_attack),
    path('report/best-ocaml-courses/', views.best_ocaml_courses),
    path('report/udemy-by-the-numbers/', views.udemy_by_the_numbers),
    path('report/list-of-mooc-based-microcredentials/', views.list_of_mooc_based_microcredentials),
    path('report/linkedin-learning-free-learning-paths/', views.linkedin_learning_free_learning_paths),
    path('report/best-resume-writing-courses/', views.best_resume_writing_courses),
    path('report/coursera-top-courses/', views.coursera_top_courses),
    path('report/mooc-based-masters-degree/', views.mooc_based_masters_degree),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
