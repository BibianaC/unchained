# Copyright 2013 Hansel Dunlop
# All rights reserved
#
# Author: Hansel Dunlop - hansel@interpretthis.org
#

from datetime import datetime
import locale

from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.utils.timezone import utc

USER_LOCALE = 'en_US.utf8'

def send_html_email(subject, template_stub, sender, recipients, context):
    email_txt = get_template(template_stub + '.txt').render(Context(context))
    email_html = get_template(template_stub + '.html').render(Context(context))
    msg = EmailMultiAlternatives(subject, email_txt, sender, recipients)
    msg.attach_alternative(email_html, "text/html")
    msg.send()

def wise_datetime_now():
    return datetime.utcnow().replace(tzinfo=utc)

def wise_datetime_from_date(dt):
    now = wise_datetime_now()
    return wise_datetime(
        day=dt.day, month=dt.month, year=dt.year,
        hour=now.hour, minute=now.minute, second=now.second,
    )

def wise_datetime(**kwargs):
    return datetime(**kwargs).replace(tzinfo=utc)

def format_cents(cents):
    locale.setlocale(locale.LC_ALL, USER_LOCALE)
    return locale.currency(cents / 100.0, symbol=False, grouping=True)
