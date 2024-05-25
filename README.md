# pygame 튜토리얼

[pygame 공식 문서](https://www.pygame.org/docs/)\
**이 문서는 파이썬 기본 문법을 모두 숙지하였다는 전제 하에 쓰여졌습니다.**\
**특히 타입 어노테이션 문법과 Typing모듈을 숙지하지 않으면 이해가 어려울 수 있습니다.**

## 1. 기본 코드

아래는 pygame 실행을 위한 기본적인 코드입니다.

```python
import pygame # pygame 불러오기

pygame.init()

screen = pygame.display.set_mode((400, 400)) # 게임 창을 400x400으로 띄우기

done = False # 게임이 종료되었는지의 여부 저장
clock = pygame.time.Clock() # 시간의 흐름 만들기

def runGame() -> None: # 게임 실행하기
    global done
    while not done:
        clock.tick(20) # 1초에 20번 감지

        for event in pygame.event.get(): # 이벤트 다루기
            if event.type == pygame.QUIT:
                done = True

runGame()
pygame.quit()
```

## 2. 기초 객체

- ### Surface

---

- ### ColorValue

ColorValue는 길이가 3인 튜플로 표현됩니다.

```python
ColorValue = (RED, GREEN, BLUE)
```

RED, GREEN, BLUE 각각은 0~255까지의 값을 가지며, (0, 0, 0)은 검은색, (255, 255, 255)는 하얀색입니다.

---

- ### Coordinate

Coordinate는 길이가 2인 튜플로 표현됩니다.

```python
Coordinate = (x, y)
```

특정 좌표를 나타낼 때 사용됩니다.

---

## 3. 도형 그리기

- ### pygame.draw.rect(surface: Surface, color: ColorValue, rect: RectValue, width: int = 0) -> Rect
  - 직사각형을 그립니다.
- ### pygame.draw.circle(surface: Surface, color: ColorValue, center: Coordinate, radius: float, width: int = 0) -> Rect
  - 원을 그립니다.
- ### pygame.draw.line(suface: Surface, color: ColorValue, start_pos: Coordinate, end_pos: Coordinate, width: int = 1) -> Rect
  - 선을 그립니다.

---

rect(RectValue)는 길이가 4인 튜플로 표현됩니다.

```python
rect = (x, y, width, height)
```

x, y는 rect의 최초 위치를 나타냅니다. 기준은 직사각형의 왼쪽 위 꼭짓점 입니다.\
width와 height는 각각 가로 폭과 세로 폭을 나타냅니다.

---

center는 circle의 중점의 위치를 나타냅니다.

---

radius는 circle의 반지름의 길이를 나타냅니다.

---

rect와 circle에서 width는 테두리의 굵기를 나타냅니다.\
line에서 width는 선의 굵기를 나타냅니다.

---

## 4. 그림 파일 그리기

- ### pygame.image.load(filename: FileArg) -> Surface
  - 이미지 경로에 있는 이미지를 불러옵니다.
- ### pygame.transform.scale(surface: Surface, size: Coordinate) -> Surface
  - surface의 크기를 조정합니다.
- ### Surface.blit(source: Surface, dest: Coordinate | RectValue) -> Rect
  - Surface에 source를 출력합니다.

---

filename(FileArg)는 문자열로 표현되며 파일의 경로를 나타냅니다.

```python
pygame.image.load("C\\ProjectFolder\\image.png")
```

---

size는 Coordinate를 받습니다.\
size[0]은 가로, size[1]은 세로의 길이를 뜻합니다.

---

blit 함수는 아래와 같이 쓸 수 있습니다.

```python
screen = pygame.display.set_mode(size)

img = pygame.image.load("examples/Background.jpg")
img = pygame.transform.scale(img, (600, 800))
screen.blit(img, (0, 0))
```

---

## 5. 글자 쓰기

- ### pygame.font.SysFont(name: str, size: int, bold=False, italic=False) -> Font
  - name에 폰트 이름을 적으면 해당하는 폰트를 반환합니다.
- ### Font.render(text: str | None, antialias: bool, color: ColorValue) -> Surface
  - 폰트를 렌더링합니다.
- ### Surface.blit(source: Surface, dest: Coordinate | RectValue) -> Rect

---

antialias는 안티에일리어싱 여부를 결정합니다.

---

아래와 같이 쓸 수 있습니다.

```python
screen = pygame.display.set_mode(size)

sysfont = pygame.font.SysFont("AppleSDGothicNeoSB00", 36)
text = sysfont.render("Hello World!", True (0, 0, 255))
screen.blit(text, (0, 0))
```

## 6. 이벤트 다루기

pygame은 이벤트를 다루는 방식으로 게임을 만듭니다.

- ### pygame.QUIT

  - 게임을 끄려고 할 때 일어나는 이벤트입니다.

- ### pygame.ACTIVEEVENT

  - 이게뭐지

- ### pygame.KEYDOWN

  - 키보드 버튼을 누르면 발생합니다.
  - 해당 이벤트가 발생하면 그 이벤트에는 key라는 멤버변수가 생겨 어느 키를 눌렀는지 알 수 있습니다. [pygame.key 공식 문서](https://www.pygame.org/docs/ref/key.html?highlight=k_up)에 자세히 나와 있습니다.

- ### pygame.KEYUP
  - 키보드 버튼을 누르고 있는 상태에서 떼면 발생합니다.
