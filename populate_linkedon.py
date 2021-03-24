import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'LinkedOn.settings')
import django
django.setup()
from django.contrib.auth.models import User
from LinkedOnApp.models import UserProfile, JobListing, Category

def populate():
    categories = ['Data Science', 'Software Engineering',
                  'Business Management', 'Consulting',
                  'Management', 'Internships',
                  'Web Development', 'Nursing',
                  'Engineering', 'Hospitality',
                  'Education', 'Retail']
    
    employers = [
            {'username' : 'ctownsend@outlookmail.com',
             'password' : 'hamster1989',
             'firstname' : 'Caitlyn',
             'lastname' : 'Townsend',
             'category' : 'Hospitality',
             'website' : 'www.themubar.co.uk',
             'company' : 'The MU Bar'},        
            {'username' : 'brownh@brownsolutionsemail.com',
             'password' : 'sdhj2js89hJkh74',
             'firstname' : 'Harry',
             'lastname' : 'Brown',
             'category' : 'Software Engineering',
             'website' : 'www.brownsolutions.com',
             'company': 'Brown Solutions'},
            {'username' : 'bross@mailhot.co.uk',
             'password' : 'passwurd123',
             'firstname' : 'Robert',
             'lastname' : 'Ross',
             'category' : 'Software Engineering',
             'website' : 'www.bobross.com',
             'company' : 'Bob Ross Tech'},
            {'username' : 'sharon435@zarashop.co.uk',
             'password' : 'mynameissharon5',
             'firstname' : 'Sharon',
             'lastname' : 'Osbourne',
             'category' : 'Retail',
             'website' : 'www.zara.co.uk',
             'company' : 'Zara'},
            {'username' : 'mkirkland@glasgowcity.gov.uk',
             'password' : 'hunter2hunter2',
             'firstname' : 'Martin',
             'lastname' : 'Kirkland',
             'category' : 'Education',
             'website' : 'www.glasgowcity.gov.uk/schools/people/mkirkland',
             'company' : 'Glasgow City Council'},
            {'username' : 'ameliablack@falconmail.com',
             'password' : 'ducks343ducks',
             'firstname' : 'Amelia',
             'lastname' : 'Black',
             'category' : 'Internships',
             'website' : 'www.falcon.com',
             'company' : 'The Falcon Company'},
            {'username' : 'donnasheridan@geemail.com',
             'password' : 'mammamia2',
             'firstname' : 'Donna',
             'lastname' : 'Sheridan',
             'category' : 'Hospitality',
             'website' : 'www.mamma-mia.com',
             'company' : 'Villa Donna'}
            ]
    
    jobseekers = [
            {'username' : 'awhite@superdupermail.com',
             'password' : '3494nabdf89',
             'firstname' : 'Anthony',
             'lastname' : 'White',
             'category' : 'Software Engineering',
             'website' : 'www.goatthub.com/awhite',
             'about' : "My name is Anthony. I am a Computer Science graduate "
                       "who specialises in Java and Python.",
             'searchinginfo': "I am looking for a job in software "
                             "engineering. I believe I have much to "
                             "offer to employers."},
            {'username' : 'mei3849@gmailfr.fr',
             'password' : '3494nabdf89',
             'firstname' : 'Mei',
             'lastname' : 'Han',
             'category' : 'Education',
             'website' : 'www.hantutoring.fr',
             'about' : "My name is Mei. I have tutored French for five "
                         "years. I speak French, English and Italian.",
             'searchinginfo': "I am looking for a job in education "
                             "as I believe I have the relevant skills and  "
                             "experience."},
            {'username' : 'mathewmcb@outlookmail.com',
             'password' : 'charlixcxfan99',
             'firstname' : 'Mathew',
             'lastname' : 'McBurney',
             'category' : 'Engineering',
             'website' : 'www.github.com/awhite',
             'about' : "I am Mathew, a hard working engineer from London.",
             'searchinginfo': "I'm looking to expand my horizons and look "
                             "for new opportunities."},
            {'username' : 'henryhoover5@outlookmail.com',
             'password' : 'numatic8347',
             'firstname' : 'Henry',
             'lastname' : 'Hoover',
             'category' : 'Hospitality',
             'website' : 'www.myhenry.co.uk',
             'about' : "My name is Henry. I have been working in the "
                         "hospitality sector for a long time.",
             'searchinginfo': "I am looking for a job as a full time cleaner"
                             "or cleaning manager. "},
            ]
    
    jobpostings = [
            {'id' : '00001',
             'poster' : 'donnasheridan@geemail.com',
             'description' : "I'm Donna and I'm looking for a full time "
                             "cleaner for my hotel in Greece. Minimum 5 years " 
                             "experience in a fast paced environment."},
            {'id' : '00002',
             'poster' : 'mkirkland@glasgowcity.gov.uk',
             'description' : "French teacher positions available at new " 
                             "school in the Glasgow area."},
            {'id' : '03560',
             'poster' : 'ctownsend@outlookmail.com',
             'description' : "New trendy bar opening in Manchester city "
                             "centre. Staff needed. Minimum 5 years "
                             "experience in the hospitality sector."}
            ]
    
    for cat in categories:
        create_category(cat)
            
    for e in employers:
        u = create_user(e)
        create_employer(e, u)
        
    for j in jobseekers:
        u = create_user(j)
        create_jobseeker(j, u)
        
    for jp in jobpostings:
        create_jobposting(jp)
    
def create_user(data):
    print("creating " + data['username'] + "...")
    user = User.objects.create_user(data['username'], data['username'], 
                                    data['password'])
    user.first_name = data['firstname']
    user.last_name = data['lastname']
    user.save()
    return user
    
def create_employer(data, u):
    cat = Category.objects.get(name=data['category'])
    profile = UserProfile.objects.get_or_create(user=u, 
                                                category=cat,
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
    print("Created profile: " + str(profile))
    profile.save()
    return profile
    
def create_jobposting(data):
    employer = User.objects.get(username=data['poster'])
    posting = JobListing.objects.get_or_create(job_id=data['id'],
                                               employer=employer,
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
        
        