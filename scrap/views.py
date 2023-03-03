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

def dhawal(request):
    template = loader.get_template('dhawal.html')
    return HttpResponse(template.render())

def heba(request):
    template = loader.get_template('heba.html')
    return HttpResponse(template.render())

def pat_bowden(request):
    template = loader.get_template('pat-bowden.html')
    return HttpResponse(template.render())

def manoel(request):
    template = loader.get_template('manoel.html')
    return HttpResponse(template.render())

def ruima(request):
    template = loader.get_template('ruima.html')
    return HttpResponse(template.render())

def ivy_league_moocs(request):
    template = loader.get_template('ivy-league-moocs.html')
    return HttpResponse(template.render())

def collections(request):
    template = loader.get_template('collections.html')
    return HttpResponse(template.render())

def sustainability_online_courses(request):
    template = loader.get_template('sustainability-online-courses.html')
    return HttpResponse(template.render())

def top_free_online_courses(request):
    template = loader.get_template('top-free-online-courses.html')
    return HttpResponse(template.render())

def salesforce(request):
    template = loader.get_template('salesforce.html')
    return HttpResponse(template.render())

def google(request):
    template = loader.get_template('google.html')
    return HttpResponse(template.render())

def smithsonian(request):
    template = loader.get_template('smithsonian.html')
    return HttpResponse(template.render())

def united_nations(request):
    template = loader.get_template('united-nations.html')
    return HttpResponse(template.render())

def ibm(request):
    template = loader.get_template('ibm.html')
    return HttpResponse(template.render())

def british_council(request):
    template = loader.get_template('british-council.html')
    return HttpResponse(template.render())

def institutions(request):
    template = loader.get_template('institutions.html')
    return HttpResponse(template.render())

def linuxfoundation(request):
    template = loader.get_template('linuxfoundation.html')
    return HttpResponse(template.render())

def amazon(request):
    template = loader.get_template('amazon.html')
    return HttpResponse(template.render())

def microsoft(request):
    template = loader.get_template('microsoft.html')
    return HttpResponse(template.render())

def mit(request):
    template = loader.get_template('mit.html')
    return HttpResponse(template.render())

def stanford(request):
    template = loader.get_template('stanford.html')
    return HttpResponse(template.render())

def gatech(request):
    template = loader.get_template('gatech.html')
    return HttpResponse(template.render())

def cornell(request):
    template = loader.get_template('cornell.html')
    return HttpResponse(template.render())

def purdue(request):
    template = loader.get_template('purdue.html')
    return HttpResponse(template.render())

def edinburgh(request):
    template = loader.get_template('edinburgh.html')
    return HttpResponse(template.render())

def iitm(request):
    template = loader.get_template('iitm.html')
    return HttpResponse(template.render())

def rice(request):
    template = loader.get_template('rice.html')
    return HttpResponse(template.render())

def umich(request):
    template = loader.get_template('umich.html')
    return HttpResponse(template.render())

def penn(request):
    template = loader.get_template('penn.html')
    return HttpResponse(template.render())

def columbia(request):
    template = loader.get_template('columbia.html')
    return HttpResponse(template.render())

def duke(request):
    template = loader.get_template('duke.html')
    return HttpResponse(template.render())

def harvard(request):
    template = loader.get_template('harvard.html')
    return HttpResponse(template.render())

def universities(request):
    template = loader.get_template('universities.html')
    return HttpResponse(template.render())

def iit_kharagpur(request):
    template = loader.get_template('iit-kharagpur.html')
    return HttpResponse(template.render())

def cs(request):
    template = loader.get_template('cs.html')
    return HttpResponse(template.render())

def best_courses(request):
    template = loader.get_template('best-courses.html')
    return HttpResponse(template.render())

def business(request):
    template = loader.get_template('business.html')
    return HttpResponse(template.render())

def subjects(request):
    template = loader.get_template('subjects.html')
    return HttpResponse(template.render())

def udemy(request):
    template = loader.get_template('udemy.html')
    return HttpResponse(template.render())

def providers(request):
    template = loader.get_template('providers.html')
    return HttpResponse(template.render())

def linkedin_learning(request):
    template = loader.get_template('linkedin-learning.html')
    return HttpResponse(template.render())

def skillshare(request):
    template = loader.get_template('skillshare.html')
    return HttpResponse(template.render())

def edx(request):
    template = loader.get_template('edx.html')
    return HttpResponse(template.render())

def udacity(request):
    template = loader.get_template('udacity.html')
    return HttpResponse(template.render())

def futurelearn(request):
    template = loader.get_template('futurelearn.html')
    return HttpResponse(template.render())

def swayam(request):
    template = loader.get_template('swayam.html')
    return HttpResponse(template.render())

def coursera(request):
    template = loader.get_template('coursera.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def help(request):
    template = loader.get_template('help.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def lists(request):
    template = loader.get_template('lists.html')
    return HttpResponse(template.render())



