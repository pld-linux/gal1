Summary:	GNOME Application Libs (GAL)
Summary(pl.UTF-8):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR.UTF-8):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru.UTF-8):	Библиотека для составных документов в GNOME
Summary(uk.UTF-8):	Бібліотека для компонентних документів в GNOME
Name:		gal1
Version:	0.24
Release:	4
Epoch:		1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gal/%{version}/gal-%{version}.tar.bz2
# Source0-md5:	9f9790d4e8763c4ce74e5d59f47aa509
Patch0:		%{name}-am15.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		%{name}-link.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel >= 1.2.12
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gnome-vfs-devel >= 1.0
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	intltool
BuildRequires:	libglade-devel >= 0.13
BuildRequires:	libglade-gnome-devel >= 0.13
BuildRequires:	libtool
BuildRequires:	libxml-devel >= 1.8.8
BuildRequires:	sed >= 4.0
Obsoletes:	libgal19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

%description -l pl.UTF-8
Pakiet zawiera funkcje pochodzące z programów Gnumeric i Evolution.
Ideą tej biblioteki jest używanie tych funkcji i wigetów w innych
programach GNOME.

%description -l pt_BR.UTF-8
Este módulo contém algumas funções de biblioteca que vinham com o
Gnumeric e com o Evolution. A idéia é reutilizar estes componentes em
uma série de aplicações GNOME maiores.

%description -l ru.UTF-8
Это пакет G App Libs (GAL). Он содержит некоторые библиотечные
функции, пришедшие из Gnumeric и Evolution. Идея в том, чтобы
использовать их виджеты в других приложениях GNOME, которым эти
виджеты могли бы пригодиться.

%description -l uk.UTF-8
Це пакет G App Libs (GAL). Він містить деякі бібліотечні функції, що
походять від Gnumeric та Evolution. Ідея в тому, щоб використати їх
віджети в інших програмах GNOME, яким ці віджети могли б стати в
нагоді.

%package devel
Summary:	gal header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja gala
Summary(pt_BR.UTF-8):	Arquivos de inclusão do gal
Summary(ru.UTF-8):	Библиотеки и хедеры для gal
Summary(uk.UTF-8):	Бібліотеки та хедери для gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gdk-pixbuf-gnome-devel
Requires:	gnome-print-devel >= 0.28
Requires:	libglade-gnome-devel >= 0.13
Requires:	libxml-devel >= 1.8.8
Obsoletes:	libgal19-devel

%description devel
Header files and development documentation for the gal libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek gal.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão necessários para compilar os aplicativos que usam
o gal.

%description devel -l ru.UTF-8
Этот пакет содержит необходимые библиотеки и файлы заголовков для
разработки программ с использованием gal.

%description devel -l uk.UTF-8
Цей пакет містить необхідні бібліотеки розробки та файли заголовків
для розробки програм з використанням gal.

%package static
Summary:	gal static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gal
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do gal
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Gal static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gal.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas do gal.

%prep
%setup -q -n gal-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i -e 's/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/' configure.in
sed -i -e 's/AM_PROG_XML_I18N_TOOLS/AC_PROG_INTLTOOL/' configure.in

mv -f po/{no,nb}.po

%build
intltoolize --copy --force
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgal.so.*.*.*
%{_datadir}/etable
%{_datadir}/gal

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgal.so
%{_libdir}/libgal.la
%attr(755,root,root) %{_libdir}/galConf.sh
%{_includedir}/gal-1.0
%{_pkgconfigdir}/gal.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgal.a
