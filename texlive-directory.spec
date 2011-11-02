Name:		texlive-directory
Version:	1.20
Release:	1
Summary:	An address book using BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/directory
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/directory.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/directory.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package for LaTeX and BibTeX that facilitates the
construction, maintenance and exploitation of an address book-
like database.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
