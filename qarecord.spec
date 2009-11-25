%define name	qarecord
%define version	0.5.0
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	QT based ALSA recording interface
Version: 	%{version}
Release: 	%{release}

Source:		http://sourceforge.net/projects/alsamodular/files/QARecord/%version/%{name}-%{version}.tar.bz2
Patch0:		qarecord-0.5.0-fix-str-fmt.patch
URL:		http://alsamodular.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt4-devel alsa-lib-devel jackit-devel

%description
QARecord is a simple multithreaded stereo recording tool. It can record both
16 bit and 32 bit WAVs. By using a large ringbuffer for the captured data,
buffer overruns are avoided. QARecord can also be used as JACK client. 

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QARecord
Comment=ALSA recording GUI
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Recorder;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_bindir}/%name
%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(de) %{_mandir}/de/man1/*
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
