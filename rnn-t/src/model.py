import torch.nn as nn
import torch

class Encoder(nn.Module):

    def __init__(self, num_inputs, output_dim, hidden_state_dim=64) -> None:
        super().__init__()
        self.rnn = nn.GRU(num_inputs, hidden_state_dim)
        self.fc = nn.Linear(hidden_state_dim, output_dim)

    def forward(self, x):
        output, _ = self.rnn(x)
        return self.fc(output)

class Decoder(nn.Module):
    """The decoder is any causal network (= can't look at the future)"""

    def __init__(self, num_classes, output_dim, hidden_state_dim=64) -> None:
        super().__init__()
        self.emb = nn.Embedding(num_classes, hidden_state_dim)
        self.rnn = nn.RNN(hidden_state_dim, hidden_state_dim)
        self.fc = nn.Linear(hidden_state_dim, output_dim)
        
        self.initial_state = nn.Parameter(torch.randn(1, hidden_state_dim))

    def step(self, yi, prev_state):
        embedded = self.emb(yi)
        output, state = self.rnn.forward(embedded, prev_state)
        return output, state

    def forward(self, y):
        U = y.shape[1]
        g = []
        prev_state = self.initial_state
        for i in range(U):
            yi = y[:, i]
            g_u, prev_state = self.step(yi, prev_state)
            g.append(g_u)
        return torch.cat(g, dim=0)

class Joiner(nn.Module):

    def __init__(self, num_classes, joiner_dim) -> None:
        super().__init__()
        self.fc = nn.Linear(joiner_dim, num_classes)

    def forward(self, f, g):
        return self.fc(f+g)

