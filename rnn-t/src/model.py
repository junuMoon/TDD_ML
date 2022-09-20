import torch.nn as nn
import torch
class Encoder(nn.Module):

    def __init__(self, num_inputs, output_dim, hidden_state_dim=64) -> None:
        super().__init__()
        self.rnn = nn.GRU(num_inputs, hidden_state_dim, batch_first=True)
        self.fc = nn.Linear(hidden_state_dim, output_dim)

    def forward(self, x):
        output, _ = self.rnn(x)
        return self.fc(output)

