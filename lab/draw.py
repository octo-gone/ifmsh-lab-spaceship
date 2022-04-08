import math

import networkx as nx
from PIL import Image, ImageDraw, ImageFont

from . import models


def generate_positions(space: models.Space):
    g = nx.Graph()

    edges = [(route[0], route[1], 1 / route[2].length) for route in space.routes]

    g.add_weighted_edges_from(edges)

    return nx.spring_layout(g)


colors = ["white", "red", "yellow", "green", "blue"]


def draw_space(space: models.Space, nodes_positions: dict, dices: tuple = None):
    size = (1200, 1200)
    half_size = (size[0] // 2, size[1] // 2)
    draw_size = (1000, 1000)
    half_draw_size = (draw_size[0] // 2, draw_size[1] // 2)

    if dices is not None:
        size = (size[0], size[1] + 100 * len(dices))

    img = Image.new("RGBA", size, "black")
    img_draw = ImageDraw.Draw(img)

    route_cell_size = 7
    for i, j, route in space.routes:
        start = (half_size[0] + nodes_positions[i][0] * half_draw_size[0],
                 half_size[1] + nodes_positions[i][1] * half_draw_size[1])
        end = (half_size[0] + nodes_positions[j][0] * half_draw_size[0],
               half_size[1] + nodes_positions[j][1] * half_draw_size[1])
        img_draw.line((start, end), fill="black", width=6)
        img_draw.line((start, end), fill="white", width=5)

        for ir, r in enumerate(route):
            delta = (1.5 + ir) / (len(route) + 2)
            pos1 = nodes_positions[i]
            pos2 = nodes_positions[j]

            pos = (half_size[0] + (pos1[0] + (pos2[0] - pos1[0]) * delta) * half_draw_size[0],
                   half_size[1] + (pos1[1] + (pos2[1] - pos1[1]) * delta) * half_draw_size[1])

            bbox = [pos[0] - route_cell_size, pos[1] - route_cell_size,
                    pos[0] + route_cell_size, pos[1] + route_cell_size]
            img_draw.ellipse(bbox, fill=colors[r], outline="black", width=2)

    node_size = 15
    font = ImageFont.truetype("arial", size=node_size)
    for node in nodes_positions.keys():
        pos = nodes_positions[node]
        center = (half_size[0] + pos[0] * half_draw_size[0],
                  half_size[1] + pos[1] * half_draw_size[1])
        bbox = [center[0] - node_size, center[1] - node_size,
                center[0] + node_size, center[1] + node_size]
        img_draw.ellipse(bbox, fill="black", outline="white", width=3)
        img_draw.text((center[0] - font.getsize(str(node))[0] / 2,
                       center[1] - font.getsize(str(node))[1] / 2), text=str(node), fill="white", font=font)

    if dices is not None:
        for i, dice in enumerate(dices):
            for j, side in enumerate(dice.sides):
                bbox = (j * 100 + 20, size[1] - 100 * len(dices) + i * 100,
                        j * 100 + 100, size[1] - 100 * len(dices) + 80 + i * 100)
                img_draw.rounded_rectangle(bbox, fill="white", radius=20, outline="black", width=5)

                point_size = 7

                side_center = (j * 100 + 60, size[1] - 100 * len(dices) + i * 100 + 40)
                if len(side) > 1:
                    points = get_regular_polygon_points(len(side), 0, side_center, 20)
                    for j, p in enumerate(points):
                        img_draw.ellipse((p[0] - point_size, p[1] - point_size, p[0] + point_size, p[1] + point_size),
                                         fill=colors[side[j]], outline="black", width=3)
                else:
                    img_draw.ellipse((side_center[0] - point_size, side_center[1] - point_size,
                                      side_center[0] + point_size, side_center[1] + point_size),
                                     fill=colors[side[j]], outline="black", width=3)

        img.save("space.png")
        del img_draw
        del img


def get_regular_polygon_points(count, rotation, position, radius):
    points = []
    for i in range(count):
        x = position[0] + radius * math.cos(rotation + math.pi * 2 * i / count)
        y = position[1] + radius * math.sin(rotation + math.pi * 2 * i / count)
        points.append((x, y))
    return points
