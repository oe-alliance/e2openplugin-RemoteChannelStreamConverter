# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os,gettext

PluginLanguageDomain = "RemoteChannelStreamConverter"
PluginLanguagePath = "Extensions/RemoteChannelStreamConverter/po"

def localeInit():
	if os.path.exists(resolveFilename(SCOPE_PLUGINS, os.path.join(PluginLanguagePath, language.getLanguage()))):
		lang = language.getLanguage()
	else:
		lang = language.getLanguage()[:2]
	os.environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))
	gettext.bindtextdomain('enigma2', resolveFilename(SCOPE_LANGUAGE, ""))

def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		t = gettext.dgettext('enigma2', txt)
	return t


localeInit()
language.addCallback(localeInit)
