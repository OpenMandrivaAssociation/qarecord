%define name	qarecord
%define version	0.0.9b
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	QT based ALSA recording interface
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.suse.de/~mana/kalsatools.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel alsa-lib-devel jackit-devel

%description
QARecord is a simple multithreaded stereo recording tool. It can record both
16 bit and 32 bit WAVs. By using a large ringbuffer for the captured data,
buffer overruns are avoided. QARecord can also be used as JACK client. 

%prep
%setup -q
perl -p -i -e "s|-O2|$RPM_OPT_FLAGS||g" make_qarecord
perl -p -i -e "s/\(QT_BASE_DIR\)\/lib/\(QT_BASE_DIR\)\/%_lib/g" make_qarecord

%build
%make -f make_qarecord
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QARecord
Comment=ALSA recording GUI
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Recorder;
Encoding=UTF-8
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop

