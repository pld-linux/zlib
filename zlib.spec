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
Summary(de):	Library fЭr die Komprimierung und Dekomprimierung
Summary(es):	Biblioteca para compresiСn y descompresiСn
Summary(fr):	BibliothХque de compression et dИcompression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR):	Biblioteca para compressЦo e descompressЦo
Summary(ru):	Библиотека для компрессии и декомпрессии
Summary(tr):	SЩkЩЧtЩrma iЧlemleri iГin kitaplЩk
Summary(uk):	Б╕бл╕отека для компрес╕╖ та декомпрес╕╖
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
und Dekomprimierungsfunktionen, einschlieъlich IntegritДtsprЭfungen
der unkomprimierten Daten. Diese Version der Library unterstЭtzt nur
eine Komprimierungsmethode (Deflation), doch kЖnnen weitere
Algorithmen nachtrДglich eingefЭgt werden und haben dann dieselbe
OberflДche.

%description -l es
La biblioteca de compresiСn 'zlib' nos ofrece funciones de compresiСn
y descompresiСn en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versiСn de la biblioteca soporta solamente
un mИtodo de compresiСn (deflaciСn) pero otros algoritmos pueden ser
aЯadidos mАs tarde y tendrАn la misma interface. Esta biblioteca se
usa por varios programas de sistema.

%description -l fr
La bibliothХque de compression ╚ zlib ╩ offre des fonctions de
compression et de dИcompression en mИmoire, ainsi qu'une vИrification
de l'intИgritИ des donnИes dИcompressИes. La version de cette
bibliothХque ne gХre qu'une mИthode de compression (deflation), mais
d'autres algorithmes peuvent Йtre ajoutИs plus tard et auront la mЙme
interface.

%description -l pl
Biblioteka zlib udostЙpnia podprogramy do kompresji i dekompresji w
pamiЙci operacyjnej wЁ╠cznie ze sprawdzaniem integralno╤ci w trakcie
dekompresji. Ta wersja biblioteki udostЙpnia tylko jedn╠ metodЙ
kompresji o nazwie deflation niemniej inne algorytmy mog╠ byФ
dodawane udostЙpniaj╠c taki sam interfejs funkcji operuj╠cych na
strumieniu danych.

%description -l pt_BR
A biblioteca de compressЦo 'zlib' oferece funГУes de compressЦo e
descompressЦo em memСria, incluindo checagem da integridade de dados
nЦo comprimidos. Essa versЦo da biblioteca suporta somente um mИtodo
de compressЦo (deflaГЦo) mas outros algoritmos podem ser adicionados
mais tarde e terЦo a mesma interface. Essa biblioteca И usada por
vАrios programas de sistema.

%description -l ru
Библиотека компрессии zlib содержит функции компрессии и декомпрессии
в памяти, включаю проверку целостности декомпрессированных данных. Эта
версия поддерживает только один метод компрессии (deflation), но
впоследствии в нее могут быть добавлены и другие методы, и все они
будут использовать тот же потоковый интерфейс.

%description -l tr
zlib sЩkЩЧtЩrma kitaplЩПЩ bellekte sЩkЩЧtЩrma ve aГma fonksiyonlarЩ
iГermektedir. Bu sЭrЭm yalnЩzca 'deflation' yЖntemini
desteklemektedir. Ancak baЧka algoritmalarЩn aynЩ arabirimle
eriЧilebilecek Чekilde eklenme olasЩlЩПЩ vardЩr. Bu kitaplЩk bir dizi
sistem yazЩlЩmЩ tarafЩndan kullanЩlmaktadЩr.

%description -l uk
Б╕бл╕отека компрес╕╖ zlib м╕стить функц╕╖ компрес╕╖ та декомпрес╕╖ в
пам'ят╕ з перев╕ркою ц╕лост╕ декомпресованих даних. Ця верс╕я
п╕дтриму╓ т╕льки один метод компрес╕╖ (deflation), але в майбутньому в
не╖ можуть бути додан╕ ╕ ╕нш╕ методи ╕ вс╕ вони будуть використовувати
той же самий потоковий ╕нтерфейс.

%package devel
Summary:	Header files and libraries for zlib development
Summary(de):	Headerdateien und Libraries fЭr zlib-Entwicklung
Summary(es):	Bibliotecas y archivos de inclusiСn para desarrollo zlib
Summary(pl):	Pliki nagЁСwkowe i dokumentacja do zlib
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolvimento zlib
Summary(ru):	Хедеры и библиотеки для программирования с zlib
Summary(uk):	Хедери та б╕бл╕отеки для програмування з zlib
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
und Dekomprimierungsfunktionen, einschlieъlich IntegritДtsprЭfungen
der dekomprimierten Daten. Diese Version der Library unterstЭtzt nur
eine Komprimierungsmethode (Deflation), doch sind weitere Algorithmen
geplant, die dieselbe Art OberflДche besitzen werden. Dieses Paket
enthДlt die Header-Dateien und Libraries, die zur Entwicklung von
Programmen benЖtigt werden, die diese zlib einsetzen.

%description devel -l es
La biblioteca de compresiСn zlib provee funciones de compresiСn y
descompresiСn en memoria, incluye chequeos de integridad para los
datos descomprimidos. Esta versiСn de la biblioteca soporta solamente
un mИtodo de compresiСn (deflation) pero otros algoritmos pueden ser
aЯadidos en el futuro y tendrАn la misma interface stream. Este
paquete contiene los archivos de inclusiСn y bibliotecas necesarios al
desarrollo de programas que usan zlib.

%description devel -l fr
La bibliothХque de compression ╚ zlib ╩ offre des fonctions de
compression et de dИcompression en mИmoire, ainsi qu'une vИrification
de l'intИgritИ des donnИes dИcompressИes. La version de cette
bibliothХque ne gХre qu'une mИthode de compression (deflation), mais
d'autres algorithmes peuvent Йtre ajoutИs plus tard et auront la mЙme
interface.

Ce paquetage contient les fichiers en-tЙtes et les bibliothХques
nИcessaires au dИveloppement des programmes qui utilisent cette zlib.

%description devel -l pl
Biblioteka zlib udostЙpnia podprogramy do kompresji i dekompresji w
pamiЙci operacyjnej wЁ╠cznie ze sprawdzaniem integralno╤ci w trakcie
dekompresjii. Ta wersja biblioteki udostЙpnia tylko jedn╠ metodЙ
kompresjii o nazwie deflation niemniej inne algorytmy mog╠ byФ
dodawane udostЙpniaj╠c taki sam interfejs funkcji operuj╠cych na
strumieniu danych.

Pakiet ten zawiera pliki nagЁowkowe i dokumentacjЙ potrzebn╠ przy
tworzeniu wЁasnych programСw wykorzystuj╠cych zlib.

%description devel -l pt_BR
A biblioteca de compressЦo zlib provЙ funГУes de compressЦo e
descompressЦo em memСria, incluindo checagens de integridade para os
dados descomprimidos. Esta versЦo da biblioteca suporta somente um
mИtodo de compressЦo (deflation) mas outros algoritmos podem ser
adicionados no futuro e terЦo a mesma interface stream.

Este pacote contИm os arquivos de inclusЦo e bibliotecas necessАrios
ao desenvolvimento de programas que usam zlib.

%description devel -l ru
Библиотека компрессии zlib содержит функции компрессии и декомпрессии
в памяти, включаю проверку целостности декомпрессированных данных. Эта
версия поддерживает только один метод компрессии (deflation), но
впоследствии в нее могут быть добавлены и другие методы, и все они
будут использовать тот же потоковый интерфейс.

Этот пакет содержит хедеры и библиотеки, необходимые для написания
программ, использующих zlib.

%description devel -l tr
zlib sЩkЩЧtЩrma kitaplЩПЩ bellekte sЩkЩЧtЩrma ve aГma fonksiyonlarЩ
iГermektedir. Bu sЭrЭm yalnЩzca 'deflation' yЖntemini
desteklemektedir. Ancak baЧka algoritmalarЩn aynЩ arabirimle
eriЧilebilecek Чekilde eklenme olasЩlЩПЩ vardЩr.

Bu paket, zlib kitaplЩПЩnЩ kullanarak program geliЧtirmek iГin gereken
statik kitaplЩklarЩ ve baЧlЩk dosyalarЩnЩ iГerir.

%description devel -l uk
Б╕бл╕отека компрес╕╖ zlib м╕стить функц╕╖ компрес╕╖ та декомпрес╕╖ в
пам'ят╕ з перев╕ркою ц╕лост╕ декомпресованих даних. Ця верс╕я
п╕дтриму╓ т╕льки один метод компрес╕╖ (deflation), але в майбутньому в
не╖ можуть бути додан╕ ╕ ╕нш╕ методи ╕ вс╕ вони будуть використовувати
той же самий потоковий ╕нтерфейс.

Цей пакет м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для написання
програм, що використовують zlib.

%package static
Summary:	Static library for zlib development
Summary(es):	Static libraries for zlib development
Summary(pl):	Biblioteka statyczna do zlib
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com a zlib
Summary(ru):	Статическая библиотека для программирования с zlib
Summary(uk):	Статична б╕бл╕отека для програмування з zlib
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
Biblioteka zlib udostЙpnia podprogramy do kompresji i dekompresji w
pamiЙci operacyjnej wЁ╠cznie ze sprawdzaniem integralno╤ci w trakcie
dekompresjii. Ta wersja biblioteki udostЙpnia tylko jedn╠ metodЙ
kompresjii o nazwie deflation niemniej inne algirytmy mog╠ byФ
dodawane udostЙpniaj╠c taki sam interfejs funkcji operuj╠cych na
strumieniu danych.

Pakiet ten zawiera bibliotekЙ statyczn╠ potrzebn╠ przy tworzeniu
wЁasnych programСw wykorzystuj╠cych zlib.

%description static -l es
Static libraries for zlib development.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com a zlib.

%description static -l ru
Этот пакет содержит статическую библиотеку, необходимую для написания
программ, использующих zlib.

%description static -l uk
Цей пакет м╕стить статичну б╕бл╕отеку, необх╕дну для написання
програм, що використовують zlib.

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
