# ===============================================================================
# Copyright 2015 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================
from __future__ import absolute_import

import os

from git import Repo

from pychron.dvc import repository_path
from pychron.paths import paths


def list_local_repos():
    for i in os.listdir(paths.repository_dataset_dir):
        if i.startswith('.'):
            continue
        elif i.startswith('~'):
            continue

        d = repository_path(i)
        if os.path.isdir(d):
            gd = os.path.join(d, '.git')
            if os.path.isdir(gd):
                r = Repo(d)
                if r.branches:
                    yield i, r.active_branch.name
# ============= EOF =============================================



