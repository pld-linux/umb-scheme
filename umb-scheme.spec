Summary:	Scheme interpreter from U of Massachusetts at Boston
Summary(de):	Scheme-Interpretierer von der Massachusetts-Uni in Boston
Summary(es):	Interpretador de esquema de la Universidad de Massachusetts en Boston
Summary(fr):	Interpréteur Scheme de l'université du Massachusetts de Boston
Summary(ja):	Scheme .$B%W%m%0%i%_%s%08@8l$N<BAu.(B
Summary(pl):	Interprter Scheme z uniwersytetu Massachusetts w Bostonie
Summary(pt_BR):	Interpretador de esquema da Universidade de Massachusetts em Boston
Summary(tr):	UMB Scheme yorumlayýcýsý
Name:		umb-scheme
Version:	3.2
Release:	25
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.cs.umb.edu/pub/scheme/%{name}-%{version}.tar.Z
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

%description -l de
UMB-Scheme ist eine Implementierung der im IEEE-Standard für die
Scheme-Programmiersprache (Dez. 1990) festgelegte Sprache.

%description -l es
UMB Scheme es una implementación al lenguaje descrito en el padrón
IEEE para el lenguaje de programación Scheme (Diciembre de 1990).

%description -l fr
UMB Scheme est une implémentation du langage dans le standard IEEE
pour la programation en langage Scheme (Décembre 1990).

%description -l pl
UMB Scheme jest implementacj± jêzyka opisanego w dokumencie: "IEEE
Standard for the Scheme Programming Language (December, 1990)".

%description -l pt_BR
UMB Scheme é uma implementação da linguagem descrita no padrão IEEE
para a linguagem de programação Scheme (Dezembro de 1990).

%description -l tr
UMB Scheme, IEEE Scheme Programlama Dili Standardý'nda (Aralýk, 1990)
tanýmlanan dilin bir gerçeklemesidir.

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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc slib/ANNOUNCE slib/FAQ slib/README
%attr(755,root,root) %{_bindir}/umb-scheme
%{_libdir}/umb-scheme
%{_mandir}/man1/*
%{_infodir}/umb-scheme.info*
