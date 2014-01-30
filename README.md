This repository contains scripts for building an RPM package for the `piqi`
command-line tool.

The package includes:

1. `/usr/bin/piqi`
2. `PIQI(1)` man page
3. HTML documentation (also available online at [http://piqi.org/doc/](http://piqi.org/doc/))


Build prerequisites
-------------------

Install the following packages:

    yum install ocaml ocaml-camlp4-devel ocaml-findlib

    # for building documentation and running tests
    yum install pandoc protobuf-devel


Building the package
--------------------

0. Optional: if your `rpm --version` is `=< 4.11.0` then modify `Makefile` to
   use explicit `VERSION` and `COMMIT` variables, which should match
   the ones in the `piqi.spec`.

1. Simply run:

    make

The resulting binary and source RPM packages will be located here:

    RPMS/*/piqi-*.rpm
    SRPMS/piqi-*.src.rpm


Updating the package
--------------------

To update the package after a new Piqi version is released, edit the following
sections in `piqi.spec`:

```
    %global commit <COMMIT>

    Version:	<VERSION>

    Release:	1%{?dist}

    %changelog
```
