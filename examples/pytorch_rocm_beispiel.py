#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ein einfaches Beispiel zur Überprüfung der PyTorch ROCm-Unterstützung
"""

import torch
import sys

def main():
    # Grundlegende PyTorch-Informationen anzeigen
    print(f"PyTorch Version: {torch.__version__}")
    print(f"CUDA verfügbar: {torch.cuda.is_available()}")
    
    # ROCm-spezifische Informationen
    if hasattr(torch, 'version') and hasattr(torch.version, 'hip') and torch.version.hip is not None:
        print(f"ROCm Version: {torch.version.hip}")
        print("HIP/ROCm ist verfügbar")
    else:
        print("HIP/ROCm ist NICHT verfügbar")
        print("PyTorch wurde möglicherweise ohne ROCm-Unterstützung kompiliert.")
        print("Installieren Sie PyTorch mit ROCm-Unterstützung:")
        print("pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4")
        return
    
    # GPU-Informationen anzeigen
    if torch.cuda.is_available():
        print(f"\nAnzahl verfügbarer GPUs: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        
        # Einfachen Tensor auf der GPU erstellen und berechnen
        print("\nEinfacher Test mit einem GPU-Tensor:")
        x = torch.randn(3, 3).cuda()
        y = torch.randn(3, 3).cuda()
        z = x @ y  # Matrixmultiplikation
        print(f"Input Tensor x:\n{x}")
        print(f"Input Tensor y:\n{y}")
        print(f"Ergebnis z = x @ y:\n{z}")
        
        # Zurück zur CPU kopieren
        z_cpu = z.cpu()
        print(f"Ergebnis auf CPU kopiert:\n{z_cpu}")
    else:
        print("\nKeine GPU gefunden. Stellen Sie sicher, dass ROCm korrekt installiert ist.")

if __name__ == "__main__":
    main() 