import sys
import copy


cells = [
  {
    'name': 'path',
    'directions': '',
    'image': ['###',
              '###',
              '###']
  }, {
    'name': 'path',
    'directions': 'down',
    'image': ['###',
              '# #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'down-left',
    'image': ['###',
              '  #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'left',
    'image': ['###',
              '  #',
              '###']
  }, {
    'name': 'path',
    'directions': 'right',
    'image': ['###',
              '#  ',
              '###']
  }, {
    'name': 'path',
    'directions': 'right-down',
    'image': ['###',
              '#  ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'right-down-left',
    'image': ['###',
              '   ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'right-left',
    'image': ['###',
              '   ',
              '###']
  }, {
    'name': 'path',
    'directions': 'up',
    'image': ['# #',
              '# #',
              '###']
  }, {
    'name': 'path',
    'directions': 'up-down',
    'image': ['# #',
              '# #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-down-left',
    'image': ['# #',
              '  #',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-left',
    'image': ['# #',
              '  #',
              '###']
  }, {
    'name': 'path',
    'directions': 'up-right',
    'image': ['# #',
              '#  ',
              '###']
  }, {
    'name': 'path',
    'directions': 'up-right-down',
    'image': ['# #',
              '#  ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-right-down-left',
    'image': ['# #',
              '   ',
              '# #']
  }, {
    'name': 'path',
    'directions': 'up-right-left',
    'image': ['# #',
              '   ',
              '###']
  }, {
    'name': 'start',
    'directions': 'down',
    'image': ['###',
              '#*#',
              '# #']
  }, {
    'name': 'end',
    'directions': 'up',
    'image': ['# #',
              '#$#',
              '###']
  }
]

directions = {
  'up': [0, -1],
  'right': [1, 0],
  'left': [-1, 0],
  'down': [0, 1]
}


def interpret(maze):
  new = []
  for line in maze:
    new.append([])
    for char in line:
      new[-1].append(int(char, 18))

  return new


def render(maze, highlight=[]):
  out = ''
  for y, line in enumerate(maze):
    row = ['', '', '']
    for x, cell in enumerate(line):
      image = cells[cell]['image']
      

      for cy in range(3):
        for cx in range(3):
          if (x, y) in highlight and image[cy][cx] == ' ':
            row[cy] += '..'
          else:
            row[cy] += image[cy][cx] * 2

    out += row[0] + '\n' + row[1] + '\n' + row[2] + '\n'

  return out


def find_start(maze):
  for y, line in enumerate(maze):
    for x, cell in enumerate(line):
      if cells[cell]['name'] == 'start':
        return x, y


def explore(maze, x, y, visited=[]):
  cell = maze[y][x]
  visited.append((x, y))

  if cells[cell]['name'] == 'end':
    return []
  else:
    for exit in cells[cell]['directions'].split('-'):
      d = directions[exit]

      nx, ny = x + d[0], y + d[1]
      if (nx, ny) not in visited:
        route = explore(maze, nx, ny, visited)
        if route is not None:
          route.append((nx, ny))
          return route


def main():
  with open(sys.argv[1]) as f:
    maze = f.read().splitlines()

  maze = interpret(maze)

  print(render(maze))
  route = explore(maze, *find_start(maze))
  print(render(maze, route))


if __name__ == '__main__':
  main()
