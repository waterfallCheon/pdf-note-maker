
🖊️ PDF 필기 노트 변환 프로그램

태블릿으로 필기를 하자니 전체 구조가 안보이고, 프린트해서 필기하자니 크기가 애매해서  
태블릿으로 필기도 하고, 나중에 프린트해서 공부하기 딱 좋은 상태를 만들고 싶어 만든 프로그램 입니다..  
  
왼쪽에는 원본 PDF 2페이지를 모으고, 오른쪽에는 필기 공간을 제공합니다.


## 주요 기능

* **PDF 페이지 2분할**: 원본 PDF의 두 페이지를 한 장의 새 PDF 왼쪽 영역에 배치합니다.
* **필기 공간 추가**: 오른쪽 영역에 필기할 수 있는 여백을 제공하며, **모눈** 또는 **라인** 스타일을 선택할 수 있습니다.
    * **모눈**: 촘촘한 격자 형태로 도형이나 그래프 그릴 때 유용합니다.
    * **라인**: 일반적인 노트처럼 줄 간격에 맞춰 필기하기 좋습니다.
* **다중 파일 처리**: 여러 PDF 파일을 한 번에 드래그 앤 드롭하거나 경로를 입력하여 변환할 수 있습니다.
* **페이지 번호 자동 추가**: 현재 페이지 / 전체 페이지 번호를 하단에 표시합니다.

## 변환 예시

| 원본 PDF | 모눈 노트 변환 | 라인 노트 변환 |
| :---: | :---: | :---: |
| <img width="300" alt="원본 PDF 예시" src="https://github.com/user-attachments/assets/310c89eb-51e0-4d51-bac0-20cac5f5edd9"> | <img width="300" alt="모눈 노트 변환 예시" src="https://github.com/user-attachments/assets/d989b299-4ec0-4b81-9631-a809e1681d71"> | <img width="300" alt="라인 노트 변환 예시" src="https://github.com/user-attachments/assets/dd41c189-06b7-49b2-a1bd-d97366041352"> |

## 사용 방법

이 프로그램은 Python 환경에서 실행됩니다.

### 1. Python 설치
Windows 사용자라면 Python 3.10 이상을 설치하세요.  
설치할 때 **"Add Python to PATH"** 옵션을 꼭 체크하세요 ✅

혹은 PowerShell에서 아래 명령으로 설치할 수도 있습니다:
```powershell
winget install Python.Python.3.11
``` 
2. 필요한 라이브러리 설치
명령 프롬프트(cmd)나 PowerShell을 열고, 아래 명령을 입력하세요:

```powershell
pip install PyMuPDF
``` 
