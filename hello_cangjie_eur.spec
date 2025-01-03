Name:           hello-cangjie-eur
Version:        v0.0.4
Release:        1%{?dist}
Summary:        Cangjie Eur demo.
License:        MIT
Source:         https://gitee.com/stevending1st/%{name}/repository/blazearchive/%{version}.tar.gz

BuildRequires:  wget, dnf-plugins-core, binutils, glibc-devel, gcc-c++, openssl

%description
A demo for Cangjie and Eur.


%global debug_package %{nil}

# 检查文件是否存在，并设置一个宏
%global file_exists 0
if [ ! -f %{_builddir}/Cangjie-0.53.13-linux_x64.tar.gz ]; then
   %global file_not_exists 1
else
   %global file_not_exists 0
fi


%prep
%setup -q

%build
cd %{_builddir}

%if %{file_not_exists}
  wget -O Cangjie-0.53.13-linux_x64.tar.gz "https://cangjie-lang.cn/v1/files/auth/downLoad?nsId=142267&fileName=Cangjie-0.53.13-linux_x64.tar.gz&objectKey=6719f1eb3af6947e3c6af327"
%endif

tar xvf Cangjie-0.53.13-linux_x64.tar.gz
source %{_builddir}/cangjie/envsetup.sh


%install
cd %{_builddir}/%{name}-%{version}
rm -rf %{_buildrootdir}
cjpm install --root %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}


%clean
rm -rf %{buildroot}


%files
# %license add-license-file-here
# %doc add-docs-here
/bin/hello_cangjie_eur
%exclude /.packages.toml


%changelog
* Thu Jan 02 2025 stevending1st <stevending1st@163.com>
Project init. 
