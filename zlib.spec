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
	--prefix=/usr \
	--shared

make
make libz.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{include,lib,share/man/man3}

install libz.a $RPM_BUILD_ROOT/usr/lib
install zutil.h $RPM_BUILD_ROOT/usr/include
install zlib.3 $RPM_BUILD_ROOT/usr/share/man/man3
make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man3/* \
	README ChangeLog algorithm.txt FAQ example.c minigzip.c

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {README,ChangeLog,algorithm.txt,FAQ,example.c,minigzip.c}.gz
/usr/include/*
%attr(755,root,root) /usr/lib/lib*.so
/usr/share/man/man3/*

%files static
%attr(644,root,root) /usr/lib/lib*.a

%changelog
* Mon May 10 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.1.3-8]
- package is now FHS 2.0 compliant.

* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.3-7]
- removed Conflicts: glibc (not neccesary now),
- recompiled on new rpm.

* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.1.3-6]
- gzipping documentation
- fixed pl translation

* Thu Mar  4 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.3-5]
- added Group(pl),
- added "Conflicts: glibc <= 2.0.7" for installing zlib in proper
  enviroment,
- changed permission on /usr/lib/lib*.so to 755,
- removed man group from man pages.

* Thu Aug  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.3-4]
- Source Url changed to ftp protocol,
- added pl translation,
- added static subpackage.

* Sat Aug  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.3-3]
- added de, fr, tr translations from orginal RH spec,
- added pl translation,
- changet way of passing $RPM_OPT_FLAGS,
- some cosmetic changes in %files nad %install,
- changed permission on shared lib to 755 (now ldd output on this files is
  correct).

* Fri Jul 31 1998 Arne Coucheron <arneco@online.no>
  [1.1.3-2]
- moved over some changes from the 1.1.3-1 package
- please guys, when updating the packages, do so using the contributed
  source packages from the contrib area. otherwise you are wasting the time
  and effort put in by a lot of people maintaining the packages.

* Mon Jun 08 1998 Arne Coucheron <arneco@online.no>
  [1.1.2-5]
- added a patch

* Sun May 31 1998 Arne Coucheron <arneco@online.no>
  [1.1.2-4]
- using %%{name} and %%{version} macros
- using %defattr macro in %files
- added -q parameter to %setup

* Sun May 03 1998 Arne Coucheron <arneco@online.no>
  [1.1.2-3]
- added stripping of the libs
- some minor changes to the spec file
- removed some older changelogs

* Fri Apr 17 1998 Arne Coucheron <arneco@online.no>
  [1.1.2-2] 
- added zlib manpage to devel package

* Mon Apr 06 1998 Arne Coucheron <arneco@online.no>
  [1.1.2-1]
- corrected Source and URL tags

* Sun Mar 01 1998 Arne Coucheron <arneco@online.no>
  [1.1.1-1]
- using buildroot
- using %attr macros in filelist
