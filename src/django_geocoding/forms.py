# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.
from django import forms


class BaseLocationForm(forms.ModelForm):
    class Meta:
        fields = [
            'lat',
            'lng',
            'street',
            'street_no',
            'postal_code',
            'post_town',
            'municipality',
            'country',
        ]
        widgets = {
            'lat': forms.HiddenInput(),
            'lng': forms.HiddenInput(),
            'street': forms.HiddenInput(),
            'street_no': forms.HiddenInput(),
            'postal_code': forms.HiddenInput(),
            'post_town': forms.HiddenInput(),
            'municipality': forms.HiddenInput(),
            'country': forms.HiddenInput(),
        }


