#
# Conditional build:
%bcond_without	asmopt	# without assembler optimization for i586+
%bcond_with	pax
#
%ifnarch i586 i686 pentium3 athlon
%undefine	with_asmopt
%endif
%if %{with pax} && %{with asmopt}
%undefine	with_asmopt
%endif
Summary:	Library for compression and decompression
Summary(de):	Library f�r die Komprimierung und Dekomprimierung
Summary(es):	Biblioteca para compresi�n y descompresi�n
Summary(fr):	Biblioth�que de compression et d�compression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR):	Biblioteca para compress�o e descompress�o
Summary(ru):	���������� ��� ���������� � ������������
Summary(tr):	S�k��t�rma i�lemleri i�in kitapl�k
Summary(uk):	��̦����� ��� ������Ӧ� �� ��������Ӧ�
Name:		zlib
Version:	1.2.2
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.zlib.net/%{name}-%{version}.tar.gz
# Source0-md5:	68bd51aaa6558c3bc3fd4890e53413de
Patch0:		%{name}-asmopt.patch
URL:		http://www.zlib.net/
Obsoletes:	zlib1
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
dekompresji. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresji o nazwie deflation niemniej inne algorytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

%description -l pt_BR
A biblioteca de compress�o 'zlib' oferece fun��es de compress�o e
descompress�o em mem�ria, incluindo checagem da integridade de dados
n�o comprimidos. Essa vers�o da biblioteca suporta somente um m�todo
de compress�o (defla��o) mas outros algoritmos podem ser adicionados
mais tarde e ter�o a mesma interface. Essa biblioteca � usada por
v�rios programas de sistema.

%description -l ru
���������� ���������� zlib �������� ������� ���������� � ������������
� ������, ������� �������� ����������� ������������������� ������. ���
������ ������������ ������ ���� ����� ���������� (deflation), ��
������������ � ��� ����� ���� ��������� � ������ ������, � ��� ���
����� ������������ ��� �� ��������� ���������.

%description -l tr
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r. Bu kitapl�k bir dizi
sistem yaz�l�m� taraf�ndan kullan�lmaktad�r.

%description -l uk
��̦����� ������Ӧ� zlib ͦ����� ����æ� ������Ӧ� �� ��������Ӧ� �
���'�Ԧ � ����צ���� æ���Ԧ ��������������� �����. �� ���Ӧ�
Ц�����դ Ԧ���� ���� ����� ������Ӧ� (deflation), ��� � ����������� �
�ŧ ������ ���� ����Φ � ��ۦ ������ � �Ӧ ���� ������ ���������������
��� �� ����� ��������� ���������.

%package devel
Summary:	Header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries f�r zlib-Entwicklung
Summary(es):	Bibliotecas y archivos de inclusi�n para desarrollo zlib
Summary(pl):	Pliki nag��wkowe i dokumentacja do zlib
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento zlib
Summary(ru):	������ � ���������� ��� ���������������� � zlib
Summary(uk):	������ �� ¦�̦����� ��� ������������� � zlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	zlib1-devel

%description devel
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains the header files needed to develop programs that
use these zlib.

%description devel -l de
Die zlip-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschlie�lich Integrit�tspr�fungen
der dekomprimierten Daten. Diese Version der Library unterst�tzt nur
eine Komprimierungsmethode (Deflation), doch sind weitere Algorithmen
geplant, die dieselbe Art Oberfl�che besitzen werden. Dieses Paket
enth�lt die Header-Dateien und Libraries, die zur Entwicklung von
Programmen ben�tigt werden, die diese zlib einsetzen.

%description devel -l es
La biblioteca de compresi�n zlib provee funciones de compresi�n y
descompresi�n en memoria, incluye chequeos de integridad para los
datos descomprimidos. Esta versi�n de la biblioteca soporta solamente
un m�todo de compresi�n (deflation) pero otros algoritmos pueden ser
a�adidos en el futuro y tendr�n la misma interface stream. Este
paquete contiene los archivos de inclusi�n y bibliotecas necesarios al
desarrollo de programas que usan zlib.

%description devel -l fr
La biblioth�que de compression � zlib � offre des fonctions de
compression et de d�compression en m�moire, ainsi qu'une v�rification
de l'int�grit� des donn�es d�compress�es. La version de cette
biblioth�que ne g�re qu'une m�thode de compression (deflation), mais
d'autres algorithmes peuvent �tre ajout�s plus tard et auront la m�me
interface.

Ce paquetage contient les fichiers en-t�tes et les biblioth�ques
n�cessaires au d�veloppement des programmes qui utilisent cette zlib.

%description devel -l pl
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algorytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

Pakiet ten zawiera pliki nag�owkowe i dokumentacj� potrzebn� przy
tworzeniu w�asnych program�w wykorzystuj�cych zlib.

%description devel -l pt_BR
A biblioteca de compress�o zlib prov� fun��es de compress�o e
descompress�o em mem�ria, incluindo checagens de integridade para os
dados descomprimidos. Esta vers�o da biblioteca suporta somente um
m�todo de compress�o (deflation) mas outros algoritmos podem ser
adicionados no futuro e ter�o a mesma interface stream.

Este pacote cont�m os arquivos de inclus�o e bibliotecas necess�rios
ao desenvolvimento de programas que usam zlib.

%description devel -l ru
���������� ���������� zlib �������� ������� ���������� � ������������
� ������, ������� �������� ����������� ������������������� ������. ���
������ ������������ ������ ���� ����� ���������� (deflation), ��
������������ � ��� ����� ���� ��������� � ������ ������, � ��� ���
����� ������������ ��� �� ��������� ���������.

���� ����� �������� ������ � ����������, ����������� ��� ���������
��������, ������������ zlib.

%description devel -l tr
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r.

Bu paket, zlib kitapl���n� kullanarak program geli�tirmek i�in gereken
statik kitapl�klar� ve ba�l�k dosyalar�n� i�erir.

%description devel -l uk
��̦����� ������Ӧ� zlib ͦ����� ����æ� ������Ӧ� �� ��������Ӧ� �
���'�Ԧ � ����צ���� æ���Ԧ ��������������� �����. �� ���Ӧ�
Ц�����դ Ԧ���� ���� ����� ������Ӧ� (deflation), ��� � ����������� �
�ŧ ������ ���� ����Φ � ��ۦ ������ � �Ӧ ���� ������ ���������������
��� �� ����� ��������� ���������.

��� ����� ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ��� ���������
�������, �� �������������� zlib.

%package static
Summary:	Static library for zlib development
Summary(es):	Static libraries for zlib development
Summary(pl):	Biblioteka statyczna do zlib
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a zlib
Summary(ru):	����������� ���������� ��� ���������������� � zlib
Summary(uk):	�������� ¦�̦����� ��� ������������� � zlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains the header files and libraries needed to develop
programs that use these zlib.

%description static -l pl
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresjii. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresjii o nazwie deflation niemniej inne algirytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

Pakiet ten zawiera bibliotek� statyczn� potrzebn� przy tworzeniu
w�asnych program�w wykorzystuj�cych zlib.

%description static -l es
Static libraries for zlib development.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a zlib.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ���������
��������, ������������ zlib.

%description static -l uk
��� ����� ͦ����� �������� ¦�̦�����, ����Ȧ��� ��� ���������
�������, �� �������������� zlib.

%prep
%setup -q

%if %{with asmopt}
%patch0 -p1
%ifarch i686 pentium3 athlon
cp contrib/asm686/match.S .
%endif
%ifarch i586
cp contrib/asm586/match.S .
%endif
%endif

%build
CFLAGS="-D_REENTRANT -fPIC %{rpmcflags} %{?with_asmopt:-DASMV}" \
CC="%{__cc}" \
./configure \
	--prefix=%{_prefix} \
	--shared

%{__make}
%{__make} libz.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_includedir},%{_libdir},%{_mandir}/man3}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%ifarch amd64 sparc64
mv $RPM_BUILD_ROOT{%{_prefix}/lib/*,%{_libdir}}
%endif

install libz.a $RPM_BUILD_ROOT%{_libdir}
install zutil.h $RPM_BUILD_ROOT%{_includedir}

mv -f $RPM_BUILD_ROOT%{_libdir}/libz.so.*.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib} && echo libz.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libz.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README algorithm.txt
%attr(755,root,root) /%{_lib}/libz.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libz.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
