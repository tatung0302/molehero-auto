# molehero-auto

自動打怪腳本 for **MoleHero (摩爾勇士復興版)**

這個專案使用 Python 實現，功能如下：

- 自動刷 **伊影 Boss**  
- 自動升級寵物精靈  
- 使用螢幕監控與滑鼠控制  
- 圖片比對機制 (若比對失敗，請自行截圖並替換素材圖片)

## 使用說明

1. 將程式與素材圖片放在同一資料夾  
2. 執行 `ivrion.py`  
3. 程式會自動監控遊戲畫面並進行操作

## 安裝套件

請先安裝以下 Python 套件：

```bash
pip install pyautogui opencv-python numpy pygetwindow keyboard Pillow

## 注意事項

- 遊戲畫面請保持清晰，避免遮擋  
- 如果圖片比對失敗，請重新截圖並替換對應的 PNG 素材  
- 本程式僅供學習與研究使用，請遵守遊戲規則

