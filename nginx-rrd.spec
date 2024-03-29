Summary:	Produce RRD graphs for nginx
Summary(pl.UTF-8):	Tworzenie wykresów RRD dla nginx
Name:		nginx-rrd
Version:	0.1.4
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.nginx.eu/nginx-rrd/%{name}-%{version}.tgz
# Source0-md5:	53c02c03cfcece0127206c0ef85a80a2
URL:		http://www.nginx.eu/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	crondaemon
Requires:	perl-HTML-Parser
Requires:	perl-HTML-Tagset
Requires:	perl-URI
Requires:	perl-libwww
Requires:	perl-rrdtool
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		/var/spool/%{name}
%define		_wwwdir		/home/services/httpd/html

%description
Produce RRD graphs for data received from nginx webserver. Nginx
server must be configured with --with-http_stub_status_module option
and have defined /nginx_status location.

%description -l pl.UTF-8
Ten pakiet odpowiada za tworzenie wykresów z danych RRD otrzymywanych
od serwera WWW nginx. Serwer nginx musi być skonfigurowany z opcją
--with-http_stub_status_module i mieć zdefiniowane położenie
/nginx_status.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_wwwdir},%{_sbindir},/etc,/etc/cron.d}

install etc/%{name}.conf $RPM_BUILD_ROOT/etc/%{name}.conf
install etc/cron.d/%{name}.cron $RPM_BUILD_ROOT/etc/cron.d/nginx
install usr/sbin/nginx-collect $RPM_BUILD_ROOT%{_sbindir}/nginx-collect
install usr/sbin/nginx-collect.pl $RPM_BUILD_ROOT%{_sbindir}/nginx-collect.pl
install usr/sbin/nginx-graph $RPM_BUILD_ROOT%{_sbindir}/nginx-graph
install usr/sbin/nginx-graph.pl $RPM_BUILD_ROOT%{_sbindir}/nginx-graph.pl
install html/index.php $RPM_BUILD_ROOT%{_wwwdir}/index.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/nginx
%attr(755,root,root) %{_sbindir}/nginx-collect
%attr(755,root,root) %{_sbindir}/nginx-collect.pl
%attr(755,root,root) %{_sbindir}/nginx-graph
%attr(755,root,root) %{_sbindir}/nginx-graph.pl
%dir %attr(775,root,stats) %{_appdir}
%{_wwwdir}/index.php
