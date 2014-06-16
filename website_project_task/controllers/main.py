# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2008-2014 AvanzOSC S.L. (Oihane) All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from openerp.addons.web import http
from openerp.addons.web.http import request


class website_project_task(http.Controller):

    @http.route(['/project/task/<model("project.task"):task>'], type='http',
                auth="public", website=True)
    def project_task(self, task=None, **post):
        cr, uid, context = request.cr, request.uid, request.context
        render_values = {
            'task': task,
        }
        return request.website.render("website_project_task.index",
                                      render_values)
