%global commit 73ca0cf4e6a735979069e52f9ffae7e0a522b26b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		piqi
Version:	0.6.3
Release:	1%{?dist}
Summary:	Set of languages and open-source tools for working with structured data.

License:	ASL 2.0
URL:		http://piqi.org
Source0:	https://github.com/alavrik/piqi/archive/%{commit}/%{name}-v%{version}-%{shortcommit}.tar.gz

#https://github.com/alavrik/piqi/pull/28
Patch0:		piqi-0.6.3-destdir.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-findlib
# Required for 'make check'
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

    - Piqi -- a powerful data definition language. It is specially designed to be
      used with Piq, but also works as a schema language for other data formats
      including JSON, XML and Protocol Buffers binary format. Tools for
      validating, pretty-printing and converting data between Piq, JSON, XML and
      Protocol Buffers binary format.

    - Piqi-RPC -- an RPC-over-HTTP system for Erlang. It provides a simple way to
      expose Erlang services via JSON, XML and Google Protocol Buffers over
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
%patch0 -p1

%build
export OCAMLPATH=
./configure --prefix=/usr
make deps
make

%check
. ./setenv.sh
make -C tests

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/piqi
%{_bindir}/piqic

%doc


%changelog

