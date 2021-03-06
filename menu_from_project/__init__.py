# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name            : menu_from_project plugin
Description          : Build layers shortcut menu based on QGis project
Date                 :  10/11/2011 
copyright            : (C) 2011 by AEAG
email                : xavier.culos@eau-adour-garonne.fr 
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
def classFactory(iface): 
  # load menu_from_project class from file menu_from_project
  from .menu_from_project import menu_from_project 
  return menu_from_project(iface)
