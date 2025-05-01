Name:           tecla
Version:        48.0.2
Release:        1%{?dist}
Summary:        GNOME fuzzy search helper library

License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/tecla
Source0:        https://download.gnome.org/sources/tecla/48/tecla-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  pkgconfig
BuildRequires:  libxkbcommon-devel


Provides:       tecla

%description
Tecla is a fuzzy search library used by GNOME components such as GNOME Control Center.

%prep
%autosetup -n tecla-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libtecla.so*
%{_libdir}/pkgconfig/tecla.pc
%{_includedir}/tecla/

%changelog
%autochangelog