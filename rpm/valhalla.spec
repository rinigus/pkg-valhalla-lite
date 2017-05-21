Summary: Open Source Routing Engine for OpenStreetMap
Name: valhalla
Version: 2.2.4
Release: 1%{?dist}
License: MIT
Group: Libraries/Location
URL: https://github.com/valhalla/valhalla

Source: https://github.com/rinigus/valhalla
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libtool
BuildRequires: libzmq-devel >= 4.1.4, czmq-devel >= 3.0, libcurl-devel >= 7.22.0
BuildRequires: jq, prime_server-devel == 0.6.3
BuildRequires: boost-devel >= 1.51, boost-chrono >= 1.51, boost-date-time >= 1.51, boost-filesystem >= 1.51
BuildRequires: boost-iostreams >= 1.51, boost-program-options >= 1.51, boost-regex >= 1.51
BuildRequires: boost-system >= 1.51, boost-thread >= 1.51
Requires: libzmq >= 4.1.4, czmq >= 3.0, libcurl >= 7.22.0, prime_server == 0.6.3
Requires: boost-chrono >= 1.51, boost-date-time >= 1.51, boost-filesystem >= 1.51
Requires: boost-iostreams >= 1.51, boost-program-options >= 1.51, boost-regex >= 1.51
Requires: boost-system >= 1.51, boost-thread >= 1.51

%description
Open Source Routing Engine for OpenStreetMap

%package devel
Summary: valhalla development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development


%package tools
Summary: valhalla tools
Group: Libraries/Location
Requires: %{name} = %{version}

%description tools
Tools for valhalla

%prep
%setup

%build
%{__make} clean || true
./autogen.sh

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure --enable-data-tools=no --enable-static=yes --enable-python-bindings=no --enable-services=yes

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post

%files
%files
%defattr(-, root, root, 0755)
%{_libdir}/libvalhalla.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/valhalla
%{_libdir}/libvalhalla.a
%{_libdir}/libvalhalla.la
%{_libdir}/pkgconfig/libvalhalla.pc

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/valhalla_*

%changelog
* Sat May 20 2017 rinigus <rinigus.git@gmail.com> - 2.2.4-1
- initial packaging release for SFOS
