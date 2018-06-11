# Group-3 

# 主題
混沌結合保密通訊

# 組員      
104022192  楊馥榕    
104022207  饒孝節    
104022209  李岱庭    
104022271  林希雲    
105022220  許祐綸     

# 目的       
1. 以混沌作為載波傳遞訊息
2. 要知道該載波混沌的初始參數才能破解 =>保密 通訊

# 原理
1. 載波就是攜帶信息/信號的波形。
2. 將要傳遞的信號加載到載波的信號上，接收方按照載波的頻率來接收傳遞的信號，有意義的信號波的波幅與無意義的信號的波幅是不同的，將這些信號提取出來就是傳送方要傳遞的信息。
3. 混沌受初始狀態影響的敏感性，初始條件非常微小的變動也可以導致最終狀態的巨大差別。所以唯有知道初始條件的接收方可以製造出相同的混沌消掉載波，提取出有意義的信號。

# 程式步驟
 傳送方：
 1. 將要傳遞的聲音訊息錄成wav檔
 2. 讀取wav檔，畫出振幅-時間圖
 3. 將聲音分析成雙聲道，分別混入3D的混沌的ＸＹ軸
 4. 播出混合後的音檔
 
 接收方：
1. 接收混合後的訊號與初始參數
2. 根據參數重新製造混沌
3. 將混合訊號扣除混沌
4. 輸出原始訊號並播放

# 分工
李岱庭:加密方、聲音播放
林希雲:加密方、投影片製作
饒孝節:解密方、圖形化對話框
許祐綸:解密方、程式碼簡化、整理
楊馥榕:混沌製造、資料收集    

# 使用方法
下載Chaos_group3.zip，並解壓縮
壓縮檔內含:
1. produce_signal.py 
2. Analysis_signal.py 
3. Recording-3.wav 
4. run.sh 

執行前需安裝python、python套件包（pyaudio、wave、tkinter），安裝方法(windows)：
1. 進入cmd
2. 輸入 pip install pyaudio
3. 輸入 pip install wave
4. 輸入 pip install tkinter

 如果你使用類linux系統，在terminal中執行run.sh即可
 
 如果你是windows使用者，windows7（含）以上系統可進入windows power shell, 請在windows power shell 中執行run.sh
 
 如果你沒有windows power shell, 請先用python 執行produce_signal.py 再執行Analysis_signal.py
 
 需要輸入的音檔是資料夾內的Recording-3,你也可以輸入自己的wav檔，但不建議超過30秒
 
 如果你對文字介面不熟悉，請將解壓後的資料夾放在桌面，在windows power shell 中輸入
 
 cd /Destop/Chaos_group3
 
 ./run.sh
