import graphics as gr

window = gr.GraphWin("some title", width=500, height=500)
A = 100, 100
B = 400, 400


def drawLine(p1, p2, depth=20):
    """
    рисуем фрактальную линию с поворотом вправо на одной трети
    """

    pass


# gr.Line(gr.Point(*A), gr.Point(B[0], A[1])).draw(window)
# gr.Line(gr.Point(B[0], A[1]), gr.Point(*B)).draw(window)
# gr.Line(gr.Point(*B), gr.Point(A[0], B[1])).draw(window)
# gr.Line(gr.Point(A[0], B[1]), gr.Point(*A)).draw(window)

drawLine(A, B, 20)
window.wait_window()
