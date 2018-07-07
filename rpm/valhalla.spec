Summary: Open Source Routing Engine for OpenStreetMap
Name: valhalla
Version: 2.6.2
Release: 1%{?dist}
License: MIT
Group: Libraries/Location
URL: https://github.com/valhalla/valhalla

#Source: https://github.com/rinigus/valhalla
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libtool vim-enhanced
BuildRequires: cmake lua lua-devel
BuildRequires: libzmq-devel >= 4.1.4, czmq-devel >= 3.0, libcurl-devel >= 7.22.0
BuildRequires: jq, protobuf-devel, prime_server-devel == 0.6.3
BuildRequires: boost-devel >= 1.51, boost-chrono >= 1.51, boost-date-time >= 1.51, boost-filesystem >= 1.51
BuildRequires: boost-iostreams >= 1.51, boost-program-options >= 1.51, boost-regex >= 1.51
BuildRequires: boost-system >= 1.51, boost-thread >= 1.51
BuildRequires: lz4-devel >= 1.7.3, zlib-devel >= 1.2.8
Requires: libzmq >= 4.1.4, czmq >= 3.0, libcurl >= 7.22.0, protobuf, prime_server == 0.6.3
Requires: boost-chrono >= 1.51, boost-date-time >= 1.51, boost-filesystem >= 1.51
Requires: boost-iostreams >= 1.51, boost-program-options >= 1.51, boost-regex >= 1.51
Requires: boost-system >= 1.51, boost-thread >= 1.51
Requires: lz4 >= 1.7.3, zlib >= 1.2.8

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
%setup -q -n %{name}-%{version}/valhalla

%build
%{__make} clean || true
mkdir build-rpm
cd build-rpm

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr -DBUILD_SHARED_LIBS=OFF -DBUILD_STATIC_LIBS=ON -DENABLE_DATA_TOOLS=OFF -DENABLE_PYTHON_BINDINGS=OFF -DENABLE_SERVICES=ON
%{__make} %{?_smp_mflags}
cd ..

%install
cd build-rpm
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
cd ..

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n valhalla -p /sbin/ldconfig

%postun -n valhalla -p /sbin/ldconfig

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
* Sat Jul 7 2018 rinigus <rinigus.git@gmail.com> - 2.6.2-1
- cmake build

* Sat May 20 2017 rinigus <rinigus.git@gmail.com> - 2.2.4-1
- initial packaging release for SFOS
