#
# Conditional build:
# _without_asmopt		- without assmbler optimization for i[56]86
# _without_embed		- don't build uClibc version

%ifnarch i586 i686 athlon
%define				_asmopt		0
%else
%{?_without_asmopt:%define	_asmopt		0}
%{!?_without_asmopt:%define	_asmopt		1}
%endif

Summary:	Library for compression and decompression
Summary(de):	Library für die Komprimierung und Dekomprimierung 
Summary(es):	Biblioteca para compresión y descompresión
Summary(fr):	bibliothèque de compression et décompression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR):	Biblioteca para compressão e descompressão
Summary(tr):	Sýkýþtýrma iþlemleri için kitaplýk
Name:		zlib
Version:	1.1.3
Release:	28
License:	BSD
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	http://www.gzip.org/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-sharedlib.patch
Patch1:		%{name}-asmopt.patch
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif
URL:		http://www.zlib.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	zlib1

%define uclibc_prefix	/usr/%{_arch}-linux-uclibc
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os

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

%description -l es
La biblioteca de compresión 'zlib' nos ofrece funciones de compresión
y descompresión en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versión de la biblioteca soporta solamente
un método de compresión (deflación) pero otros algoritmos pueden ser
añadidos más tarde y tendrán la misma interface. Esta biblioteca se
usa por varios programas de sistema.

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

%description -l pt_BR
A biblioteca de compressão 'zlib' oferece funções de compressão e
descompressão em memória, incluindo checagem da integridade de dados
não comprimidos. Essa versão da biblioteca suporta somente um método
de compressão (deflação) mas outros algoritmos podem ser adicionados
mais tarde e terão a mesma interface. Essa biblioteca é usada por
vários programas de sistema.

%description -l tr
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini
desteklemektedir. Ancak baþka algoritmalarýn ayný arabirimle
eriþilebilecek þekilde eklenme olasýlýðý vardýr. Bu kitaplýk bir dizi
sistem yazýlýmý tarafýndan kullanýlmaktadýr.

%package devel
Summary:	header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries für zlib-Entwicklung 
Summary(es):	Bibliotecas y archivos de inclusión para desarrollo zlib
Summary(pl):	Pliki nag³ówkowe i dokumentacja do zlib
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Obsoletes:	zlib1-devel

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

%description -l es devel
La biblioteca de compresión zlib provee funciones de compresión y
descompresión en memoria, incluye chequeos de integridad para los
datos descomprimidos. Esta versión de la biblioteca soporta solamente
un método de compresión (deflation) pero otros algoritmos pueden ser
añadidos en el futuro y tendrán la misma interface stream. Este
paquete contiene los archivos de inclusión y bibliotecas necesarios al
desarrollo de programas que usan zlib.

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

%description -l pt_BR devel
A biblioteca de compressão zlib provê funções de compressão e
descompressão em memória, incluindo checagens de integridade para os
dados descomprimidos. Esta versão da biblioteca suporta somente um
método de compressão (deflation) mas outros algoritmos podem ser
adicionados no futuro e terão a mesma interface stream.

Este pacote contém os arquivos de inclusão e bibliotecas necessários
ao desenvolvimento de programas que usam zlib.

%description -l tr devel
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini
desteklemektedir. Ancak baþka algoritmalarýn ayný arabirimle
eriþilebilecek þekilde eklenme olasýlýðý vardýr.

Bu paket, zlib kitaplýðýný kullanarak program geliþtirmek için gereken
statik kitaplýklarý ve baþlýk dosyalarýný içerir.

%package static
Summary:	Static library for zlib development
Summary(es):	Static libraries for zlib development
Summary(pl):	Biblioteka statyczna do zlib
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com a zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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

%description -l es static
Static libraries for zlib development.

%description -l pt_BR static
Bibliotecas estáticas para desenvolvimento com a zlib.

%package devel-embed
Summary:	Embedded library for zlib development
Summary(pl):	Wbudowana biblioteka zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ

%description devel-embed
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains libraries and headers needed for embedded applications
development.

%description -l pl devel-embed
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w
pamiêci operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie
dekompresjii. Ta wersja biblioteki udostêpnia tylko jedn± metodê
kompresjii o nazwie deflation niemniej inne algirytmy mog± byæ
dodawane udostêpniaj±c taki sam interfejs funkcji operuj±cych na
strumieniu danych.

Pakiet ten zawiera bibliotekê i pliki nag³ówkowe potrzebne do tworzenia
aplikacji wbudowanych.

%prep
%setup -q
%patch0 -p1
%{?_with_asmopt:%patch1 -p1}

%if %{_asmopt}
%patch1 -p1
%ifarch i686 athlon
cp contrib/asm686/match.S .
%endif
%ifarch i586
cp contrib/asm586/match.S .
%endif
%endif

%build
%if %{!?_without_embed:1}%{?_without_embed:0}
CFLAGS="-D_REENTRANT %{embed_cflags}" \
CC=%{embed_cc} ./configure \
	--prefix=%{_prefix}
%{__make} libz.a
mv -f libz.a libz.a-embed
%{__make} distclean
%endif

CFLAGS="-D_REENTRANT -fPIC %{rpmcflags}"
%if %{_asmopt}
CFLAGS="$CFLAGS -O3 -DASMV"
%endif
export CFLAGS

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

%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT%{uclibc_prefix}/{lib,include}
install libz.a-embed $RPM_BUILD_ROOT%{uclibc_prefix}/lib/libz.a
cp $RPM_BUILD_ROOT%{_includedir}/* $RPM_BUILD_ROOT%{uclibc_prefix}/include
%endif

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

%if %{!?_without_embed:1}%{?_without_embed:0}
%files devel-embed
%defattr(644,root,root,755)
%{uclibc_prefix}/lib/*
%{uclibc_prefix}/include/*
%endif
