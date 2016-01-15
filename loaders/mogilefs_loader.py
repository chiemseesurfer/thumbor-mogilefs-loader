#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Max Oberberger (max@oberbergers.de)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from pymogile import Client
from tornado.concurrent import return_future

@return_future
def load(context, path, callback):
    domain = context.config.MOGILEFS_STORAGE_DOMAIN
    trackers = context.config.MOGILEFS_STORAGE_TRACKERS
    storage = Client(domain=domain, trackers=trackers)

    if not storage.get_file_data(path):
        return callback(None)
    return callback(storage.get_file_data(path))
