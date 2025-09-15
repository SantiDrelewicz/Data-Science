import torch.nn as nn

class AutoEncoder(nn.Module):
    def __init__(self, latent_dim):
        super().__init__()
        self.latend_dim = latent_dim
        # usando nn.Sequential definan las capas del stacked autoencoder, 
        # tanto en el encoder, como en el decoder
        self.encoder = 
        self.decoder = 

    def forward(self, x):
        x = x.view(len(x), -1)
        # COMPLETAR AQUI
        
        ############################
        x = x.view(len(x), 1, 28, 28)
        return x