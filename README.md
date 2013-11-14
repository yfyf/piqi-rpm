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

    make

The resulting binary and source RPM packages will be located here:

    RPMS/*/piqi-*.rpm
    SRPMS/piqi-*.src.rpm


Updating the package
--------------------

To update the package after a new Piqi version is released:

1. Set the `VERSION` and `COMMIT` variables in `./Makefile` to the new upstream
   version.
2. Edit the following sections in `piqi.spec`:
```
    %global commit <COMMIT>

    Version:	<VERSION>

    Release:	1%{?dist}

    %changelog
```

