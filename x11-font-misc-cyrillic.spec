Name: x11-font-misc-cyrillic
Version: 1.0.0
Release: %mkrel 5
Summary: Xorg X11 font misc-cyrillic
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-misc-cyrillic-%{version}.tar.bz2
License: CHECK
BuildArch: noarch
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-cyrillic-fonts <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font misc-cyrillic

%prep
%setup -q -n font-misc-cyrillic-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/cyrillic

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/cyrillic/fonts.dir
rm -f %{buildroot}%_datadir/fonts/cyrillic/fonts.scale

%post
mkfontscale %_datadir/fonts/cyrillic
mkfontdir %_datadir/fonts/cyrillic

%postun
mkfontscale %_datadir/fonts/cyrillic
mkfontdir %_datadir/fonts/cyrillic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/cyrillic/koi*.pcf.gz
