# Meanwhile Tears

[![Join the chat at https://gitter.im/pavgup/meanwhile-sametime-tears](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pavgup/meanwhile-sametime-tears?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/pavgup/meanwhile-sametime-tears.svg)](https://travis-ci.org/pavgup/meanwhile-sametime-tears)
[![Coverity Status](https://scan.coverity.com/projects/7115/badge.svg)](https://scan.coverity.com/projects/pavgup-meanwhile-sametime-tears)[![Coverage Status](https://coveralls.io/repos/pavgup/meanwhile-sametime-tears/badge.svg?branch=master&service=github)](https://coveralls.io/github/pavgup/meanwhile-sametime-tears?branch=master)

This project intends to extend meanwhile (the open source sametime protocol implementation) with fixes (destined for the upstream project) and, perhaps more importantly, a set of server-side utilities to obviate the need for client-side tools.  Christopher (siege) O'Brien <siege@preoccupied.net> is the current meanwhile maintainer and a ton of awesome people have made the suffering associated with IBM's incredibly persistent notes abomination liveable. Free software kind of rocks and in that spirit, importantly, I'm choosing to exclusively license this code using GNU's most-stringent copy-left license: AGPL 3.0.

### Baselining Meanwhile 1.1.0 Library
This initial baseline contains as many publically available patches as I could stumble into from a variety of sources (ubuntu, debian, upstream, github users, etc.).  Honestly, finding a consistent baseline for this library has been surprisingly hard, so here's to hoping I have something that looks like the latest and greatest 1.1.0 meanwhile implementation.  Here's to that always being true.

### Building Meanwhile Tears on OS X 10.11
For the moment this code compiles and runs smoothly on my OSX 10.11 El Capitan macbook pro, but that's not to say you will have success just yet. A little CI will help keep building this project under control more broadly.  The INSTALL file has information that worked for me, but I hope to deprecate that in favor of a short set of blips in this readme.

### Moving from LGPL 2.0 (old and busted) to AGPL 3.0 (new hotness)
The upstream meanwhile project is licensed under the antiquated GNU Library General Public License 2.0.  Within that context the FSF intended to allow proprietary users an exception to use libraries without exposing their source.  This update to AGPL 3.0 intends to very specifically suggest the use of this project should always constitute the disclosure of source code.  IANAL, but if I'm to understand Stallman correctly, lets try to all help the world.

Installation
------------
Almost nothing but a macbook pro running a beta variant of xcode and osx has provably run this codebase.  I suspect it will compile very broadly, however.
### Version: Arsenic (0.1.0-alpha)

The major versino will just correspond to the first letter of an amusing common-name.  Semantic versioning and all being considerd.
## OS X using Homebrew!
Pre-requisites first (probably incomplete -- maybe xcode is required):
```sh
$ brew install glib automake libtool pkg-config doxygen git
```
Grab the code:
```sh
$ git clone https://github.com/pavgup/meanwhile-sametime-tears.git
$ cd meanwhile-sametime-tears
```
Now build this!
```sh
$ ./autogen.sh
$ make
```
### Elsewhere?  You'll likely find success, but I've yet to test elsewhere.
Soon, linux will be tested (at least Debian/Ubuntu where strong meanwhile patches are maintained).  Maybe I'll give this a whirl on a Windows machine some day.

Development and Contribution
----------------------------
Lots of opensource projects make contribution daunting. It's a wee bit dispiriting. I know they're all super busy, but I'm not.  I'm nothing fancy and you're probably fancier than I am.  Feel free to take what I've done and feel free to build into this space cleverly too.  If you've never written a line of code before, well, I was there, you can try your hand here.  The bottom-line is that contribution is welcome and the source is strictly open to all.
### Arsenic Goals
 - Open IBM Sametime Backend Server
 - Consolidate and triage meanwhile protocol issues
 - Drop in a quick angularjs chat implementation
 - Unclose Sametime; Connect Services

License
--
AGPL 3.0 - Open Source All The Things
