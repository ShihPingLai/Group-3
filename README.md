# Group-3   

# Topic       
混沌同步保密通訊

# Group member      
104022192  楊馥榕    
104022207  饒孝節    
104022209  李岱庭    
104022271  林希雲    
105022220  許祐綸     

# Goal  
設一輸出端輸出蔡式電路的混沌訊號，再設一接收端判定訊號是否正確。  

# Method   
1. 使用Python做出蔡式電路模型   
2. 將電路模型輸出之混沌訊號會製成3D圖形   
3. 將混沌訊號與保密通訊結合   
4. 設立接收端接收混沌訊號   
5. 確認其訊號是否與預設相符   
6. 嘗試將原本輸出的sine波改為聲音訊號測試

# Assignment
楊馥榕：debug、資料收集    
饒孝節：接收訊號並分析    
李岱庭：製造訊號    
林希雲：製造訊號    
許祐綸：接收訊號並分析    

# 使用方法
下載Chaos_group3.zip，並解壓縮
壓縮檔內含:
1. produce_signal.py 
2. Analysis_signal.py 
3. Recording-3.wav 
4. run.sh 

 如果你使用類linux系統，在terminal中執行run.sh即可
 
 如果你是windows使用者，windows7（含）以上系統可進入windows power shell, 請在windows power shell 中執行run.sh
 
 如果你沒有windows power shell, 請先用python 執行produce_signal.py 再執行Analysis_signal.py
 
 需要輸入的音檔是資料夾內的Recording-3,你也可以輸入自己的wav檔，但不建議超過30秒
