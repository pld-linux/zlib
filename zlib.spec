#
# Conditional build:
%bcond_without	asmopt	# without assembler optimization for i686+
%bcond_without	tests
#
%ifnarch i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_asmopt
%endif
Summary:	Library for compression and decompression
Summary(de.UTF-8):	Library für die Komprimierung und Dekomprimierung
Summary(es.UTF-8):	Biblioteca para compresión y descompresión
Summary(fr.UTF-8):	Bibliothèque de compression et décompression
Summary(pl.UTF-8):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR.UTF-8):	Biblioteca para compressão e descompressão
Summary(ru.UTF-8):	Библиотека для компрессии и декомпрессии
Summary(tr.UTF-8):	Sıkıştırma işlemleri için kitaplık
Summary(uk.UTF-8):	Бібліотека для компресії та декомпресії
Name:		zlib
Version:	1.2.4.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.zlib.net/current/beta/%{name}-%{version}.tar.gz
# Source0-md5:	aa47da7df06b7c3a7ea9bc25eba24487
Patch0:		minizip-autotools.patch
Patch1:		%{name}-asm.patch
URL:		http://www.zlib.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpm >= 4.4.9-56
Obsoletes:	zlib1
Conflicts:	poldek-libs < 0.30-0.20080820.23.40
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

%description -l de.UTF-8
Die zlib-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen
der unkomprimierten Daten. Diese Version der Library unterstützt nur
eine Komprimierungsmethode (Deflation), doch können weitere
Algorithmen nachträglich eingefügt werden und haben dann dieselbe
Oberfläche.

%description -l es.UTF-8
La biblioteca de compresión 'zlib' nos ofrece funciones de compresión
y descompresión en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versión de la biblioteca soporta solamente
un método de compresión (deflación) pero otros algoritmos pueden ser
añadidos más tarde y tendrán la misma interface. Esta biblioteca se
usa por varios programas de sistema.

%description -l fr.UTF-8
La bibliothèque de compression «zlib» offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la même
interface.

%description -l pl.UTF-8
Biblioteka zlib udostępnia podprogramy do kompresji i dekompresji w
pamięci operacyjnej włącznie ze sprawdzaniem integralności w trakcie
dekompresji. Ta wersja biblioteki udostępnia tylko jedną metodę
kompresji o nazwie deflation niemniej inne algorytmy mogą być dodawane
udostępniając taki sam interfejs funkcji operujących na strumieniu
danych.

%description -l pt_BR.UTF-8
A biblioteca de compressão 'zlib' oferece funções de compressão e
descompressão em memória, incluindo checagem da integridade de dados
não comprimidos. Essa versão da biblioteca suporta somente um método
de compressão (deflação) mas outros algoritmos podem ser adicionados
mais tarde e terão a mesma interface. Essa biblioteca é usada por
vários programas de sistema.

%description -l ru.UTF-8
Библиотека компрессии zlib содержит функции компрессии и декомпрессии
в памяти, включаю проверку целостности декомпрессированных данных. Эта
версия поддерживает только один метод компрессии (deflation), но
впоследствии в нее могут быть добавлены и другие методы, и все они
будут использовать тот же потоковый интерфейс.

%description -l tr.UTF-8
zlib sıkıştırma kitaplığı bellekte sıkıştırma ve açma fonksiyonları
içermektedir. Bu sürüm yalnızca 'deflation' yöntemini
desteklemektedir. Ancak başka algoritmaların aynı arabirimle
erişilebilecek şekilde eklenme olasılığı vardır. Bu kitaplık bir dizi
sistem yazılımı tarafından kullanılmaktadır.

%description -l uk.UTF-8
Бібліотека компресії zlib містить функції компресії та декомпресії в
пам'яті з перевіркою цілості декомпресованих даних. Ця версія
підтримує тільки один метод компресії (deflation), але в майбутньому в
неї можуть бути додані і інші методи і всі вони будуть використовувати
той же самий потоковий інтерфейс.

%package devel
Summary:	Header files and libraries for zlib development
Summary(de.UTF-8):	Headerdateien und Libraries für zlib-Entwicklung
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para desarrollo zlib
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do zlib
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento zlib
Summary(ru.UTF-8):	Хедеры и библиотеки для программирования с zlib
Summary(uk.UTF-8):	Хедери та бібліотеки для програмування з zlib
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

%description devel -l de.UTF-8
Die zlip-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen
der dekomprimierten Daten. Diese Version der Library unterstützt nur
eine Komprimierungsmethode (Deflation), doch sind weitere Algorithmen
geplant, die dieselbe Art Oberfläche besitzen werden. Dieses Paket
enthält die Header-Dateien und Libraries, die zur Entwicklung von
Programmen benötigt werden, die diese zlib einsetzen.

%description devel -l es.UTF-8
La biblioteca de compresión zlib provee funciones de compresión y
descompresión en memoria, incluye chequeos de integridad para los
datos descomprimidos. Esta versión de la biblioteca soporta solamente
un método de compresión (deflation) pero otros algoritmos pueden ser
añadidos en el futuro y tendrán la misma interface stream. Este
paquete contiene los archivos de inclusión y bibliotecas necesarios al
desarrollo de programas que usan zlib.

%description devel -l fr.UTF-8
La bibliothèque de compression « zlib » offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la même
interface.

Ce paquetage contient les fichiers en-têtes et les bibliothèques
nécessaires au développement des programmes qui utilisent cette zlib.

%description devel -l pl.UTF-8
Biblioteka zlib udostępnia podprogramy do kompresji i dekompresji w
pamięci operacyjnej włącznie ze sprawdzaniem integralności w trakcie
dekompresjii. Ta wersja biblioteki udostępnia tylko jedną metodę
kompresjii o nazwie deflation niemniej inne algorytmy mogą być
dodawane udostępniając taki sam interfejs funkcji operujących na
strumieniu danych.

Pakiet ten zawiera pliki nagłowkowe i dokumentację potrzebną przy
tworzeniu własnych programów wykorzystujących zlib.

%description devel -l pt_BR.UTF-8
A biblioteca de compressão zlib provê funções de compressão e
descompressão em memória, incluindo checagens de integridade para os
dados descomprimidos. Esta versão da biblioteca suporta somente um
método de compressão (deflation) mas outros algoritmos podem ser
adicionados no futuro e terão a mesma interface stream.

Este pacote contém os arquivos de inclusão e bibliotecas necessários
ao desenvolvimento de programas que usam zlib.

%description devel -l ru.UTF-8
Библиотека компрессии zlib содержит функции компрессии и декомпрессии
в памяти, включаю проверку целостности декомпрессированных данных. Эта
версия поддерживает только один метод компрессии (deflation), но
впоследствии в нее могут быть добавлены и другие методы, и все они
будут использовать тот же потоковый интерфейс.

Этот пакет содержит хедеры и библиотеки, необходимые для написания
программ, использующих zlib.

%description devel -l tr.UTF-8
zlib sıkıştırma kitaplığı bellekte sıkıştırma ve açma fonksiyonları
içermektedir. Bu sürüm yalnızca 'deflation' yöntemini
desteklemektedir. Ancak başka algoritmaların aynı arabirimle
erişilebilecek şekilde eklenme olasılığı vardır.

Bu paket, zlib kitaplığını kullanarak program geliştirmek için gereken
statik kitaplıkları ve başlık dosyalarını içerir.

%description devel -l uk.UTF-8
Бібліотека компресії zlib містить функції компресії та декомпресії в
пам'яті з перевіркою цілості декомпресованих даних. Ця версія
підтримує тільки один метод компресії (deflation), але в майбутньому в
неї можуть бути додані і інші методи і всі вони будуть використовувати
той же самий потоковий інтерфейс.

Цей пакет містить хедери та бібліотеки, необхідні для написання
програм, що використовують zlib.

%package static
Summary:	Static library for zlib development
Summary(es.UTF-8):	Static libraries for zlib development
Summary(pl.UTF-8):	Biblioteka statyczna do zlib
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com a zlib
Summary(ru.UTF-8):	Статическая библиотека для программирования с zlib
Summary(uk.UTF-8):	Статична бібліотека для програмування з zlib
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

%description static -l pl.UTF-8
Biblioteka zlib udostępnia podprogramy do kompresji i dekompresji w
pamięci operacyjnej włącznie ze sprawdzaniem integralności w trakcie
dekompresjii. Ta wersja biblioteki udostępnia tylko jedną metodę
kompresjii o nazwie deflation niemniej inne algirytmy mogą być
dodawane udostępniając taki sam interfejs funkcji operujących na
strumieniu danych.

Pakiet ten zawiera bibliotekę statyczną potrzebną przy tworzeniu
własnych programów wykorzystujących zlib.

%description static -l es.UTF-8
Static libraries for zlib development.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com a zlib.

%description static -l ru.UTF-8
Этот пакет содержит статическую библиотеку, необходимую для написания
программ, использующих zlib.

%description static -l uk.UTF-8
Цей пакет містить статичну бібліотеку, необхідну для написання
програм, що використовують zlib.

%package -n minizip
Summary:	Minizip manipulates files from a .zip archive
Summary(pl.UTF-8):	Minizip - biblioteka i narzędzia obrabiające pliki w archiwum .zip
Group:		Libraries
URL:		http://www.winimage.com/zLibDll/minizip.html
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description  -n minizip
Minizip manipulates files from a .zip archive.

%description  -n minizip -l pl.UTF-8
Minizip - biblioteka i narzędzia obrabiające pliki w archiwum .zip

%package -n minizip-devel
Summary:	Development files for the minizip library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki minizip
Group:		Development/Libraries
Requires:	minizip = %{epoch}:%{version}-%{release}

%description -n minizip-devel
This package contains the header files needed for developing
applications which use minizip.

%description -n minizip-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia aplikacji
wykorzystujących bibliotekę minizip.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%if %{with asmopt}
%ifarch i686 pentium3 pentium4 athlon
cp contrib/asm686/match.S .
%endif
%ifarch %{x8664}
cp contrib/amd64/amd64-match.S match.S
%endif
%endif

%build
CC="%{__cc}" \
CFLAGS="-D_REENTRANT %{rpmcppflags} %{rpmcflags} %{?with_asmopt:-DASMV}" \
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--sharedlibdir=%{_libdir}

%{__make} \
	%{?with_asmopt:OBJA=match.o PIC_OBJA=match.lo}

cd contrib/minizip
%{__aclocal}
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
# SMP flags are explicitly omitted due to a libtool/autoconf
# dependency race condition
%{__make} -j1
cd ../..

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install zutil.h $RPM_BUILD_ROOT%{_includedir}

%{__make} -C contrib/minizip install \
	DESTDIR=$RPM_BUILD_ROOT \

mv -f $RPM_BUILD_ROOT%{_libdir}/libz.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libz.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libz.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n minizip -p /sbin/ldconfig
%postun	-n minizip -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README doc/algorithm.txt doc/txtvsbin.txt
%attr(755,root,root) /%{_lib}/libz.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libz.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libz.so
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_includedir}/zutil.h
%{_pkgconfigdir}/zlib.pc
%{_mandir}/man3/zlib.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libz.a

%files -n minizip
%defattr(644,root,root,755)
%doc contrib/minizip/MiniZip64_{Changes,info}.txt
%attr(755,root,root) %{_bindir}/miniunzip
%attr(755,root,root) %{_bindir}/minizip
%attr(755,root,root) %{_libdir}/libminizip.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libminizip.so.0

%files -n minizip-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libminizip.so
%{_libdir}/libminizip.la
%{_includedir}/minizip
%{_pkgconfigdir}/minizip.pc
