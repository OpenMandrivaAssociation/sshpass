Name: sshpass
Version: 1.05
Release: 1
Source0: http://switch.dl.sourceforge.net/project/sshpass/sshpass/%{version}/sshpass-%{version}.tar.gz
Summary: Tool for non-interactively performing ssh password authentication
URL: http://sshpass.sf.net/
License: GPL
Group: System/Base

%description
Tool for non-interactively performing ssh password authentication

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/*/*
