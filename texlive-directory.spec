Name:		texlive-directory
Version:	15878
Release:	1
Summary:	An address book using BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/directory
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/directory.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/directory.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for LaTeX and BibTeX that facilitates the
construction, maintenance and exploitation of an address book-
like database.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/directory/business.bib
%{_texmfdistdir}/bibtex/bib/directory/family.bib
%{_texmfdistdir}/bibtex/bst/directory/address-html.bst
%{_texmfdistdir}/bibtex/bst/directory/address-ldif.bst
%{_texmfdistdir}/bibtex/bst/directory/address-vcard.bst
%{_texmfdistdir}/bibtex/bst/directory/address.bst
%{_texmfdistdir}/bibtex/bst/directory/birthday.bst
%{_texmfdistdir}/bibtex/bst/directory/email-html.bst
%{_texmfdistdir}/bibtex/bst/directory/email.bst
%{_texmfdistdir}/bibtex/bst/directory/letter.bst
%{_texmfdistdir}/bibtex/bst/directory/phone.bst
%{_texmfdistdir}/tex/latex/directory/directory.sty
%doc %{_texmfdistdir}/doc/latex/directory/README
%doc %{_texmfdistdir}/doc/latex/directory/directory.pdf
%doc %{_texmfdistdir}/doc/latex/directory/directory.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
