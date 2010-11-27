import getopt
import sys
import os
import unittest

root = os.path.abspath(os.path.join(__file__, "..", ".."))

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    if os.path.exists(os.path.join(root, "settings.py")):
        print "No DJANGO_SETTINGS_MODULE is set, found a settings.py and using that.\n" \
            "If that is incorrect please specify a DJANGO_SETTINGS_MODULE.\n"
        os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

sys.path.append(root)

from django import test
from django.test.simple import build_suite, get_tests
from django.test.utils import setup_test_environment, teardown_test_environment
from django.db import connection
from django.conf import settings
from django.db.models import get_app
from django.core.management import call_command
from django.test.client import Client

def usage():
    print """
--help or -h
--test or -t recipe 
--start or -s recipe

recipe: can be either the full name eg: recipe_01, or 1
"""

def validate_options(*args):
    if len(args) < 1:
        recipes = []
        for fle in os.listdir(root):
            if fle.startswith("recipe_"):
                recipes.append(fle)
        return recipes
    else:
        recipe = args[0]

        if not str(recipe).startswith("recipe_"):
            recipe = "recipe_%02d" % int(recipe)
        path = os.path.join(root, recipe)
        if not os.path.exists(path):
            raise ValueError, "Cannot find the recipe: %s, tried: %s" % (recipe, path)
    
        return [recipe, ]

def test(recipes, options={}):
    verbosity = 1
    interactive = False
    
    setup_test_environment()
    settings.DEBUG = True
    iapps = list(settings.INSTALLED_APPS)
    
    for recipe in recipes:    
        iapps.append("%s" % recipe)
        settings.ROOT_URLCONF = "%s.urls" % recipe
    
    for recipe in recipes:
        obj = __import__("%s" % recipe, globals(), locals(), ["settings_extra",])
        if hasattr(obj, "settings_extra"):
            for k, v in obj.settings_extra.items():
                if isinstance(v, (tuple, list)) and hasattr(settings, k):
                    value = list(getattr(settings, k))
                    value.extend(v)
                    setattr(settings, k, value)
                else:
                    setattr(settings, k, v)
    
    print "*" * 40
    print iapps
    settings.INSTALLED_APPS = iapps

    connection.creation.create_test_db(verbosity, autoclobber=not interactive)

    suite = unittest.TestSuite()
    suite.addTest(build_suite(get_app(recipe)))
    
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

def start(recipes, options={}):
    test(recipes, options=options)
    
    from django.contrib.auth.models import User
    u = User.objects.create(
        username='admin',
        email='andy@clearwind.ca',
        is_superuser=True,
        is_staff=True,
        is_active=True
    )
    u.set_password("admin")
    u.save()
    
    for recipe in recipes:
        call_command('loaddata', recipe)
        call_command('sqlall', recipe)

    call_command('runserver', '0.0.0.0:8000', use_reloader=False)

def insert(recipe, options={}):
    recipe = int(recipe[0].split("recipe_")[-1])
    recipes = []
    for fle in os.listdir(root):
        if fle.startswith("recipe_"):
            number = int(fle.split("recipe_")[-1])
            if number >= recipe:
                recipes.append(number)
    
    recipes.sort()
    recipes.reverse()

    for dr in recipes:
        old = "recipe_%02d" % dr
        new = "recipe_%02d" % (dr + 1)

        os.system("svn mv %s %s" % (old, new))
        os.system("rm -rf %s" % old)
        for path, dirs, fles in os.walk(new):
            if path.find(".svn") > -1:
                continue
            else:
                for fle in fles:
                    abspath = os.path.join(path, fle)
                    data = open(abspath, "rb").read()
                    data = data.replace(old, new)
                    out = open(abspath, "wb")
                    out.write(data)
                
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "htsi", ["help", "test", "start",])
    except getopt.GetoptError, err:
        print str(err) 
        usage()
        sys.exit(2)

    recipes = validate_options(*args)
    
    for o, a in opts:
        if o in ("--h", "--help"):
            usage()
            sys.exit()
        elif o in ("-t", "--test"):
            test(recipes, options=dict(opts))
        elif o in ("-s", "--start"):
            start(recipes, options=dict(opts))
        #elif o in ("-i"):
        #    insert(recipes, options=dict(opts))

if __name__ == "__main__":
    main()