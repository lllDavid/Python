import torch
from torch import nn
from pathlib import Path

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class Model(nn.Module):
    pass

model = Model()
MODEL_PATH = Path("saved_models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "Model.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

print(f"Saving model to: {MODEL_SAVE_PATH}")
torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)

loaded_model_1 = Model(3)
loaded_model_1.load_state_dict(torch.load(MODEL_SAVE_PATH,weights_only=True))
loaded_model_1.to(device)