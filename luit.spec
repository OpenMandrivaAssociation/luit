Name: luit
Version: 1.0.1
Release: %mkrel 4
Summary: Locale and ISO 2022 support for Unicode terminals
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libfontenc-devel >= 1.0.1
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Luit is a filter that can be run between an arbitrary application and a UTF-8
terminal emulator. It will convert application output from the locale's
encoding into UTF-8, and convert terminal input from UTF-8 into the locale's
encoding.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-localealiasfile=%{_datadir}/X11/locale/locale.dir

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# for compatibility
mkdir -p %{buildroot}/usr/X11R6/bin
ln -s ../../bin/luit %{buildroot}/usr/X11R6/bin/luit

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/luit
%{_mandir}/man1/luit.1x.bz2
# compatibility link, needed as long as xterm looks there
/usr/X11R6/bin/luit


