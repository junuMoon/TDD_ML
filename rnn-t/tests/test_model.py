import pytest
import torch

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

