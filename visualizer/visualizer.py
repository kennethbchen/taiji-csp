from ursina import *
from Node import Node
from Edge import Edge

layers = [
    [
        [1, 1, 1, 1, 1, 4],
        [2, 2, 2, 2, 1, 4],
        [2, 3, 3, 2, 1, 4],
        [2, 3, 4, 1, 1, 4],
        [2, 3, 4, 4, 4, 4],
        [2, 3, 3, 3, 3, 3],
    ],
    [
        [1, 1, 1, 1, 1, 2],
        [3, 3, 3, 3, 1, 2],
        [3, 3, 3, 4, 2, 2],
        [5, 3, 4, 4, 4, 2],
        [5, 3, 3, 3, 3, 6],
        [5, 5, 3, 3, 7, 8],
    ],
    [
        [1, 1, 1, 2, 2, 7],
        [1, 2, 2, 2, 8, 9],
        [1, 2, 3, 3, 10, 11],
        [1, 1, 4, 4, 1, 6],
        [5, 1, 4, 1, 1, 6],
        [5, 1, 1, 1, 6, 6],
    ],

]

layers = [
    [
        [1, 2, 2, 2],
        [1, 1, 2, 3],
    ],
    [
        [1, 1, 2, 2],
        [1, 2, 2, 2],
    ],
    [
        [1, 1, 1, 1],
        [2, 2, 2, 1],
    ],
]

layer_colors = [color.red, color.green, color.blue]

tiles = {}
edges = []

spacing = 1.5

app = Ursina()
camera = EditorCamera()

# Setup
for layer_i, layer in enumerate(layers):

    # Create node objects
    for row in range(0, len(layer)):
        for col in range(0, len(layer[row])):
            tiles[(col, row, layer_i)] = Node(col=col, row=row, layer=layer_i, region=layer[row][col], model="sphere", color=layer_colors[layer_i], scale=Vec3(0.5, 0.5, 0.5), position=Vec3(col * spacing, layer_i * spacing, row * spacing))


    # Add neighbors
    for i, (key, tile) in enumerate(tiles.items()):

        neighbors = [
            (tile.col - 1, tile.row, tile.layer),
            (tile.col + 1, tile.row, tile.layer),
            (tile.col, tile.row - 1, tile.layer),
            (tile.col, tile.row + 1, tile.layer),
        ]

        for neighbor in neighbors:
            if neighbor in tiles:
                tile.add_neighbor(tiles[neighbor])


# Axes
x_axis = Entity(model=Pipe(path=((-1, -1, -1), (10, -1, -1)), thicknesses=(0.1, 0.1)), color=color.red)
y_axis = Entity(model=Pipe(path=((-1, -1, -1), (-1, 10, -1)), thicknesses=(0.1, 0.1)), color=color.green)
z_axis = Entity(model=Pipe(path=((-1, -1, -1), (-1, -1, 10)), thicknesses=(0.1, 0.1), cap_ends=False), color=color.blue)



app.run()