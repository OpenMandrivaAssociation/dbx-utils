%define	major 0
%define libname	%mklibname dbx %{major}
%define develname	%mklibname dbx -d

Summary:	Extracts emails from MS Outlook Express 5.0
Name:   	dbx-utils
Version: 	1.0.3
Release: 	%mkrel 6
License:	GPLv2+
Group:		Networking/Mail
URL:		http://sourceforge.net/projects/ol2mbox
Source0:	libdbx_%{version}.tar.bz2
Patch0:		libdbx_1.0.3-shared.diff
Patch1:		libdbx_1.0.3-Mail-Transport-Dbx-0.07.diff
BuildRequires:	libtool
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
%{_libdir}/*.a
%{_libdir}/*.la
