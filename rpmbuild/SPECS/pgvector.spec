Name:           pgvector
Version:        0.6.2
Release:        1%{?dist}
Summary:        pgvector for postgresql 16
BuildArch:      x86_64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       postgresql-server

%description


%prep
%autosetup


%build
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_prefix}/share/pgsql/*
%{_prefix}/src/debug/pgvector-0.6.2-1.fc40.x86_64/src/*
%{_prefix}/lib64/pgsql/*
%{_prefix}/include/pgsql/server/extension/vector/*



%changelog
* Fri Apr 19 2024 harry <yelcat@gmail.com>
- 
