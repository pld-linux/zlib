Summary:	Library for compression and decompression
Summary(de):	Library für die Komprimierung und Dekomprimierung 
Summary(fr):	bibliothèque de compression et décompression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(tr):	Sýkýþtýrma iþlemleri için kitaplýk
Name:		zlib
Version:	1.1.3
Release:	8
Copyright:	BSD
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.cdrom.com/pub/infozip/zlib/%{name}-%{version}.tar.gz
URL:		http://www.cdrom.com/pub/infozip/zlib/
BuildRoot:	/tmp/%{name}-%{version}-root 

%description
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the uncompressed
data.  This version of the library supports only one compression method
(deflation) but other algorithms may be added later and will have the same
stream interface.

This library is used by a number of different system programs.

%description -l de
Die zlib-Komprimierungs-Library bietet speicherinterne Komprimierungs- 
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen 
der unkomprimierten Daten. Diese Version der Library unterstützt nur 
eine Komprimierungsmethode (Deflation), doch können weitere Algorithmen 
nachträglich eingefügt werden und haben dann dieselbe Oberfläche. 

Diese Library wird von verschiedenen Systemprogrammen genutzt. 

%description -l fr
La bibliothèque de compression « zlib » offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la
même interface.

Cette bibliothèque est utilisée par de nombreux programmes système.

%description -l pl
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w pamiêci
operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie dekompresjii.
Ta wersja biblioteki udostêpnia tylko jedn± metodê kompresjii o nazwie
deflation niemniej inne algorytmy mog± byæ dodawane udostêpniaj±c taki sam
interfejs funkcji operuj±cych na strumieniu danych.

Ta biblioteka jest u¿ywana m.in. przez ró¿ne programy systemowe.

%description -l tr
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini desteklemektedir.
Ancak baþka algoritmalarýn ayný arabirimle eriþilebilecek þekilde eklenme
olasýlýðý vardýr. Bu kitaplýk bir dizi sistem yazýlýmý tarafýndan
kullanýlmaktadýr.

%package devel
Summary:	header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries für zlib-Entwicklung 
Summary(pl):	Pliki nag³ówkowe i dokumentacja do zlib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the uncompressed
data.  This version of the library supports only one compression method
(deflation) but other algorithms may be added later and will have the same
stream interface.

This package contains the header files needed to develop programs that use
these zlib.

%description -l de devel
Die zlip-Komprimierungs-Library bietet speicherinterne Komprimierungs- und
Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen der
dekomprimierten Daten. Diese Version der Library unterstützt nur eine
Komprimierungsmethode (Deflation), doch sind weitere Algorithmen geplant,
die dieselbe Art Oberfläche besitzen werden. Dieses Paket enthält die
Header-Dateien und Libraries, die zur Entwicklung von Programmen benötigt
werden, die diese zlib einsetzen.

%description -l fr devel
La bibliothèque de compression « zlib » offre des fonctions de compression
et de décompression en mémoire, ainsi qu'une vérification de l'intégrité des
données décompressées. La version de cette bibliothèque ne gère qu'une
méthode de compression (deflation), mais d'autres algorithmes peuvent être
ajoutés plus tard et auront la même interface.

Ce paquetage contient les fichiers en-têtes et les bibliothèques nécessaires
au développement des programmes qui utilisent cette zlib.

%description -l pl
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w pamiêci
operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie dekompresjii.
Ta wersja biblioteki udostêpnia tylko jedn± metodê kompresjii o nazwie
deflation niemniej inne algorytmy mog± byæ dodawane udostêpniaj±c taki sam
interfejs funkcji operuj±cych na strumieniu danych.

Pakiet ten zawiera pliki nag³owkowe i dokumentacjê potrzebn± przy tworzeniu
w³asnych programów wykorzystuj±cych zlib.

%description -l tr devel
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini desteklemektedir.
Ancak baþka algoritmalarýn ayný arabirimle eriþilebilecek þekilde eklenme
olasýlýðý vardýr.

Bu paket, zlib kitaplýðýný kullanarak program geliþtirmek için gereken
statik kitaplýklarý ve baþlýk dosyalarýný içerir.

%package static
Summary:	Static library for zlib development
Summary(pl):	Biblioteka statyczna do zlib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the uncompressed
data.  This version of the library supports only one compression method
(deflation) but other algorithms may be added later and will have the same
stream interface.

This package contains the header files and libraries needed to develop 
programs that use these zlib.

%description -l pl static
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w pamiêci
operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie dekompresjii.
Ta wersja biblioteki udostêpnia  tylko jedn± metodê kompresjii o nazwie
deflation niemniej inne algirytmy mog± byæ dodawane udostêpniaj±c taki sam
interfejs funkcji operuj±cych na strumieniu danych.

Pakiet ten zawiera bibliotekê statyczn± potrzebn± przy tworzeniu wa³asnych
programów wykorzystuj±cych zlib.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=%{_prefix} \
	--shared

make
make libz.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_mandir}/man3}

install libz.a $RPM_BUILD_ROOT%{_libdir}
install zutil.h $RPM_BUILD_ROOT%{_includedir}
install zlib.3 $RPM_BUILD_ROOT%{_mandir}/man3
make prefix=$RPM_BUILD_ROOT/usr install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README ChangeLog algorithm.txt FAQ example.c minigzip.c

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {README,ChangeLog,algorithm.txt,FAQ,example.c,minigzip.c}.gz
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Fri May 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.3-8]
- spec based on RH version,
- pl translation by me,
- spec rewrited by Piotr Czerwiñski <pius@pld.org.pl>, Micha³ Kuratczyk
  <kura@pld.org.pl> and me.
