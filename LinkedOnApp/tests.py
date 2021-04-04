import os
import inspect
from django.test import TestCase
from django.urls import reverse, resolve
from LinkedOnApp.models import UserProfile
from LinkedOnApp.forms import UserForm, UserProfileForm, UserUpdateForm, UserProfileUpdateForm

# Create your tests here.
FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TEST FAILURE{os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class LinkedOn_URLTesting(TestCase):
    # Tests for the pages in the website system and if they match the mapping assigned to them.
    
    
       
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
        
        