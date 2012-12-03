LANGS = ar bg ca cs da de el en en_GB es et fa fi fr fy he hr hu is it lt lv nl no nb pl pt pt_BR ro ru sv sk sl sr th tr uk
LANGMO = $(LANGS:=.mo)
LANGPO = $(LANGS:=.po)

if UPDATE_PO
# the TRANSLATORS: allows putting translation comments before the to-be-translated line.
rcsc-py.pot: $(top_srcdir)/src/*.py
	$(XGETTEXT) --no-wrap -L Python --from-code=UTF-8 --add-comments="TRANSLATORS:" -d @PACKAGE_NAME@ -s -o $@ $^

rcsc.pot: rcsc-py.pot
	sed --in-place rcsc-py.pot --expression=s/CHARSET/UTF-8/
	$(MSGUNIQ) --no-wrap --no-location $^ -o $@

%.po: rcsc.pot
	if [ -f $@ ]; then \
		$(MSGMERGE) --backup=none --no-wrap --no-location -s -N -U $@ $< && touch $@; \
	else \
		$(MSGINIT) -l $@ -o $@ -i $< --no-translator; \
	fi
endif

.po.mo:
	$(MSGFMT) -o $@ $<

BUILT_SOURCES = $(LANGMO)
CLEANFILES = $(LANGMO) rcsc-py.pot rcsc.pot

dist-hook: $(LANGPO)

install-data-local: $(LANGMO)
	for lang in $(LANGS); do \
		$(mkinstalldirs) $(DESTDIR)/usr/lib/enigma2/python/Plugins/Extensions/RemoteChannelStreamConverter/po/$$lang/LC_MESSAGES; \
		$(INSTALL_DATA) $$lang.mo $(DESTDIR)/usr/lib/enigma2/python/Plugins/Extensions/RemoteChannelStreamConverter/po/$$lang/LC_MESSAGES/RemoteChannelStreamConverter.mo; \
	done

uninstall-local:
	for lang in $(LANGS); do \
		$(RM) $(DESTDIR)/usr/lib/enigma2/python/Plugins/Extensions/RemoteChannelStreamConverter/po/$$lang/LC_MESSAGES/RemoteChannelStreamConverter.mo; \
	done
