Summary:	syslogd to MySQL wrapper
Name:		sqlsyslogd
Version:	0.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.pld.org.pl/people/speedy/%{name}.tgz
URL:		http://www.frasunek.com/sources/security/sqlsyslogd/
BuildRequires:	mysql-devel
Requires:	mysql-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLSyslogd is simple syslogd to MySQL wrapper. It's invoked by syslogd
from syslog.conf and redirects all messages to MySQL database.

%prep
%setup -q -n %{name}

%build
%{__cc} %{rpmcflags} %{rpmldflags} -lmysqlclient -DCONF=\"%{_sysconfdir}/sqlsyslogd.conf\" -o sqlsyslogd sqlsyslogd.c
#%{__cc} %{rpmcflags} %{rpmldflags} -lmysqlclient -DCONF=\"/etc/sqlsyslogd.conf\" -o ntsyslogd ntsyslogd.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install sqlsyslogd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sqlsyslogd
%doc INSTALL sqlsyslogd.sql
