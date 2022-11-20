lottery = {3, 22, 7, 87, 45, 672}
players = [
    {
        "name": "sowmya",
        "numbers": {2, 7, 98, 88, 82, 28}
    },
    {
        "name": "zameel",
        "numbers": {23, 837, 9723, 54, 45}
    }

]
name=players[0]["name"]
numbers=players[0]["numbers"].intersection(lottery)
print(f"player {name} got {len(numbers)} right")

name=players[1]["name"]
numbers=players[1]["numbers"].intersection(lottery)
print(f"player {name} got {len(numbers)} right")