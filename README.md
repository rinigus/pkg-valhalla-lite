# pkg-valhalla-lite

RPM packaging of Valhalla C++ API for Sailfish. This version packages 
Valhalla as a library that is usable via `actor_t` C++ API. 

# Build and install

```
export SFARCH=armv7hl
mb2 -t SailfishOS-$SFARCH -s ../rpm/valhalla.spec build
sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -i <INSERT-PATH>/valhalla*$SFARCH.rpm
```
