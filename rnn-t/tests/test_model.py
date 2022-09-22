import pytest
import torch
import torch.nn.functional as  F
from src.model import Encoder, Decoder, Joiner


def test_encoder():
    seq_len = 10  # T
    input_dim = 8  # size of each input vector
    encoder_dim = 64 # E
    encoder_input_shape = (seq_len, input_dim)  # (T, D)
    encoder_output_shape = (seq_len, encoder_dim)  # (T, E)

    encoder = Encoder(num_inputs=input_dim, output_dim=encoder_dim)
    x = torch.rand(*encoder_input_shape)
    f = encoder(x)
    assert f.shape == encoder_output_shape

class TestDecoder:
    
    def setup(self):
        seq_len = 5  # U
        num_vocab = 4  # V: {v1, v2, v3, v4}
        decoder_dim = 64  # D

        self.decoder_input_shape = (seq_len+1, num_vocab+1)  # (U+1, V+1), V+1 because of the ∅ token and U+1 for the initial state
        self.decoder_output_shape = (seq_len+1, decoder_dim)  # (U+1, D)

        self.decoder = Decoder(num_classes=num_vocab+1, output_dim=decoder_dim)
        self.y = torch.randint(1, num_vocab, (seq_len+1, )).unsqueeze(0)  # (U+1, ), unsqueeze to add batch dimension
        self.y[0][0] = 0

    def test_one_step_forward(self):
        g0, _ = self.decoder.step(self.y[:, 0], self.decoder.initial_state)
        assert g0.shape == (1, self.decoder_output_shape[-1])

    def test_sequnce_forward(self):
        g = self.decoder(self.y)
        assert g.shape == self.decoder_output_shape
