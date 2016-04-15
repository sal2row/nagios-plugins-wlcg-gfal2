#!/bin/sh
ver=$1
if [ -z "$ver" ] ; then
        echo "Specify version!"
        exit 1
fi
specver=`grep 'Version:' nagios-plugins-wlcg-gfal2.spec | cut -d' ' -f2`
if [ "$specver" != $ver ] ; then
        echo "Spec file not updated!"
        exit 1
fi

user=`whoami`


rm -rf tmp/nagios-plugins-wlcg-gfal2-$ver
mkdir -p tmp/nagios-plugins-wlcg-gfal2-$ver

cp -a org.atlas tmp/nagios-plugins-wlcg-gfal2-$ver
cp -a org.atlas/config tmp/nagios-plugins-wlcg-gfal2-$ver

cd tmp
for f in `find nagios-plugins-wlcg-gfal2-$ver -name .svn`;do rm -rf $f;done
for f in `find nagios-plugins-wlcg-gfal2-$ver -name *.pyo`;do rm -f $f;done
for f in `find nagios-plugins-wlcg-gfal2-$ver -name *.pyc`;do rm -f $f;done

tar zcf nagios-plugins-wlcg-gfal2-$ver.tgz nagios-plugins-wlcg-gfal2-$ver
mv nagios-plugins-wlcg-gfal2-$ver.tgz ../SOURCES/
mkdir -p /tmp/${user}/BUILD
mkdir -p /tmp/${user}/SRPMS

cd ..
rpmbuild --define "_source_filedigest_algorithm md5"  --define "_binary_filedigest_algorithm md5" --define 'dist .el6' --buildroot /tmp/${user}/buildroot --target noarch -bs nagios-plugins-wlcg-gfal2.spec

# get release number from the spec file
release=`grep Release nagios-plugins-wlcg-gfal2.spec | awk '{ print $2 }' | cut -d"%" -f 1`

mkdir -p BUILD
cp /tmp/${user}/SRPMS/nagios-plugins-wlcg-gfal2-${ver}-${release}.el6.src.rpm BUILD/

if [ $? -eq 0 ];
then
  echo 
  echo "RPM built and copied into `pwd`/BUILD"
else
  echo "Something went wrong with the RPM building..."
fi
