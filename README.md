# pkg-valhalla
RPM packaging of valhalla for Sailfish

Packages are made from the current github sources. Since SFOS provides
boost-1.51, the upstream requirements have been relaxed in Sailfish
branch at https://github.com/rinigus/valhalla/tree/sailfish . The
corresponding pull request is under review upstream (as of May 21,
2017).

# Download

```
git clone https://github.com/rinigus/valhalla.git
cd valhalla
git checkout sailfish
git submodule update --init --recursive 
```

# Build and install

```
export SFARCH=armv7hl
mb2 -t SailfishOS-$SFARCH -s ../rpm/valhalla.spec build
sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -i <INSERT-PATH>/valhalla*$SFARCH.rpm
```
