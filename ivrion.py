import pyautogui
import cv2
import numpy as np
import pygetwindow as gw
import time
import keyboard  # pip install keyboard

# -----------------------------
# 啟用 PyAutoGUI FailSafe
# -----------------------------
pyautogui.FAILSAFE = True

# -----------------------------
# 自動抓取遊戲窗口區域
# -----------------------------
def get_game_region(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"[錯誤] 找不到窗口: {window_title}")
        return None
    win = windows[0]
    left, top = win.topleft
    width, height = win.width, win.height
    print(f"[遊戲區域] left={left}, top={top}, width={width}, height={height}")
    return (left, top, width, height)

# -----------------------------
# 工具函式：找到圖片並點擊（限定遊戲區域）
# -----------------------------
def locate_and_click(template_path, game_region, confidence=0.8):
    left, top, width, height = game_region
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        print(f"[錯誤] 找不到模板圖片: {template_path}")
        return False

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= confidence)
    points = list(zip(*loc[::-1]))

    if points:
        x, y = points[0]
        pyautogui.click(x + template.shape[1]//2 + left, y + template.shape[0]//2 + top)
        return True
    return False

# -----------------------------
# 自動戰鬥函式
# -----------------------------
def auto_battle(game_region, attack_key='space', check_interval=1):
    print("[開始戰鬥]")
    while True:
        if keyboard.is_pressed('q'):  # 按 Q 鍵退出
            print("[偵測到退出按鍵 Q，停止戰鬥]")
            return
        pyautogui.press(attack_key)
        time.sleep(check_interval)
        if locate_and_click('complete.png', game_region, confidence=0.85):
            print("[戰鬥結束]")
            time.sleep(1)
            return

# -----------------------------
# 主流程
# -----------------------------
def main_loop(game_region):
    while True:
        if keyboard.is_pressed('q'):
            print("[偵測到退出按鍵 Q，停止腳本]")
            break

        if locate_and_click('boss.png', game_region, confidence=0.7):
            print("[點擊 Boss]")
            time.sleep(1)

            if locate_and_click('fight.png', game_region, confidence=0.7):
                print("[對話 NPC]")
                time.sleep(2)

                auto_battle(game_region)

                if locate_and_click('ok.png', game_region, confidence=0.7):
                    print("[關閉結算表]")
                    time.sleep(1)
        else:
            print("[找不到 Boss，等待5秒]")
            time.sleep(5)

# -----------------------------
# 執行腳本
# -----------------------------
if __name__ == "__main__":
    print("=== 自動打怪腳本啟動 ===")
    time.sleep(3)  # 給你切換到遊戲視窗

    game_region = get_game_region("摩尔勇士复兴版")  # 改成遊戲窗口名稱
    if game_region:
        try:
            main_loop(game_region)
        except KeyboardInterrupt:
            print("\n[Ctrl+C 中斷，腳本已停止]")
        except pyautogui.FailSafeException:
            print("\n[滑鼠移到左上角，腳本已停止]")
