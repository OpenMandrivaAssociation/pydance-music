%define	oname	pydance
%define	name	%{oname}-music
%define	version	1.0
%define release %mkrel 4
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

