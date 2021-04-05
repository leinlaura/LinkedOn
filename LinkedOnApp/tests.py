import os
import inspect
import os
import re
import importlib
from django.test import TestCase
from django.urls import reverse, resolve
from LinkedOnApp.models import UserProfile, Category, JobListing
from LinkedOnApp.forms import UserForm, UserProfileForm, UserUpdateForm, UserProfileUpdateForm
from LinkedOn import settings
from django.conf import settings

# Create your tests here.
FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TEST FAILURE{os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

# Tests for the pages in the website system and if they match the mapping assigned to them.
class LinkedOn_URLTesting(TestCase):
    
    
    def test_index_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:index', f"{FAILURE_HEADER} Lookup of 'index' didn't return mapping of 'LinkedOn:index'.{FAILURE_FOOTER}")
    def test_signup_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/signup/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:signup', f"{FAILURE_HEADER} Lookup of '/LinkedOn/signup/' didn't return mapping of 'LinkedOn:signup'.{FAILURE_FOOTER}")
    
    
    def test_aboutus_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/aboutus/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:aboutus', f"{FAILURE_HEADER} Lookup of '/LinkedOn/aboutus/' didn't return mapping of 'LinkedOn:aboutus'.{FAILURE_FOOTER}")

    def test_categories_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/categories/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:categories', f"{FAILURE_HEADER} Lookup of '/LinkedOn/categories/' didn't return mapping of 'LinkedOn:categories'.{FAILURE_FOOTER}")

    def test_categories_joblistings_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/categories/joblistings/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:joblistings', f"{FAILURE_HEADER} Lookup of '/LinkedOn/categories/joblistings/' didn't return mapping of 'LinkedOn:joblistings'.{FAILURE_FOOTER}")
    
    def test_categories_joblistings_create_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/categories/joblistings/createjoblisting/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:create_joblisting', f"{FAILURE_HEADER} Lookup of '/LinkedOn/categories/joblistings/createjoblistings/' didn't return mapping of 'LinkedOn:createjoblistings'.{FAILURE_FOOTER}")
    
    def test_categories_profile_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/categories/profiles/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:profiles', f"{FAILURE_HEADER} Lookup of '/LinkedOn/categories/profiles/' didn't return mapping of 'LinkedOn:profiles'.{FAILURE_FOOTER}")

    def test_logout_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/logout/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:logout', f"{FAILURE_HEADER} Lookup of '/LinkedOn/logout/' didn't return mapping of 'LinkedOn:logout'.{FAILURE_FOOTER}")
   
    def test_editprofile_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/editprofile/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:edit_profile', f"{FAILURE_HEADER} Lookup of '/LinkedOn/editprofile/' didn't return mapping of 'LinkedOn:editprofile'.{FAILURE_FOOTER}")
    
    def test_settings_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/settings/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:settings', f"{FAILURE_HEADER} Lookup of '/LinkedOn/settings/' didn't return mapping of 'LinkedOn:settings'.{FAILURE_FOOTER}")
    
    def test_change_password_url(self):
        

        try:
            resolved_name = resolve('/LinkedOn/settings/change_password/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:change_password', f"{FAILURE_HEADER} Lookup of '/LinkedOn/settings/change_password' didn't return mapping of 'LinkedOn:change_password'.{FAILURE_FOOTER}")
    
    def test_settings_url(self):
        
       
        try:
            resolved_name = resolve('/LinkedOn/settings/delete_acc/').view_name
        except:
            resolved_name = ' '

        self.assertEqual(resolved_name, 'LinkedOn:delete_acc', f"{FAILURE_HEADER} Lookup of '/LinkedOn/settings/delete_acc/' didn't return mapping of 'LinkedOn:delete_acc'.{FAILURE_FOOTER}")
    

class FormTesting(TestCase):
    
    def test_forms(self):
        
        self.assertTrue(UserForm(data={'username':"test@google.com", 'password':"pass", 'first_name':"Cool", 'last_name':"Person",}).is_valid()) # Should be valid because all inputs are valid.
        self.assertFalse(UserForm(data={'username':"isthisatest@imnotsure.yeah", 'password':"", 'first_name':"Cool", 'last_name':"Person",}).is_valid()) # Shouldn't be valid because password can't be null
        
        # Everything else for this form eg. empty first or last name, or an empty email, are addressed on the website with input checks to make sure they are not left empty when hitting submit.
        
        self.assertTrue(UserProfileForm(data={'website':"test@google.com", 'company':"Amazon", 'about':"Hey there, nice weather we're having?", 'searchinginfo':"Lorum Ipsum", 'isEmployer':False,}).is_valid()) # Should be valid because all inputs are valid.
        

        self.assertTrue(UserUpdateForm(data={'first_name':"Cool", 'password':"pass", 'last_name':"Person",}).is_valid()) # Should be valid because all inputs are valid.
        self.assertTrue(UserProfileUpdateForm(data={'website':"test@google.com", 'company':"Amazon", 'about':"Hey there, nice weather we're having?", 'searchinginfo':"Lorum Ipsum",}).is_valid()) # Should be valid because all inputs are valid.

class LinkedOn_TemplatesStructureTests(TestCase):
    """
    Have you set templates, static files and media files up correctly, as per the book?
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.rango_templates_dir = os.path.join(self.templates_dir, 'LinkedOnApp')
    
    def test_templates_directory_exists(self):
        """
        Does the templates/ directory exist?
        """
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your project's templates directory does not exist.{FAILURE_FOOTER}")
    

    
    def test_template_dir_setting(self):
        """
        Does the TEMPLATE_DIR setting exist, and does it point to the right directory?
        """
        variable_exists = 'TEMPLATE_DIR' in dir(settings)
        self.assertTrue(variable_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable TEMPLATE_DIR defined!{FAILURE_FOOTER}")
        
        template_dir_value = os.path.normpath(settings.TEMPLATE_DIR)
        template_dir_computed = os.path.normpath(self.templates_dir)
        self.assertEqual(template_dir_value, template_dir_computed, f"{FAILURE_HEADER}Your TEMPLATE_DIR setting does not point to the expected path. Check your configuration, and try again.{FAILURE_FOOTER}")
    
    def test_template_lookup_path(self):
        """
        Does the TEMPLATE_DIR value appear within the lookup paths for templates?
        """
        lookup_list = settings.TEMPLATES[0]['DIRS']
        found_path = False
        
        for entry in lookup_list:
            entry_normalised = os.path.normpath(entry)
            
            if entry_normalised == os.path.normpath(settings.TEMPLATE_DIR):
                found_path = True
        
        self.assertTrue(found_path, f"{FAILURE_HEADER}Your project's templates directory is not listed in the TEMPLATES>DIRS lookup list. Check your settings.py module.{FAILURE_FOOTER}")
    
class LinkedOn_DatabaseConfigurationTests(TestCase):
    """
    Is the database configured correctly?
    """
    def setUp(self):
        pass
    
    def does_gitignore_include_database(self, path):
        """
        Takes the path to a .gitignore file, and checks to see whether the db.sqlite3 database is present in that file.
        """
        f = open(path, 'r')
        
        for line in f:
            line = line.strip()
            
            if line.startswith('db.sqlite3'):
                return True
        
        f.close()
        return False
    
    def test_databases_variable_exists(self):
        """
        Does the DATABASES settings variable exist, and does it have a default configuration?
        """
        self.assertTrue(settings.DATABASES, f"{FAILURE_HEADER}Your project's settings module does not have a DATABASES variable, which is required. Check the start of Chapter 5.{FAILURE_FOOTER}")
        self.assertTrue('default' in settings.DATABASES, f"{FAILURE_HEADER}You do not have a 'default' database configuration in your project's DATABASES configuration variable. Check the start of Chapter 5.{FAILURE_FOOTER}")
    
    def test_gitignore_for_database(self):
        """
        If you are using a Git repository and have set up a .gitignore, checks to see whether the database is present in that file.
        """
        git_base_dir = os.popen('git rev-parse --show-toplevel').read().strip()
        
        if git_base_dir.startswith('fatal'):
            warnings.warn("No github repository used")
        else:
            gitignore_path = os.path.join(git_base_dir, '.gitignore')
            
            if os.path.exists(gitignore_path):
                self.assertTrue(self.does_gitignore_include_database(gitignore_path), f"{FAILURE_HEADER}Your .gitignore file does not include 'db.sqlite3' {FAILURE_FOOTER}")
            else:
                warnings.warn("No .gitignore file")


class LinkedOn_PopulationScriptTests(TestCase):
    """
    Tests whether the population script puts the expected data into a test database.
    All values that are explicitly mentioned in the book are tested.
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populate_linkedon
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}Population script could not be imported.{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populate_linkedon):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate_linkedon module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populate_linkedon.populate()
    
    def test_categories(self):
        """
        There should be 12 categories.
        """
        categories = Category.objects.filter()
        categories_len = len(categories)
        categories_strs = map(str, categories)
        
        self.assertEqual(categories_len, 12, f"{FAILURE_HEADER}Expecting 12 categories to be created from the populate_linkedon module; found {categories_len}.{FAILURE_FOOTER}")
        self.assertTrue('Data Science' in categories_strs, f"{FAILURE_HEADER}The category 'Data Science' was expected but not created by populate_linkedon.{FAILURE_FOOTER}")
        self.assertTrue('Nursing' in categories_strs, f"{FAILURE_HEADER}The category 'Nursing' was expected but not created by populate_linkedon.{FAILURE_FOOTER}")

    def test_joblistings(self):
        """
        There should be 3 joblistings.
        """
        joblistings = JobListing.objects.filter()
        joblistings_len = len(joblistings)
        
        self.assertEqual(joblistings_len, 3, f"{FAILURE_HEADER}Expecting 3 joblistings to be created from the populate_linkedon module; found {joblistings_len}.{FAILURE_FOOTER}")
        
    def test_profiles(self):
        """
        There should be 21 profiles (including both jobseekers and employers).
        """
        profiles = UserProfile.objects.filter()
        profiles_len = len(profiles)
        
        self.assertEqual(profiles_len, 21, f"{FAILURE_HEADER}Expecting 21 profiles to be created from the populate_linkedon module; found {profiles_len}.{FAILURE_FOOTER}")
        
        

        
    
  
    