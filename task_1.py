class GeometricFigure:
    """
    Базовый класс для геометрических фигур.
    """

    def __init__(self, name: str) -> None:
        """
        Инициализация геометрической фигуры.

        Args:
            name: Название фигуры.
        """
        self.name: str = name

    def __str__(self) -> str:
        """
        Возвращает строковое представление фигуры.
        """
        return f"Фигура: {self.name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.
        """
        return f"GeometricFigure(name='{self.name}')"

    def area(self) -> float:
        """
        Вычисляет площадь фигуры.  Это абстрактный метод, который должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Метод area должен быть переопределен в дочернем классе.")


class Circle(GeometricFigure):
    """
    Класс для круга.  Наследует от GeometricFigure.
    """

    def __init__(self, name: str, radius: float) -> None:
        """
        Инициализация круга.

        Args:
            name: Название круга.
            radius: Радиус круга.
        """
        super().__init__(name) # вызов конструктора родительского класса
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным.")
        self._radius: float = radius # _radius - инкапсулированный атрибут

    def __str__(self) -> str:
        """
        Переопределенный метод __str__ для вывода информации о круге.
        """
        return f"Круг: {self.name}, радиус = {self._radius}"

    def __repr__(self) -> str:
        """
        Переопределенный метод __repr__ для отладки.
        """
        return f"Circle(name='{self.name}', radius={self._radius})"


    def area(self) -> float:
        """
        Переопределенный метод для вычисления площади круга.
        """
        import math
        return math.pi self._radius**2

    def circumference(self) -> float:
        """
        Вычисляет длину окружности круга.
        """
        import math
        return 2 math.pi self._radius


class Square(GeometricFigure):
    """
    Класс для квадрата. Наследует от GeometricFigure.
    """
    def __init__(self, name: str, side: float) -> None:
        """
        Инициализация квадрата.

        Args:
            name: Название квадрата.
            side: Длина стороны квадрата.
        """
        super().__init__(name)
        if side < 0:
            raise ValueError("Длина стороны не может быть отрицательной.")
        self._side: float = side # _side - инкапсулированный атрибут

    def __str__(self) -> str:
        """
        Переопределённый метод __str__ для вывода информации о квадрате.
        """
        return f"Квадрат: {self.name}, сторона = {self._side}"

    def __repr__(self) -> str:
        """
        Переопределённый метод __repr__ для отладки.
        """
        return f"Square(name='{self.name}', side={self._side})"

    def area(self) -> float:
        """
        Переопределённый метод для вычисления площади квадрата.
        """
        return self._side**2

    def perimeter(self) -> float:
        """
        Вычисляет периметр квадрата.
        """
        return 4 self._side

