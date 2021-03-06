%define with_doc_subpackage  1%{nil}


Summary: IBM/Lotus Sametime Protocol Decentralization Client
Name: meanwhile-tears
Epoch: 0
Version: 0.1.0
Release: arsenic
License: GNU Affero General Public License Version 3
Group: Applications/Internet
URL: https://github.com/pavgup/meanwhile-sametime-tears/

Requires: glib2 >= 2.0.0

Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel >= 2.0.0

%if %{with_doc_subpackage}
BuildRequires: doxygen
%endif


%description
Library for connecting as a client to a Lotus Sametime
community. Provides a simplified interface for authentication,
presence, messaging, conferencing, and remote preferences.


%prep
%setup -q


%build
%if %{with_doc_subpackage}
%configure --enable-doxygen
%else
%configure
%endif
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{makeinstall}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog INSTALL LICENSE README.md
%{_libdir}/libmeanwhile.so*


%package devel
Group: Applications/Internet
Summary: Development package for the Meanwhile library
License: LGPL
Requires: %{name} = %{version}-%{release}


%description devel
Development package for the Meanwhile Tears Client


%files devel
%defattr(-,root,root,-)
%{_includedir}/meanwhile/
%{_libdir}/libmeanwhile.a
%{_libdir}/libmeanwhile.la
%{_libdir}/pkgconfig/meanwhile.pc


%if %{with_doc_subpackage}
%package doc
Group: Applications/Internet
Summary: Documentation for the Meanwhile library
License: GNU Free Documentation License


%description doc
Documentation for the Meanwhile library


%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/%{name}-doc-%{version}/
%endif


%post
/sbin/ldconfig 2> /dev/null


%postun
/sbin/ldconfig 2> /dev/null


%changelog
* Fri Nov 27 2015 <pg8p@virginia.edu>
- the loathing of sametime finally broke me; IBM why.
- consolidated the excellent meanwhile library across lots of repos
- dropped the ability for my changes to be closed using AGPL 3
- upgraded all existing LGPL 2.0 code to LGPL 2.1; LGPL 2.0 is deprecated

* Tue Jul 31 2012 <mrcsparker@gmail.com>
- glib header fixes
- st_list.c crash bug fixed

* Fri Nov 18 2005  <siege@preoccupied.net>
- removed the gmp and gmp-devel requirements

* Wed Sep 21 2005  <siege@preoccupied.net>
- added doc sub package

* Sat Sep 17 2005  <siege@preoccupied.net>
- added gmp and gmp-devel requrements

* Sun Jan 16 2005  <siege@preoccupied.net>
- removed python package (now in meanwhile-python module)

* Mon Dec 27 2004  <siege@preoccupied.net>
- updated python package

* Thu Jul 22 2004  <siege@preoccupied.net>
- moved .a, .la into -devel package
- added docs to install

* Mon May 10 2004  <siege@preoccupied.net>
- Separated meanwhile from meanwhile-gaim
- First distribution with autoconf/automake/libtool

* Tue Apr 13 2004  <siege@preoccupied.net> 
- Initial rpm build.
