# AMD ROCm KI-Umgebung mit Docker

Dieses Repository enthält eine Docker-Compose-Konfiguration für eine umfassende KI-Entwicklungsumgebung für AMD GPUs mit ROCm.

## Komponenten

- **Ollama**: LLM-Inferenz-Server für das Ausführen lokaler KI-Modelle
- **PyTorch mit ROCm**: Entwicklungsumgebung für PyTorch auf AMD GPUs
- **Jupyter Lab**: Interaktive Entwicklungsumgebung für ML/KI-Anwendungen

## Voraussetzungen

- Linux-System mit installiertem Docker und Docker Compose
- AMD GPU (getestet mit Radeon RX 6700 XT)
- AMD ROCm-Treiber (mindestens 5.4)
- Mindestens 16GB RAM empfohlen

## Installation

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/ChristianGruend/AMD-ROCm-KI-Umgebung.git
   cd amd-rocm-ki-umgebung
   ```

2. Starten Sie die Container:
   ```bash
   docker compose up -d
   ```

## Nutzung

### Ollama

Ollama ist über Port 11435 erreichbar. Sie können Modelle wie folgt herunterladen und verwenden:

```bash
curl -X POST http://localhost:11435/api/pull -d '{"name": "llama3"}'
```

### Jupyter Lab

Jupyter Lab ist über http://localhost:8888 erreichbar. Das Zugriffstoken ist `amd123`.

### PyTorch-Entwicklungsumgebung

Sie können auf die PyTorch-Entwicklungsumgebung zugreifen mit:

```bash
docker exec -it pytorch-amd bash
```

Innerhalb des Containers können Sie PyTorch installieren:

```bash
apt-get update && apt-get install -y python3-pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4
```

## Anpassungen

### GPU-Auswahl

Wenn Sie mehrere GPUs haben, können Sie die gewünschte GPU über die Umgebungsvariable `HIP_VISIBLE_DEVICES` auswählen. 0 ist die erste GPU.

### HSA-Version

Die Umgebungsvariable `HSA_OVERRIDE_GFX_VERSION` ist für ältere GPUs wichtig. Der Wert `10.3.0` ist für die RX 6700 XT geeignet.

## Fehlerbehebung

Bei Problemen mit der GPU-Erkennung:
1. Stellen Sie sicher, dass die ROCm-Treiber korrekt installiert sind
2. Überprüfen Sie die Berechtigungen für `/dev/kfd` und `/dev/dri`
3. Prüfen Sie, ob die richtige GPU ausgewählt ist (`HIP_VISIBLE_DEVICES`)

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE) für Details. 