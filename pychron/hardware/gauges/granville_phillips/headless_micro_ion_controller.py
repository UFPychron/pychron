# ===============================================================================
# Copyright 2017 Jake Ross
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
# =============enthought library imports=======================
# =============standard library imports ========================

# =============local library imports  ==========================
from __future__ import absolute_import
from pychron.hardware.core.headless.core_device import HeadlessCoreDevice
from pychron.hardware.gauges.granville_phillips.base_micro_ion_controller import BaseMicroIonController


class HeadlessMicroIonController(BaseMicroIonController, HeadlessCoreDevice):
    pass

# ============= EOF ====================================
