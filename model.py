import torch
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

class WiFiThreatModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(5, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 2)
        )
    def forward(self, x):
        return self.net(x)

def detect_threat(file="wifi6_packets.csv"):
    df = pd.read_csv(file).fillna("unknown")
    le = LabelEncoder()
    for col in ['mac_src', 'mac_dst']:
        df[col] = le.fit_transform(df[col])
    X = StandardScaler().fit_transform(df[['mac_src', 'mac_dst', 'signal_strength', 'pkt_type', 'pkt_subtype']])
    model = WiFiThreatModel().cuda()
    X_tensor = torch.tensor(X, dtype=torch.float32).cuda()
    with torch.no_grad():
        preds = model(X_tensor)
        results = torch.argmax(preds, dim=1).cpu().numpy()
    df['threat'] = results
    df.to_csv(file, index=False)
    return df