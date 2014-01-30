%global commit d4e0d42922ae2069e025c73564d5a74bf7b78e11
%global shortcommit %(echo %{commit} | cut -c 1-7)

Name:		piqi
Version:	0.6.5
Release:	2%{?dist}
Summary:	Set of languages and tools for working with structured data

Group:	Development/Languages

License:	ASL 2.0
URL:		http://piqi.org
Source0:	https://github.com/alavrik/piqi/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-findlib

# For building documentation
BuildRequires:	pandoc

# For 'make check'
BuildRequires:	protobuf-devel

%description
Piqi is a set of languages and open-source tools for working with structured
data. It includes:

    - A cross-language data serialization system compatible with Google Protocol
      Buffers. It allows programs implemented in various languages to exchange
      and persist data in a portable manner.

    - Piq -- a human-friendly typed data representation language. It is designed
      to be more convenient for representing, viewing and editing data than
      JSON, XML, CSV, S-expressions and other formats.

    - Piqi -- a powerful data definition language. It is specially designed to
      be used with Piq, but also works as a schema language for other data
      formats including JSON, XML and Protocol Buffers binary format. Tools for
      validating, pretty-printing and converting data between Piq, JSON, XML
      and Protocol Buffers binary format.

    - Piqi-RPC -- an RPC-over-HTTP system for Erlang. It provides a simple way
      to expose Erlang services via JSON, XML and Google Protocol Buffers over
      HTTP.

As a data serialization system, Piqi implements native support for OCaml and
Erlang. Connectivity with other programming languages is provided via Google
Protocol Buffers. Overall, Piqi provides a more natural mapping to functional
programming languages compared to various serialization systems that were
originally designed for imperative or object-oriented languages.

Piqi was inspired by Google Protocol Buffers and specially designed to be
largely compatible with it. Like Protocol Buffers, Piqi relies on type
definitions and supports data schema evolution. The main difference is that Piqi
has a richer data model, high-level modules and a powerful data representation
language (Piq).

The combination of data representation (Piq) and data definition (Piqi)
languages is similar to the concept of "valid XML" (i.e. XML conforming to some
XML Schema). However, unlike XML, Piq has a concise, clean syntax and a data
model similar to those of high-level programming languages.


%prep
%setup -qn %{name}-%{commit}


%build
export OCAMLPATH=
## override the hardcoded piqi version to be the same as the package version
echo "%{version}" | sed 's/^v//' > VERSION
./configure --prefix=/usr
make deps
make
make -C doc


%check
. ./setenv.sh
make -C tests


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1 \
		%{_builddir}/%{buildsubdir}/doc/piqi.1


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/piqi
%{_mandir}/man1/piqi.1.gz
%doc doc/*.html


%changelog

* Thu Nov 14 2013 Anton Lavrik <alavrik@piqi.org> 0.6.5-2
- Cosmetic changes

* Thu Nov 7 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.5-1
- Bump upstream 0.6.4 -> 0.6.5

* Fri Apr 21 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.4-1
- Bump upstream 0.6.3 -> 0.6.4

* Fri Apr 15 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-4
- Stand-alone HTML documentation files

* Fri Apr 15 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-3
- Remove patch "default values in record definitions"
- Add documentation
- Add manual page

* Fri Apr 5 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-2
- [patch] Default values in record definitions

* Fri Apr 5 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-1
- Initial version with /usr/bin/piqi and /usr/bin/piqic
