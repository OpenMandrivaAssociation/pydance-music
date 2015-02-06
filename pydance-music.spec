%define	oname	pydance
%define	name	%{oname}-music
%define	version	1.0
%define release 10
%define	Summary	Songs and step patterns for PyDDR

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Url:		http://icculus.org/pyddr/get.php
Source0:	%{name}.tar.bz2
Group:		Games/Other
Summary:	%{Summary}
BuildArch:	noarch
Requires:	%{oname}
Provides:	pyddr-music
Obsoletes:	pyddr-music
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PyDDR is a simulator of the popular arcade game "Dance Dance Revolution",
in which you must step on particular arrows on the floor in time with
music playing in the background. This package contains the following songs,
and step patterns for them: 
* "6th, January", by Brendan Becker
* "SyNRG", by Brendan Becker
* "Forkbomb", by Pajama Crisis
   
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}/songs
tar -xjf %{SOURCE0} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}/songs

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_gamesdatadir}/%{oname}/songs/*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-9mdv2010.0
+ Revision: 433737
- rebuild
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2009.0
+ Revision: 259418
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-6mdv2009.0
+ Revision: 247261
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0-4mdv2008.1
+ Revision: 125796
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import pydance-music


* Mon Feb 07 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-4mdk
- rebuild

* Tue Jan 13 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-3mdk
- update to latest stuff that will work with pydance-0.8.4

* Wed Jul 30 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-2mdk
- name change to pydance

* Thu Apr 10 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-1mdk
- initial release
