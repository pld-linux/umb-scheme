Summary:	Scheme interpreter from U of Massachusetts at Boston
Summary(de):	Scheme-Interpretierer von der Massachusetts-Uni in Boston 
Summary(fr):	Interpr�teur Scheme de l'universit� du Massachusetts de Boston
Summary(pl):	Interprter Scheme z uniwersytetu Massachusetts w Bostonie
Summary(tr):	UMB Scheme yorumlay�c�s�
Name:		umb-scheme
Version:	3.2
Release:	10
Copyright:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Source:		ftp://ftp.cs.umb.edu/pub/scheme/%{name}-%{version}.tar.Z
Patch0:		umb-scheme-misc.patch
Patch1:		umb-scheme-texinfo.patch
Patch2:		umb-scheme-config.patch
Patch3:		umb-scheme-man.patch
Patch4:		umb-scheme-info.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
UMB Scheme is an implementation of the language described in the IEEE
Standard for the Scheme Programming Language (December, 1990).

%description -l de
UMB-Scheme ist eine Implementierung der im IEEE-Standard f�r die
Scheme-Programmiersprache (Dez. 1990) festgelegte Sprache.

%description -l fr
UMB Scheme est une impl�mentation du langage dans le standard IEEE pour
la programation en langage Scheme (D�cembre 1990).

%description -l pl
UMB Scheme jest implementacj� j�zyka opisanego w dokumencie:
"IEEE Standard for the Scheme Programming Language (December, 1990)".

%description -l tr
UMB Scheme, IEEE Scheme Programlama Dili Standard�'nda (Aral�k, 1990)
tan�mlanan dilin bir ger�eklemesidir.

%prep
%setup -q -n scheme-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make
makeinfo scheme.texinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,info,lib/umb-scheme/slib,man/man1}

install -s scheme $RPM_BUILD_ROOT/usr/bin/umb-scheme
install scheme.1 $RPM_BUILD_ROOT%{_mandir}/man1/umb-scheme.1

install slib/*.{scm,init} $RPM_BUILD_ROOT/usr/lib/umb-scheme/slib
install prelude.scheme $RPM_BUILD_ROOT/usr/lib/umb-scheme
install SLIB-for-umb-scheme.init $RPM_BUILD_ROOT/usr/lib/umb-scheme

install scheme.info $RPM_BUILD_ROOT%{_infodir}/umb-scheme.info
gzip -9nf $RPM_BUILD_ROOT/usr/{info/*info*,man/man1/*} \
	slib/ANNOUNCE slib/FAQ slib/README

%post
/sbin/install-info %{_infodir}/umb-scheme.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/umb-scheme.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {slib/ANNOUNCE,slib/FAQ,slib/README}.gz
/usr/lib/umb-scheme

%attr(755,root,root) /usr/bin/umb-scheme
%{_mandir}/man1/*

%{_infodir}/umb-scheme.info.gz

%changelog
* Mon Apr 12 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2-10]
- added Group(pl),
- standarized {un}registering info pages (added umb-scheme-info.patch).

* Sun Mar 14 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2-9]
- removed man group from man pages.

* Sun Dec 13 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [3.2-8d]
- major changes -- build for PLD Tornado. 

* Thu Nov 12 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2-8]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- in /usr/lib/umb-scheme/slib are installed only *.{scm,init} files.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- install-info

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
