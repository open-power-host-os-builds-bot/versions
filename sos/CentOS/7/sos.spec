%global commit          %{?git_commit_id}
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gitcommittag    .git%{shortcommit}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: A set of tools to gather troubleshooting information from a system
Name: sos
Version: 3.4
Release: 1%{?extraver}%{gitcommittag}%{?dist}
Group: Applications/System
Source0: %{name}.tar.gz
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/sos
BuildRequires: python-devel
BuildRequires: python-sphinx
BuildRequires: gettext
BuildRequires: python-six
Requires: libxml2-python
Requires: rpm-python
Requires: tar
Requires: bzip2
Requires: xz
Requires: python-six

%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
%find_lang %{name} || echo 0

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(-, root, root, -)
%{_sbindir}/sosreport
%{_datadir}/%{name}
%{python_sitelib}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%doc AUTHORS README.md LICENSE
%doc /usr/share/doc/sos/html
%config(noreplace) %{_sysconfdir}/sos.conf

%changelog
* Fri Aug 25 2017 OpenPOWER Host OS Builds Bot <open-power-host-os-builds-bot@users.noreply.github.com> - 3.4-1.git
- Version update
- Updating to 8523982 [sos] bump version to 3.4

* Mon Aug 14 2017 Olav Philipp Henschel <olavph@linux.vnet.ibm.com> - 3.3-20.git
- Bump release

* Mon Aug 07 2017 Fabiano Rosas <farosas@linux.vnet.ibm.com> - 3.3-19.git
- Add extraver macro to Release field

* Thu Nov 3 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 3.3-18
- Spec cleanup

* Tue Aug 30 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 3.3-17.1
- Build August, 24th, 2016

* Wed Jul 13 2016 baseuser <baseuser@us.ibm.com> = 3.3
- 52dd1dbc52783e622ca0a96e3e9c182bb26887fe sos: Decrease sos timeout from 300 to 180 sec
- b4bb649d64b62051893fa22803205b30fd6cc84b IBM branding
- ecdb6e46c26bab4eba86370befe041bbe8586bfd [sos] bump version to 3.3
- dc37f9f720863cc981447e491fb470260e6636e0 [origin] New plugin for OpenShift Origin / OSE 3.x
- c72f2e1f3a13713a9902a8ee42857d124ff72933 [kubernetes] fix string substitution
- 047a207b8f3d90ac8e4223cec0b6de44c1a36611 [kubernetes] new data, namespace support, and options
- d3cb5416571cd04d0a8e5025075d016259460c97 [Plugin] Add mechanism to remove certificates and keys from output
- c6d0d286a00afd0e5e8bad95249740e00904caa0 [lxd] Use add_copy_spec_limit
- 5e4991f3d9b3b9356e6a3e1551adf9ce753a03e2 [reporting] html_report skips plugins .. with nonASCII
- 4522d11c2f4478ead563bfbb34b0c834b9326301 [gdm] Fix misspelled units
- c5e1bd7410eaf2deeb9267eeffef8bb9d151b5e8 [tomcat] Added collection of all tomcat* logs
- f2d8b81061fa55a686b30e3303d27aa92bde036f [gluster] limit size of logs collected
- e0dbf5957623764118d6f05e10611a941a5985cc [policies/redhat] update container detection test
- 1fd12690870e85e8ac83b0e99bb272ce4489dc60 [reporting] deal with UTF-8 characters
- b523592d69b4eebd23a83a06ff3df7d906ddd95f [lightdm] Add missing "" to command
- fde5809bc2a2c3993060d70ce17e3007f6308df9 [processor] Capture turbostat output
- 25ab9f3a25337343d00f01abe6c187c062e89c5d [memory] Capture status of hugepages
- 00d9f31d19518661fafd80f03b3f1598a14b08ef [block] Capture the scheduler used by all block devices
- 6c8147ca297937e0b7b1407bafb7f2548b7a3e12 [ipmi] Fix ipmitool options
- 8e82c10c05e0e2c36554de394d979a32ed0ae924 [pacemaker] Call crm_report with --sos-mode option

* Tue Sep 30 2014 Bryn M. Reeves <bmr@redhat.com> = 3.2
- New upstream release

* Wed Sep 17 2014 Bryn M. Reeves <bmr@redhat.com> = 3.2-beta1
- New upstream beta release

* Thu Jun 12 2014 Bryn M. Reeves <bmr@redhat.com> = 3.2-alpha1
- New upstream alpha release

* Mon Jan 27 2014 Bryn M. Reeves <bmr@redhat.com> = 3.1-1
- New upstream release

* Mon Jun 10 2013 Bryn M. Reeves <bmr@redhat.com> = 3.0-1
- New upstream release

* Thu May 23 2013 Bryn M. Reeves <bmr@redhat.com> = 2.2-39
- Always invoke tar with '-f-' option
  Resolves: bz966602

* Mon Jan 21 2013 Bryn M. Reeves <bmr@redhat.com> = 2.2-38
- Fix interactive mode regression when --ticket unspecified
  Resolves: bz822113

* Fri Jan 18 2013 Bryn M. Reeves <bmr@redhat.com> = 2.2-37
- Fix propagation of --ticket parameter in interactive mode
  Resolves: bz822113

* Thu Jan 17 2013 Bryn M. Reeves <bmr@redhat.com> = 2.2-36
- Revert OpenStack patch
  Resolves: bz840057

* Wed Jan  9 2013 Bryn M. Reeves <bmr@redhat.com> = 2.2-35
- Report --name and --ticket values as defaults
  Resolves: bz822113
- Fix device-mapper command execution logging
  Resolves: bz824378
- Fix data collection and rename PostreSQL module to pgsql
  Resolves: bz852049

* Fri Oct 19 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-34
- Add support for content delivery hosts to RHUI module
  Resolves: bz821323

* Thu Oct 18 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-33
- Add Red Hat Update Infrastructure module
  Resolves: bz821323
- Collect /proc/iomem in hardware module
  Resolves: bz840975
- Collect subscription-manager output in general module
  Resolves: bz825968
- Collect rhsm log files in general module
  Resolves: bz826312
- Fix exception in gluster module on non-gluster systems
  Resolves: bz849546
- Fix exception in psql module when dbname is not given
  Resolves: bz852049

* Wed Oct 17 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-32
- Collect /proc/pagetypeinfo in memory module
  Resolves: bz809727
- Strip trailing newline from command output
  Resolves: bz850433
- Add sanlock module
  Resolves: bz850779
- Do not collect archived accounting files in psacct module
  Resolves: bz850542
- Call spacewalk-debug from rhn module to collect satellite data
  Resolves: bz859142

* Mon Oct 15 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-31
- Avoid calling volume status when collecting gluster statedumps
  Resolves: bz849546
- Use a default report name if --name is empty
  Resolves: bz822113
- Quote tilde characters passed to shell in RPM module
  Resolves: bz821005
- Collect KDC and named configuration in ipa module
  Resolves: bz825149
- Sanitize hostname characters before using as report path
  Resolves: bz822174
- Collect /etc/multipath in device-mapper module
  Resolves: bz817093
- New plug-in for PostgreSQL
  Resolves: bz852049
- Add OpenStack module
  Resolves: bz840057
- Avoid deprecated sysctls in /proc/sys/net
  Resolves: bz834594
- Fix error logging when calling external programs
  Resolves: bz824378
- Use ip instead of ifconfig to generate network interface lists
  Resolves: bz833170

* Wed May 23 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-29
- Collect the swift configuration directory in gluster module
  Resolves: bz822442
- Update IPA module and related plug-ins
  Resolves: bz812395

* Fri May 18 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-28
- Collect mcelog files in the hardware module
  Resolves: bz810702

* Wed May 02 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-27
- Add nfs statedump collection to gluster module
  Resolves: bz752549

* Tue May 01 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-26
- Use wildcard to match possible libvirt log paths
  Resolves: bz814474

* Mon Apr 23 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-25
- Add forbidden paths for new location of gluster private keys
  Resolves: bz752549

* Fri Mar  9 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-24
- Fix katello and aeolus command string syntax
  Resolves: bz752666
- Remove stray hunk from gluster module patch
  Resolves: bz784061

* Thu Mar  8 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-22
- Correct aeolus debug invocation in CloudForms module
  Resolves: bz752666
- Update gluster module for gluster-3.3
  Resolves: bz784061
- Add additional command output to gluster module
  Resolves: bz768641
- Add support for collecting gluster configuration and logs
  Resolves: bz752549

* Wed Mar  7 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-19
- Collect additional diagnostic information for realtime systems
  Resolves: bz789096
- Improve sanitization of RHN user and case number in report name
  Resolves: bz771393
- Fix verbose output and debug logging
  Resolves: bz782339
- Add basic support for CloudForms data collection
  Resolves: bz752666
- Add support for Subscription Asset Manager diagnostics
  Resolves: bz752670

* Tue Mar  6 2012 Bryn M. Reeves <bmr@redhat.com> = 2.2-18
- Collect fence_virt.conf in cluster module
  Resolves: bz760995
- Fix collection of /proc/net directory tree
  Resolves: bz730641
- Gather output of cpufreq-info when present
  Resolves: bz760424
- Fix brctl showstp output when bridges contain multiple interfaces
  Resolves: bz751273
- Add /etc/modprobe.d to kernel module
  Resolves: bz749919
- Ensure relative symlink targets are correctly handled when copying
  Resolves: bz782589
- Fix satellite and proxy package detection in rhn plugin
  Resolves: bz749262
- Collect stderr output from external commands
  Resolves: bz739080
- Collect /proc/cgroups in the cgroups module
  Resolve: bz784874
- Collect /proc/irq in the kernel module
  Resolves: bz784862
- Fix installed-rpms formatting for long package names
  Resolves: bz767827
- Add symbolic links for truncated log files
  Resolves: bz766583
- Collect non-standard syslog and rsyslog log files
  Resolves: bz771501
- Use correct paths for tomcat6 in RHN module
  Resolves: bz749279
- Obscure root password if present in anacond-ks.cfg
  Resolves: bz790402
- Do not accept embedded forward slashes in RHN usernames
  Resolves: bz771393
- Add new sunrpc module to collect rpcinfo for gluster systems
  Resolves: bz784061

* Tue Nov  1 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-17
- Do not collect subscription manager keys in general plugin
  Resolves: bz750607

* Fri Sep 23 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-16
- Fix execution of RHN hardware.py from hardware plugin
  Resolves: bz736718
- Fix hardware plugin to support new lsusb path
  Resolves: bz691477

* Fri Sep 09 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-15
- Fix brctl collection when a bridge contains no interfaces
  Resolves: bz697899
- Fix up2dateclient path in hardware plugin
  Resolves: bz736718

* Mon Aug 15 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-14
- Collect brctl show and showstp output
  Resolves: bz697899
- Collect nslcd.conf in ldap plugin
  Resolves: bz682124

* Sun Aug 14 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-11
- Truncate files that exceed specified size limit
  Resolves: bz683219
- Add support for collecting Red Hat Subscrition Manager configuration
  Resolves: bz714293
- Collect /etc/init on systems using upstart
  Resolves: bz694813
- Don't strip whitespace from output of external programs
  Resolves: bz713449
- Collect ipv6 neighbour table in network module
  Resolves: bz721163
- Collect basic cgroups configuration data
  Resolves: bz729455

* Sat Aug 13 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-10
- Fix collection of data from LVM2 reporting tools in devicemapper plugin
  Resolves: bz704383
- Add /proc/vmmemctl collection to vmware plugin
  Resolves: bz709491

* Fri Aug 12 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-9
- Collect yum repository list by default
  Resolves: bz600813
- Add basic Infiniband plugin
  Resolves: bz673244
- Add plugin for scsi-target-utils iSCSI target
  Resolves: bz677124
- Fix autofs plugin LC_ALL usage
  Resolves: bz683404
- Fix collection of lsusb and add collection of -t and -v outputs
  Resolves: bz691477
- Extend data collection by qpidd plugin
  Resolves: bz726360
- Add ethtool pause, coalesce and ring (-a, -c, -g) options to network plugin
  Resolves: bz726427

* Thu Apr 07 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-8
- Use sha256 for report digest when operating in FIPS mode
  Resolves: bz689387

* Tue Apr 05 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-7
- Fix parted and dumpe2fs output on s390
  Resolves: bz622784

* Fri Feb 25 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-6
- Fix collection of chkconfig output in startup.py
  Resolves: bz659467
- Collect /etc/dhcp in dhcp.py plugin
  Resolves: bz676522
- Collect dmsetup ls --tree output in devicemapper.py
  Resolves: bz675559
- Collect lsblk output in filesys.py
  Resolves: bz679433

* Thu Feb 24 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-4
- Fix collection of logs and config files in sssd.py
  Resolves: bz624162
- Add support for collecting entitlement certificates in rhn.py
  Resolves: bz678665

* Thu Feb 03 2011 Bryn M. Reeves <bmr@redhat.com> = 2.2-3
- Fix cluster plugin dlm lockdump for el6
  Resolves: bz622407
- Add sssd plugin to collect configuration and logs
  Resolves: bz624162
- Collect /etc/anacrontab in system plugin
  Resolves: bz622527
- Correct handling of redhat-release for el6
  Resolves: bz622528

* Thu Jul 29 2010 Adam Stokes <ajs at redhat dot com> = 2.2-2
- Resolves: bz582259
- Resolves: bz585942
- Resolves: bz584253
- Resolves: bz581817

* Thu Jun 10 2010 Adam Stokes <ajs at redhat dot com> = 2.2-0
- Resolves: bz581921
- Resolves: bz584253
- Resolves: bz562651
- Resolves: bz566170
- Resolves: bz586450
- Resolves: bz588223
- Resolves: bz559737
- Resolves: bz586405
- Resolves: bz598978
- Resolves: bz584763

* Wed Apr 28 2010 Adam Stokes <ajs at redhat dot com> = 2.1-0
- Resolves: bz585923
- Resolves: bz585942
- Resolves: bz586409
- Resolves: bz586389
- Resolves: bz548096
- Resolves: bz557828
- Resolves: bz563637
- Resolves: bz584253
- Resolves: bz462823
- Resolves: bz528881
- Resolves: bz566170
- Resolves: bz578787
- Resolves: bz581817
- Resolves: bz581826
- Resolves: bz584695
- Resolves: bz568637
- Resolves: bz584767
- Resolves: bz586370

* Mon Apr 12 2010 Adam Stokes <ajs at redhat dot com> = 2.0-0
- Resolves: bz580015

* Tue Mar 30 2010 Adam Stokes <ajs at redhat dot com> = 1.9-3
- fix setup.py to autocompile translations and man pages
- rebase 1.9

* Fri Mar 19 2010 Adam Stokes <ajs at redhat dot com> = 1.9-2
- updated translations

* Thu Mar 04 2010 Adam Stokes <ajs at redhat dot com> = 1.9-1
- version bump 1.9
- replaced compression utility with xz
- strip threading/multiprocessing
- simplified progress indicator
- pylint update
- put global vars in class container
- unittests
- simple profiling
- make use of xgettext as pygettext is deprecated

* Mon Jan 18 2010 Adam Stokes <ajs at redhat dot com> = 1.8-21
- more sanitizing options for log files
- rhbz fixes from RHEL version merged into trunk
- progressbar update

* Thu Nov 19 2009 Adam Stokes <ajs at redhat dot com> = 1.8-20
- dont copy unwanted files due to symlinks
- More plugin enhancements

* Thu Nov 5 2009 Adam Stokes <ajs at redhat dot com> = 1.8-18
- Option to enable selinux fixfiles check
- Start of replacing Thread module with multiprocessing
- Update translations
- More checks against conf file versus command line opts

* Wed Sep 9 2009 Adam Stokes <ajs at redhat dot com> = 1.8-16
- Update rh-upload-core to rh-upload and allows general files
- Fix cluster plugin with pwd mangling invalidating xml
- Cluster support detecting invalid fence_id and fence states
- Read variables from conf file

* Thu Jul 23 2009 Adam Stokes <ajs at redhat dot com> = 1.8-14
- resolves: rhbz512536 wrong group in spec file
- resolves: rhbz498398 A series of refactoring patches to sos
- resolves: rhbz501149 A series of refactoring patches to sos (2)
- resolves: rhbz503804 remove obsolete translation
- resolves: rhbz502455 tricking sosreport into rm -rf /
- resolves: rhbz501146 branding in fedora

* Mon Jul 20 2009 Adam Stokes <ajs at redhat dot com> = 1.8-13
- Add requirements for tar,bzip2 during minimal installs
- More merges from reports against RHEL version of plugins
- Remove unecessary definition of localdir in spec

* Tue May 05 2009 Adam Stokes <ajs at redhat dot com> - 1.8-11
- Remove all instances of sysrq
- Consistent macro usage in spec

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Adam Stokes <ajs at redhat dot com> - 1.8-5
- removed source defines as python manifest handles this

* Fri Dec 19 2008 Adam Stokes <ajs at redhat dot com> - 1.8-4
- spec cleanup, fixed license, source
- reworked Makefile to build properly

* Thu Oct 23 2008 Adam Stokes <astokes at redhat dot com> - 1.8-1
- Resolves: bz459845 collect krb5.conf
- Resolves: bz457880 include output of xm list and xm list --long
- Resolves: bz457919 add support for openswan and ipsec-tools
- Resolves: bz456378 capture elilo configuration
- Resolves: bz445007 s390 support
- Resolves: bz371251 hangs when running with a xen kernel where xend has not been started
- Resolves: bz452705 Add /root/anaconda-ks-cfg to sosreport archive
- Resolves: bz445510 Do not rely on env to execute python
- Resolves: bz446868 add support for emc devices
- Resolves: bz453797 fails to generate fdisk -l
- Resolves: bz433183 does not collect ext3 information
- Resolves: bz444838 systool is passed deprecated arguments
- Resolves: bz455096 add %{INSTALLTIME:date} to rpm --qf collection
- Resolves: bz332211 avoid hazardous filenames

* Wed Nov 21 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.8-0
- Resolves: bz368261 sosGetCommandOutput() does not block on hung processes
- Resolves: bz361861 work-around missing traceback.format_exc() in RHEL4
- Resolves: bz394781 device-mapper: use /sbin/lvm_dump to collect dm related info
- Resolves: bz386691 unattended --batch option
- Resolves: bz371251 sos could hang when accessing /sys/hypervisor/uuid
- selinux: always collect sestatus
- added many languages
- added --debug option which causes exceptions not to be trapped
- updated to sysreport-1.4.3-13.el5
- ftp upload to dropbox with --upload
- cluster: major rewrite to support different versions of RHEL
- cluster: check rg_test for errors
- minor changes in various plug-ins (yum, networking, process, kernel)
- fixed some exceptions in threads which were not properly trapped
- veritas: don't run rpm -qa every time
- using rpm's python bindings instead of external binary
- corrected autofs and ldap plugin that were failing when debug option was not found in config file.
- implemented built-in checkdebug() that uses self.files and self.packages to make the decision
- missing binaries are properly detected now.
- better doExitCode handling
- fixed problem with rpm module intercepting SIGINT
- error when user specifies an invalid plugin or plugin option
- named: fixed indentation
- replaced isOptionEnabled() with getOption()
- tune2fs and fdisk were not always run against the correct devices/mountpoint
- added gpg key to package
- updated README with new svn repo and contributors
- updated manpage
- better signal handling
- caching of rpm -q outputs
- report filename includes rhnUsername if available
- report encryption via gpg and support pubkey
- autofs: removed redundant files
- filesys: better handling of removable devices
- added sosReadFile() returns a file's contents
- return after looping inside a directory
- collect udevinfo for each block device
- simply collect output of fdisk -l in one go
- handle sysreport invocation properly (warn if shell is interactive, otherwise spawn sysreport.legacy)
- progress bar don't show 100% until finished() is called
- Resolves: bz238778 added lspci -t
- now runs on RHEL3 as well (python 2.2)
- replaced commonPrefix() with faster code
- filesys: one fdisk -l for all
- selinux: collect fixfilex check output
- devicemapper: collect udevinfo for all block devices
- cluster: validate node names according to RFC 2181
- systemtap: cleaned up and added checkenabled() method
- added kdump plugin
- added collection of /etc/inittab
- Resolves: bz332151 apply regex to case number in sysreport for RHEL4
- Resolves: bz332211 apply regex to case number in sysreport for RHEL5
- Resolves: bz400111 sos incorrectly reports cluster data in SMP machine

* Mon Aug 13 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-8
- added README.rh-upload-core

* Mon Aug 13 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-7
- Resolves: bz251927 SOS errata needs to be respin to match 4.6 code base
- added extras/rh-upload-core script from David Mair <dmair@redhat.com>

* Thu Aug  9 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-6
- more language fixes
- added arabic, italian and french
- package prepared for release
- included sysreport as sysreport.legacy

* Thu Aug  9 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-5
- package obsoletes sysreport and creates a link pointing to sosreport
- added some commands in cluster and process plugins
- fixed html output (wrong links to cmds, thanks streeter)
- process: back down sleep if D state doesn't change
- Resolves: bz241277 Yum Plugin for sos
- Resolves: bz247520 Spelling mistake in sosreport output
- Resolves: bz247531 Feature: plugin to gather initial ramdisk scripts
- Resolves: bz248252 sos to support language localization
- Resolves: bz241282 Make SOS for RHEL 4

* Wed Aug  1 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-4
- catch KeyboardInterrupt when entering sosreport name
- added color output for increased readability
- list was sorted twice, removing latter .sort()

* Tue Jul 31 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-3
- added preliminary problem diagnosis support
- better i18n initialization
- better user messages
- more progressbar fixes
- catch and log python exceptions in report
- use python native commands to create symlinks
- limit concurrent running threads

* Sat Jul 28 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-2
- initial language localization support
- added italian translation

* Mon Jul 16 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-1
- split up command outputs in sub-directories (sos_command/plugin/command instead of sos_command/plugin.command)
- fixed doExitCode() calling thread.wait() instead of join()
- curses menu is disabled by default
- multithreading is enabled by default
- major progressbar changes (now has ETA)
- multithreading fixes
- plugins class descriptions shortened to fix better in --list-plugins
- rpm -Va in plugins/rpm.py sets eta_weight to 200 (plugin 200 longer than other plugins, for ETA calculation)
- beautified command output filenames in makeCommandFilename()

* Thu Jul 12 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-0
- curses menu disabled by default (enable with -c)
- sosreport output friendlier to the user (and similar to sysreport)
- smarter plugin listing which also shows options and disable/enabled plugins
- require root permissions only for actual sosreport generation
- fix in -k where option value was treated as string instead of int
- made progressbar wider (60 chars)
- selinux plugin is enabled only if selinux is also enabled on the system
- made some errors less verbose to the user
- made sosreport not copy files pointed by symbolic links (same as sysreport, we don't need /usr/bin/X or /sbin/ifup)
- copy links as links (cp -P)
- added plugin get_description() that returns a short decription for the plugin
- guess sosreport name from system's name

* Thu Jul  5 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-5
- Yet more fixes to make package Fedora compliant.

* Thu Jul  5 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-4
- More fixes to make package Fedora compliant.

* Mon Jul  2 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-3
- Other fixes to make package Fedora compliant.

* Mon Jul  2 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-2
- Minor fixes.

* Mon Jul  2 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-1
- Beautified output of --list-plugins.
- GPL licence is now included in the package.
- added python-devel requirement for building package
- Resolves: bz241282 fixed incompatibility with python from RHEL4

* Fri May 25 2007 Steve Conklin <sconklin at redhat dot com> - 1.5-1
- Bumped version

* Fri May 25 2007 Steve Conklin <sconklin at redhat dot com> - 1.4-2
- Fixed a backtrace on nonexistent file in kernel plugin (thanks, David Robinson)

* Mon Apr 30 2007 Steve Conklin <sconklin at redhat dot com> - 1.4-1
- Fixed an error in option handling
- Forced the file generated by traceroute to not end in .com
- Fixed a problem with manpage
- Added optional traceroute collection to networking plugin
- Added clalance's patch to gather iptables info.
- Fixes to the device-mapper plugin
- Fixed a problem with installation of man page

* Mon Apr 16 2007 Steve Conklin <sconklin at redhat dot com> - 1.3-3
- including patches to fix the following:
- Resolves: bz219745 sosreport needs a man page
- Resolves: bz219667 sosreport does not terminate cleanly on ^C
- Resolves: bz233375 Make SOS flag the situation when running on a fully virtu...
- Resolves: bz234873 rhel5 sos needs to include rpm-va by default
- Resolves: bz219669 sosreport multi-threaded option sometimes fails
- Resolves: bz219671 RFE for sosreport - allow specification of plugins to be run
- Resolves: bz219672 RFE - show progress while sosreport is running
- Resolves: bz219673 Add xen information gathering to sosreport
- Resolves: bz219675 Collect information related to the new driver update model
- Resolves: bz219877 'Cancel' button during option selection only cancels sele...

* Tue Feb 20 2007 John Berninger <jwb at redhat dot com> - 1.3-2
- Add man page

* Fri Dec 15 2006 Steve Conklin <sconklin at redhat dot com> - 1.3-1
- really fixed bz_219654

* Fri Dec 15 2006 Steve Conklin <sconklin at redhat dot com> - 1.2-1
- fixed a build problem

* Fri Dec 15 2006 Steve Conklin <sconklin at redhat dot com> - 1.1-1
- Tighten permissions of tmp directory so only readable by creator bz_219657
- Don't print message 'Problem at path ...'  bz_219654
- Removed useless message bz_219670
- Preserve file modification times bz_219674
- Removed unneeded message about files on copyProhibitedList bz_219712

* Wed Aug 30 2006 Steve Conklin <sconklin at redhat dot com> - 1.0-1
- Seperated upstream and RPM versioning

* Mon Aug 21 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-11
- Code cleanup, fixed a regression in threading

* Mon Aug 14 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-10
- minor bugfixes, added miltithreading option, setup now quiet

* Mon Jul 17 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-9
- migrated to svn on 108.redhat.com, fixed a problem with command output linking in report

* Mon Jun 19 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-6
- Added LICENSE file containing GPL

* Wed May 31 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-5
- Added fixes to network plugin and prepped for Fedora submission

* Wed May 31 2006 John Berninger <jwb at redhat dot com> - 0.1-4
- Reconsolidated subpackages into one package per discussion with sconklin

* Mon May 22 2006 John Berninger <jwb at redhat dot com> - 0.1-3
- Added ftp, ldap, mail, named, samba, squid SOS plugins
- Fixed various errors in kernel and hardware plugins

* Mon May 22 2006 John Benringer <jwb at redhat dot com> - 0.1-2
- split off cluster plugin into subpackage
- correct file payload lists

* Mon May 22 2006 John Berninger <jwb at redhat dot com> - 0.1-1
- initial package build
