# NOTE: this package is NoSource because the file is _enormous_,
#	and I don't want to pollute distfiles with it - baggins

%define		packname	BSgenome.Hsapiens.UCSC.hg19

Summary:	Homo sapiens (Human) full genome (UCSC version hg19)
Name:		R-%{packname}
Version:	1.3.19
Release:	1
License:	Artistic 2.0
Group:		Applications/Science
Source0:	http://bioconductor.org/packages/release/data/annotation/src/contrib//%{packname}_%{version}.tar.gz
# NoSource0-md5:	d8cc70ba24b9c320ca45c3dc56f5f9b2
NoSource:	0
URL:		http://bioconductor.org/packages/release/bioc/html/Biobase.html
BuildRequires:	R
BuildRequires:	R-BSgenome >= 1.25.4
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BSgenome >= 1.25.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Homo sapiens (Human) full genome as provided by UCSC (hg19, Feb. 2009)
and stored in Biostrings objects.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/UnitTests/
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/ExpressionSet
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/Code
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/testClass.R
%{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
