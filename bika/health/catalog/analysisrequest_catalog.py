# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.HEALTH.
#
# SENAITE.HEALTH is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2020 by it's authors.
# Some rights reserved, see README and LICENSE.

from bika.lims.catalog import CATALOG_ANALYSIS_REQUEST_LISTING

# Defines the extension for catalogs created in Bika LIMS.
# Only add the items you would like to add!
analysisrequest_catalog_definition = {
    CATALOG_ANALYSIS_REQUEST_LISTING: {
            'indexes': {
                'getClientReference': 'FieldIndex',
                'getDoctorUID': 'FieldIndex',
                'getPatientUID': 'FieldIndex',

                # Indexes to sort in listing view
                'getDoctorTitle': 'FieldIndex',
                'getPatientTitle': 'FieldIndex',
                'getPatientID': 'FieldIndex',
            },
            'columns': [
                'getClientPatientID',
                'getDoctorTitle',
                'getDoctorUID',
                'getDoctorURL',
                'getPatientID',
                'getPatientTitle',
                'getPatientUID',
                'getPatientURL',
            ]
        }
    }
