#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kate
Version  : 19.12.2
Release  : 19
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kate-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kate-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kate-19.12.2.tar.xz.sig
Summary  : Advanced Text Editor
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kate-bin = %{version}-%{release}
Requires: kate-data = %{version}-%{release}
Requires: kate-lib = %{version}-%{release}
Requires: kate-license = %{version}-%{release}
Requires: kate-locales = %{version}-%{release}
Requires: kate-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev
BuildRequires : ktexteditor-dev
BuildRequires : threadweaver-dev

%description
Kate XML plugin 0.9, 2002-07-20, Daniel Naber <daniel.naber@t-online.de>
This plugin gives hints about what's allowed at a certain position in
an XML file, according to the file's DTD. It will list possible
elements, attributes, attribute values or named entities, depending
on the cursor position. It's also possible to close the nearest
not-yet-closed element (this function's scope is limited to some
hundred characters).

%package bin
Summary: bin components for the kate package.
Group: Binaries
Requires: kate-data = %{version}-%{release}
Requires: kate-license = %{version}-%{release}

%description bin
bin components for the kate package.


%package data
Summary: data components for the kate package.
Group: Data

%description data
data components for the kate package.


%package doc
Summary: doc components for the kate package.
Group: Documentation
Requires: kate-man = %{version}-%{release}

%description doc
doc components for the kate package.


%package lib
Summary: lib components for the kate package.
Group: Libraries
Requires: kate-data = %{version}-%{release}
Requires: kate-license = %{version}-%{release}

%description lib
lib components for the kate package.


%package license
Summary: license components for the kate package.
Group: Default

%description license
license components for the kate package.


%package locales
Summary: locales components for the kate package.
Group: Default

%description locales
locales components for the kate package.


%package man
Summary: man components for the kate package.
Group: Default

%description man
man components for the kate package.


%prep
%setup -q -n kate-19.12.2
cd %{_builddir}/kate-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581015101
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581015101
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kate
cp %{_builddir}/kate-19.12.2/COPYING-GPL3 %{buildroot}/usr/share/package-licenses/kate/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/kate-19.12.2/COPYING-LGPL3 %{buildroot}/usr/share/package-licenses/kate/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/kate-19.12.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kate/e2b9735e3fe7740e377cd085eee521c819a4e736
cp %{_builddir}/kate-19.12.2/kate/COPYING.LIB %{buildroot}/usr/share/package-licenses/kate/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang kate-ctags-plugin
%find_lang kate-replicode-plugin
%find_lang kate
%find_lang katebacktracebrowserplugin
%find_lang katebuild-plugin
%find_lang katecloseexceptplugin
%find_lang katefilebrowserplugin
%find_lang katefiletree
%find_lang kategdbplugin
%find_lang katekonsoleplugin
%find_lang kateopenheader
%find_lang kateproject
%find_lang katesearch
%find_lang katesnippetsplugin
%find_lang katesql
%find_lang katesymbolviewer
%find_lang katetextfilter
%find_lang katexmlcheck
%find_lang katexmltools
%find_lang kwrite
%find_lang plasma_applet_org.kde.plasma.katesessions
%find_lang tabswitcherplugin
%find_lang ktexteditorpreviewplugin
%find_lang kateexternaltoolsplugin
%find_lang lspclient

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kate
/usr/bin/kwrite

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kate.desktop
/usr/share/applications/org.kde.kwrite.desktop
/usr/share/icons/hicolor/128x128/apps/kate.png
/usr/share/icons/hicolor/128x128/apps/kwrite.png
/usr/share/icons/hicolor/150x150/apps/kate.png
/usr/share/icons/hicolor/16x16/apps/kate.png
/usr/share/icons/hicolor/16x16/apps/kwrite.png
/usr/share/icons/hicolor/22x22/apps/kate.png
/usr/share/icons/hicolor/22x22/apps/kwrite.png
/usr/share/icons/hicolor/310x310/apps/kate.png
/usr/share/icons/hicolor/32x32/apps/kate.png
/usr/share/icons/hicolor/32x32/apps/kwrite.png
/usr/share/icons/hicolor/44x44/apps/kate.png
/usr/share/icons/hicolor/48x48/apps/kate.png
/usr/share/icons/hicolor/48x48/apps/kwrite.png
/usr/share/icons/hicolor/64x64/apps/kate.png
/usr/share/icons/hicolor/64x64/apps/kwrite.png
/usr/share/icons/hicolor/scalable/apps/kate.svg
/usr/share/icons/hicolor/scalable/apps/kwrite.svgz
/usr/share/kateproject/kateproject.example
/usr/share/katexmltools/html4-loose.dtd.xml
/usr/share/katexmltools/html4-strict.dtd.xml
/usr/share/katexmltools/kcfg.dtd.xml
/usr/share/katexmltools/kde-docbook.dtd.xml
/usr/share/katexmltools/kpartgui.dtd.xml
/usr/share/katexmltools/language.dtd.xml
/usr/share/katexmltools/simplify_dtd.xsl
/usr/share/katexmltools/testcases.xml
/usr/share/katexmltools/xhtml1-frameset.dtd.xml
/usr/share/katexmltools/xhtml1-strict.dtd.xml
/usr/share/katexmltools/xhtml1-transitional.dtd.xml
/usr/share/katexmltools/xslt-1.0.dtd.xml
/usr/share/metainfo/org.kde.kate.appdata.xml
/usr/share/metainfo/org.kde.kwrite.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kate/arrow-down-double-22.png
/usr/share/doc/HTML/ca/kate/arrow-up-double-22.png
/usr/share/doc/HTML/ca/kate/backtrace-settings.png
/usr/share/doc/HTML/ca/kate/bookmarks-22.png
/usr/share/doc/HTML/ca/kate/build-output.png
/usr/share/doc/HTML/ca/kate/close-except-like.png
/usr/share/doc/HTML/ca/kate/configdialog01.png
/usr/share/doc/HTML/ca/kate/configure-22.png
/usr/share/doc/HTML/ca/kate/configure-shortcuts-22.png
/usr/share/doc/HTML/ca/kate/configuring.docbook
/usr/share/doc/HTML/ca/kate/ctags-global-setting.png
/usr/share/doc/HTML/ca/kate/ctags-session-setting.png
/usr/share/doc/HTML/ca/kate/development.docbook
/usr/share/doc/HTML/ca/kate/dialog-ok-22.png
/usr/share/doc/HTML/ca/kate/document-new-22.png
/usr/share/doc/HTML/ca/kate/document-open-22.png
/usr/share/doc/HTML/ca/kate/document-save-22.png
/usr/share/doc/HTML/ca/kate/document-save-as-22.png
/usr/share/doc/HTML/ca/kate/documentswitcher.png
/usr/share/doc/HTML/ca/kate/edit-copy-22.png
/usr/share/doc/HTML/ca/kate/edit-delete-22.png
/usr/share/doc/HTML/ca/kate/edit-select-all-22.png
/usr/share/doc/HTML/ca/kate/format-text-superscript-22.png
/usr/share/doc/HTML/ca/kate/fundamentals.docbook
/usr/share/doc/HTML/ca/kate/games-config-options-22.png
/usr/share/doc/HTML/ca/kate/gdb-call-stack.png
/usr/share/doc/HTML/ca/kate/gdb-io.png
/usr/share/doc/HTML/ca/kate/gdb-locals.png
/usr/share/doc/HTML/ca/kate/gdb-output.png
/usr/share/doc/HTML/ca/kate/gdb-settings.png
/usr/share/doc/HTML/ca/kate/go-down-22.png
/usr/share/doc/HTML/ca/kate/go-next-22.png
/usr/share/doc/HTML/ca/kate/go-previous-22.png
/usr/share/doc/HTML/ca/kate/go-up-22.png
/usr/share/doc/HTML/ca/kate/index.cache.bz2
/usr/share/doc/HTML/ca/kate/index.docbook
/usr/share/doc/HTML/ca/kate/kate.png
/usr/share/doc/HTML/ca/kate/list-add-22.png
/usr/share/doc/HTML/ca/kate/mascot_kate.png
/usr/share/doc/HTML/ca/kate/menus.docbook
/usr/share/doc/HTML/ca/kate/plugins.docbook
/usr/share/doc/HTML/ca/kate/project-completition.png
/usr/share/doc/HTML/ca/kate/project-configure.png
/usr/share/doc/HTML/ca/kate/project-current-analysis.png
/usr/share/doc/HTML/ca/kate/project-quickopen.png
/usr/share/doc/HTML/ca/kate/project-search.png
/usr/share/doc/HTML/ca/kate/project-view.png
/usr/share/doc/HTML/ca/kate/snippets-form.png
/usr/share/doc/HTML/ca/kate/snippets-panel.png
/usr/share/doc/HTML/ca/kate/snippets-repository.png
/usr/share/doc/HTML/ca/kate/snippets-usage.png
/usr/share/doc/HTML/ca/kate/symbolviewer-settings.png
/usr/share/doc/HTML/ca/kate/system-switch-user-22.png
/usr/share/doc/HTML/ca/kate/tab-duplicate-22.png
/usr/share/doc/HTML/ca/kate/tab-new-22.png
/usr/share/doc/HTML/ca/kate/textfilter.png
/usr/share/doc/HTML/ca/kate/view-refresh-22.png
/usr/share/doc/HTML/ca/kate/view-split-left-right-22.png
/usr/share/doc/HTML/ca/katepart/advanced.docbook
/usr/share/doc/HTML/ca/katepart/arrow-down-double-22.png
/usr/share/doc/HTML/ca/katepart/arrow-up-double-22.png
/usr/share/doc/HTML/ca/katepart/comma-to.png
/usr/share/doc/HTML/ca/katepart/configure-shortcuts-22.png
/usr/share/doc/HTML/ca/katepart/configuring.docbook
/usr/share/doc/HTML/ca/katepart/development.docbook
/usr/share/doc/HTML/ca/katepart/edit-select-all-22.png
/usr/share/doc/HTML/ca/katepart/format-text-superscript-22.png
/usr/share/doc/HTML/ca/katepart/fundamentals.docbook
/usr/share/doc/HTML/ca/katepart/index.cache.bz2
/usr/share/doc/HTML/ca/katepart/index.docbook
/usr/share/doc/HTML/ca/katepart/line-modification-system.png
/usr/share/doc/HTML/ca/katepart/menus.docbook
/usr/share/doc/HTML/ca/katepart/minimap.png
/usr/share/doc/HTML/ca/katepart/part.docbook
/usr/share/doc/HTML/ca/katepart/regular-expressions.docbook
/usr/share/doc/HTML/ca/katepart/vi.docbook
/usr/share/doc/HTML/ca/kwrite/index.cache.bz2
/usr/share/doc/HTML/ca/kwrite/index.docbook
/usr/share/doc/HTML/de/kate/configuring.docbook
/usr/share/doc/HTML/de/kate/development.docbook
/usr/share/doc/HTML/de/kate/fundamentals.docbook
/usr/share/doc/HTML/de/kate/index.cache.bz2
/usr/share/doc/HTML/de/kate/index.docbook
/usr/share/doc/HTML/de/kate/menus.docbook
/usr/share/doc/HTML/de/kate/plugins.docbook
/usr/share/doc/HTML/de/katepart/advanced.docbook
/usr/share/doc/HTML/de/katepart/configuring.docbook
/usr/share/doc/HTML/de/katepart/development.docbook
/usr/share/doc/HTML/de/katepart/fundamentals.docbook
/usr/share/doc/HTML/de/katepart/index.cache.bz2
/usr/share/doc/HTML/de/katepart/index.docbook
/usr/share/doc/HTML/de/katepart/menus.docbook
/usr/share/doc/HTML/de/katepart/part.docbook
/usr/share/doc/HTML/de/katepart/regular-expressions.docbook
/usr/share/doc/HTML/de/katepart/vi.docbook
/usr/share/doc/HTML/de/kwrite/index.cache.bz2
/usr/share/doc/HTML/de/kwrite/index.docbook
/usr/share/doc/HTML/en/kate/arrow-down-double-22.png
/usr/share/doc/HTML/en/kate/arrow-up-double-22.png
/usr/share/doc/HTML/en/kate/backtrace-settings.png
/usr/share/doc/HTML/en/kate/bookmarks-22.png
/usr/share/doc/HTML/en/kate/build-output.png
/usr/share/doc/HTML/en/kate/close-except-like.png
/usr/share/doc/HTML/en/kate/configdialog01.png
/usr/share/doc/HTML/en/kate/configure-22.png
/usr/share/doc/HTML/en/kate/configure-shortcuts-22.png
/usr/share/doc/HTML/en/kate/configuring.docbook
/usr/share/doc/HTML/en/kate/ctags-global-setting.png
/usr/share/doc/HTML/en/kate/ctags-session-setting.png
/usr/share/doc/HTML/en/kate/development.docbook
/usr/share/doc/HTML/en/kate/dialog-ok-22.png
/usr/share/doc/HTML/en/kate/document-new-22.png
/usr/share/doc/HTML/en/kate/document-open-22.png
/usr/share/doc/HTML/en/kate/document-save-22.png
/usr/share/doc/HTML/en/kate/document-save-as-22.png
/usr/share/doc/HTML/en/kate/documentswitcher.png
/usr/share/doc/HTML/en/kate/edit-copy-22.png
/usr/share/doc/HTML/en/kate/edit-delete-22.png
/usr/share/doc/HTML/en/kate/edit-select-all-22.png
/usr/share/doc/HTML/en/kate/format-text-superscript-22.png
/usr/share/doc/HTML/en/kate/fundamentals.docbook
/usr/share/doc/HTML/en/kate/games-config-options-22.png
/usr/share/doc/HTML/en/kate/gdb-call-stack.png
/usr/share/doc/HTML/en/kate/gdb-io.png
/usr/share/doc/HTML/en/kate/gdb-locals.png
/usr/share/doc/HTML/en/kate/gdb-output.png
/usr/share/doc/HTML/en/kate/gdb-settings.png
/usr/share/doc/HTML/en/kate/go-down-22.png
/usr/share/doc/HTML/en/kate/go-next-22.png
/usr/share/doc/HTML/en/kate/go-previous-22.png
/usr/share/doc/HTML/en/kate/go-up-22.png
/usr/share/doc/HTML/en/kate/index.cache.bz2
/usr/share/doc/HTML/en/kate/index.docbook
/usr/share/doc/HTML/en/kate/kate.png
/usr/share/doc/HTML/en/kate/list-add-22.png
/usr/share/doc/HTML/en/kate/mascot_kate.png
/usr/share/doc/HTML/en/kate/menus.docbook
/usr/share/doc/HTML/en/kate/plugins.docbook
/usr/share/doc/HTML/en/kate/project-completition.png
/usr/share/doc/HTML/en/kate/project-configure.png
/usr/share/doc/HTML/en/kate/project-current-analysis.png
/usr/share/doc/HTML/en/kate/project-quickopen.png
/usr/share/doc/HTML/en/kate/project-search.png
/usr/share/doc/HTML/en/kate/project-view.png
/usr/share/doc/HTML/en/kate/snippets-form.png
/usr/share/doc/HTML/en/kate/snippets-panel.png
/usr/share/doc/HTML/en/kate/snippets-repository.png
/usr/share/doc/HTML/en/kate/snippets-usage.png
/usr/share/doc/HTML/en/kate/symbolviewer-settings.png
/usr/share/doc/HTML/en/kate/system-switch-user-22.png
/usr/share/doc/HTML/en/kate/tab-duplicate-22.png
/usr/share/doc/HTML/en/kate/tab-new-22.png
/usr/share/doc/HTML/en/kate/textfilter.png
/usr/share/doc/HTML/en/kate/view-refresh-22.png
/usr/share/doc/HTML/en/kate/view-split-left-right-22.png
/usr/share/doc/HTML/en/katepart/advanced.docbook
/usr/share/doc/HTML/en/katepart/arrow-down-double-22.png
/usr/share/doc/HTML/en/katepart/arrow-up-double-22.png
/usr/share/doc/HTML/en/katepart/comma-to.png
/usr/share/doc/HTML/en/katepart/configure-shortcuts-22.png
/usr/share/doc/HTML/en/katepart/configuring.docbook
/usr/share/doc/HTML/en/katepart/development.docbook
/usr/share/doc/HTML/en/katepart/edit-select-all-22.png
/usr/share/doc/HTML/en/katepart/format-text-superscript-22.png
/usr/share/doc/HTML/en/katepart/fundamentals.docbook
/usr/share/doc/HTML/en/katepart/highlighted.png
/usr/share/doc/HTML/en/katepart/index.cache.bz2
/usr/share/doc/HTML/en/katepart/index.docbook
/usr/share/doc/HTML/en/katepart/line-modification-system.png
/usr/share/doc/HTML/en/katepart/menus.docbook
/usr/share/doc/HTML/en/katepart/minimap.png
/usr/share/doc/HTML/en/katepart/part.docbook
/usr/share/doc/HTML/en/katepart/regular-expressions.docbook
/usr/share/doc/HTML/en/katepart/unhighlighted.png
/usr/share/doc/HTML/en/katepart/vi.docbook
/usr/share/doc/HTML/en/kwrite/index.cache.bz2
/usr/share/doc/HTML/en/kwrite/index.docbook
/usr/share/doc/HTML/es/kwrite/index.cache.bz2
/usr/share/doc/HTML/es/kwrite/index.docbook
/usr/share/doc/HTML/it/kate/configuring.docbook
/usr/share/doc/HTML/it/kate/development.docbook
/usr/share/doc/HTML/it/kate/fundamentals.docbook
/usr/share/doc/HTML/it/kate/index.cache.bz2
/usr/share/doc/HTML/it/kate/index.docbook
/usr/share/doc/HTML/it/kate/menus.docbook
/usr/share/doc/HTML/it/kate/plugins.docbook
/usr/share/doc/HTML/it/katepart/advanced.docbook
/usr/share/doc/HTML/it/katepart/configuring.docbook
/usr/share/doc/HTML/it/katepart/development.docbook
/usr/share/doc/HTML/it/katepart/fundamentals.docbook
/usr/share/doc/HTML/it/katepart/index.cache.bz2
/usr/share/doc/HTML/it/katepart/index.docbook
/usr/share/doc/HTML/it/katepart/menus.docbook
/usr/share/doc/HTML/it/katepart/part.docbook
/usr/share/doc/HTML/it/katepart/regular-expressions.docbook
/usr/share/doc/HTML/it/katepart/vi.docbook
/usr/share/doc/HTML/it/kwrite/index.cache.bz2
/usr/share/doc/HTML/it/kwrite/index.docbook
/usr/share/doc/HTML/nl/kate/configuring.docbook
/usr/share/doc/HTML/nl/kate/development.docbook
/usr/share/doc/HTML/nl/kate/fundamentals.docbook
/usr/share/doc/HTML/nl/kate/index.cache.bz2
/usr/share/doc/HTML/nl/kate/index.docbook
/usr/share/doc/HTML/nl/kate/menus.docbook
/usr/share/doc/HTML/nl/kate/plugins.docbook
/usr/share/doc/HTML/nl/katepart/advanced.docbook
/usr/share/doc/HTML/nl/katepart/configuring.docbook
/usr/share/doc/HTML/nl/katepart/development.docbook
/usr/share/doc/HTML/nl/katepart/fundamentals.docbook
/usr/share/doc/HTML/nl/katepart/index.cache.bz2
/usr/share/doc/HTML/nl/katepart/index.docbook
/usr/share/doc/HTML/nl/katepart/menus.docbook
/usr/share/doc/HTML/nl/katepart/part.docbook
/usr/share/doc/HTML/nl/katepart/regular-expressions.docbook
/usr/share/doc/HTML/nl/katepart/vi.docbook
/usr/share/doc/HTML/nl/kwrite/index.cache.bz2
/usr/share/doc/HTML/nl/kwrite/index.docbook
/usr/share/doc/HTML/pt/kwrite/index.cache.bz2
/usr/share/doc/HTML/pt/kwrite/index.docbook
/usr/share/doc/HTML/pt_BR/kate/comma-to.png
/usr/share/doc/HTML/pt_BR/kate/configdialog01.png
/usr/share/doc/HTML/pt_BR/kate/configuring.docbook
/usr/share/doc/HTML/pt_BR/kate/development.docbook
/usr/share/doc/HTML/pt_BR/kate/fundamentals.docbook
/usr/share/doc/HTML/pt_BR/kate/highlighted.png
/usr/share/doc/HTML/pt_BR/kate/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kate/index.docbook
/usr/share/doc/HTML/pt_BR/kate/mascot_kate.png
/usr/share/doc/HTML/pt_BR/kate/menus.docbook
/usr/share/doc/HTML/pt_BR/kate/plugins.docbook
/usr/share/doc/HTML/pt_BR/kate/unhighlighted.png
/usr/share/doc/HTML/pt_BR/katepart/advanced.docbook
/usr/share/doc/HTML/pt_BR/katepart/configuring.docbook
/usr/share/doc/HTML/pt_BR/katepart/development.docbook
/usr/share/doc/HTML/pt_BR/katepart/fundamentals.docbook
/usr/share/doc/HTML/pt_BR/katepart/index.cache.bz2
/usr/share/doc/HTML/pt_BR/katepart/index.docbook
/usr/share/doc/HTML/pt_BR/katepart/menus.docbook
/usr/share/doc/HTML/pt_BR/katepart/part.docbook
/usr/share/doc/HTML/pt_BR/katepart/regular-expressions.docbook
/usr/share/doc/HTML/pt_BR/katepart/vi.docbook
/usr/share/doc/HTML/pt_BR/kwrite/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kwrite/index.docbook
/usr/share/doc/HTML/ru/kwrite/index.cache.bz2
/usr/share/doc/HTML/ru/kwrite/index.docbook
/usr/share/doc/HTML/sv/kate/configuring.docbook
/usr/share/doc/HTML/sv/kate/development.docbook
/usr/share/doc/HTML/sv/kate/fundamentals.docbook
/usr/share/doc/HTML/sv/kate/index.cache.bz2
/usr/share/doc/HTML/sv/kate/index.docbook
/usr/share/doc/HTML/sv/kate/menus.docbook
/usr/share/doc/HTML/sv/kate/plugins.docbook
/usr/share/doc/HTML/sv/katepart/advanced.docbook
/usr/share/doc/HTML/sv/katepart/configuring.docbook
/usr/share/doc/HTML/sv/katepart/development.docbook
/usr/share/doc/HTML/sv/katepart/fundamentals.docbook
/usr/share/doc/HTML/sv/katepart/index.cache.bz2
/usr/share/doc/HTML/sv/katepart/index.docbook
/usr/share/doc/HTML/sv/katepart/menus.docbook
/usr/share/doc/HTML/sv/katepart/part.docbook
/usr/share/doc/HTML/sv/katepart/regular-expressions.docbook
/usr/share/doc/HTML/sv/katepart/vi.docbook
/usr/share/doc/HTML/sv/kwrite/index.cache.bz2
/usr/share/doc/HTML/sv/kwrite/index.docbook
/usr/share/doc/HTML/uk/kate/backtrace-settings.png
/usr/share/doc/HTML/uk/kate/build-output.png
/usr/share/doc/HTML/uk/kate/close-except-like.png
/usr/share/doc/HTML/uk/kate/configdialog01.png
/usr/share/doc/HTML/uk/kate/configuring.docbook
/usr/share/doc/HTML/uk/kate/ctags-global-setting.png
/usr/share/doc/HTML/uk/kate/ctags-session-setting.png
/usr/share/doc/HTML/uk/kate/development.docbook
/usr/share/doc/HTML/uk/kate/fundamentals.docbook
/usr/share/doc/HTML/uk/kate/gdb-output.png
/usr/share/doc/HTML/uk/kate/gdb-settings.png
/usr/share/doc/HTML/uk/kate/index.cache.bz2
/usr/share/doc/HTML/uk/kate/index.docbook
/usr/share/doc/HTML/uk/kate/kate.png
/usr/share/doc/HTML/uk/kate/menus.docbook
/usr/share/doc/HTML/uk/kate/plugins.docbook
/usr/share/doc/HTML/uk/kate/project-completition.png
/usr/share/doc/HTML/uk/kate/project-configure.png
/usr/share/doc/HTML/uk/kate/project-current-analysis.png
/usr/share/doc/HTML/uk/kate/project-quickopen.png
/usr/share/doc/HTML/uk/kate/project-search.png
/usr/share/doc/HTML/uk/kate/project-view.png
/usr/share/doc/HTML/uk/kate/rust-configuration.png
/usr/share/doc/HTML/uk/kate/textfilter.png
/usr/share/doc/HTML/uk/katepart/advanced.docbook
/usr/share/doc/HTML/uk/katepart/configuring.docbook
/usr/share/doc/HTML/uk/katepart/development.docbook
/usr/share/doc/HTML/uk/katepart/fundamentals.docbook
/usr/share/doc/HTML/uk/katepart/index.cache.bz2
/usr/share/doc/HTML/uk/katepart/index.docbook
/usr/share/doc/HTML/uk/katepart/menus.docbook
/usr/share/doc/HTML/uk/katepart/part.docbook
/usr/share/doc/HTML/uk/katepart/regular-expressions.docbook
/usr/share/doc/HTML/uk/katepart/vi.docbook
/usr/share/doc/HTML/uk/kwrite/index.cache.bz2
/usr/share/doc/HTML/uk/kwrite/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/ktexteditor/externaltoolsplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katebacktracebrowserplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katebuildplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katecloseexceptplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katectagsplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katefilebrowserplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katefiletreeplugin.so
/usr/lib64/qt5/plugins/ktexteditor/kategdbplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katekonsoleplugin.so
/usr/lib64/qt5/plugins/ktexteditor/kateopenheaderplugin.so
/usr/lib64/qt5/plugins/ktexteditor/kateprojectplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katereplicodeplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katesearchplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katesnippetsplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katesqlplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katesymbolviewerplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katexmlcheckplugin.so
/usr/lib64/qt5/plugins/ktexteditor/katexmltoolsplugin.so
/usr/lib64/qt5/plugins/ktexteditor/ktexteditorpreviewplugin.so
/usr/lib64/qt5/plugins/ktexteditor/lspclientplugin.so
/usr/lib64/qt5/plugins/ktexteditor/tabswitcherplugin.so
/usr/lib64/qt5/plugins/ktexteditor/textfilterplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kate/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/kate/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/kate/e2b9735e3fe7740e377cd085eee521c819a4e736
/usr/share/package-licenses/kate/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kate.1
/usr/share/man/de/man1/kate.1
/usr/share/man/es/man1/kate.1
/usr/share/man/it/man1/kate.1
/usr/share/man/man1/kate.1
/usr/share/man/nl/man1/kate.1
/usr/share/man/pt/man1/kate.1
/usr/share/man/pt_BR/man1/kate.1
/usr/share/man/sv/man1/kate.1
/usr/share/man/uk/man1/kate.1

%files locales -f kate-ctags-plugin.lang -f kate-replicode-plugin.lang -f kate.lang -f katebacktracebrowserplugin.lang -f katebuild-plugin.lang -f katecloseexceptplugin.lang -f katefilebrowserplugin.lang -f katefiletree.lang -f kategdbplugin.lang -f katekonsoleplugin.lang -f kateopenheader.lang -f kateproject.lang -f katesearch.lang -f katesnippetsplugin.lang -f katesql.lang -f katesymbolviewer.lang -f katetextfilter.lang -f katexmlcheck.lang -f katexmltools.lang -f kwrite.lang -f plasma_applet_org.kde.plasma.katesessions.lang -f tabswitcherplugin.lang -f ktexteditorpreviewplugin.lang -f kateexternaltoolsplugin.lang -f lspclient.lang
%defattr(-,root,root,-)

