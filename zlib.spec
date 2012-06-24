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
Summary(de):	Library f�r die Komprimierung und Dekomprimierung 
Summary(es):	Biblioteca para compresi�n y descompresi�n
Summary(fr):	biblioth�que de compression et d�compression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR):	Biblioteca para compress�o e descompress�o
Summary(tr):	S�k��t�rma i�lemleri i�in kitapl�k
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
Group(ru):	����������
Group(uk):	��̦�����
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
und Dekomprimierungsfunktionen, einschlie�lich Integrit�tspr�fungen
der unkomprimierten Daten. Diese Version der Library unterst�tzt nur
eine Komprimierungsmethode (Deflation), doch k�nnen weitere
Algorithmen nachtr�glich eingef�gt werden und haben dann dieselbe
Oberfl�che.

%description -l es
La biblioteca de compresi�n 'zlib' nos ofrece funciones de compresi�n
y descompresi�n en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versi�n de la biblioteca soporta solamente
un m�todo de compresi�n (deflaci�n) pero otros algoritmos pueden ser
a�adidos m�s tarde y tendr�n la misma interface. Esta biblioteca se
usa por varios programas de sistema.

%description -l fr
La biblioth�que de compression � zlib � offre des fonctions de
compression et de d�compression en m�moire, ainsi qu'une v�rification
de l'int�grit� des donn�es d�compress�es. La version de cette
biblioth�que ne g�re qu'une m�thode de compression (deflation), mais
d'autres algorithmes peuvent �tre ajout�s plus tard et auront la m�me
interface.

%description -l pl
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algorytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

%description -l pt_BR
A biblioteca de compress�o 'zlib' oferece fun��es de compress�o e
descompress�o em mem�ria, incluindo checagem da integridade de dados
n�o comprimidos. Essa vers�o da biblioteca suporta somente um m�todo
de compress�o (defla��o) mas outros algoritmos podem ser adicionados
mais tarde e ter�o a mesma interface. Essa biblioteca � usada por
v�rios programas de sistema.

%description -l tr
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r. Bu kitapl�k bir dizi
sistem yaz�l�m� taraf�ndan kullan�lmaktad�r.

%package devel
Summary:	header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries f�r zlib-Entwicklung 
Summary(es):	Bibliotecas y archivos de inclusi�n para desarrollo zlib
Summary(pl):	Pliki nag��wkowe i dokumentacja do zlib
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
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
und Dekomprimierungsfunktionen, einschlie�lich Integrit�tspr�fungen
der dekomprimierten Daten. Diese Version der Library unterst�tzt nur
eine Komprimierungsmethode (Deflation), doch sind weitere Algorithmen
geplant, die dieselbe Art Oberfl�che besitzen werden. Dieses Paket
enth�lt die Header-Dateien und Libraries, die zur Entwicklung von
Programmen ben�tigt werden, die diese zlib einsetzen.

%description -l es devel
La biblioteca de compresi�n zlib provee funciones de compresi�n y
descompresi�n en memoria, incluye chequeos de integridad para los
datos descomprimidos. Esta versi�n de la biblioteca soporta solamente
un m�todo de compresi�n (deflation) pero otros algoritmos pueden ser
a�adidos en el futuro y tendr�n la misma interface stream. Este
paquete contiene los archivos de inclusi�n y bibliotecas necesarios al
desarrollo de programas que usan zlib.

%description -l fr devel
La biblioth�que de compression � zlib � offre des fonctions de
compression et de d�compression en m�moire, ainsi qu'une v�rification
de l'int�grit� des donn�es d�compress�es. La version de cette
biblioth�que ne g�re qu'une m�thode de compression (deflation), mais
d'autres algorithmes peuvent �tre ajout�s plus tard et auront la m�me
interface.

Ce paquetage contient les fichiers en-t�tes et les biblioth�ques
n�cessaires au d�veloppement des programmes qui utilisent cette zlib.

%description -l pl devel
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algorytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

Pakiet ten zawiera pliki nag�owkowe i dokumentacj� potrzebn� przy
tworzeniu w�asnych program�w wykorzystuj�cych zlib.

%description -l pt_BR devel
A biblioteca de compress�o zlib prov� fun��es de compress�o e
descompress�o em mem�ria, incluindo checagens de integridade para os
dados descomprimidos. Esta vers�o da biblioteca suporta somente um
m�todo de compress�o (deflation) mas outros algoritmos podem ser
adicionados no futuro e ter�o a mesma interface stream.

Este pacote cont�m os arquivos de inclus�o e bibliotecas necess�rios
ao desenvolvimento de programas que usam zlib.

%description -l tr devel
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r.

Bu paket, zlib kitapl���n� kullanarak program geli�tirmek i�in gereken
statik kitapl�klar� ve ba�l�k dosyalar�n� i�erir.

%package static
Summary:	Static library for zlib development
Summary(es):	Static libraries for zlib development
Summary(pl):	Biblioteka statyczna do zlib
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
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
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algirytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

Pakiet ten zawiera bibliotek� statyczn� potrzebn� przy tworzeniu
wa�asnych program�w wykorzystuj�cych zlib.

%description -l es static
Static libraries for zlib development.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento com a zlib.

%package devel-embed
Summary:	Embedded library for zlib development
Summary(pl):	Wbudowana biblioteka zlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����

%description devel-embed
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains libraries and headers needed for embedded applications
development.

%description -l pl devel-embed
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algirytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

Pakiet ten zawiera bibliotek� i pliki nag��wkowe potrzebne do tworzenia
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
