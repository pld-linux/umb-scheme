Summary:     Scheme interpreter from U of Massachusetts at Boston
Summary(de): Scheme-Interpretierer von der Massachusetts-Uni in Boston 
Summary(fr): Interpr�teur Scheme de l'universit� du Massachusetts de Boston
Summary(tr): UMB Scheme yorumlay�c�s�
Name:        umb-scheme
Version:     3.2
Release:     8
Copyright:   GPL
Group:       Development/Languages
Source:      ftp://ftp.cs.umb.edu/pub/scheme/%{name}-%{version}.tar.Z
Patch0:      umb-scheme-3.2-misc.patch
Patch1:      umb-scheme-3.2-texinfo.patch
Patch2:      umb-scheme-3.2-config.patch
Patch3:      umb-scheme-3.2-man.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
UMB Scheme is an implementation of the language described in the IEEE
Standard for the Scheme Programming Language (December, 1990).

%description -l de
UMB-Scheme ist eine Implementierung der im IEEE-Standard f�r die
Scheme-Programmiersprache (Dez. 1990) festgelegte Sprache.

%description -l fr
UMB Scheme est une impl�mentation du langage dans le standard IEEE pour
la programation en langage Scheme (D�cembre 1990).

%description -l tr
UMB Scheme, IEEE Scheme Programlama Dili Standard�'nda (Aral�k, 1990)
tan�mlanan dilin bir ger�eklemesidir.

%prep
%setup -q -n scheme-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make
makeinfo scheme.texinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,info,lib/umb-scheme/slib,man/man1}

install -s scheme $RPM_BUILD_ROOT/usr/bin/umb-scheme
install scheme.1 $RPM_BUILD_ROOT/usr/man/man1/umb-scheme.1

install slib/*.{scm,init} $RPM_BUILD_ROOT/usr/lib/umb-scheme/slib
install prelude.scheme $RPM_BUILD_ROOT/usr/lib/umb-scheme
install SLIB-for-umb-scheme.init $RPM_BUILD_ROOT/usr/lib/umb-scheme

install scheme.info $RPM_BUILD_ROOT/usr/info/umb-scheme.info
gzip -9nf $RPM_BUILD_ROOT/usr/info/umb-scheme.info

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/umb-scheme.info.gz /usr/info/dir \
  --entry="* umb-scheme: (umb-scheme).                     UMB Scheme Interpreter."

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/umb-scheme.info.gz /usr/info/dir \
      --entry="* umb-scheme: (umb-scheme).                     UMB Scheme Interpreter."
fi

%files
%defattr(644, root, root, 755)
%doc slib/ANNOUNCE slib/FAQ slib/README
/usr/lib/umb-scheme
%attr(755, root, root) /usr/bin/umb-scheme
%attr(644, root,  man) /usr/man/man1/umb-scheme.1
/usr/info/umb-scheme.info.gz

%changelog
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
