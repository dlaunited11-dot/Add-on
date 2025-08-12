# -*- coding: utf-8 -*-
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

# Global variables
_URL = sys.argv[0]
_HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon()

def log(msg, level=xbmc.LOGINFO):
    xbmc.log(f"[Italian TV Web]: {msg}", level)

def launch_web_view():
    """
    Startet das Add-on, indem es eine Web-URL in Kodi öffnet.
    """
    # **Hier die GitHub Pages URL einfügen**
    web_url = "https://[Ihr-Benutzername].github.io/kodi-italiantv/index.html" 
    
    log(f"Launching web view for URL: {web_url}")

    list_item = xbmcgui.ListItem(label="Italian TV (Web)")
    list_item.setInfo('video', {'title': "Italian TV Web-Addon"})
    list_item.setProperty('IsPlayable', 'true')

    xbmcplugin.setResolvedUrl(_HANDLE, True, listitem=list_item)
    xbmc.executebuiltin(f"RunPlugin(plugin://plugin.video.webview/?url={web_url})")


if __name__ == '__main__':
    log("Web-based Add-on started")
    launch_web_view()
