%define ibm_release .1

Name:       ginger
Version:    2.3.0
Release:    2%{?dist}
Summary:    Host management plugin for Wok - Webserver Originated from Kimchi
BuildRoot:  %{_topdir}/BUILD/%{name}-%{version}-%{release}
Group:      System Environment/Base
License:    LGPL/ASL2
Source0:    %{name}.tar.gz
BuildArch:  noarch
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libxslt
Requires:   gettext >= 0.17
Requires:   wok >= 2.1.0
Requires:   ginger-base
Requires:   libuser-python
Requires:       libvirt
Requires:   python-ethtool
Requires:   python-ipaddr
Requires:   python-magic
Requires:   python-netaddr
Requires:   python-augeas
Requires:	python2-crypto
Requires:       libvirt-python


%description
Ginger is a host management plugin for Wok (Webserver Originated from Kimchi),
that provides an intuitive web panel with common tools for configuring and
operating Linux systems. Kimchi is a Wok plugin for managing KVM/Qemu virtual
machines.

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%global with_systemd 1
%endif

%prep
%setup -n %{name}


%build
./autogen.sh --system
make


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf $RPM_BUILD_ROOT


%post
%if 0%{?with_systemd}
	install -dm 0755 %{_unitdir}/wokd.service.requires
	ln -sf ../tuned.service %{_unitdir}/wokd.service.requires
%endif


%postun
%if 0%{?with_systemd}
	if [ $1 == 0 ]; then # uninstall
		rm -f %{_unitdir}/wokd.service.requires/tuned.service
	fi
%endif

%posttrans
%if 0%{?with_systemd}
	if [ $1 == 0 ]; then # upgrade
		if ! [ -f %{_unitdir}/wokd.service.requires ]; then
			ln -sf ../tuned.service %{_unitdir}/wokd.service.requires
		fi
		/bin/systemctl daemon-reload >/dev/null 2>&1 || :
		service wokd restart
	fi
%endif


%files
%attr(-,root,root)
%dir %{python_sitelib}/wok/plugins/ginger
%{python_sitelib}/wok/plugins/ginger/*.py*
%{python_sitelib}/wok/plugins/ginger/API.json
%dir %{python_sitelib}/wok/plugins/ginger/control
%{python_sitelib}/wok/plugins/ginger/control/*.py*
%dir %{python_sitelib}/wok/plugins/ginger/model
%{python_sitelib}/wok/plugins/ginger/model/*.py*
%{_prefix}/share/locale/*/LC_MESSAGES/ginger.mo
%dir %{_datadir}/wok/plugins/ginger/ui
%dir %{_datadir}/wok/plugins/ginger/ui/config
%{_datadir}/wok/plugins/ginger/ui/config/tab-ext.xml
%dir %{_datadir}/wok/plugins/ginger/ui/css
%{_datadir}/wok/plugins/ginger/ui/css/ginger.css
%dir %{_datadir}/wok/plugins/ginger/ui/css/base
%dir %{_datadir}/wok/plugins/ginger/ui/css/base/images
%{_datadir}/wok/plugins/ginger/ui/css/base/images/*.gif
%{_datadir}/wok/plugins/ginger/ui/css/base/images/*.png
%dir %{_datadir}/wok/plugins/ginger/ui/images
%{_datadir}/wok/plugins/ginger/ui/images/*.svg
%dir %{_datadir}/wok/plugins/ginger/ui/js
%{_datadir}/wok/plugins/ginger/ui/js/*.js
%dir %{_datadir}/wok/plugins/ginger/ui/pages
%{_datadir}/wok/plugins/ginger/ui/pages/i18n.json.tmpl
%{_datadir}/wok/plugins/ginger/ui/pages/*.html.tmpl
%dir %{_datadir}/wok/plugins/ginger/ui/pages/help
%{_datadir}/wok/plugins/ginger/ui/pages/help/ginger-help.css
%dir %{_datadir}/wok/plugins/ginger/ui/pages/help/en_US
%dir %{_datadir}/wok/plugins/ginger/ui/pages/help/pt_BR
%dir %{_datadir}/wok/plugins/ginger/ui/pages/help/zh_CN
%{_datadir}/wok/plugins/ginger/ui/pages/help/en_US/*.html
%{_datadir}/wok/plugins/ginger/ui/pages/help/pt_BR/*.html
%{_datadir}/wok/plugins/ginger/ui/pages/help/zh_CN/*.html
%dir %{_datadir}/wok/plugins/ginger/ui/pages/tabs
%{_datadir}/wok/plugins/ginger/ui/pages/tabs/*.html.tmpl
%{_sysconfdir}/wok/plugins.d/ginger.conf
%{_sysconfdir}/systemd/system/wokd.service.d/ginger.conf


%changelog
* Wed Oct 26 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 2.3.0-2
- ed6b5cc Updating ginger.css to latest versions
e7c45de Introducing OSA port & Buffer count functionalities
13ad599 Introducing OSA port & Buffer count functionalities
35af4b2 Removing commented code in ui/js/host-network-vlan.js
26e977b Issue #450 : Seperate the buttons from datatable configuration for Network Configuration.
884bb3d Issue #448 iSCSI get operation on invalid IQN fails with 500
03f01c6 Improve error message propagation in Filesystems
0beaf4e Modified the network code to support OPTIONS in ifcfg file.
bac7977 Changed volumn to volume in ui/pages/i18n.json.tmpl
58bc368 Changed message for delete partition if VG name exist
11c0910 Fixed Issue #449 Loading icon is always visible while creating partition
42cab03 For FC and Iscsi devices while creating partition pass device ID as parameter to API
648ab0a Fix for the size slider in storage devices.
1f52e1f Check for file path for create swap API
7d7a850 Issue #226: Show GiB instead of g for Volume Group sizes
6920356 Issue #442 DASD create partition API does not give an error for more than 3 partitions
4dca998 This patch removes a repeated key key in the dictionary
1baf499 Improving Swap Device Partition listing
1e3aaec Issue # 437 :Volume Group list is not getting refreshed post deletion of volume group.

* Wed Oct 05 2016 user - 2.2.0-7
- 3c049fb Returning rows_indexes as part of ginger.listNetworkConfig object.
831a43b Issue #414: service disapear after stopping it at opensuse 42.1
5fec64a Updating po files
4ba7319 Update changelog for 2.3.0
fbbde90 Changing version to 2.3.0
af9e56c ChangeLog and VERSION changes for 2.3.0-rc1
a706dae Fixing is_feature_available method of model/graph.py

* Thu Sep 29 2016 Olav Philipp Henschel <olavph@linux.vnet.ibm.com> - 2.2.0-6
- a706dae Fixing is_feature_available method of model/graph.py
75f30e6 Issue # 61 :Add Adapter button missing in Host -> Network tab.
b621d55 Issue #412: python-pygraphviz not listed as dependency
6268db6 Fix build process
012673b Fix make-rpm target
551d9cf Issue #413: spec asks for python2-crypto on opensuse 42.1, which does not exists
a3a1149 Issue #433: refactor rpm building
923861a Moving Platform Management data to state_dir
5e4f120 Issue #403 - Make system services UI more failproof
b4f7875 Makefile.am: CLEANFILES must clean pyc files
b4bac12 Issue #381: make clean does not revert its changes from make rpm
fe2566a Fix PEP8 issues
90bff39 Issue # 430 :UI displays blank in Volume Group list when checking more details for selected vg.

* Thu Sep 22 2016 user - 2.2.0-5
- 90bff39 Issue # 430 :UI displays blank in Volume Group list when checking more details for selected vg.
6395b8b Fixes on tests/test_graph.py:
c092063 Issue #384 : Fixing the broken /ginger/stgdevs API
81bc523 Issue #418 : Disable iscsi target discovery auth methods for individual IQNs
af5f9b7 Issue #415 : Disable auth for iSCSI target and initiator selectively
937e083 Added columns in detailed report for graph creation.
ad3318b Implemented audit graph backend.
d38b15f Issue #389 : iSCSI Auth model class loading fix
086765c Update functionalities for Platform Management

* Wed Sep 07 2016 user - 2.2.0-3.pkvm3_1_1
- 086765c Update functionalities for Platform Management
30cefe3 UT implemented for the new features implemented.
fbd22ff Audit graph backend implemetation.
0fc004a Audit predefined rules backend implementation.
e093afb Updated docs and i18n.py for the new features implemented.
d4101d1 Backend code implemented to get list of system calls.
c1d2fd7 Audit report implementation from the backend.
630bfae Audit log implementation from the backend.
bdea605 Audit conf implemented in the backend.
1c528ad Modified audit rules code for comments and added new features.
fe4324f Issue #166 : nfs mount fails with 500
ee3d989 Backend Changes for Sensor Data Records for Platform Management
670ff8c [HostOS] Revert Introducing iSCSI implementation for Storage devices

* Thu Sep 01 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 2.2.0-2.pkvm3_1_1
- Build August, 31st, 2016

* Wed Aug 24 2016 <baseuser@ibm.com>
  Log from git:
- 4b9924f023099d28c919e55e0834860ca8342d06 Issue #381: 'make clean' does not revert its changes from 'make rpm'
- 6fec29c3ecbf857a8cd3199cc8fcf3eb038e1ffa Capabilities API: get current feature state
- 2b9565f2887b38789b957fe4fed1b4f6ce4d160e Make all is_feature_available methods static
- 317d4d73265759802a2c498d86791f76e2a6bec4 Fixing miscellaneous issues in swap functionalities
- 6c73928647a85b998e0122a66469741a3c55ee48 Fixing miscellaneous issues in swap functionalities
- 10af984cf47d9f0cfd7abbaa2a2a509a3efa8e4d Add missing user request log messages
- 762e2e98de6d9d9bcb9901d7a5852f55493b1723 Remove duplicated entry
- 4826f3b56e33ee7f803506856840e4b75c7d0176 Revert "Use past verbs and other log message improvements"
- 56b0aaa70d386eda6a6b168d1637081a4ea461ee Move audit error messages along to correct section
- 260e87bcf63e35bac328a438fe64f912984d1aaa Ginger control: import control classes using sub_node
- 9bd9ee1f293d76c7d684b637362e21bd41db84a8 test/test_authorization.py: test changes after urlsubnode change
- ba0c0862aabd02ace16cd3fb07588ff3723b7b8b Removing control/nfsshares.py file
- 5affd694999fb83e6e566b9cd14044db7fa9c96a Control classes: fixing @UrlSubNode calls
- a1054c215ad1ebef319227dfdcc57255013d661e Issue #372 : Add support for target rescan
- 0efe8265ecbd70750875125f5ead7bded5019578 docs/API.md : adding configuration backup APIs
- 3fac3f0b38bdfb506d3ef957ff8d3162e0b7be8f docs/API.md: removing duplicated ibm_sep entry
- 3988eabb242f6524e0db585185c7424056e35f10 Introducing Volume Group related operations.
- 6df0850a73c26a499b63609b778e735ca7bba03b Introducing Volume group related operations.
- 17cca53e5f7d3df3f2d44fa6794467e63ba59398 Introducing Volume group related operations.
- 597159efa472e0c797484e96fc8013d500485c45 Update stringutils imports
- fb9b53d74e81bdc83eaaf49617813cd396ce3740 Issue #377 : Full Width and Arabic digits not accepted for batch delete of config backup
- e4beb6d74b8302f593028713190e52d2eea4af79 Revert "Globalisation support - externalize all remaining strings for ginger plugin."
- 3b3a91bb64f19692800f348df96b9e1a70f0a3ff Issue #372 : Add support to target authentication
- 7a762e61e808f8ba5b4ff4a57fe3f84fc469b410 Globalisation support - externalize all remaining strings for ginger plugin.
- e79ead0fe695cffabbb051ff6fa51c06d11fcea5 Modify the info returned by partitions listing API
- 9dbae80e2eef671f482b8733bd6aa224c7957b09 Issue #375 :Fifteen Character VLAN device name not being recognized as a valid VLAN Interface name.
- 85317f0b8f3b68f0dced1115ef19057205af0c28 Issue #376:Unable to edit the text field or click submit/cancel after press ESC or click outside the error message dialog of Add User.
- 74182c95dc44ef83e5dcd0431a167ab3fd66e195 Time out while generating config back up file leave the tar file behind
- 9439806d811a7c2bbbb7907cb3ab507e65b3f212 Issue #372 : iSCSI Discovery and IQN actions support
- a84c1c51b07da6e763f19653b884df55bd222d4a Audit rules backend: new tests file test_rules
- 617cf532691b23c51a09d7ecdcbd303552c560f7 Audit rules backend: changes in controls, ginger.py and model/model.py
- bbeea7b374749ab5539db3859900b1f452c252c9 Audit rules backend: API doc and i18n.py changes.
- ebce57e2d0461d215422a9b5c9ba69c63d48f4ea Audit rules backend: new model/rules.py module
- a1e3df94a82457c6e8e2b8e810904537220ee1fa Introducing File system related operations.
- 26e08586e2f0b8901b5f7efe2d40016026f34b7c Introducing File system related operations.
- f93c2f6c4bf242cad45e43fb77ab1b43d056fd28 Introducing File system related operations.
- b85b15f732d2ad442597696faf903351f93bbcad Extend Filesystem mounting to include mount options
- 4de6c1454ace270454c6fec08c923c03ae072c10 Added cursor for tasks in progress
- e3d52545c4b6fa49dc4489f39d4ffdac663fbd99 Improvements on Configuration Backup UI
- 670fdf8457768f01646fc9537b77025572f7b8c2 Github #94: OpenSUSE network support
- ba7623c6c47daef6bbe9ceaabbd5638a89db4e47 Implementation of Partition for storage devices
- 97f0d08f6a296eb789167edec53d6984ab07b2c5 Issue #371 : Create disk partitions takes integer input for size
- 4c1f481b48b6f52fe337a12e63330ef8f41117ae Github #121: WoK log flooded by hddtemp messages
- 84f43d5188892e30b39793d9c6e43d555f0ed88d Issue #300 : Redesign "Network Configuration" UI
- 4cb9b33e90d32d140b9db2545df4c8076531e330 Fixing wok_log redundancy and i18n.py error messages
- 681174296d5c0f70ff8609e82e24921ec3edbbc1 Fixing wok_log redundancy and i18n.py error messages
- aea7709b8e2d8c5fadd5ee164a1b56e95aee8e38 Fixing wok_log redundancy and i18n.py error messages
- 32f2841ca3e893f1346b4210b922bebcf89ebc07 Fixing wok_log redundancy and i18n.py error messages
- 930c71db18c3bdeabc98580679696fe81db448cd Issue #299: Redesign "Global Network Configuration" UI
- 3529cd987e7d7202b94771882337b94e3efd54a6 Removing debug info from model/users.py

* Tue Jul 12 2016 Daniel Henrique Barboza <danielhb@linux.vnet.ibm.com>
- Added 'dir' directives for each dir and subdir in the 'files' section
- rpmlint fixes

* Tue May 31 2016 Ramon Medeiros <ramonn@linux.vnet.ibm.com>
- Update spec with Fedora community Guidelines

* Mon May 16 2016 Ramon Medeiros <ramonn@linux.vnet.ibm.com>
- Does not disable tuned service as dependency when update package

* Wed Mar 23 2016 Daniel Henrique Barboza <dhbarboza82@gmail.com>
- Removed 'pyparted' from dependencies because it is a Ginger-base dependency
- Removed 'python-cheetah' from build dependencies
- Added wok version restriction >= 2.1.0

* Tue Mar 1 2016 Daniel Henrique Barboza <dhbarboza82@gmail.com>
- added ui/images/*.svg in 'files' section

* Sat Feb 6 2016 Chandra Shekhar Reddy Potula <chandra@linux.vnet.ibm.com>
- Add libvirt service dependencies to Ginger

* Mon Jan 25 2016 Daniel Henrique Barboza <dhbarboza82@gmail.com>
- Changed 'controls' dir to 'control' in 'files' section
- Added 'datadir'/wok/plugins/ginger/ui/pages/*.html.tmpl to 'files'
- Changed 'models' dir to 'model' in 'files' section

* Fri Dec 25 2015 Daniel Henrique Barboza <dhbarboza82@gmail.com>
- Changed 'files' to include all ui/js/*.js js files
- Changed 'files' to include all ui/pages/help/*/*.html help files
- Changed 'files' to include all ui/pages/tabs/*.html.tmpl tabs

* Wed Dec 16 2015 Daniel Henrique Barboza  <dhbarboza82@gmail.com>
- Removed 'host-admin.css' from 'files'
- added 'ui/js/ginger-bootgrid.js' in 'files'

* Fri Dec 11 2015 Daniel Henrique Barboza  <dhbarboza82@gmail.com>
- Added ui/pages/tabs/host-admin.html.tmpl to 'files'

* Fri Nov 27 2015 Chandra Shekhar Reddy Potula <chandra@linux.vnet.ibm.com>
- Add missing dependencies for Ginger

* Thu Oct 2 2014 Rodrigo Trujillo <rodrigo.trujillo@linux.vnet.ibm.com>
- Add Help pages for Ginger
- Change build system to enable and release Help pages

* Wed Jul  2 2014 Paulo Vital <pvital@linux.vnet.ibm.com> 1.2.1
- Changed the package name from kimchi-ginger to ginger

* Wed Apr 16 2014 Zhou Zheng Sheng <zhshzhou@linux.vnet.ibm.com> 1.2.0
- Initial release of Kimchi-ginger dedicated RPM package
