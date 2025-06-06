#!/usr/bin/env python3
#
# File   : types.py
# Author : Hang Gao
# Email  : hangg.sv7@gmail.com
#
# Copyright 2022 Adobe. All rights reserved.
#
# This file is licensed to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR REPRESENTATIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from typing import Any, Callable, Tuple, Union

# import jax.numpy as np
import numpy as np


PRNGKey = np.ndarray
Shape = Tuple[int]
Dtype = Any
Array = Union[np.ndarray, np.ndarray]

Activation = Callable[[Array], Array]
Initializer = Callable[[PRNGKey, Shape, Dtype], Array]

PathType = str
ScheduleType = Callable[[int], float]
EngineType = Any
