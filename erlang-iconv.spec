%global srcname iconv
%define _disable_ld_no_undefined 1

Name:       erlang-%{srcname}
Version:    1.0.2
Release:    %mkrel 1

Group:      Development/Erlang

Summary:    Fast encoding conversion library for Erlang / Elixir
License:    ASL 2.0
URL:        https://github.com/processone/iconv/
Source0:    https://github.com/processone/iconv/archive/%{version}.tar.gz

Provides:   erlang-p1_iconv = %{version}-%{release}
Obsoletes:  erlang-p1_iconv <= 1.0.0-2

BuildRequires: erlang-p1_utils >= 1.0.5
BuildRequires: erlang-rebar

%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
Erlang bindings for libiconv. This is used by ejabberd.


%prep
%autosetup -n iconv-%{version}


%build
%configure --enable-nif
%{rebar_compile}


%check
%{rebar_eunit}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/iconv.so $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.2-1.mga6
+ Revision: 1067967
- imported package erlang-iconv

