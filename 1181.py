n = int(input())
words = set()  # 중복을 제거하기 위해 set 사용

# 입력받기
for _ in range(n):
    words.add(input().strip())

# 리스트로 변환한 후 정렬 수행
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)
