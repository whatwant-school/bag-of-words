# bag-of-words
Bag of Words


## Python version (pyenv)
- pyenv 설치된 환경에서는 아래 내용 무시

```bash
// 사용 가능한(설치된) python version 확인
$ pyenv versions

// 해당 디렉토리에서 특정 Python version 지정
$ pyenv local 3.8.13
```


## Python virtual environment (venv)
- activate/deactivate 만 신경쓰면 됨

```bash
// 가상환경 생성
$ python -m venv .venv/

// 가상환경 실행
$ source .venv/bin/activate

// 가상환경 종료
$ deactivate
```

## JDK (openjdk)
- Java로 구현된 Konlpy를 위해 JDK 설치

```bash
$ sudo apt install g++ openjdk-8-jdk
```

## Konlpy

```bash
$ pip install konlpy
```

---

## Execute

```bash
$ python bag-of-words.py
```

## Results

```bash
vocabulary : {'나': 0, '는': 1, '자연어': 2, '처리': 3, '를': 4, '배운다': 5, '재미있다': 6, 'aplle': 7, 'is': 8, 'good': 9}
bag of words vector : [1, 2, 2, 2, 1, 1, 1, 1, 1, 1]
```




