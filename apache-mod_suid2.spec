%define		mod_name	suid2
%define		ver		0.3
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: execution of scripts under their own uids
Summary(pl):	Modu³ do apache: wykonywanie skryptów pod wskazanym uidem
Name:		apache-mod_%{mod_name}
Version:	%{ver}
Release:	1
License:	ASL v2.0
Group:		Networking/Daemons
Source0:	http://bluecoara.net/download/apache/mod_%{mod_name}-%{version}.tar.gz
# Source0-md5:	275a1372a63bd2f9031b71f8a621f531
Patch0:		%{name}-conf.patch
URL:		http://bluecoara.net/servers/apache/mod_suid2_en.phtml
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0.0
Requires(post,preun):	%{apxs}
Requires:	apache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR)

%description
Apache module: execution of scripts under their own uids per-vhost.

%description -l pl
Modu³ do apache: wykonywanie skryptów pod wskazanym uidem per-vhost.

%prep
%setup -q -n mod_%{mod_name}-%{version}
%patch0 -p1

%build
%{apxs} -c mod_%{mod_name}.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkglibdir}

libtool install mod_%{mod_name}.la $RPM_BUILD_ROOT%{_pkglibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_pkglibdir}/*.so
