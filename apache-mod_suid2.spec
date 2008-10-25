%define		mod_name	suid2
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: execution of scripts under their own uids
Summary(pl.UTF-8):	Moduł do apache: wykonywanie skryptów pod wskazanym uidem
Name:		apache-mod_%{mod_name}
Version:	0.3
Release:	1
License:	ASL v2.0
Group:		Networking/Daemons/HTTP
Source0:	http://bluecoara.net/download/apache/mod_%{mod_name}-%{version}.tar.gz
# Source0-md5:	275a1372a63bd2f9031b71f8a621f531
Patch0:		%{name}-conf.patch
Patch1:		%{name}-groups.patch
URL:		http://bluecoara.net/servers/apache/mod_suid2_en.phtml
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0.0
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache(modules-api) = %apache_modules_api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
Apache module: execution of scripts under their own uids per-vhost.

%description -l pl.UTF-8
Moduł do apache: wykonywanie skryptów pod wskazanym uidem per-vhost.

%prep
%setup -q -n mod_%{mod_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{apxs} -c mod_%{mod_name}.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/httpd.conf}

install .libs/mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}
echo 'LoadModule %{mod_name}_module modules/mod_%{mod_name}.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/90_mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q httpd restart

%postun
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*.so
