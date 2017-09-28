# -*- coding: utf-8 -*-
import os
from aldryn_client import forms
from aldryn_client import forms

class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        settings["STRIPE_PUBLIC_KEY"] = os.environ.get("STRIPE_PUBLIC_KEY", "your test public key")
        settings["STRIPE_SECRET_KEY"] = os.environ.get("STRIPE_PRIVATE_KEY", "your test public key")
        return settings
