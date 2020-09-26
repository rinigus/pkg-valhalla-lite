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

Patch0: 0001-set-python-version-in-a-script.patch

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
Valhalla Libraries - Open Source Routing Engine for OpenStreetMap

%package devel
Summary: Valhalla development package
Group: Development/Libraries/Other
Requires: %{name} = %{version}

%description devel
%summary

%package tools
Summary: valhalla tools
Group: Libraries/Location
#Requires: %{name} = %{version}
Conflicts: valhalla-tools

%description tools
Tools for valhalla

%prep
%setup -q -n %{name}-%{version}/valhalla
%patch -p1

%build
%{__make} clean || true
mkdir build-rpm || true
cd build-rpm

%cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr -DBUILD_SHARED_LIBS=ON -DENABLE_DATA_TOOLS=OFF -DENABLE_PYTHON_BINDINGS=OFF -DENABLE_SERVICES=OFF -DENABLE_NODE_BINDINGS=OFF
%{__make} %{?_smp_mflags}
#%{__make} -j1
cd ..

%install
cd build-rpm
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
cd ..

# rm -rf %{buildroot}/usr/include/gmock
# rm -rf %{buildroot}/usr/include/gtest
# rm -rf %{buildroot}%{_libdir}/cmake/GTest
# rm -rf %{buildroot}%{_libdir}/libgmock*
# rm -rf %{buildroot}%{_libdir}/libgtest*
# rm -rf %{buildroot}%{_libdir}/pkgconfig/gmock*
# rm -rf %{buildroot}%{_libdir}/pkgconfig/gtest*

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n valhalla-lite-devel -p /sbin/ldconfig

%postun -n valhalla-lite-devel -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libvalhalla.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/valhalla
%{_libdir}/pkgconfig/libvalhalla.pc
%{_docdir}/libvalhalla-dev/*
%{_docdir}/valhalla/*
%{_docdir}/libvalhalla0/*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/valhalla_*

%changelog
* Mon Aug 27 2018 rinigus <rinigus.git@gmail.com> - 2.6.3-1
- packaging lite version

* Tue Jul 10 2018 rinigus <rinigus.git@gmail.com> - 2.6.2-1
- packaging lite version
