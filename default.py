# -*- coding: utf-8 -*-
import sys
import urllib.parse
from urllib.parse import urlencode, parse_qs, quote, urlparse

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

ADDON = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])

# Android-Chrome User-Agent (funktioniert i.d.R. am zuverlässigsten)
DEFAULT_UA = "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"

# Alle 41 Kanäle wie gewünscht
CHANNELS = [
    {
        "name": "Rai 1",
        "stream_url": "https://dash2.antik.sk/live/test_rai_uno_tizen/playlist.m3u8",
        "logo": "https://i.imgur.com/CAx7yRm.png",
        "group": "National DVB-T",
        "channel": "1"
    },
    {
        "name": "Rai 2",
        "stream_url": "https://ilglobotv-live.akamaized.net/channels/RAI2/Live.m3u8",
        "logo": "https://i.imgur.com/zA0PTcs.png",
        "group": "National DVB-T",
        "channel": "2"
    },
    {
        "name": "Rai 3",
        "stream_url": "https://dash2.antik.sk/live/test_rai_tre_tizen/playlist.m3u8",
        "logo": "https://i.imgur.com/9kuQCIi.png",
        "group": "National DVB-T",
        "channel": "3"
    },
    {
        "name": "Rete 4",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-r4/r4-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/GWx2Fkl.png",
        "group": "National DVB-T",
        "channel": "4"
    },
    {
        "name": "Canale 5",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-c5/c5-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/p6YdiR1.png",
        "group": "National DVB-T",
        "channel": "5"
    },
    {
        "name": "Italia 1",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-i1/i1-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/oCiOxBG.png",
        "group": "National DVB-T",
        "channel": "6"
    },
    {
        "name": "Italia 2",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-i2/i2-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/nq48sjO.png",
        "group": "National DVB-T",
        "channel": "7"
    },
    {
        "name": "Italia 1 HD",
        "stream_url": "https://live03-col.msf.cdn.mediaset.net/live/ch-i1/i1-clr.isml/manifest.mpd",
        "logo": "https://i.imgur.com/oCiOxBG.png",
        "group": "National DVB-T",
        "channel": "8"
    },
    {
        "name": "La7",
        "stream_url": "https://d3749synfikwkv.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-74ylxpgd78bpb/Live.m3u8",
        "logo": "https://i.imgur.com/F90mpSa.png",
        "group": "National DVB-T",
        "channel": "9"
    },
    {
        "name": "TV8",
        "stream_url": "https://hlslive-web-gcdn-skycdn-it.akamaized.net/TACT/11223/tv8web/master.m3u8?hdnea=st=1701861650~exp=1765449000~acl=/*~hmac=84c9f3f71e57b13c3a67afa8b29a8591ea9ed84bf786524399545d94be1ec04d",
        "logo": "https://i.imgur.com/xvoHVOU.png",
        "group": "National DVB-T",
        "channel": "10"
    },
    {
        "name": "DMAX",
        "stream_url": "https://amg16146-wbdi-amg16146c8-samsung-it-1841.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-dmax-samsungit/playlist.m3u8",
        "logo": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAZlBMVEX//////fv88e7549vePwDgTwDgSwD659/dQQDcVh/jfl3je1jeZTraRgDhdVHaSQDfakDcUxnbTQnidE3++PXnkHLeXi/wuqj32c7ickr43dLvtaH21Mn77urywKzsqJLzyr3eRgDF+PAjAAAAjklEQVR4Ae3OhQHDMAwAwVeYmcn2/kOWuRkhZ0aJm4NYu4Qr23E9z3Pv1b3W69Lx74dBGMVJmmV5EZdlXFZxHEdl8Dh0amhaWzqbpKUNehjy1+EITBNz03QLS5raTVj9HgpN1CBJuTLmn99KawPNBigNfhl8JxRf1Jc2XloUvl56xniX9slzbK5k3SUcrs51kQuFU/NLZAAAAABJRU5ErkJggg==",
        "group": "National DVB-T",
        "channel": "11"
    },
    {
        "name": "Nove",
        "stream_url": "https://amg16146-wbdi-amg16146c1-samsung-it-1831.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-nove-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/Hp723RU.png",
        "group": "National DVB-T",
        "channel": "12"
    },
    {
        "name": "20 Mediaset",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-lb/lb-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/It13jwX.png",
        "group": "National DVB-T",
        "channel": "13"
    },
    {
        "name": "Rai 4",
        "stream_url": "https://raievent10-elem-live.akamaized.net/hls/live/619189/raievent10/raievent10/playlist.m3u8",
        "logo": "https://i.imgur.com/XFkZRfv.png",
        "group": "National DVB-T",
        "channel": "14"
    },
    {
        "name": "Iris",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-ki/ki-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/Ixz1BY3.png",
        "group": "National DVB-T",
        "channel": "15"
    },
    {
        "name": "Rai 5",
        "stream_url": "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=395276&output=7&forceUserAgent=rainet/4.0.5",
        "logo": "https://i.imgur.com/Leu2zTO.png",
        "group": "National DVB-T",
        "channel": "16"
    },
    {
        "name": "Rai Movie",
        "stream_url": "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=747002&output=7&forceUserAgent=rainet/4.0.5",
        "logo": "https://i.imgur.com/RKpO8CE.png",
        "group": "National DVB-T",
        "channel": "17"
    },
    {
        "name": "Rai Premium",
        "stream_url": "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746992&output=7&forceUserAgent=rainet/4.0.5",
        "logo": "https://i.imgur.com/RKI4nFy.png",
        "group": "National DVB-T",
        "channel": "18"
    },
    {
        "name": "Cielo",
        "stream_url": "https://hlslive-web-gcdn-skycdn-it.akamaized.net/TACT/11219/cieloweb/master.m3u8?hdnea=st=1701861650~exp=1765449000~acl=/*~hmac=84c9f3f71e57b13c3a67afa8b29a8591ea9ed84bf786524399545d94be1ec04d",
        "logo": "https://i.imgur.com/cPluF03.png",
        "group": "National DVB-T",
        "channel": "19"
    },
    {
        "name": "27 Twentyseven",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-ts/ts-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/y2PdPCK.png",
        "group": "National DVB-T",
        "channel": "20"
    },
    {
        "name": "RaiItalia",
        "stream_url": "https://ilglobotv-live.akamaized.net/channels/RAIItaliaSudAfrica/Live.m3u8",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Rai_Italia_-_Logo_2017.svg/2560px-Rai_Italia_-_Logo_2017.svg.png",
        "group": "Rai Italia Africa",
        "channel": "21"
    },
    {
        "name": "TV 2000",
        "stream_url": "https://hls-live-tv2000.akamaized.net/hls/live/2028510/tv2000/master.m3u8",
        "logo": "https://i.imgur.com/x7RaK3a.png",
        "group": "National DVB-T",
        "channel": "22"
    },
    {
        "name": "La7d",
        "stream_url": "https://viamotionhsi.netplus.ch/live/eds/la7d/browser-HLS8/la7d.m3u8",
        "logo": "https://i.imgur.com/AOL9nMw.png",
        "group": "National DVB-T",
        "channel": "23"
    },
    {
        "name": "La 5",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-ka/ka-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/UNyJaho.png",
        "group": "National DVB-T",
        "channel": "24"
    },
    {
        "name": "Real Time",
        "stream_url": "https://amg16146-wbdi-amg16146c2-samsung-it-1835.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-realtime-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/9dcTYg1.png",
        "group": "National DVB-T",
        "channel": "25"
    },
    {
        "name": "QVC",
        "stream_url": "https://qrg.akamaized.net/hls/live/2017383/lsqvc1it/master.m3u8",
        "logo": "https://i.imgur.com/Ea7iUX2.png",
        "group": "National DVB-T",
        "channel": "26"
    },
    {
        "name": "Food Network",
        "stream_url": "https://amg16146-wbdi-amg16146c3-samsung-it-1836.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-foodnetwork-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/i60OYr9.png",
        "group": "National DVB-T",
        "channel": "27"
    },
    {
        "name": "Cine34",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-b6/b6-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/YyldwhI.png",
        "group": "National DVB-T",
        "channel": "28"
    },
    {
        "name": "Focus",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-fu/fu-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/M4smqpF.png",
        "group": "National DVB-T",
        "channel": "29"
    },
    {
        "name": "RTL 102.5",
        "stream_url": "https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S97044836/tbbP8T1ZRPBL/playlist.m3u8",
        "logo": "https://i.imgur.com/KdissvS.png",
        "group": "National DVB-T",
        "channel": "30"
    },
    {
        "name": "Warner TV",
        "stream_url": "https://amg16146-wbdi-amg16146c4-samsung-it-1837.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-warnertv-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/oIWFcOC.png",
        "group": "National DVB-T",
        "channel": "31"
    },
    {
        "name": "Giallo",
        "stream_url": "https://amg16146-wbdi-amg16146c5-samsung-it-1838.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-giallo-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/0PIRwZS.png",
        "group": "National DVB-T",
        "channel": "32"
    },
    {
        "name": "Top Crime",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-lt/lt-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/RFIwv9O.png",
        "group": "National DVB-T",
        "channel": "33"
    },
    {
        "name": "BOING",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-kb/kb-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/niSlrqT.png",
        "group": "National DVB-T",
        "channel": "34"
    },
    {
        "name": "K2",
        "stream_url": "https://amg16146-wbdi-amg16146c6-samsung-it-1839.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-k2-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/wlLgSiA.png",
        "group": "National DVB-T",
        "channel": "35"
    },
    {
        "name": "Rai Gulp",
        "stream_url": "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746953&output=7&forceUserAgent=rainet/4.0.5",
        "logo": "https://i.imgur.com/lu1DPVb.png",
        "group": "National DVB-T",
        "channel": "36"
    },
    {
        "name": "Rai YoYo",
        "stream_url": "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746899&output=7&forceUserAgent=rainet/4.0.5",
        "logo": "https://i.imgur.com/DRSa3ys.png",
        "group": "National DVB-T",
        "channel": "37"
    },
    {
        "name": "Frisbee",
        "stream_url": "https://amg16146-wbdi-amg16146c7-samsung-it-1840.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-frisbee-samsungit/playlist.m3u8",
        "logo": "https://i.imgur.com/9y1zIAe.png",
        "group": "National DVB-T",
        "channel": "38"
    },
    {
        "name": "Cartoonito",
        "stream_url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-la/la-clr.isml/index.m3u8",
        "logo": "https://i.imgur.com/zqc0TrY.png",
        "group": "National DVB-T",
        "channel": "39"
    },
    {
        "name": "Super!",
        "stream_url": "https://495c5a85d9074f29acffeaea9e0215eb.msvdn.net/super/super_main/super_main_hbbtv/playlist.m3u8",
        "logo": "https://i.imgur.com/zDByOwo.png",
        "group": "National DVB-T",
        "channel": "40"
    },
    {
        "name": "Rai News 24",
        "stream_url": "https://rainews1-live.akamaized.net/hls/live/598326/rainews1/rainews1/playlist.m3u8",
        "logo": "https://i.imgur.com/gdzGwB6.png",
        "group": "National DVB-T",
        "channel": "41"
    }
]

def _manifest_type(url: str) -> str:
    u = url.lower()
    if ".mpd" in u or "manifest.mpd" in u:
        return "mpd"
    return "hls"

def _referer_for(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}/" if p.scheme and p.netloc else ""

def _headers(ref: str) -> str:
    return f"User-Agent={quote(DEFAULT_UA)}&Referer={quote(ref)}"

def list_channels():
    for idx, ch in enumerate(CHANNELS):
        label = f"{ch.get('channel', idx+1)} • {ch.get('name','Channel')}"
        li = xbmcgui.ListItem(label=label)
        li.setInfo("video", {"title": ch.get("name",""), "genre": ch.get("group","")})
        logo = ch.get("logo")
        if logo and not str(logo).startswith("data:"):
            li.setArt({"thumb": logo, "icon": logo, "logo": logo})
        li.setProperty("IsPlayable", "true")
        # Wir rufen beim Klick das Plugin erneut mit ?play=<index> auf
        play_url = f"{sys.argv[0]}?play={idx}"
        xbmcplugin.addDirectoryItem(HANDLE, play_url, li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE, cacheToDisc=False)

def play_channel(index: int):
    ch = CHANNELS[index]
    url = ch["stream_url"]
    ref = _referer_for(url)
    headers = _headers(ref)
    full_url = url + "|" + headers

    li = xbmcgui.ListItem(path=full_url)
    li.setProperty("IsPlayable", "true")

    mtype = _manifest_type(url)
    li.setMimeType("application/dash+xml" if mtype == "mpd" else "application/vnd.apple.mpegurl")
    li.setContentLookup(False)
    li.setProperty("inputstream", "inputstream.adaptive")
    li.setProperty("inputstream.adaptive.manifest_type", mtype)
    li.setProperty("inputstream.adaptive.stream_headers", headers)

    logo = ch.get("logo")
    if logo and not str(logo).startswith("data:"):
        li.setArt({"thumb": logo, "icon": logo, "logo": logo})

    xbmcplugin.setResolvedUrl(HANDLE, True, li)

def get_params():
    # argv[2] beginnt mit "?". Beispiel: "?play=0"
    if len(sys.argv) > 2 and sys.argv[2]:
        return parse_qs(sys.argv[2][1:])
    return {}

if __name__ == "__main__":
    params = get_params()
    if "play" in params:
        try:
            idx = int(params["play"][0])
            play_channel(idx)
        except Exception as e:
            xbmc.log(f"[CrushTV] play error: {e}", xbmc.LOGERROR)
            xbmcgui.Dialog().notification("CrushTV", "Stream konnte nicht gestartet werden", xbmcgui.NOTIFICATION_ERROR, 5000)
    else:
        list_channels()
