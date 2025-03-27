import os
import shutil
from pathlib import Path
from PIL import Image
import subprocess

# Caminhos
base_dir = Path("analise/RHO_10.0")
output_dir = Path("painel")
frames_dir = output_dir / "frames"
videos_dir = output_dir / "videos"
output_html = output_dir / "painel_interativo.html"

# Criar pastas
frames_dir.mkdir(parents=True, exist_ok=True)
videos_dir.mkdir(parents=True, exist_ok=True)

# Coletar dados do painel
painel_info = []

for eta_dir in base_dir.glob("ETA_*"):
    eta_val = float(eta_dir.name.replace("ETA_", ""))
    for lambda_dir in eta_dir.glob("LAMBDA_*"):
        lambda_val = float(lambda_dir.name.replace("LAMBDA_", ""))
        imagens_path = lambda_dir / "TESTL/imagens"

        # Frame final (miniatura)
        frame_files = sorted(imagens_path.glob("frame_*.png"))
        if not frame_files:
            continue
        frame_final = frame_files[-1]
        frame_out_name = f"frame_ETA_{eta_val}_LAMBDA_{lambda_val}.png"

        # Redimensionar mantendo proporcao (altura fixa = 240px)
        img = Image.open(frame_final)
        aspect_ratio = img.width / img.height
        target_height = 240
        target_width = int(target_height * aspect_ratio)
        img_resized = img.resize((target_width, target_height), Image.LANCZOS)
        img_resized.save(frames_dir / frame_out_name)

        # Copiar vídeo
        video_files = list(imagens_path.glob("*.mp4"))
        if not video_files:
            continue
        video_file = video_files[0]
        video_out_name = f"video_ETA_{eta_val}_LAMBDA_{lambda_val}.mp4"
        shutil.copy2(video_file, videos_dir / video_out_name)

        painel_info.append((eta_val, lambda_val, frame_out_name, video_out_name))

# Organizar parametros unicos
etas = sorted(set(p[0] for p in painel_info), reverse=True)
lambdas = sorted(set(p[1] for p in painel_info))

# Criar HTML
with open(output_html, "w") as f:
    f.write("""
<html>
<head>
  <meta charset=\"UTF-8\" />
  <title>Painel Interativo ETA × LAMBDA</title>
  <style>
    body { font-family: sans-serif; }
    table { border-collapse: collapse; margin-top: 20px; }
    td { padding: 6px; border: 1px solid #ccc; text-align: center; vertical-align: middle; }
    img { display: block; margin: auto; border-radius: 6px; }
    small { display: block; margin-top: 4px; color: #555; }
  </style>
</head>
<body>
<h2>Painel Interativo ETA × LAMBDA</h2>
<table>
""")

    for eta in etas:
        f.write("<tr>\n")
        for lamb in lambdas:
            match = next((p for p in painel_info if p[0] == eta and p[1] == lamb), None)
            if match:
                frame_file, video_file = match[2], match[3]
                f.write(f"<td><a href='videos/{video_file}' target='_blank'>")
                f.write(f"<img src='frames/{frame_file}' height='240'></a>")
                f.write(f"<small>η = {eta:.2f}, λ = {lamb:.2f}</small>")
                f.write("</td>\n")
            else:
                f.write("<td style='background:#eee;'></td>\n")
        f.write("</tr>\n")

    f.write("</table>\n</body></html>\n")

print("\n✅ Painel atualizado com sucesso em: painel/painel_interativo.html")

# Git commit e push automaticamente
try:
    subprocess.run(["git", "add", "-f", "painel/videos/*.mp4"], shell=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Atualiza painel com novas simulações"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ Atualizações enviadas para o GitHub Pages!")
except subprocess.CalledProcessError:
    print("⚠️  Nenhuma alteração nova para commitar ou erro durante o push.")
