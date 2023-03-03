from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def home_page(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def report_cer(request):
    template = loader.get_template("report_cer.html")
    return HttpResponse(template.render())

def report_free_2022(request):
    template = loader.get_template("report_free_2022.html")
    return HttpResponse(template.render())

def report_free_2021(request):
    template = loader.get_template("report_free_2021.html")
    return HttpResponse(template.render())

def report_2022(request):
    template = loader.get_template("report_cource.html")
    return HttpResponse(template.render())

def report_pop_cource(request):
    template = loader.get_template("report_most_pop.html")
    return HttpResponse(template.render())


def harvard_cs50_guide(request):
    template = loader.get_template('harvard-cs50-guide.html')
    return HttpResponse(template.render())

def report(request):
    template = loader.get_template('report.html')
    return HttpResponse(template.render())

def emoocs_2023_cfp(request):
    template = loader.get_template('emoocs-2023-cfp.html')
    return HttpResponse(template.render())

def coursera_google_new_deal(request):
    template = loader.get_template('coursera-google-new-deal.html')
    return HttpResponse(template.render())

def best_digital_art_courses(request):
    template = loader.get_template('best-digital-art-courses.html')
    return HttpResponse(template.render())

def year_in_review(request):
    template = loader.get_template('2022-year-in-review.html')
    return HttpResponse(template.render())

def online_learning_deals(request):
    template = loader.get_template('online-learning-deals.html')
    return HttpResponse(template.render())

def best_free_online_courses_2021(request):
    template = loader.get_template('best-free-online-courses-2021.html')
    return HttpResponse(template.render())

def review_china_economic_transformation(request):
    template = loader.get_template('review-china-economic-transformation.html')
    return HttpResponse(template.render())

def free_certificates(request):
    template = loader.get_template('free-certificates.html')
    return HttpResponse(template.render())

def best_elm_courses(request):
    template = loader.get_template('best-elm-courses.html')
    return HttpResponse(template.render())

def chinese_mooc_platforms(request):
    template = loader.get_template('chinese-mooc-platforms.html')
    return HttpResponse(template.render())

def free_google_certifications(request):
    template = loader.get_template('free-google-certifications.html')
    return HttpResponse(template.render())

def most_cited_mooc_research(request):
    template = loader.get_template('most-cited-mooc-research.html')
    return HttpResponse(template.render())

def coursera_free_online_courses(request):
    template = loader.get_template('coursera-free-online-courses.html')
    return HttpResponse(template.render())

def udemy_layoffs(request):
    template = loader.get_template('udemy-layoffs.html')
    return HttpResponse(template.render())

def futurelearn_expands_paywall(request):
    template = loader.get_template('futurelearn-expands-paywall.html')
    return HttpResponse(template.render())

def best_davinci_resolve_courses(request):
    template = loader.get_template('best-davinci-resolve-courses.html')
    return HttpResponse(template.render())

def google_free_certificates(request):
    template = loader.get_template('google-free-certificates.html')
    return HttpResponse(template.render())

def udemy_top_courses(request):
    template = loader.get_template('udemy-top-courses.html')
    return HttpResponse(template.render())

def most_popular_courses_2023(request):
    template = loader.get_template('most-popular-courses-2023.html')
    return HttpResponse(template.render())

def india_online_degrees(request):
    template = loader.get_template('india-online-degrees.html')
    return HttpResponse(template.render())

def open_university_insiders_perspective(request):
    template = loader.get_template('open-university-insiders-perspective.html')
    return HttpResponse(template.render())

def writing_free_online_courses(request):
    template = loader.get_template('writing-free-online-courses.html')
    return HttpResponse(template.render())

def cs50_free_certificate(request):
    template = loader.get_template('cs50-free-certificate.html')
    return HttpResponse(template.render())

def edx_top_courses(request):
    template = loader.get_template('edx-top-courses.html')
    return HttpResponse(template.render())

def class_central_ddos_attack(request):
    template = loader.get_template('class-central-ddos-attack.html')
    return HttpResponse(template.render())

def best_ocaml_courses(request):
    template = loader.get_template('best-ocaml-courses.html')
    return HttpResponse(template.render())

def udemy_by_the_numbers(request):
    template = loader.get_template('udemy-by-the-numbers.html')
    return HttpResponse(template.render())

def list_of_mooc_based_microcredentials(request):
    template = loader.get_template('list-of-mooc-based-microcredentials.html')
    return HttpResponse(template.render())

def linkedin_learning_free_learning_paths(request):
    template = loader.get_template('linkedin-learning-free-learning-paths.html')
    return HttpResponse(template.render())

def best_resume_writing_courses(request):
    template = loader.get_template('best-resume-writing-courses.html')
    return HttpResponse(template.render())

def coursera_top_courses(request):
    template = loader.get_template('coursera-top-courses.html')
    return HttpResponse(template.render())

def mooc_based_masters_degree(request):
    template = loader.get_template('mooc-based-masters-degree.html')
    return HttpResponse(template.render())


