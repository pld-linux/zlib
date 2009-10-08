#
# Conditional build:
%bcond_without	asmopt	# without assembler optimization for i586+
%bcond_with	pax
#
%ifnarch i586 i686 pentium3 pentium4 athlon
%undefine	with_asmopt
%endif
%if %{with pax} && %{with asmopt}
%undefine	with_asmopt
%endif

%if "%{pld_release}" == "ac"
# on 2.4 kernel i586 doesn't work either:
# open("/usr/lib/libcrypto.so.0.9.7", O_RDONLY) = 3
# ...
# mprotect...= -1 EINVAL (Invalid argument)
# mprotect...= -1 ENOMEM (Cannot allocate memory)
%ifarch i586
%undefine	with_asmopt
%endif
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
Version:	1.2.3
Release:	8
License:	BSD
Group:		Libraries
Source0:	http://www.zlib.net/%{name}-%{version}.tar.gz
# Source0-md5:	debc62758716a169df9f62e6ab2bc634
URL:		http://www.zlib.net/
BuildRequires:	rpm >= 4.4.9-56
Obsoletes:	zlib1
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

%prep
%setup -q

%ifarch i686 pentium3 pentium4 athlon
cp contrib/asm686/match.S .
%endif
%ifarch i586
cp contrib/asm586/match.S .
%endif

%build
CFLAGS="-D_REENTRANT -fPIC %{rpmcflags} %{?with_asmopt:-DASMV}" \
LDSHARED="%{__cc} $CFLAGS -shared -Wl,-soname,libz.so.1" \
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

%if "%{_libdir}" != "%{_prefix}/lib"
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
