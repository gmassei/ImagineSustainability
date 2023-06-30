# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name            : LifeImagine
Description     : geographical MCDA for sustainability assessment
Date            : 25/06/2023
copyright       : Università degli Studi di Perugia (C) 2023
email           : (developper) Gianluca Massei (geonomica@gmail.com)

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


def classFactory(iface):	# inizializza il plugin
	from .LifeImagine import LifeImagine	# importiamo la classe che realizza il plugin
	return LifeImagine(iface)	# creiamo una istanza del plugin
