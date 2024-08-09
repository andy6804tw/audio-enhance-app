# Resemble Enhance App

## 概述

Resemble Enhance App 是一個基於 Streamlit 的音頻處理 Web 應用程式，專注於音頻的去噪和增強功能。這個應用利用了 PyTorch 和 Torchaudio 進行音頻處理，並結合了 Resemble Enhance 模組，提供高效的音頻增強與去噪功能。

### 技術特點

- **Denoised Audio**: 透過先進的音頻去噪技術，消除背景噪音，提升音頻的清晰度。
- **Enhanced Audio**: 基於 Resemble Enhance 的增強功能，使用不同的數值方法和參數來增強音頻質量，使其更加專業和高效。

## 功能介紹

- **音頻上傳**: 支持 `.wav`, `.mp3`, `.ogg` 等多種格式的音頻文件上傳。
- **音頻去噪**: 可選擇性地對音頻進行去噪處理。
- **音頻增強**: 支持多種數值方法（如 Midpoint, RK4, Euler）來增強音頻，並允許調整相關參數以獲得最佳效果。
- **播放與下載**: 支持在網頁中直接播放處理後的音頻，並提供下載鏈接。

## 安裝

### 先決條件

請確保您的系統已經安裝了以下軟件：
- **Python 3.7 或更高版本**
- **pip**（Python 的包管理工具）
- **ffmpeg**（處理音頻文件格式的工具）

### 安裝步驟

1. Clone 專案

```bash
git clone https://github.com/yourusername/resemble-enhance-app.git
cd resemble-enhance-app
```

2. 安裝所需的 Python 套件

```bash
pip install -r requirements.txt
```

## 啟動應用程式
安裝完成後，使用以下指令啟動應用程式：

```sh
streamlit run app.py
```

應用程式將在本地運行，並在瀏覽器中自動打開。預設情況下，您可以在 http://localhost:8501 訪問應用程式。

## 使用方式
1. 上傳音頻文件。
2. 根據需求選擇音頻增強的參數設定。
3. 點擊「Process」按鈕進行音頻處理。
4. 播放處理後的音頻或下載到本地。

## 貢獻
歡迎對此專案進行貢獻。如果您有任何建議或發現了問題，請提交 issue 或開啟 pull request。

## 授權
此專案基於 MIT 授權條款發佈。