MogileFS loader backend for thumbor
-----------
Copyright &copy; 2014 Max Oberberger (max@oberbergers.de)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

* * *

### Installation

To install the MogileFS loader backend, mv the mogilefs_loader.py to the
loader directory of thumbor.

Example:

    mv loaders/mogilefs_loader.py /usr/local/lib/python2.7/dist-packages/thumbor/loaders/


### Configuration

To use it at thumbor enable it as a loader:

    ## The loader thumbor should use to load the original image. This must be the
    ## full name of a python module (python must be able to import it)
    ## Defaults to: thumbor.loaders.http_loader
    LOADER = 'thumbor.loaders.mogilefs_loader'

and add the following settings for your loader:

    MOGILEFS_STORAGE_DOMAIN = 'YOUR_DOMAIN'
    MOGILEFS_STORAGE_TRACKERS = [ 'TRACKER1:PORT', 'TRACKER2:PORT' ]
