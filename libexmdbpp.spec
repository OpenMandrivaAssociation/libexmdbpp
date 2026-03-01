%define major 0
%define libname %mklibname exmdbpp
%define devname %mklibname exmdbpp -d

Name:		libexmdbpp
Version:	1.11
Release:	1
Source0:	https://github.com/grommunio/libexmdbpp/archive/refs/tags/%{version}.tar.gz
Summary:	A C++ implementation of the exmdb wire protocol
URL:		https://github.com/grommunio/libexmdbpp
License:	GPL
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	pkgconfig(pybind11)
BuildRequires:	pkgconfig(python3)
BuildSystem:	cmake

%description
libexmdbpp is a secondary C++ implementation of the exmdb wire protocol (after
exmdb_client from Gromox), for use with grommunio. libexmdbpp provides
bindings for Python via pybind11 for use by e.g. grommunio-admin-api.

%package -n %{libname}
Summary:	A C++ implementation of the exmdb wire protocol
Group:		System/Libraries
Provides:	python%{pyver}dist(pyexmdb)

%description -n %{libname}
libexmdbpp is a secondary C++ implementation of the exmdb wire protocol (after
exmdb_client from Gromox), for use with grommunio. libexmdbpp provides
bindings for Python via pybind11 for use by e.g. grommunio-admin-api.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

libexmdbpp is a secondary C++ implementation of the exmdb wire protocol (after
exmdb_client from Gromox), for use with grommunio. libexmdbpp provides
bindings for Python via pybind11 for use by e.g. grommunio-admin-api.

%install -a
mkdir -p %{buildroot}%{_libdir}/cmake
mv %{buildroot}%{_datadir}/exmdbpp/cmake %{buildroot}%{_libdir}/cmake/exmdbpp

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{python_sitearch}/pyexmdb.cpython*.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/exmdbpp
