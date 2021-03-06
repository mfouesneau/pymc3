#   Copyright 2020 The PyMC Developers
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from theano.tensor import Constant as tensor_constant
from theano.gof.graph import Constant as graph_constant


__all__ = [
    "bool_types",
    "int_types",
    "float_types",
    "complex_types",
    "continuous_types",
    "discrete_types",
    "typefilter",
    "isgenerator",
    "theano_constant",
]

bool_types = set(["int8"])

int_types = set(
    ["int8", "int16", "int32", "int64", "uint8", "uint16", "uint32", "uint64"]
)
float_types = set(["float32", "float64"])
complex_types = set(["complex64", "complex128"])
continuous_types = float_types | complex_types
discrete_types = bool_types | int_types

string_types = str


def typefilter(vars, types):
    # Returns variables of type `types` from `vars`
    return [v for v in vars if v.dtype in types]


def isgenerator(obj):
    return hasattr(obj, "__next__")


theano_constant = (tensor_constant, graph_constant)
