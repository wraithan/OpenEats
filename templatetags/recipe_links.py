from django import template
from recipe.models import StoredRecipe, Recipe,ReportedRecipe
from django.utils import translation
register = template.Library()

@register.simple_tag
def fav_link(user, recipe_id):
    cur_language = translation.get_language()
    translation.activate(cur_language)
    if  user.is_authenticated(): #make sure the user is signed in
        check = StoredRecipe.objects.filter(user = user.id, recipe = recipe_id) #check to see if the recipe is stored
        if check:
            return "<a href=\"#\">%s</a>" % translation.ugettext('bookmakred')
        else: #must not be stored yet
            return "<button id=\"recipe-store\">%s</button>" % translation.ugettext('favorite')
            
    else:
        recipe = Recipe.objects.get(pk=recipe_id)
        return "<a href=\"/accounts/login?next=/recipe/%s/\">%s</a>" % (recipe.slug, translation.ugettext('favorite'))

@register.simple_tag
def report_link(user, recipe_id):
    cur_language = translation.get_language()
    translation.activate(cur_language)
    if  user.is_authenticated(): #make sure the user is signed in
        check = ReportedRecipe.objects.filter(recipe = recipe_id) #check to see if the recipe is stored
        if check:
            return "<a id=\"recipe-report\" href=\"#\" title=\"recipe has been reported as spam\">%s</a>" % translation.ugettext('reported!')
        else: #must not been reported yet yet
            return "<button id=\"recipe-report\" title=\"report inappropriate recipe to the admins\">%s</button>" % translation.ugettext('report')

    else:
        recipe = Recipe.objects.get(pk=recipe_id)
        return "<a href=\"/accounts/login?next=/recipe/%s/\">%s</a>" % (recipe.slug, translation.ugettext('favorite'))
    
