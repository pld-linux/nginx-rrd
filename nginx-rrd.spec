Summary:	Produce RRD graphs for nginx
Summary(pl.UTF-8):	Tworzenie wykresów RRD dla nginx
Name:		nginx-rrd
Version:	0.1.2
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.nginx.eu/nginx-rrf/%{name}-%{version}.tgz
# Source0-md5:	738d5ab1d04a3ff4679318abcea6caeb
URL:		http://www.nginx.eu/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	crondaemon
Requires:	perl-libwww
Requires:	perl-rrdtool
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		/var/spool/%{name}
%define		_wwwdir		/home/services/httpd/html

%description
Produce RRD graphs for data recived from nginx webserver. Nginx server
must be configured with --with-http_stub_status_module option and have
defined /nginx_status location

%description -l pl.UTF-8
Tworzenie wykresów z danych RRD tworzonych przez moduł mod_rrdtool
lighttpd.

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
