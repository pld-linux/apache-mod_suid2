%define		mod_name	suid2
%define		ver		0.2
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: execution of scripts under their own uids
Summary(pl):	Modu³ do apache: wykonywanie skryptów pod wskazanym uidem
Name:		apache-mod_%{mod_name}
Version:	%{ver}
Release:	0.1
License:	ASL v2.0
Group:		Networking/Daemons
Source0:	http://bluecoara.net/download/apache/mod_%{mod_name}-%{version}.tar.gz
# Source0-md5:	c45ba4932cade36468deacf484c4207f
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

install .libs/mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_pkglibdir}/*
