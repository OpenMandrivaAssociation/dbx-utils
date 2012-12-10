%define	major 0
%define libname	%mklibname dbx %{major}
%define develname	%mklibname dbx -d

Summary:	Extracts emails from MS Outlook Express 5.0
Name:   	dbx-utils
Version: 	1.0.3
Release: 	9
License:	GPLv2+
Group:		Networking/Mail
URL:		http://sourceforge.net/projects/ol2mbox
Source0:	libdbx_%{version}.tar.bz2
Patch0:		libdbx_1.0.3-shared.diff
Patch1:		libdbx_1.0.3-Mail-Transport-Dbx-0.07.diff
BuildRequires:	libtool

%description
Extract emails from MS Outlook Express 5.0 directory, and DBX files into mbox
format files.

%package -n	%{libname}
Summary:	Shared libdbx library
Group:          System/Libraries

%description -n	%{libname}
Extract emails from MS Outlook Express 5.0 directory, and DBX files into mbox
format files.

This package contains the shared libdbx library.

%package -n	%{develname}
Summary:	Development files for the libdbx library
Group:		Development/C
Provides:	libdbx-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
Extract emails from MS Outlook Express 5.0 directory, and DBX files into mbox
format files.

This package contains the static libdbx library and header files.

%prep

%setup -q -n libdbx_%{version}
%patch0 -p0
%patch1 -p1

%build

%make CFLAGS="%{optflags} -DDBX_BIG_ENDIAN" libdir=%{_libdir}

%install
%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%files
%defattr(-,root,root)
%doc AUTHORS FILE-FORMAT README*
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/libdbx
%{_libdir}/*.so


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-8mdv2011.0
+ Revision: 617521
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-7mdv2010.0
+ Revision: 427720
- rebuild

* Tue Aug 26 2008 Emmanuel Andry <eandry@mandriva.org> 1.0.3-6mdv2009.0
+ Revision: 276309
- apply devel policy
- fix license
- check major

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-5mdv2009.0
+ Revision: 243976
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.3-3mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdv2008.0
+ Revision: 25428
- Import dbx-utils



* Mon Apr 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdk
- added fixes from Mail-Transport-Dbx-0.07 (P1)
- use libtool

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.3-2mdk
- rebuild
- rename patch

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0.3-1mdk
- 1.0.3
- fix P0
- misc spec file fixes

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0.2-4mdk
- mr lint fixes

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0.2-3mdk
- build release

* Sun Aug  4 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0.2-2mdk
- rebuilt with gcc-3.2

* Thu Jun 13 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0.2-1mdk
- new version
- initial cooker contrib

* Fri Aug 10 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-1mdk
- First version.
