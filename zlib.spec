Summary:	Library for compression and decompression
Summary(de):	Library für die Komprimierung und Dekomprimierung 
Summary(fr):	bibliothèque de compression et décompression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(tr):	Sýkýþtýrma iþlemleri için kitaplýk
Name:		zlib
Version:	1.1.3
Release:	18
License:	BSD
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.cdrom.com/pub/infozip/zlib/%{name}-%{version}.tar.gz
Patch0:		%{name}-sharedlib.patch
URL:		http://www.cdrom.com/pub/infozip/zlib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

%description -l de
Die zlib-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen
der unkomprimierten Daten. Diese Version der Library unterstützt nur
eine Komprimierungsmethode (Deflation), doch können weitere
Algorithmen nachträglich eingefügt werden und haben dann dieselbe
Oberfläche.

%description -l fr
La bibliothèque de compression « zlib » offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la même
interface.

%description -l pl
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w
pamiêci operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie
dekompresjii. Ta wersja biblioteki udostêpnia tylko jedn± metodê
kompresjii o nazwie deflation niemniej inne algorytmy mog± byæ
dodawane udostêpniaj±c taki sam interfejs funkcji operuj±cych na
strumieniu danych.

%description -l tr
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini
desteklemektedir. Ancak baþka algoritmalarýn ayný arabirimle
eriþilebilecek þekilde eklenme olasýlýðý vardýr. Bu kitaplýk bir dizi
sistem yazýlýmý tarafýndan kullanýlmaktadýr.

%package devel
Summary:	header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries für zlib-Entwicklung 
Summary(pl):	Pliki nag³ówkowe i dokumentacja do zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains the header files needed to develop programs that
use these zlib.

%description -l de devel
Die zlip-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen
der dekomprimierten Daten. Diese Version der Library unterstützt nur
eine Komprimierungsmethode (Deflation), doch sind weitere Algorithmen
geplant, die dieselbe Art Oberfläche besitzen werden. Dieses Paket
enthält die Header-Dateien und Libraries, die zur Entwicklung von
Programmen benötigt werden, die diese zlib einsetzen.

%description -l fr devel
La bibliothèque de compression « zlib » offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la même
interface.

Ce paquetage contient les fichiers en-têtes et les bibliothèques
nécessaires au développement des programmes qui utilisent cette zlib.

%description -l pl devel
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w
pamiêci operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie
dekompresjii. Ta wersja biblioteki udostêpnia tylko jedn± metodê
kompresjii o nazwie deflation niemniej inne algorytmy mog± byæ
dodawane udostêpniaj±c taki sam interfejs funkcji operuj±cych na
strumieniu danych.

Pakiet ten zawiera pliki nag³owkowe i dokumentacjê potrzebn± przy
tworzeniu w³asnych programów wykorzystuj±cych zlib.

%description -l tr devel
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini
desteklemektedir. Ancak baþka algoritmalarýn ayný arabirimle
eriþilebilecek þekilde eklenme olasýlýðý vardýr.

Bu paket, zlib kitaplýðýný kullanarak program geliþtirmek için gereken
statik kitaplýklarý ve baþlýk dosyalarýný içerir.

%package static
Summary:	Static library for zlib development
Summary(pl):	Biblioteka statyczna do zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains the header files and libraries needed to develop
programs that use these zlib.

%description -l pl static
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w
pamiêci operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie
dekompresjii. Ta wersja biblioteki udostêpnia tylko jedn± metodê
kompresjii o nazwie deflation niemniej inne algirytmy mog± byæ
dodawane udostêpniaj±c taki sam interfejs funkcji operuj±cych na
strumieniu danych.

Pakiet ten zawiera bibliotekê statyczn± potrzebn± przy tworzeniu
wa³asnych programów wykorzystuj±cych zlib.

%prep
%setup -q
%patch -p1

%build
CFLAGS="-D_REENTRANT -fPIC %{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
./configure \
	--prefix=%{_prefix} \
	--shared 

%{__make}

%{__make} libz.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_includedir},%{_libdir},%{_mandir}/man3}

install libz.a $RPM_BUILD_ROOT%{_libdir}
install zutil.h $RPM_BUILD_ROOT%{_includedir}
install zlib.3 $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

mv $RPM_BUILD_ROOT%{_libdir}/libz.so.*.* $RPM_BUILD_ROOT/lib
cd $RPM_BUILD_ROOT%{_libdir}
ln -sf ../../lib/libz.so.*.* $RPM_BUILD_ROOT%{_libdir}/libz.so
cd -

gzip -9nf README ChangeLog algorithm.txt FAQ

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {README,ChangeLog,algorithm.txt,FAQ}.gz
%attr(755,root,root) %{_libdir}/lib*.so

%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
