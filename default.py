#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Mario Gonzales (mgonzales71)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import xbmcaddon
import xbmcgui
import xbmc
import random
import os
from datetime import datetime

Addon = xbmcaddon.Addon('screensaver.skinnable')

#__scriptname__ = Addon.getAddonInfo('name')
__path__ = Addon.getAddonInfo('path')
__location__ = xbmc.getSkinDir()
#__scriptname__='main.xml'
__scriptname__ = __location__ + '.xml'

class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        self.log('INIT')
        self.abort_requested = False
        self.started = False
        self.exit_monitor = self.ExitMonitor(self.exit)
		
    def Display(self):
        while not self.abort_requested:
		
            xbmc.sleep(500)
			
        if self.abort_requested:
            self.log('screensaver abort_requested')
            self.exit()
            return	
		
    def exit(self):
        self.abort_requested = True
        self.exit_monitor = None
        self.log('exit')
        self.close()

    def log(self, msg):
        xbmc.log(u'Screensaver: %s' % msg)

if __name__ == '__main__':
    if(os.path.isfile(xbmc.translatePath('special://skin/1080i/script-screensaver-skinnable-custom.xml'))):
        screensaver = Screensaver("script-screensaver-skinnable-custom.xml", xbmc.translatePath('special://skin/1080i/'), 'default')
    elif(os.path.isfile(xbmc.translatePath('special://skin/720p/script-screensaver-skinnable-custom.xml'))):
        screensaver = Screensaver("script-screensaver-skinnable-custom.xml", xbmc.translatePath('special://skin/720p/'), 'default')
    elif(os.path.isfile(xbmc.translatePath('special://skin/21x9/script-screensaver-skinnable-custom.xml'))):
        screensaver = Screensaver("script-screensaver-skinnable-custom.xml", xbmc.translatePath('special://skin/21x9/'), 'default')
    elif(os.path.isfile(xbmc.translatePath('special://skin/16x9/script-screensaver-skinnable-custom.xml'))):
        screensaver = Screensaver("script-screensaver-skinnable-custom.xml", xbmc.translatePath('special://skin/16x9/'), 'default')
    elif(os.path.isfile(xbmc.translatePath('special://skin/4x3Hirez/script-screensaver-skinnable-custom.xml'))):
        screensaver = Screensaver("script-screensaver-skinnable-custom.xml", xbmc.translatePath('special://skin/4x3Hirez/'), 'default')
    else:
        screensaver = Screensaver("skin.default.xml", __path__, 'default')	
    screensaver.doModal()
    del screensaver
    sys.modules.clear()