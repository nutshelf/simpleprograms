import graphics as gr
window = gr.GraphWin("some title", width=500, height=500)


def draw_line(window1, p1x, p1y, p6x, p6y, depth=5, alpha=1/3):
    """
    рисуем фрактальную линию с поворотом вправо на одной трети. Остаток от отрезка делим пополам и на первой
     (средней половине) рисуем "П"
    """
    if depth == 1:
        return
    p2x = int(p1x * (1 - alpha) + p6x * alpha)
    p2y = int(p1y * (1 - alpha) + p6y * alpha)
    gr.Line(gr.Point(p1x, p1y), gr.Point(p2x, p2y)).draw(window1)
    p3x = p2x
    p3y = int(p2y + (p2x + p6x) / 2)
    draw_line(window1, p2x, p2x, p3x, p3y, depth-1, alpha)
    p5x = int((p2x + p6x) / 2)
    p5y = int((p2y + p6y) / 2)
    gr.Line(gr.Point(p5x, p5y), gr.Point(p6x, p6y)).draw(window1)
    return


# gr.Line(gr.Point(*A), gr.Point(B[0], A[1])).draw(window)
# gr.Line(gr.Point(B[0], A[1]), gr.Point(*B)).draw(window)
# gr.Line(gr.Point(*B), gr.Point(A[0], B[1])).draw(window)
# gr.Line(gr.Point(A[0], B[1]), gr.Point(*A)).draw(window)

def main_f(window1):
    draw_line(window1, 100, 100, 400, 100, 20, 1/3)
    window1.wait_window()


main_f(window)