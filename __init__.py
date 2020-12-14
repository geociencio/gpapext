# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gpapExtract
                                 A QGIS plugin
 Extract data from Geopaparazzi-Smash database
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-11-03
        copyright            : (C) 2020 by Juan Bernales
        email                : juanbernales@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load gpapExtract class from file gpapExtract.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gpapext import gpapExtract
    return gpapExtract(iface)