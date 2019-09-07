Summary: Open Source Routing Engine for OpenStreetMap
Name: valhalla-lite-devel
Version: 3.0.8
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: https://github.com/valhalla/valhalla

#Source: https://github.com/rinigus/valhalla
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: opt-gcc6 gcc-c++
BuildRequires: gcc-c++ libtool vim-enhanced
BuildRequires: cmake lua lua-devel
BuildRequires: jq, protobuf-devel, libcurl-devel >= 7.22.0
BuildRequires: boost-devel >= 1.51, boost-date-time >= 1.51, boost-filesystem >= 1.51
BuildRequires: boost-iostreams >= 1.51, boost-regex >= 1.51
BuildRequires: boost-system >= 1.51
BuildRequires: lz4-devel >= 1.7.3, zlib-devel >= 1.2.8
Requires: protobuf
Requires: boost-date-time >= 1.51, boost-filesystem >= 1.51
Requires: boost-iostreams >= 1.51, boost-regex >= 1.51
Requires: boost-system >= 1.51
Requires: lz4 >= 1.7.3, zlib >= 1.2.8
Conflicts: valhalla-devel

%description
Libraries for development with Valhalla - Open Source Routing Engine for OpenStreetMap

%package tools
Summary: valhalla tools
Group: Libraries/Location
#Requires: %{name} = %{version}
Conflicts: valhalla-tools

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
CXX=/opt/gcc6/bin/g++
CC=/opt/gcc6/bin/gcc
LINK=/opt/gcc6/bin/g++
%cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr -DBUILD_SHARED_LIBS=OFF -DBUILD_STATIC_LIBS=ON -DENABLE_DATA_TOOLS=OFF -DENABLE_PYTHON_BINDINGS=OFF -DENABLE_SERVICES=OFF -DENABLE_NODE_BINDINGS=OFF
#%{__make} %{?_smp_mflags}
%{__make} -j1
cd ..

%install
cd build-rpm
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
cd ..

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n valhalla-lite-devel -p /sbin/ldconfig

%postun -n valhalla-lite-devel -p /sbin/ldconfig

%files
%files
%defattr(-, root, root, 0755)
%{_includedir}/valhalla
%{_libdir}/libvalhalla.a
#%{_libdir}/libvalhalla.la
%{_libdir}/pkgconfig/libvalhalla.pc
%{_docdir}/libvalhalla-dev/COPYING
%{_docdir}/libvalhalla-dev/ChangeLog
%{_docdir}/libvalhalla-dev/README.md
%{_docdir}/valhalla/COPYING
%{_docdir}/valhalla/ChangeLog

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/valhalla_*
%{_libdir}/libvalhalla.so*

%changelog
* Mon Aug 27 2018 rinigus <rinigus.git@gmail.com> - 2.6.3-1
- packaging lite version

* Tue Jul 10 2018 rinigus <rinigus.git@gmail.com> - 2.6.2-1
- packaging lite version
