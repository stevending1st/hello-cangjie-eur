Name:           hello-cangjie-eur
Version:        0.0.5
Release:        1%{?dist}
Summary:        Cangjie Eur demo.
License:        MIT
Source:         https://github.com/stevending1st/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  wget, dnf-plugins-core, binutils, glibc-devel, gcc-c++, openssl

%description
A demo for Cangjie and Eur.

%global debug_package %{nil}

# 根据环境设置下载地址
%ifarch x86_64
# 这里的指令仅在 x86_64 架构下运行
   %global download_url "https://cangjie-lang.cn/v1/files/auth/downLoad?nsId=142267&fileName=Cangjie-0.53.13-linux_x64.tar.gz&objectKey=6719f1eb3af6947e3c6af327"
%endif

%ifarch aarch64 armv7hl armv7l
# 这里的指令仅在 ARM 架构下运行（这里包括了32位和64位）
   %global download_url "https://cangjie-lang.cn/v1/files/auth/downLoad?nsId=142267&fileName=Cangjie-0.53.13-darwin_aarch64.tar.gz&objectKey=6719f1b33af6947e3c6af322"
%endif


%prep
%autosetup -n %{name}-%{version}

%build
cd %{_builddir}

# 检查文件是否存在，并设置一个宏
if [ ! -f %{_builddir}/Cangjie-0.53.13-linux.tar.gz ]; then
   wget -O Cangjie-0.53.13-linux.tar.gz %{download_url}
fi

tar xvf Cangjie-0.53.13-linux.tar.gz


%install
cd %{_builddir}/%{name}-%{version}
rm -rf %{_buildrootdir}/*
source %{_builddir}/cangjie/envsetup.sh
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
