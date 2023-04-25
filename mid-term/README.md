# CTF 期中版本

## Transformation
`灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽`文件內容\
`https://string-functions.com/encodedecode.aspx` 解碼網站\
UTF16BE 轉 UTF8\
`picoCTF{16_bits_inst34d_of_8_0ddcd97a}`FLAG

## crackme-py
程式內有提示用ROT47解碼\
`https://www.dcode.fr/rot-47-cipher` 解碼網站

## Safe Opener
程式內有提示用BASE64解碼\
`https://www.base64decode.org/` 解碼網站

## file-run1
`chmod +x ./run` 給予權限
`./run` 開啟檔案

## file-run1
`chmod +x ./run` 給予權限
`./run Hello!` 開啟檔案 加上參數

## patcheme.py
將下載的檔案放入同個資料夾下\
將判斷密碼的判斷移除\
即可獲得flag

## speeds and feeds
將連結到的網站內容
複製下來並丟到
`https://ncviewer.com/` 線上gcode\
即可看出flag

## stonks
參考 ./python/pwm.py\
一定量的%X\
即可推出flag

## shop
考C的變數溢位\
將購買數兩改為負的即可\
得到`Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 57 99 49 49 56 98 98 102 125]`\
透過`http://www.unit-conversion.info/texttools/octal/`\
轉回來即可

## New Caesar 
參考 ./python/new_caesar.py\
做反編譯\
即可推出flag

## who are you
需要參考`https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers` HTTP-header查表\
`User-Agent`登入人\
`Referer` 登入端\
`Date` 當下時間\
`DNT` 是否追蹤\
`Forwarded-For`登入的位址IP\
`Accept-Language` 接受語言

## Local Authority
查看原始碼\
檢視login.php\
檢視 secure.js\
密碼藏在程式裡

## Inspect HTML 
查看原始碼即可獲得flag

## Includes
查看原始碼\
檢視index.css\
檢視script.js\
合起來即是flag

## Lookey here
使用尋找工具\
`grep -r 'pico'`\ 
即可獲得flag

## rail-fence
rail-key為3\
使用`http://www.atoolbox.net/Tool.php?Id=777` 柵欄密碼


