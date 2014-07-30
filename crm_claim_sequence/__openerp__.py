# -*- encoding: utf-8 -*-
##############################################################################
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

{
    "name": "Sequence for Claims",
    "version": "1.0",
    "depends": [
        "crm",
    ],
    "author": "AvanzOSC",
    "contributors": [
        "Iker Coranti <ikercoranti@avanzosc.com>",
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
    ],
    "category": "CRM & SRM",
    "website": "http://www.avanzosc.es",
    "summary": "Claim sequence generator",
    "description": """
    This module adds a sequence for claims
    """,
    "data": [
        "views/crm_claim_view.xml",
        "data/claim_sequence.xml",
    ],
    "installable": True,
    "auto_install": False,
}
