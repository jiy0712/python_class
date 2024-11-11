#WriteText텍스트 파일 만들려고함
#파일 저장을 위한 함수 2개의 다른 접근 방식으로 사용해 텍스트 파일 만들 수 있느 코드 자가성
#"파이썬 수행평가", "2 - 2" 두 문장을 저장한 후, "Saving", "Text" 두 문장을 추가하여 저장하도록 한다

#잘 된다면
#파이썬 수행평가
#2 - 2
#Saving
#Text 이렇게 저장이 되어야한다.

f = open("WriteText.txt", "w", encoding="utf8")
f.write("파이썬 수행평가\n")
f.write("2 - 2\n")
f.write("Saving\n")
f.write("Text\n")
f.close()

