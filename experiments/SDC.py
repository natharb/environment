#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Nathalia Batista <nathbapt@decom.fee.unicamp.br>
# Fri  28 Set 17:00:00 2018
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Shifted Delta Coefficients for language/accent recognition"""

import numpy
import bob.ap
from .. import utils

import logging
logger = logging.getLogger("bob.bio.spear")

from bob.bio.base.extractor import Extractor


class SDC(Cepstral):

     """Extract shifted delta coefficients"""

    def __init__(
            self,
            win_length_ms=20.,  # 20 ms
            win_shift_ms=10.,  # 10 ms
            n_filters=40,
            f_min=0.0,  # 0 Hz
            f_max=8000,  # 8 KHz - this is an important value. Normally it should be half of the sampling frequency
            pre_emphasis_coef=1.0,
            mel_scale=False,
            rect_filter=False,
            inverse_filter=False,
            delta_win=2,
            n_ceps=19,  # 0-->18,
            dct_norm=False,
            d= 1,
            p= 3,
            k= 7,
            with_delta=True,
            with_delta_delta=False,
            with_energy=False,
            normalize_spectrum=False,
            keep_only_deltas=True,
            log_filter=True,
            energy_filter=False,
            vad_filter="no_filter",  # we do apply any trim filter by default
            normalize_feature_vector = False,
            **kwargs
    ):
        # call base class constructor with its set of parameters
        Extractor.__init__(
            self,
            requires_training=False, split_training_data_by_client=False,
            **kwargs
        )
        # copy parameters
        self.win_length_ms = win_length_ms
        self.win_shift_ms = win_shift_ms
        self.n_filters = n_filters
        self.f_min = f_min
        self.f_max = f_max
        self.pre_emphasis_coef = pre_emphasis_coef
        self.mel_scale = mel_scale
        self.rect_filter = rect_filter
        self.inverse_filter = inverse_filter
        self.delta_win = delta_win
        self.n_ceps = n_ceps
        self.dct_norm = dct_norm
        self.d = d
        self.p = p
        self.k = k
        self.with_delta = with_delta
        self.with_delta_delta = with_delta_delta
        self.with_energy = with_energy
        self.normalize_spectrum = normalize_spectrum
        self.keep_only_deltas = keep_only_deltas
        self.log_filter = log_filter
        self.energy_filter = energy_filter
        self.vad_filter = vad_filter
        self.normalize_feature_vector = normalize_feature_vector

        # compute the size of the feature vector
        self.features_len = self.n_ceps
        if self.with_delta:
            self.features_len += self.n_ceps
        if self.with_delta_delta:
            self.features_len += self.n_ceps


        def normalize_features(self, features):
        mean = numpy.mean(features, axis=0)
        std = numpy.std(features, axis=0)
        return numpy.divide(features-mean, std)


        def compute_ceps(self, rate, data):
    
        ceps = bob.ap.Ceps(rate, self.win_length_ms, self.win_shift_ms, self.n_filters, self.n_ceps, self.f_min,
                           self.f_max, self.delta_win, self.pre_emphasis_coef)
        ceps.dct_norm = self.dct_norm
        ceps.mel_scale = self.mel_scale
        ceps.rect_filter = self.rect_filter
        ceps.inverse_filter = self.inverse_filter
        ceps.with_energy = self.with_energy
        ceps.with_delta = self.with_delta
        ceps.with_delta_delta = self.with_delta_delta
        ceps.normalize_spectrum = self.normalize_spectrum
        ceps.log_filter = self.log_filter
        ceps.energy_filter = self.energy_filter

        cepstral_features = ceps(data)

        if self.keep_only_deltas:
            cepstral_features = cepstral_features[:, self.n_ceps:]
        return cepstral_features


        def shifted_delta_cepstral(cep, d, p, k):
        
        y = numpy.r_[numpy.resize(cep[0, :], (d, cep.shape[1])), cep, numpy.resize(cep[-1, :], (k * 3 + d, cep.shape[1]))]

        delta = self.with_delta
        sdc = numpy.empty((cep.shape[0], cep.shape[1] * k))

        idx = numpy.zeros(delta.shape[0], dtype='bool')
        for ii in range(k):
            idx[d + ii * p] = True
        for ff in range(len(cep)):
            sdc[ff, :] = delta[idx, :].reshape(1, -1)
            idx = numpy.roll(idx, 1)
        return numpy.hstack((cep, sdc))


        def _call_(self, input_data):
        
        ceps = self._call_(input_data)
        return shifted_delta_cepstral(ceps,d,p,k)
