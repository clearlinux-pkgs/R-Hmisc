#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Hmisc
Version  : 4.2.0
Release  : 24
URL      : https://cran.r-project.org/src/contrib/Hmisc_4.2-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Hmisc_4.2-0.tar.gz
Summary  : Harrell Miscellaneous
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-Hmisc-lib = %{version}-%{release}
Requires: R-RColorBrewer
Requires: R-backports
Requires: R-data.table
Requires: R-gridExtra
Requires: R-latticeExtra
Requires: R-xfun
BuildRequires : R-Formula
BuildRequires : R-RColorBrewer
BuildRequires : R-acepack
BuildRequires : R-backports
BuildRequires : R-base64enc
BuildRequires : R-checkmate
BuildRequires : R-data.table
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-htmlTable
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-latticeExtra
BuildRequires : R-rstudioapi
BuildRequires : R-viridis
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
Hmisc
=====
Harrell Miscellaneous
Current Goals
=============
* Continue to refine the summaryX class of functions that replace tables with graphics
* See also bpplotM and tabulr
* See http://biostat.mc.vanderbilt.edu/HmiscNew

%package lib
Summary: lib components for the R-Hmisc package.
Group: Libraries

%description lib
lib components for the R-Hmisc package.


%prep
%setup -q -c -n Hmisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556474385

%install
export SOURCE_DATE_EPOCH=1556474385
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Hmisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Hmisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Hmisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Hmisc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Hmisc/CHANGELOG
/usr/lib64/R/library/Hmisc/DESCRIPTION
/usr/lib64/R/library/Hmisc/INDEX
/usr/lib64/R/library/Hmisc/Meta/Rd.rds
/usr/lib64/R/library/Hmisc/Meta/features.rds
/usr/lib64/R/library/Hmisc/Meta/hsearch.rds
/usr/lib64/R/library/Hmisc/Meta/links.rds
/usr/lib64/R/library/Hmisc/Meta/nsInfo.rds
/usr/lib64/R/library/Hmisc/Meta/package.rds
/usr/lib64/R/library/Hmisc/NAMESPACE
/usr/lib64/R/library/Hmisc/NEWS
/usr/lib64/R/library/Hmisc/R/Hmisc
/usr/lib64/R/library/Hmisc/R/Hmisc.rdb
/usr/lib64/R/library/Hmisc/R/Hmisc.rdx
/usr/lib64/R/library/Hmisc/THANKS
/usr/lib64/R/library/Hmisc/WISHLIST
/usr/lib64/R/library/Hmisc/help/AnIndex
/usr/lib64/R/library/Hmisc/help/Hmisc.rdb
/usr/lib64/R/library/Hmisc/help/Hmisc.rdx
/usr/lib64/R/library/Hmisc/help/aliases.rds
/usr/lib64/R/library/Hmisc/help/paths.rds
/usr/lib64/R/library/Hmisc/html/00Index.html
/usr/lib64/R/library/Hmisc/html/R.css
/usr/lib64/R/library/Hmisc/tests/Ecdf.r
/usr/lib64/R/library/Hmisc/tests/ace.s
/usr/lib64/R/library/Hmisc/tests/american-medical-association.csl
/usr/lib64/R/library/Hmisc/tests/areg.s
/usr/lib64/R/library/Hmisc/tests/aregImpute.r
/usr/lib64/R/library/Hmisc/tests/aregImpute2.r
/usr/lib64/R/library/Hmisc/tests/aregImpute3.r
/usr/lib64/R/library/Hmisc/tests/aregImpute4.r
/usr/lib64/R/library/Hmisc/tests/bootkm.r
/usr/lib64/R/library/Hmisc/tests/consolidate.R
/usr/lib64/R/library/Hmisc/tests/csv/FORMAT.csv
/usr/lib64/R/library/Hmisc/tests/csv/TEST.csv
/usr/lib64/R/library/Hmisc/tests/csv/_contents_.csv
/usr/lib64/R/library/Hmisc/tests/cut2.r
/usr/lib64/R/library/Hmisc/tests/dataframeReduce.r
/usr/lib64/R/library/Hmisc/tests/describe.Rmd
/usr/lib64/R/library/Hmisc/tests/dotchartpl.r
/usr/lib64/R/library/Hmisc/tests/examples.Rmd
/usr/lib64/R/library/Hmisc/tests/fit.mult.impute.bootstrap.r
/usr/lib64/R/library/Hmisc/tests/fit.mult.impute.r
/usr/lib64/R/library/Hmisc/tests/gbayes.r
/usr/lib64/R/library/Hmisc/tests/histSpike.r
/usr/lib64/R/library/Hmisc/tests/histSpikeg.r
/usr/lib64/R/library/Hmisc/tests/hoeff.r
/usr/lib64/R/library/Hmisc/tests/howto.html
/usr/lib64/R/library/Hmisc/tests/html-summaryM.r
/usr/lib64/R/library/Hmisc/tests/html.data.frame.r
/usr/lib64/R/library/Hmisc/tests/html.summaryM.Rmd
/usr/lib64/R/library/Hmisc/tests/inverseFunction.r
/usr/lib64/R/library/Hmisc/tests/label.r
/usr/lib64/R/library/Hmisc/tests/largest.empty.r
/usr/lib64/R/library/Hmisc/tests/latex-color.r
/usr/lib64/R/library/Hmisc/tests/latex-html.Rmd
/usr/lib64/R/library/Hmisc/tests/latex.s
/usr/lib64/R/library/Hmisc/tests/latex.summaryM.Rnw
/usr/lib64/R/library/Hmisc/tests/latexTabular.r
/usr/lib64/R/library/Hmisc/tests/latexTherm.Rnw
/usr/lib64/R/library/Hmisc/tests/latexTherm.r
/usr/lib64/R/library/Hmisc/tests/latexpng.r
/usr/lib64/R/library/Hmisc/tests/mChoice.r
/usr/lib64/R/library/Hmisc/tests/minor.tick.r
/usr/lib64/R/library/Hmisc/tests/panelbp.r
/usr/lib64/R/library/Hmisc/tests/plot.summaryM.plotly.r
/usr/lib64/R/library/Hmisc/tests/procmeans.txt
/usr/lib64/R/library/Hmisc/tests/rcspline.plot.r
/usr/lib64/R/library/Hmisc/tests/readsasxml.r
/usr/lib64/R/library/Hmisc/tests/redun.r
/usr/lib64/R/library/Hmisc/tests/simRegOrd.r
/usr/lib64/R/library/Hmisc/tests/summary.formula.r
/usr/lib64/R/library/Hmisc/tests/summary.formula.response.stratify.r
/usr/lib64/R/library/Hmisc/tests/summaryD.r
/usr/lib64/R/library/Hmisc/tests/summaryM-customtest.r
/usr/lib64/R/library/Hmisc/tests/summaryP.r
/usr/lib64/R/library/Hmisc/tests/summaryP2.r
/usr/lib64/R/library/Hmisc/tests/summaryRc.r
/usr/lib64/R/library/Hmisc/tests/summaryS.r
/usr/lib64/R/library/Hmisc/tests/summarySp.r
/usr/lib64/R/library/Hmisc/tests/test.rda
/usr/lib64/R/library/Hmisc/tests/test.sas
/usr/lib64/R/library/Hmisc/tests/test.xml
/usr/lib64/R/library/Hmisc/tests/test.xpt
/usr/lib64/R/library/Hmisc/tests/test2.xpt
/usr/lib64/R/library/Hmisc/tests/testexportlib.r
/usr/lib64/R/library/Hmisc/tests/testexportlib.sas
/usr/lib64/R/library/Hmisc/tests/upData.r
/usr/lib64/R/library/Hmisc/tests/wtd.r
/usr/lib64/R/library/Hmisc/tests/xYplotFilledBands.r
/usr/lib64/R/library/Hmisc/todo

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Hmisc/libs/Hmisc.so
/usr/lib64/R/library/Hmisc/libs/Hmisc.so.avx2
/usr/lib64/R/library/Hmisc/libs/Hmisc.so.avx512
