import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'LinkedOn.settings')
import django

django.setup()
from django.contrib.auth.models import User
from django.core.files import File
from LinkedOnApp.models import UserProfile, JobListing, Category


def populate():
    # List of categories
    categories = ['Data Science', 'Software Engineering',
                  'Business Management', 'Consulting',
                  'Management', 'Internships',
                  'Web Development', 'Nursing',
                  'Engineering', 'Hospitality',
                  'Education', 'Retail']

    # Employer acctount details, stored in list of dictionaries
    employers = [
        {'username': 'ctownsend@outlookmail.com',
         'password': 'hamster1989',
         'firstname': 'Caitlyn',
         'lastname': 'Townsend',
         'website': 'www.themubar.co.uk',
         'company': 'The MU Bar'},
        {'username': 'brownh@brownsolutionsemail.com',
         'password': 'sdhj2js89hJkh74',
         'firstname': 'Harry',
         'lastname': 'Brown',
         'website': 'www.brownsolutions.com',
         'company': 'Brown Solutions'},
        {'username': 'bross@mailhot.co.uk',
         'password': 'passwurd123',
         'firstname': 'Robert',
         'lastname': 'Ross',
         'website': 'www.bobross.com',
         'company': 'Bob Ross Tech'},
        {'username': 'sharon435@zarashop.co.uk',
         'password': 'mynameissharon5',
         'firstname': 'Sharon',
         'lastname': 'Osbourne',
         'website': 'www.zara.co.uk',
         'company': 'Zara'},
        {'username': 'mkirkland@glasgowcity.gov.uk',
         'password': 'hunter2hunter2',
         'firstname': 'Martin',
         'lastname': 'Kirkland',
         'website': 'www.glasgowcity.gov.uk/schools/people/mkirkland',
         'company': 'Glasgow City Council'},
        {'username': 'ameliablack@falconmail.com',
         'password': 'ducks343ducks',
         'firstname': 'Amelia',
         'lastname': 'Black',
         'website': 'www.falcon.com',
         'company': 'The Falcon Company'},
        {'username': 'donnasheridan@geemail.com',
         'password': 'mammamia2',
         'firstname': 'Donna',
         'lastname': 'Sheridan',
         'website': 'www.mamma-mia.com',
         'company': 'Villa Donna'}
    ]

    # Jobseeker account details, stored in list of dictionaries
    jobseekers = [
        {'username': 'awhite@superdupermail.com',
         'password': '3494nabdf89',
         'firstname': 'Anthony',
         'lastname': 'White',
         'category': 'Software Engineering',
         'website': 'www.goatthub.com/awhite',
         'about': "My name is Anthony. I am a Computer Science graduate "
                  "who specialises in Java and Python.",
         'searchinginfo': "I am looking for a job in software "
                          "engineering. I believe I have much to "
                          "offer to employers.",
         'profileimage': 'awhite'},

        {'username': 'mei3849@gmailfr.fr',
         'password': '3494nabdf89',
         'firstname': 'Mei',
         'lastname': 'Han',
         'category': 'Education',
         'website': 'www.hantutoring.fr',
         'about': "My name is Mei. I have tutored French for five "
                  "years. I speak French, English and Italian.",
         'searchinginfo': "I am looking for a job in education "
                          "as I believe I have the relevant skills and  "
                          "experience.",
         'profileimage': 'mei3849'},

        {'username': 'mathewmcb@outlookmail.com',
         'password': 'charlixcxfan99',
         'firstname': 'Mathew',
         'lastname': 'McBurney',
         'category': 'Engineering',
         'website': 'www.github.com/awhite',
         'about': "I am Mathew, a hard working engineer from London.",
         'searchinginfo': "I'm looking to expand my horizons and look "
                          "for new opportunities.",
         'profileimage': 'mathewmcb'},

        {'username': 'henryhoover5@outlookmail.com',
         'password': 'numatic8347',
         'firstname': 'Henry',
         'lastname': 'Hoover',
         'category': 'Hospitality',
         'website': 'www.myhenry.co.uk',
         'about': "My name is Henry. I have been working in the "
                  "hospitality sector for a long time.",
         'searchinginfo': "I am looking for a job as a full time cleaner "
                          "or cleaning manager. ",
         'profileimage': 'henryhoover5'},

        {'username': 'faisalmein23@geemail.com',
         'password': '33junk923',
         'firstname': 'Faisal',
         'lastname': 'Mein',
         'category': 'Web Development',
         'website': 'www.fmwebdev.co.uk',
         'about': "Web developer with 10 years industry experience.",
         'searchinginfo': "I'm looking to expand my horizons and find new "
                          "projects I can be passionate about.",
         'profileimage': 'faisalmein23'},

        {'username': 'lj@ljunggrent.nl',
         'password': 'july231970',
         'firstname': 'Trijntje',
         'lastname': 'Ljunggren',
         'category': 'Data Science',
         'website': 'www.ljunggrent.nl',
         'about': "Data Scientist from Rotterdam. Passionate about data.",
         'searchinginfo': "Looking for new opportunities. Willing to "
                          "relocate.",
         'profileimage': 'lj'},

        {'username': 'bevspence1970@geemail.com',
         'password': 'doublep0ints98',
         'firstname': 'Bev',
         'lastname': 'Spence',
         'category': 'Business Management',
         'website': 'www.bspence.co.uk/about',
         'about': "Recent graduate from the University of St Andrews in "
                  "business.",
         'searchinginfo': "Looking for opportunities as a business "
                          "adviser.",
         'profileimage': 'bevspence197'},

        {'username': 'fareeha55@outlookmail.com',
         'password': 'fjsiu894y8fdsf',
         'firstname': 'Fareeha',
         'lastname': 'Gulbahar',
         'category': 'Management',
         'website': 'www.fareehagulbahar.com',
         'about': "Advertising manager based in London. 5 years.",
         'searchinginfo': "Opportunities in London wanted. See portfolio. "
                          "Contact for more information.",
         'profileimage': 'fareeha55'},

        {'username': 'fowlercasey1999@wahoo.co.uk',
         'password': 'sudh094nv',
         'firstname': 'Casey',
         'lastname': 'Fowler',
         'category': 'Internships',
         'website': 'www.caseyfowler.ie',
         'about': "Recent graduate from Dublin University.",
         'searchinginfo': "Looking for an internship in a company based "
                          "in Ireland.",
         'profileimage': 'fowlercasey1999'},

        {'username': 'loricoleman7667@geemail.com',
         'password': 'lcomm77bd8b',
         'firstname': 'Lorraine',
         'lastname': 'Coleman',
         'category': 'Nursing',
         'website': 'www.facebook.com/lorrainecoleman',
         'about': "Experienced nurse for over 20 years specialising in "
                  "home care.",
         'searchinginfo': "Willing to take up a variety of nursing "
                          "positions, enquire for info.",
         'profileimage': 'loricoleman7667'},

        {'username': 'younggipark@ygp.kr',
         'password': 'ygkygk3434',
         'firstname': 'Young Gi',
         'lastname': 'Park',
         'category': 'Engineering',
         'website': 'www.ygp.kr',
         'about': "Civil Engineer from Seoul, Korea.",
         'searchinginfo': "Looking for opportunities to travel and use "
                          "my skills around the world.",
         'profileimage': 'younggipark'},

        {'username': 'charlesrhodes@crr.co.uk',
         'password': '5i90asbc098',
         'firstname': 'Charles',
         'lastname': 'Rhodes',
         'category': 'Retail',
         'website': 'www.crrrasffretail.co.uk',
         'about': "Working in fashion retail for 6 years. ",
         'searchinginfo': "Looking for jobs in retail management. Very "
                          "experienced.",
         'profileimage': 'charlesrhodes'},

        {'username': 'contactjk@kimathieducation.com',
         'password': 'ilovemaths99',
         'firstname': 'Jordan',
         'lastname': 'Kimathi',
         'category': 'Education',
         'website': 'www.kimathieducation.com',
         'about': "Math tutor in Boston.",
         'searchinginfo': "Teaching jobs in Boston wanted. Math and "
                          "Physics.",
         'profileimage': 'contactjk'},

        {'username': 'jordansimpson@consultings.com',
         'password': '4889er9gn98sdfng',
         'firstname': 'Jordan',
         'lastname': 'Simpson',
         'category': 'Consulting',
         'website': 'www.consultings.com/about/jordan',
         'about': "I'm a consultant in Newcastle.",
         'searchinginfo': "Offering expert business advice. Looking for "
                          "a job in a consulting firm.",
         'profileimage': 'jordansimpson'},
    ]

    # List of job postings, stored in list of dictionaries
    jobpostings = [
        {'id': '00001',
         'poster': 'donnasheridan@geemail.com',
         'category': 'Hospitality',
         'description': "I'm Donna and I'm looking for a full time "
                        "cleaner for my hotel in Greece. Minimum 5 years "
                        "experience in a fast paced environment."},
        {'id': '00002',
         'poster': 'mkirkland@glasgowcity.gov.uk',
         'category': 'Education',
         'description': "French teacher positions available at new "
                        "school in the Glasgow area."},
        {'id': '03560',
         'poster': 'ctownsend@outlookmail.com',
         'category': 'Hospitality',
         'description': "New trendy bar opening in Manchester city "
                        "centre. Staff needed. Minimum 5 years "
                        "experience in the hospitality sector."}
    ]

    # Create categories
    for cat in categories:
        create_category(cat)

    # Create employer
    for e in employers:
        u = create_user(e)
        create_employer(e, u)

    # Create job seeker
    for j in jobseekers:
        u = create_user(j)
        create_jobseeker(j, u)

    # Create job posting
    for jp in jobpostings:
        create_jobposting(jp)


def create_user(data):
    # Creates user, which is a part of the UserProfile
    print("creating " + data['username'] + "...")
    user = User.objects.create_user(data['username'], data['username'],
                                    data['password'])
    user.first_name = data['firstname']
    user.last_name = data['lastname']
    user.save()
    return user


def create_employer(data, u):
    profile = UserProfile.objects.get_or_create(user=u,
                                                website=data['website'],
                                                company=data['company'],
                                                isEmployer=True)[0]
    profile.save()
    print("Created Profile: " + str(profile))
    return profile


def create_jobseeker(data, u):
    cat = Category.objects.get(name=data['category'])
    profile = UserProfile.objects.get_or_create(user=u,
                                                category=cat,
                                                website=data['website'],
                                                about=data['about'],
                                                searchingInfo=
                                                data['searchinginfo'],
                                                isEmployer=False)[0]

    # Jobseeker image is taken from populationimages folder
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(THIS_FOLDER + '\\populationimages\\'
                            + data['profileimage'] + '.PNG')

    with open(filepath, 'rb') as f:
        profile.profileImage.save(u.username + '.png', f)
    print("Created profile: " + str(profile))
    profile.save()
    return profile


def create_jobposting(data):
    cat = Category.objects.get(name=data['category'])
    temp = User.objects.get(username=data['poster'])
    employer = UserProfile.objects.get(user=temp)
    posting = JobListing.objects.get_or_create(job_id=data['id'],
                                               employer=employer,
                                               category=cat,
                                               description=
                                               data['description'])[0]
    print("Created job posting: " + str(posting))
    posting.save()
    return posting


def create_category(name):
    cat = Category.objects.get_or_create(name=name)[0]
    cat.save()
    print("Created category: " + str(cat))
    return cat


# Execution starts here
if __name__ == '__main__':
    print('Starting LinkedOn population script...')
    populate()
