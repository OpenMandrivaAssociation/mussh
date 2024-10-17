Summary: MUltihost SSH
Name: mussh
Version: 1.0
Release: 2
License: GPL
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}
Group: Networking/Remote access
Source: %{name}-%{version}.tar.bz2
URL: https://www.sourceforge.net/projects/mussh
requires: openssh-clients, openssh-server

%description
Mussh is a shell script that allows you to execute a command or script
over ssh on multiple hosts with one command. When possible mussh will use
ssh-agent and RSA/DSA keys to minimize the need to enter your password
more than once.

%prep
%setup -q -n %name

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 755 mussh $RPM_BUILD_ROOT%{_bindir}/
install -m 644 mussh.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT%

%files
%defattr(-,root,root) 
%doc INSTALL README BUGS CHANGES EXAMPLES
%attr(755,root,root) %{_bindir}/mussh
%{_mandir}/man1/%{name}*



%changelog
* Thu Nov 17 2011 Antoine Ginies <aginies@mandriva.com> 1.0-1mdv2012.0
+ Revision: 731321
- version 1.0
- create _bindir in %%install section

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdv2011.0
+ Revision: 612970
- the mass rebuild of 2010.1 packages

* Tue Feb 09 2010 Antoine Ginies <aginies@mandriva.com> 0.7-1mdv2010.1
+ Revision: 502832
- mussh release 0.7

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-6mdv2010.0
+ Revision: 430137
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.5-5mdv2009.0
+ Revision: 253402
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2008.1
+ Revision: 132770
- kill invalid packager tag
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import mussh

