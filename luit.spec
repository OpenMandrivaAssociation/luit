Summary:	Locale and ISO 2022 support for Unicode terminals
Name:		luit
Version:	1.1.1
Release:	6
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		aarch64.patch

BuildRequires:	pkgconfig(fontenc) >= 1.0.1
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1


%description
Luit is a filter that can be run between an arbitrary application and a UTF-8
terminal emulator. It will convert application output from the locale's
encoding into UTF-8, and convert terminal input from UTF-8 into the locale's
encoding.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-localealiasfile=%{_datadir}/X11/locale/locale.dir

%make

%install
%makeinstall_std

%files
%{_bindir}/luit
%{_mandir}/man1/luit.1*

