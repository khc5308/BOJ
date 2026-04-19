import webbrowser
import os
import time

def open_all_problems():
    file_path = 'asdf.txt'
    
    if not os.path.exists(file_path):
        print(f"오류: {file_path} 파일이 없습니다.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        problems = file.readlines()
        
        for p_num in range(100):
            problem_number = problems[p_num].strip() # 공백 및 줄바꿈 제거
            
            # 빈 줄은 건너뜁니다.
            if not problem_number:
                continue
                
            url = f'https://www.acmicpc.net/status?from_mine=1&problem_id={problem_number}&user_id=khc5308'
            
            print(f"여는 중: 문제 번호 {problem_number}")
            webbrowser.open(url)
            
            time.sleep(0.1)

if __name__ == "__main__":
    open_all_problems()