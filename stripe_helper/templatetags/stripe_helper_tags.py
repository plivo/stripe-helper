from django.core.urlresolvers import reverse
from django import template
from django.template.loader import render_to_string
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from stripe_helper.conf import options


register = template.Library()

def _set_up_zebra_form(context):
    if not "stripe_helper_form" in context:
        if "form" in context:
            context["stripe_helper_form"] = context["form"]
        else:
            raise Exception, "Missing stripe form."
    context["STRIPE_PUBLISHABLE"] = options.STRIPE_PUBLISHABLE
    return context


@register.inclusion_tag('stripe_helper/_stripe_js_and_set_stripe_key.html', takes_context=True)
def stripe_helper_head_and_stripe_key(context):
    return _set_up_zebra_form(context)


@register.inclusion_tag('stripe_helper/_basic_card_form.html', takes_context=True)
def stripe_helper_card_form(context):
    return _set_up_zebra_form(context)
