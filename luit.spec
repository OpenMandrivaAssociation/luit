Name: luit
Version: 1.1.1
Release: 1
Summary: Locale and ISO 2022 support for Unicode terminals
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libfontenc-devel >= 1.0.1
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Patch0:		aarch64.patch

%description
Luit is a filter that can be run between an arbitrary application and a UTF-8
terminal emulator. It will convert application output from the locale's
encoding into UTF-8, and convert terminal input from UTF-8 into the locale's
encoding.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir} \
		--with-localealiasfile=%{_datadir}/X11/locale/locale.dir

%make

%install
%makeinstall_std

%files
%{_bindir}/luit
%{_mandir}/man1/luit.1*



%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 786824
- version update 1.1.

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 666105
- mass rebuild

* Thu Oct 07 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 583913
- new release

* Wed Feb 10 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.5-1mdv2010.1
+ Revision: 503786
- New version: 1.0.5

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.4-1mdv2010.1
+ Revision: 464635
- New version: 1.0.4

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-4mdv2010.0
+ Revision: 426017
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.3-3mdv2009.1
+ Revision: 351545
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 223133
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-1mdv2008.1
+ Revision: 166386
- Revert to use upstream tarball, build requires and remove non mandatory local patches.
  New upstream release version 1.0.3.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-4mdv2008.1
+ Revision: 156500
- Updated BuildRequires and resubmit package.

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 152883
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Herton Ronaldo Krzesinski <herton@mandriva.com.br>
    - Updated to 1.0.2.
    - Removed compatibility symlink at /usr/X11R6/bin, as xterm now is ok
      with /usr/bin.

