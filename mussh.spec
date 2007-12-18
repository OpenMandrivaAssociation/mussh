Summary: MUltihost SSH
Name: mussh
Version: 0.5
Release: %mkrel 3
License: GPL
BuildArch: noarch
Group: Networking/Remote access
Source: %{name}-%{version}.tar.bz2
URL: http://www.sourceforge.net/projects/mussh
requires: openssh-clients, openssh-server

%description
Mussh is a shell script that allows you to execute a command or script
over ssh on multiple hosts with one command. When possible mussh will use
ssh-agent and RSA/DSA keys to minimize the need to enter your password
more than once.

%prep
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%setup

%install
install -m 755 mussh $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT%

%files
%defattr(-,root,root) 
%doc INSTALL README BUGS CHANGES EXAMPLES
%attr(755,root,root) %{_bindir}/mussh

