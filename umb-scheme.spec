Summary:	Scheme interpreter from U of Massachusetts at Boston
Summary(de.UTF-8):	Scheme-Interpretierer von der Massachusetts-Uni in Boston
Summary(es.UTF-8):	Interpretador de esquema de la Universidad de Massachusetts en Boston
Summary(fr.UTF-8):	Interpréteur Scheme de l'université du Massachusetts de Boston
Summary(ja.UTF-8):	Scheme プログラミング言語の実装
Summary(pl.UTF-8):	Interprter Scheme z uniwersytetu Massachusetts w Bostonie
Summary(pt_BR.UTF-8):	Interpretador de esquema da Universidade de Massachusetts em Boston
Summary(tr.UTF-8):	UMB Scheme yorumlayıcısı
Name:		umb-scheme
Version:	3.2
Release:	26
License:	GPL v1+
Group:		Development/Languages
# now https://github.com/ieee8023/UMB-Scheme ?
Source0:	http://www.cs.umb.edu/~wrc/scheme/%{name}-%{version}.tar.Z
# Source0-md5:	dca1a603c32fab21aed6b769b02a3f82
Patch0:		%{name}-misc.patch
Patch1:		%{name}-texinfo.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-man.patch
Patch4:		%{name}-info.patch
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UMB Scheme is an implementation of the language described in the IEEE
Standard for the Scheme Programming Language (December, 1990).

%description -l de.UTF-8
UMB-Scheme ist eine Implementierung der im IEEE-Standard für die
Scheme-Programmiersprache (Dez. 1990) festgelegte Sprache.

%description -l es.UTF-8
UMB Scheme es una implementación al lenguaje descrito en el padrón
IEEE para el lenguaje de programación Scheme (Diciembre de 1990).

%description -l fr.UTF-8
UMB Scheme est une implémentation du langage dans le standard IEEE
pour la programation en langage Scheme (Décembre 1990).

%description -l pl.UTF-8
UMB Scheme jest implementacją języka opisanego w dokumencie: "IEEE
Standard for the Scheme Programming Language (December, 1990)".

%description -l pt_BR.UTF-8
UMB Scheme é uma implementação da linguagem descrita no padrão IEEE
para a linguagem de programação Scheme (Dezembro de 1990).

%description -l tr.UTF-8
UMB Scheme, IEEE Scheme Programlama Dili Standardı'nda (Aralık, 1990)
tanımlanan dilin bir gerçeklemesidir.

%prep
%setup -q -n scheme-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"
makeinfo scheme.texinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_libdir}/umb-scheme/slib,%{_mandir}/man1}

install scheme $RPM_BUILD_ROOT%{_bindir}/umb-scheme
install scheme.1 $RPM_BUILD_ROOT%{_mandir}/man1/umb-scheme.1

install slib/*.{scm,init} $RPM_BUILD_ROOT%{_libdir}/umb-scheme/slib
install prelude.scheme $RPM_BUILD_ROOT%{_libdir}/umb-scheme
install SLIB-for-umb-scheme.init $RPM_BUILD_ROOT%{_libdir}/umb-scheme

install scheme.info $RPM_BUILD_ROOT%{_infodir}/umb-scheme.info

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc slib/ANNOUNCE slib/FAQ slib/README
%attr(755,root,root) %{_bindir}/umb-scheme
%{_libdir}/umb-scheme
%{_mandir}/man1/umb-scheme.1*
%{_infodir}/umb-scheme.info*
