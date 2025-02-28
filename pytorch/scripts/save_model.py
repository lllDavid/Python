from pathlib import Path
import torch

MODEL_PATH = Path("saved_models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "AnimalCNNModel.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

print(f"Saving model to: {MODEL_SAVE_PATH}")
torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)

loaded_model_1 = AnimalCNNModel(3)
loaded_model_1.load_state_dict(torch.load(MODEL_SAVE_PATH,weights_only=True))
loaded_model_1.to(device)