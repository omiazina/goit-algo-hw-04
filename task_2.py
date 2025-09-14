import turtle


def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)


def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(800, 800)
    t = turtle.Turtle()
    t.speed(0)

    size = 300
    for _ in range(3):
        koch_snowflake(t, size, level)
        t.right(120)

    screen.mainloop()


if __name__ == "__main__":
    main()
