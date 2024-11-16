import os

# 디렉토리 및 파일 생성
os.makedirs('geo', exist_ok=True)

# 파일 생성
with open('geo/__init__.py', 'w') as f:
    pass

with open('geo/utils.py', 'w') as f:
    pass

with open('tester.py', 'w') as f:
    pass
