%define name    qarecord
%define version 0.5.0
%define release %mkrel 4

Name:           %{name} 
Summary:        QT based ALSA recording interface
Version:        %{version} 
Release:        %{release}

Source:         http://dl.sf.net/alsamodular/%{name}-%{version}.tar.bz2
Patch0:         qarecord-0.5.0-upstream1.patch
URL:            http://alsamodular.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRequires:  qt4-devel alsa-lib-devel jackit-devel

%description
QARecord is a simple multithreaded stereo recording tool. It can record both
16 bit and 32 bit WAVs. By using a large ringbuffer for the captured data,
buffer overruns are avoided. QARecord can also be used as JACK client. 

%prep
%setup -q
%patch0 -p1
%if %mdkversion >= 201000
iconv -f=latin1 -t=utf8 man/de/%{name}.1 -o man/de/%{name}.1
iconv -f=latin1 -t=utf8 man/fr/%{name}.1 -o man/fr/%{name}.1
%endif

%build
%configure2_5x
%make
                                        
%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m 0644 src/pixmaps/%{name}_48.xpm %{buildroot}%{_datadir}/pixmaps/%name.xpm

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QARecord
Comment=ALSA recording GUI
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Recorder;
EOF

%clean

%if %mdkversion < 200900
%post
%update_menus
%endif
        
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop

%changelog
