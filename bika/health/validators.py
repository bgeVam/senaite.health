# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.HEALTH
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE.rst, CONTRIBUTORS.rst.

from Products.CMFPlone.utils import safe_unicode
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import to_utf8
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from Products.validation import validation
from Products.validation.interfaces.IValidator import IValidator
from datetime import datetime
from senaite import api
from bika.health.catalog.patient_catalog import CATALOG_PATIENT_LISTING


class Date_Format_Validator:

    """ Verifies whether the format is the correct or not """

    implements(IValidator)
    name = "isDateFormat"

    def __call__(self, value, *args, **kwargs):
        instance = kwargs['instance']
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            instance = kwargs['instance']
            title = kwargs['field'].widget.label
            trans = getToolByName(instance, 'translation_service').translate
            msg = _(
                "Incorrect data format in '${title}', should be YYYY-MM-DD",
                mapping={'title': safe_unicode(value)}
            )
            return to_utf8(trans(msg))
        return True

validation.register(Date_Format_Validator())


class UniqueClientPatientIDValidator:
    """
    Checks if the client patient ID is unique. It does
    so only if the checkbox 'Client Patient ID must be
    unique' is selected . This checkbox can be found in
    Bika Setup under Id server tab
    """

    implements(IValidator)
    name = "unique_client_patient_ID_validator"

    def __call__(self, value, *args, **kwargs):
        # avoid the catalog query if the option is not selected
        if not api.get_bika_setup().ClientPatientIDUnique:
            return True
        else:
            patient_catalog = api.get_tool(CATALOG_PATIENT_LISTING)
            patients = patient_catalog(getClientPatientID=value)
            # If the search by Client Patient ID (value) returns
            # one or more values then it is not unique
            if patients:
                instance = kwargs['instance']
                trans = getToolByName(instance, 'translation_service').translate
                msg = _(
                    "Validation failed: '${value}' is not unique",
                    mapping={
                        'value': safe_unicode(value)
                    })
                return to_utf8(trans(msg))
            return True

validation.register(UniqueClientPatientIDValidator())
