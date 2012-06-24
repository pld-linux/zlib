Summary:	Library for compression and decompression
Summary(de):	Library f�r die Komprimierung und Dekomprimierung 
Summary(fr):	biblioth�que de compression et d�compression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(tr):	S�k��t�rma i�lemleri i�in kitapl�k
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
und Dekomprimierungsfunktionen, einschlie�lich Integrit�tspr�fungen
der unkomprimierten Daten. Diese Version der Library unterst�tzt nur
eine Komprimierungsmethode (Deflation), doch k�nnen weitere
Algorithmen nachtr�glich eingef�gt werden und haben dann dieselbe
Oberfl�che.

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

%description -l tr
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r. Bu kitapl�k bir dizi
sistem yaz�l�m� taraf�ndan kullan�lmaktad�r.

%package devel
Summary:	header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries f�r zlib-Entwicklung 
Summary(pl):	Pliki nag��wkowe i dokumentacja do zlib
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
und Dekomprimierungsfunktionen, einschlie�lich Integrit�tspr�fungen
der dekomprimierten Daten. Diese Version der Library unterst�tzt nur
eine Komprimierungsmethode (Deflation), doch sind weitere Algorithmen
geplant, die dieselbe Art Oberfl�che besitzen werden. Dieses Paket
enth�lt die Header-Dateien und Libraries, die zur Entwicklung von
Programmen ben�tigt werden, die diese zlib einsetzen.

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

%description -l tr devel
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r.

Bu paket, zlib kitapl���n� kullanarak program geli�tirmek i�in gereken
statik kitapl�klar� ve ba�l�k dosyalar�n� i�erir.

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
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algirytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

Pakiet ten zawiera bibliotek� statyczn� potrzebn� przy tworzeniu
wa�asnych program�w wykorzystuj�cych zlib.

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
