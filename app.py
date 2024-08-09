import streamlit as st
import torch
import torchaudio
from resemble_enhance.enhancer.inference import denoise, enhance
import numpy as np
import soundfile as sf
import io

# 設定裝置
device = "cuda" if torch.cuda.is_available() else "cpu"

# 定義處理函數
def process_audio(path, solver, nfe, tau, denoising):
    if path is None:
        return None, None

    solver = solver.lower()
    nfe = int(nfe)
    lambd = 0.9 if denoising else 0.1

    dwav, sr = torchaudio.load(path)
    dwav = dwav.mean(dim=0)

    wav1, new_sr = denoise(dwav, sr, device)
    wav2, new_sr = enhance(dwav, sr, device, nfe=nfe, solver=solver, lambd=lambd, tau=tau)

    wav1 = wav1.cpu().numpy()
    wav2 = wav2.cpu().numpy()

    return (new_sr, wav1), (new_sr, wav2)

# Streamlit 應用程式介面
def main():
    st.title("Resemble Enhance")
    st.write("AI-driven audio enhancement for your audio files, powered by Resemble AI.")

    # 輸入元件
    audio_file = st.file_uploader("Upload an Audio File", type=["wav", "mp3", "ogg"])
    solver = st.selectbox("CFM ODE Solver", ["Midpoint", "RK4", "Euler"])
    nfe = st.slider("CFM Number of Function Evaluations", min_value=1, max_value=128, value=64, step=1)
    tau = st.slider("CFM Prior Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    denoising = st.checkbox("Denoise Before Enhancement", value=False)

    if st.button("Process"):
        if audio_file is not None:
            # 將上傳的文件保存至本地臨時目錄
            temp_file = f"temp_{audio_file.name}"
            with open(temp_file, "wb") as f:
                f.write(audio_file.read())

            # 處理音頻
            denoised, enhanced = process_audio(temp_file, solver, nfe, tau, denoising)

            if denoised and enhanced:
                # 顯示和下載處理後的音頻
                st.audio(denoised[1], format="audio/wav", start_time=0)
                st.audio(enhanced[1], format="audio/wav", start_time=0)

                # 下載處理後的音頻
                denoised_bytes = io.BytesIO()
                enhanced_bytes = io.BytesIO()

                sf.write(denoised_bytes, denoised[1], denoised[0], format="WAV")
                sf.write(enhanced_bytes, enhanced[1], enhanced[0], format="WAV")

                st.download_button("Download Denoised Audio", data=denoised_bytes, file_name="denoised_audio.wav")
                st.download_button("Download Enhanced Audio", data=enhanced_bytes, file_name="enhanced_audio.wav")

if __name__ == "__main__":
    main()
