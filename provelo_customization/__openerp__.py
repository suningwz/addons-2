# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017- Coop IT Easy.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Provelo Customization",
    "version": "9.0.1.0",
    "depends": [
        'analytic',
        'hr',
        'hr_contract',
        'hr_timesheet',
        'hr_timesheet_auto_creation',
        'hr_timesheet_default_analytic_account',
        'hr_timesheet_holiday',
        'hr_timesheet_overtime',
        'resource_planning',
        'resource_activity',
    ],
    "author": "Coop IT Easy - Robin Keunen <robin@coopiteasy.be>",
    "license": "AGPL-3",
    "category": "",
    "website": "www.coopiteasy.be",
    "description": """
        Specifics customizations for Pro Velo
    """,
    'data': [
        'views/location_filters.xml',
        'views/res_partner_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
