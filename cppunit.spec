%define		hash	fa9aa839145cdf860bf596532bb8af97

Summary:	The C++ Unit Test Library
Name:		cppunit
Version:	1.13.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/%{hash}-%{name}-%{version}.tar.gz
# Source0-md5:	fa9aa839145cdf860bf596532bb8af97
URL:		http://www.freedesktop.org/wiki/Software/cppunit
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%package devel
Summary:	cppunit header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
cppunit header files.

%prep
%setup -q

echo 'libcppunit_la_LIBADD = -ldl' >> src/cppunit/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}/cppunit/{ui/mfc,ui/qt,config/config-[bm]*}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/DllPlugInTester
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
#%doc doc/FAQ doc/html
%attr(755,root,root) %{_bindir}/cppunit-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cppunit
%{_aclocaldir}/cppunit.m4
%{_pkgconfigdir}/cppunit.pc
%{_mandir}/man1/cppunit-config.1*

